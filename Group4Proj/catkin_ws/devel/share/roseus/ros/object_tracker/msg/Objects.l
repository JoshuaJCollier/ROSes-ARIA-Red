;; Auto-generated. Do not edit!


(when (boundp 'object_tracker::Objects)
  (if (not (find-package "OBJECT_TRACKER"))
    (make-package "OBJECT_TRACKER"))
  (shadow 'Objects (find-package "OBJECT_TRACKER")))
(unless (find-package "OBJECT_TRACKER::OBJECTS")
  (make-package "OBJECT_TRACKER::OBJECTS"))

(in-package "ROS")
;;//! \htmlinclude Objects.msg.html


(defclass object_tracker::Objects
  :super ros::object
  :slots (_cone _bucket _obstacle _bucketDist _time ))

(defmethod object_tracker::Objects
  (:init
   (&key
    ((:cone __cone) 0)
    ((:bucket __bucket) 0)
    ((:obstacle __obstacle) 0)
    ((:bucketDist __bucketDist) 0.0)
    ((:time __time) 0.0)
    )
   (send-super :init)
   (setq _cone (round __cone))
   (setq _bucket (round __bucket))
   (setq _obstacle (round __obstacle))
   (setq _bucketDist (float __bucketDist))
   (setq _time (float __time))
   self)
  (:cone
   (&optional __cone)
   (if __cone (setq _cone __cone)) _cone)
  (:bucket
   (&optional __bucket)
   (if __bucket (setq _bucket __bucket)) _bucket)
  (:obstacle
   (&optional __obstacle)
   (if __obstacle (setq _obstacle __obstacle)) _obstacle)
  (:bucketDist
   (&optional __bucketDist)
   (if __bucketDist (setq _bucketDist __bucketDist)) _bucketDist)
  (:time
   (&optional __time)
   (if __time (setq _time __time)) _time)
  (:serialization-length
   ()
   (+
    ;; int32 _cone
    4
    ;; int32 _bucket
    4
    ;; int32 _obstacle
    4
    ;; float64 _bucketDist
    8
    ;; float64 _time
    8
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;; int32 _cone
       (write-long _cone s)
     ;; int32 _bucket
       (write-long _bucket s)
     ;; int32 _obstacle
       (write-long _obstacle s)
     ;; float64 _bucketDist
       (sys::poke _bucketDist (send s :buffer) (send s :count) :double) (incf (stream-count s) 8)
     ;; float64 _time
       (sys::poke _time (send s :buffer) (send s :count) :double) (incf (stream-count s) 8)
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;; int32 _cone
     (setq _cone (sys::peek buf ptr- :integer)) (incf ptr- 4)
   ;; int32 _bucket
     (setq _bucket (sys::peek buf ptr- :integer)) (incf ptr- 4)
   ;; int32 _obstacle
     (setq _obstacle (sys::peek buf ptr- :integer)) (incf ptr- 4)
   ;; float64 _bucketDist
     (setq _bucketDist (sys::peek buf ptr- :double)) (incf ptr- 8)
   ;; float64 _time
     (setq _time (sys::peek buf ptr- :double)) (incf ptr- 8)
   ;;
   self)
  )

(setf (get object_tracker::Objects :md5sum-) "57c2ce73fa9cbfd6f321f8c8cacc21d6")
(setf (get object_tracker::Objects :datatype-) "object_tracker/Objects")
(setf (get object_tracker::Objects :definition-)
      "int32 cone
int32 bucket
int32 obstacle
float64 bucketDist
float64 time

")



(provide :object_tracker/Objects "57c2ce73fa9cbfd6f321f8c8cacc21d6")


