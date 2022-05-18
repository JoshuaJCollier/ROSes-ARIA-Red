from typing import Tuple

import math
import cv2
import numpy as np
import itertools

from atlas.infrastructure.stream import Stream
from atlas.vision.image import Image
from atlas.vision.util import PixelCoordinate, HsvColour
from atlas.vision.colourrange import ColourRange
from atlas.vision.table_cropper import crop_to_table_by_contours

import atlas.vision.colourspace as colourspace

TRIM_Y = -15
TRIM_X = 15

def detect_block(bgr_image: Image, colour_range: ColourRange):
    if colour_range.value == ColourRange.black.value:
        bounds = colour_range.value
        results, _ = detect_black(bgr_image, *bounds)
        if results:
            return results
        else:
            results, _ = detect_black(bgr_image, *bounds, offset_x=TRIM_X - 10, offset_y=TRIM_Y)
            if not results:
                results, _ = detect_black(bgr_image, *bounds, offset_x=TRIM_X, offset_y=TRIM_Y)
            return results

    elif colour_range.value == ColourRange.white.value:
        bounds = colour_range.value
        results, _ = detect_white(bgr_image, *bounds)

        if not results:
            bounds2 = colour_range.white2.value
            results.clear()
            results, _ = detect_white(bgr_image, *bounds2)

        white = []
        for block in results:
            if not block.x < 0.5 * bgr_image.width:
                white.append(block)
        return white

    elif colour_range.value == ColourRange.green.value:
        bounds = colour_range.value
        results, _ = detect_coloured_block(bgr_image, *bounds)

        if not results:
            bounds2 = colour_range.darkgreen.value
            results.clear()
            results, _ = detect_coloured_block(bgr_image, *bounds2)

        green = []
        for block in results:
            if not block.x < 0.6*bgr_image.width:
                green.append(block)
        return green

    elif colour_range.value == ColourRange.blue.value:
        bounds = colour_range.value
        results, _ = detect_coloured_block(bgr_image, *bounds)

        if not results:
            bounds2 = colour_range.darkblue.value
            results.clear()
            results, _ = detect_coloured_block(bgr_image, *bounds2)
        return results

    elif colour_range.value == ColourRange.yellow.value:
        bounds = colour_range.value
        results, _ = detect_coloured_block(bgr_image, *bounds)

        if not results:
            bounds2 = colour_range.darkyellow.value
            results.clear()
            results, _ = detect_coloured_block(bgr_image, *bounds2)

        yellow = []
        for block in results:
            if not block.x < 0.6*bgr_image.width:
                yellow.append(block)
        return yellow

    else:
        bounds = colour_range.value
        results, _ = detect_coloured_block(bgr_image, *bounds)
        coloured = []
        for block in results:
            if not block.x < 0.4 * bgr_image.width:
                coloured.append(block)
        return coloured


def detect_block_with_output(bgr_image: Image, colour_range: ColourRange):
    results = detect_block(bgr_image, colour_range)
    for result in results:
        cv2.circle(bgr_image.frame, (result.x, result.y), 5, (0, 255, 255), 2)

    return results


def detect_block_and_angle(bgr_image: Image, colour_range: ColourRange) -> Tuple[list, list]:
    if colour_range.value == ColourRange.black.value:
        bounds = colour_range.value
        results, contours = detect_black(bgr_image, *bounds)

    elif colour_range.value == ColourRange.white.value:
        bounds = colour_range.value
        results, contours = detect_white(bgr_image, *bounds)

        if not results:
            bounds2 = colour_range.white2.value
            results.clear()
            results, contours = detect_white(bgr_image, *bounds2)

    elif colour_range.value == ColourRange.green.value:
        bounds = colour_range.value
        results, contours = detect_coloured_block(bgr_image, *bounds, erode=0, dilate=0)

        if not results:
            bounds2 = colour_range.darkgreen.value
            results.clear()
            results, contours = detect_coloured_block(bgr_image, *bounds2, erode=0, dilate=0)

    elif colour_range.value == ColourRange.blue.value:
        bounds = colour_range.value
        results, contours = detect_coloured_block(bgr_image, *bounds, erode=0, dilate=0)

        if not results:
            bounds2 = colour_range.darkblue.value
            results.clear()
            results, contours = detect_coloured_block(bgr_image, *bounds2, erode=0, dilate=0)

    else:
        bounds = colour_range.value
        results, contours = detect_coloured_block(bgr_image, *bounds, erode=0, dilate=0)

    if results and contours:
        angles = filter_contours_and_find_angles(bgr_image, contours)
        return results, angles
    else:
        return results, []


def detect_coloured_block(bgr_image: Image, lower_colour: HsvColour, higher_colour: HsvColour,
                          negative_lower_colour=None, negative_higher_colour=None,
                          erode: int = 17, dilate: int = 17) -> tuple:
    hsv_image = colourspace.bgr_to_hsv(bgr_image)
    lower_mask = hsv_image.get_in_range_mask(lower_colour.colour, higher_colour.colour)

    if negative_lower_colour is not None and negative_higher_colour is not None:
        higher_red_mask = hsv_image.get_in_range_mask(negative_lower_colour.colour, negative_higher_colour.colour)
        mask = lower_mask + higher_red_mask
    else:
        mask = lower_mask

    output_image = hsv_image.apply_mask(mask)
    opened_image = output_image.erode_rect(erode).dilate_rect(dilate)
    gray_image = colourspace.hsv_to_gray(opened_image)
    binary_image = gray_image.binary_threshold(0, 180)
    results, contours = filter_contours(binary_image, bgr_image, bgr_image.width / 40, bgr_image.width / 18)

    return results, contours


def detect_black(bgr_image: Image, lower_colour: HsvColour, higher_colour: HsvColour,
                 offset_x=TRIM_X, offset_y=TRIM_Y) -> tuple:
    cube_storage = crop_image_to_cube_storage(bgr_image, offset_x=offset_x, offset_y=offset_y)
    results = []
    contours = []
    for side in cube_storage:
        image = side[0]
        hsv_image = colourspace.bgr_to_hsv(image)
        lower_mask = hsv_image.get_in_range_mask(lower_colour.colour, higher_colour.colour)
        mask = lower_mask
        output_image = hsv_image.apply_mask(mask)
        opened_image = output_image.erode_rect(15).dilate_rect(15)
        gray_image = colourspace.hsv_to_gray(opened_image)
        binary_image = gray_image.binary_threshold(0, 80)
        # binary_image.show_on_window()
        if binary_image.width > binary_image.height:
            result, contour = filter_contours_in_cube_storage(binary_image, binary_image.width/14,
                                                              binary_image.width/3)
        else:
            result, contour = filter_contours_in_cube_storage(binary_image, 20, 50)

        for res in result:
            res.x += side[1]
            res.y += side[2]
        results.extend(result)
        contours.extend(contour)

    return results, contours


def detect_white(bgr_image: Image, lower_white: HsvColour, higher_white: HsvColour) -> tuple:
    hsv_image = colourspace.bgr_to_hsv(bgr_image)
    lower_mask = hsv_image.get_in_range_mask(lower_white.colour, higher_white.colour)
    mask = lower_mask

    output_image = hsv_image.apply_mask(mask)
    opened_image = output_image.erode_rect(15).dilate_rect(15)
    gray_image = colourspace.hsv_to_gray(opened_image)

    binary_image = gray_image.binary_threshold(0, 180)
    # binary_image.show_on_window()

    results, contours = filter_contours(binary_image, bgr_image,
                                        bgr_image.width / 45, bgr_image.width / 18)
    white_blocks = Stream(results).filter(lambda point: is_not_black_block(hsv_image, point)).toList()

    return white_blocks, contours


def is_not_black_block(hsv_image: Image, coordinate: PixelCoordinate) -> bool:
    return hsv_image[coordinate][2] > 30


def shape_matches_width(contour: np.ndarray, min_width: int, max_width: int) -> bool:
    area = cv2.contourArea(contour)
    block_min_area = min_width ** 2
    block_max_area = max_width ** 2
    perimeter_max = max_width * 4
    perimeter_min = min_width * 4

    if block_min_area < area < block_max_area:
        rc = cv2.minAreaRect(contour)

        box = cv2.boxPoints(rc)

        box_width = math.sqrt(math.pow(box[1][0] - box[0][0], 2) + math.pow(box[1][1] - box[0][1], 2))
        box_height = math.sqrt(math.pow(box[2][0] - box[1][0], 2) + math.pow(box[2][1] - box[1][1], 2))
        perimeter = cv2.arcLength(contour, True)
        if math.isclose(box_width, box_height, rel_tol=0.7) \
                and perimeter_min < perimeter < perimeter_max:
            return True

    return False


def is_point_on_table(bgr_image: Image, x: int, y: int) -> bool:
    rect = crop_to_table_by_contours(bgr_image, 50, 50)

    table = np.array([[rect[0], rect[1]], [rect[0], rect[3]], [rect[2], rect[3]], [rect[2], rect[1]]])

    if cv2.pointPolygonTest(table, (x, y), False) >= 0:
        return True

    return False


def crop_image_to_table(bgr_image: Image, offset_x: int, offset_y: int, crop_in_y=0) -> tuple:
    rect = crop_to_table_by_contours(bgr_image, offset_x, offset_y, crop_into_table=crop_in_y)
    return Image(bgr_image.frame[rect[1]:rect[3], rect[0]:rect[2]]), rect


def crop_image_to_cube_storage(bgr_image: Image, offset_x: int = 0, offset_y: int = 5) -> tuple:
    table = crop_to_table_by_contours(bgr_image)
    east = int(0.7 * bgr_image.width)
    north = int(table[1] - offset_y)
    south = int(table[3] + offset_y)
    west = int(table[2] - offset_x)
    side1 = Image(bgr_image.frame[north:north + 60, east:west])
    side2 = Image(bgr_image.frame[south - 60:south, east:west])
    side3 = Image(bgr_image.frame[north:south, west - 45:west])
    return (side1, east, north), (side2, east, south-40), (side3, west - 45, north)


def filter_contours(binary_image: Image, bgr_image: Image, min_width: int, max_width: int,
                    table=None, do_not_check_table=False) -> tuple:
    im, contours, hierarchy = binary_image.find_contours()

    results = []
    for contour in contours:
        if shape_matches_width(contour, min_width, max_width):

            rc = cv2.minAreaRect(contour)
            box = cv2.boxPoints(rc)
            sum_x = 0
            sum_y = 0

            for p in box:
                pt = (p[0], p[1])
                sum_x += pt[0]
                sum_y += pt[1]

            if table is not None:
                moy_x = int(sum_x / 4) + table[0]
                moy_y = int(sum_y / 4) + table[1] + TRIM_Y
                results.append(PixelCoordinate(moy_x, moy_y))

            else:
                moy_x = int(sum_x / 4)
                moy_y = int(sum_y / 4)

                if is_point_on_table(bgr_image, moy_x, moy_y) or do_not_check_table:
                    results.append(PixelCoordinate(moy_x, moy_y))

    return results, contours


def filter_contours_in_cube_storage(binary_image: Image, min_width: int, max_width: int) -> tuple:
    im, contours, hierarchy = binary_image.find_contours()

    results = []
    for contour in contours:
        #cv2.drawContours(binary_image.frame, contour, -1, [255, 0, 0], 2)
        #binary_image.show_on_window()
        if shape_matches_width(contour, min_width, max_width):

            rc = cv2.minAreaRect(contour)
            box = cv2.boxPoints(rc)
            sum_x = 0
            sum_y = 0

            for p in box:
                pt = (p[0], p[1])
                sum_x += pt[0]
                sum_y += pt[1]

            moy_x = int(sum_x / 4)
            moy_y = int(sum_y / 4)

            results.append(PixelCoordinate(moy_x, moy_y))

    return results, contours


def filter_contours_and_find_angles(bgr_image: Image, contours):
    angles = []

    for contour in contours:
        if shape_matches_width(contour, bgr_image.width / 40, bgr_image.width / 18):

            rc = cv2.minAreaRect(contour)
            box = cv2.boxPoints(rc)
            box = np.int0(box)
            corners = []
            for p in box:
                corners.append((int(p[0]), int(p[1])))
            dx = corners[1][0] - corners[0][0]
            dy = corners[1][1] - corners[0][1]
            if abs(dx) > 0:
                angles.append(math.atan(dy / dx) * 180 / math.pi)
            else:
                angles.append(0)
    return angles


def remove_black_block_from_results(bgr_image: Image, results: list) -> list:
    # Remove black block from results. Caused by noise...
    if results:
        block_pos = results[0]
        for result in results:
            is_block = True
            for j in range(5):
                pixel = bgr_image.frame[result.y + j][result.x - j]
                if pixel[0] < 200 and pixel[1] < 200 and pixel[2] < 200:
                    is_block = False
                    break
            if is_block:
                block_pos = result

        return [block_pos]
    else:
        return []


def in_cube_storage(bgr_image: Image, point: PixelCoordinate, offset_x: int = 15, offset_y: int = -15) -> bool:
    table = crop_to_table_by_contours(bgr_image)
    east = int(0.6 * bgr_image.width)
    north = int(table[1] - offset_y)
    south = int(table[3] + offset_y)
    west = int(table[2] + offset_x)

    if north <= point.y <= north + 45 and east <= point.x <= west:
        return True
    if south - 45 <= point.y <= south and east <= point.x <= west:
        return True
    if north <= point.y <= south and west-45 <= point.x <= west:
        return True
    return False