#include "opencv2/imgcodecs.hpp"
#include "opencv2/highgui.hpp"
#include "opencv2/imgproc.hpp"

#include <iostream>

using namespace std;
using namespace cv;

#define filname "Resources/IMG_2112.png"

///// Colour Detection  /////


class colourDetect {
	//original image 
	Mat img;

	//store the converted image 
	Mat imgHSV;

	//show colour detected image mask
	Mat mask;

	void importImage() {
		//defining the path of the image stored in the project
		String path = filename;

		//read the image on the matrix from the path provided
		//Mat : matrix data type in open cv to handle all the images
		img = imread(path);

		//show the image 
		//imshow(nameOfTheImage,imageMatrix)
		imshow("Image", img);
	}

	//convert the image to hsv space 
	//easier to detect the color 
	//alternative to rgb colour model 
	//parts: saturation hue and value 
	void convertToHSV() {

		//convert the RGB image to HSV image 
		cvtColor(img, imgHSV, COLOR_BGR2HSV);

		//display the HSV image 
		imshow("HSV Image", imgHSV);
	}

	//track-bars to find the min and max values of hsv colour model
	void trackBarToDetectColour() {
		//window to track the value of HSV min and max
		namedWindow("TrackBars", (640, 200));

		//variables to store the min and max values
		int hMin = 0, sMin = 0, vMin = 0;
		int hMax = 179, sMax = 255, vMax = 255;

		//vlaues got with the help of trackbars
		//hMin = 0, sMin = 114, vMin = 165;
		//hMax = 21, sMax = 255, vMax = 255;

		//creating 6 track bars
		createTrackbar("Hue min", "TrackBars", &hMin, 179);
		createTrackbar("Hue max", "TrackBars", &hMax, 179);
		createTrackbar("Sat min", "TrackBars", &sMin, 255);
		createTrackbar("Sat max", "TrackBars", &sMax, 255);
		createTrackbar("Val min", "TrackBars", &vMin, 255);
		createTrackbar("Val max", "TrackBars", &vMax, 255);

		while (true) {
			//HSV : hue saturation value
			//min :  light and max : bright
			Scalar lower(hMin, sMin, vMin);
			Scalar upper(hMax, sMax, vMax);

			//searching the colour belonging to the particular range and assigning to mask image 
			//everything will become black and white portion depicts the colour in the image 
			inRange(imgHSV, lower, upper, mask);

			//displaying the mask image 
			imshow("Mask Imaging", mask);

			waitKey(1);
		}
	}

	//inRange function : collect the colour 
	//because of the shadow the colours in the image will be within a range 
	//detecting the colours in the particular range : here Orange 
	void detectColour() {
		//searching Orange Colour 
		int hMin = 0, sMin = 110, vMin = 153;
		int hMax = 19, sMax = 240, vMax = 255;

		//HSV : hue saturation value
		//min :  light and max : bright
		Scalar lower(hMin, sMin, vMin);
		Scalar upper(hMax, sMax, vMax);

		//searching the colour belonging to the particular range and assigning to mask image 
		//everything will become black and white portion depicts the colour in the image 
		inRange(imgHSV, lower, upper, mask);

		//displaying the mask image 
		imshow("Mask Image", mask);
	}

public:
	void initClass() {
		importImage();
		convertToHSV();
		//trackBarToDetectColour();
		//detecting the colour after tracking the colour using trackbars
		detectColour();
		waitKey(0);
	}
};

int main() {
	colourDetect detect;
	detect.initClass();
	return 0;
}