## *********************************************************
##
## File autogenerated for the rosaria package
## by the dynamic_reconfigure package.
## Please do not edit.
##
## ********************************************************/

from dynamic_reconfigure.encoding import extract_params

inf = float('inf')

config_description = {'name': 'Default', 'type': '', 'state': True, 'cstate': 'true', 'id': 0, 'parent': 0, 'parameters': [{'name': 'trans_accel', 'type': 'double', 'default': 0, 'level': 0, 'description': 'Translational acceleration (m/s^2)', 'min': -inf, 'max': inf, 'srcline': 291, 'srcfile': '/opt/ros/noetic/lib/python3/dist-packages/dynamic_reconfigure/parameter_generator_catkin.py', 'edit_method': '', 'ctype': 'double', 'cconsttype': 'const double'}, {'name': 'trans_decel', 'type': 'double', 'default': 0, 'level': 0, 'description': 'Translational deceleration (m/s^2)', 'min': -inf, 'max': inf, 'srcline': 291, 'srcfile': '/opt/ros/noetic/lib/python3/dist-packages/dynamic_reconfigure/parameter_generator_catkin.py', 'edit_method': '', 'ctype': 'double', 'cconsttype': 'const double'}, {'name': 'lat_accel', 'type': 'double', 'default': 0, 'level': 0, 'description': 'Lateral acceleration (m/s^2)', 'min': -inf, 'max': inf, 'srcline': 291, 'srcfile': '/opt/ros/noetic/lib/python3/dist-packages/dynamic_reconfigure/parameter_generator_catkin.py', 'edit_method': '', 'ctype': 'double', 'cconsttype': 'const double'}, {'name': 'lat_decel', 'type': 'double', 'default': 0, 'level': 0, 'description': 'Lateral deceleration (m/s^2)', 'min': -inf, 'max': inf, 'srcline': 291, 'srcfile': '/opt/ros/noetic/lib/python3/dist-packages/dynamic_reconfigure/parameter_generator_catkin.py', 'edit_method': '', 'ctype': 'double', 'cconsttype': 'const double'}, {'name': 'rot_accel', 'type': 'double', 'default': 0, 'level': 0, 'description': 'Rotational acceleration (rad/s^2)', 'min': -inf, 'max': inf, 'srcline': 291, 'srcfile': '/opt/ros/noetic/lib/python3/dist-packages/dynamic_reconfigure/parameter_generator_catkin.py', 'edit_method': '', 'ctype': 'double', 'cconsttype': 'const double'}, {'name': 'rot_decel', 'type': 'double', 'default': 0, 'level': 0, 'description': 'Rotational deceleration (rad/s^2)', 'min': -inf, 'max': inf, 'srcline': 291, 'srcfile': '/opt/ros/noetic/lib/python3/dist-packages/dynamic_reconfigure/parameter_generator_catkin.py', 'edit_method': '', 'ctype': 'double', 'cconsttype': 'const double'}, {'name': 'TicksMM', 'type': 'int', 'default': 0, 'level': 0, 'description': 'Encoder ticks/mm, or 0 to disable and use robot internal setting', 'min': -2147483648, 'max': 2147483647, 'srcline': 291, 'srcfile': '/opt/ros/noetic/lib/python3/dist-packages/dynamic_reconfigure/parameter_generator_catkin.py', 'edit_method': '', 'ctype': 'int', 'cconsttype': 'const int'}, {'name': 'DriftFactor', 'type': 'int', 'default': -99999, 'level': 0, 'description': 'Value in 1/8192 increments to be added or subtracted from the left encoder ticks in order to compensate for tire differences. Or -99999 to disable and use robot internal setting', 'min': -2147483648, 'max': 2147483647, 'srcline': 291, 'srcfile': '/opt/ros/noetic/lib/python3/dist-packages/dynamic_reconfigure/parameter_generator_catkin.py', 'edit_method': '', 'ctype': 'int', 'cconsttype': 'const int'}, {'name': 'RevCount', 'type': 'int', 'default': 0, 'level': 0, 'description': 'The number of differential encoder ticks for a 180-degree revolution of the robot.Or 0 to disable and use robot internal setting.', 'min': -2147483648, 'max': 2147483647, 'srcline': 291, 'srcfile': '/opt/ros/noetic/lib/python3/dist-packages/dynamic_reconfigure/parameter_generator_catkin.py', 'edit_method': '', 'ctype': 'int', 'cconsttype': 'const int'}], 'groups': [], 'srcline': 246, 'srcfile': '/opt/ros/noetic/lib/python3/dist-packages/dynamic_reconfigure/parameter_generator_catkin.py', 'class': 'DEFAULT', 'parentclass': '', 'parentname': 'Default', 'field': 'default', 'upper': 'DEFAULT', 'lower': 'groups'}

min = {}
max = {}
defaults = {}
level = {}
type = {}
all_level = 0

#def extract_params(config):
#    params = []
#    params.extend(config['parameters'])
#    for group in config['groups']:
#        params.extend(extract_params(group))
#    return params

for param in extract_params(config_description):
    min[param['name']] = param['min']
    max[param['name']] = param['max']
    defaults[param['name']] = param['default']
    level[param['name']] = param['level']
    type[param['name']] = param['type']
    all_level = all_level | param['level']

