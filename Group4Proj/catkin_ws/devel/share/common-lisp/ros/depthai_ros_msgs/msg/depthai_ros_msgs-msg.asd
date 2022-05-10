
(cl:in-package :asdf)

(defsystem "depthai_ros_msgs-msg"
  :depends-on (:roslisp-msg-protocol :roslisp-utils :geometry_msgs-msg
               :std_msgs-msg
               :vision_msgs-msg
)
  :components ((:file "_package")
    (:file "AutoFocusCtrl" :depends-on ("_package_AutoFocusCtrl"))
    (:file "_package_AutoFocusCtrl" :depends-on ("_package"))
    (:file "HandLandmark" :depends-on ("_package_HandLandmark"))
    (:file "_package_HandLandmark" :depends-on ("_package"))
    (:file "HandLandmarkArray" :depends-on ("_package_HandLandmarkArray"))
    (:file "_package_HandLandmarkArray" :depends-on ("_package"))
    (:file "SpatialDetection" :depends-on ("_package_SpatialDetection"))
    (:file "_package_SpatialDetection" :depends-on ("_package"))
    (:file "SpatialDetectionArray" :depends-on ("_package_SpatialDetectionArray"))
    (:file "_package_SpatialDetectionArray" :depends-on ("_package"))
  ))