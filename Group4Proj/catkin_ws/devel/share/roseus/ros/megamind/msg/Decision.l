;; Auto-generated. Do not edit!


(when (boundp 'megamind::Decision)
  (if (not (find-package "MEGAMIND"))
    (make-package "MEGAMIND"))
  (shadow 'Decision (find-package "MEGAMIND")))
(unless (find-package "MEGAMIND::DECISION")
  (make-package "MEGAMIND::DECISION"))

(in-package "ROS")
;;//! \htmlinclude Decision.msg.html


(defclass megamind::Decision
  :super ros::object
  :slots (_currentGoal _startHeading _startTime _gps_travel_on _mindState ))

(defmethod megamind::Decision
  (:init
   (&key
    ((:currentGoal __currentGoal) 0)
    ((:startHeading __startHeading) 0.0)
    ((:startTime __startTime) 0.0)
    ((:gps_travel_on __gps_travel_on) 0)
    ((:mindState __mindState) 0)
    )
   (send-super :init)
   (setq _currentGoal (round __currentGoal))
   (setq _startHeading (float __startHeading))
   (setq _startTime (float __startTime))
   (setq _gps_travel_on (round __gps_travel_on))
   (setq _mindState (round __mindState))
   self)
  (:currentGoal
   (&optional __currentGoal)
   (if __currentGoal (setq _currentGoal __currentGoal)) _currentGoal)
  (:startHeading
   (&optional __startHeading)
   (if __startHeading (setq _startHeading __startHeading)) _startHeading)
  (:startTime
   (&optional __startTime)
   (if __startTime (setq _startTime __startTime)) _startTime)
  (:gps_travel_on
   (&optional __gps_travel_on)
   (if __gps_travel_on (setq _gps_travel_on __gps_travel_on)) _gps_travel_on)
  (:mindState
   (&optional __mindState)
   (if __mindState (setq _mindState __mindState)) _mindState)
  (:serialization-length
   ()
   (+
    ;; int32 _currentGoal
    4
    ;; float32 _startHeading
    4
    ;; float32 _startTime
    4
    ;; int32 _gps_travel_on
    4
    ;; int32 _mindState
    4
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;; int32 _currentGoal
       (write-long _currentGoal s)
     ;; float32 _startHeading
       (sys::poke _startHeading (send s :buffer) (send s :count) :float) (incf (stream-count s) 4)
     ;; float32 _startTime
       (sys::poke _startTime (send s :buffer) (send s :count) :float) (incf (stream-count s) 4)
     ;; int32 _gps_travel_on
       (write-long _gps_travel_on s)
     ;; int32 _mindState
       (write-long _mindState s)
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;; int32 _currentGoal
     (setq _currentGoal (sys::peek buf ptr- :integer)) (incf ptr- 4)
   ;; float32 _startHeading
     (setq _startHeading (sys::peek buf ptr- :float)) (incf ptr- 4)
   ;; float32 _startTime
     (setq _startTime (sys::peek buf ptr- :float)) (incf ptr- 4)
   ;; int32 _gps_travel_on
     (setq _gps_travel_on (sys::peek buf ptr- :integer)) (incf ptr- 4)
   ;; int32 _mindState
     (setq _mindState (sys::peek buf ptr- :integer)) (incf ptr- 4)
   ;;
   self)
  )

(setf (get megamind::Decision :md5sum-) "af844dac541f02d8db9a23f015cc9488")
(setf (get megamind::Decision :datatype-) "megamind/Decision")
(setf (get megamind::Decision :definition-)
      "int32 currentGoal
float32 startHeading
float32 startTime
int32 gps_travel_on
int32 mindState

")



(provide :megamind/Decision "af844dac541f02d8db9a23f015cc9488")


