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
  :slots (_cone _bucket _obstacle _coneDist _bucketDist _obstacleDist _coneSize _bucketSize _obstacleSize _time ))

(defmethod object_tracker::Objects
  (:init
   (&key
    ((:cone __cone) 0)
    ((:bucket __bucket) 0)
    ((:obstacle __obstacle) 0)
    ((:coneDist __coneDist) 0.0)
    ((:bucketDist __bucketDist) 0.0)
    ((:obstacleDist __obstacleDist) 0.0)
    ((:coneSize __coneSize) 0.0)
    ((:bucketSize __bucketSize) 0.0)
    ((:obstacleSize __obstacleSize) 0.0)
    ((:time __time) 0.0)
    )
   (send-super :init)
   (setq _cone (round __cone))
   (setq _bucket (round __bucket))
   (setq _obstacle (round __obstacle))
   (setq _coneDist (float __coneDist))
   (setq _bucketDist (float __bucketDist))
   (setq _obstacleDist (float __obstacleDist))
   (setq _coneSize (float __coneSize))
   (setq _bucketSize (float __bucketSize))
   (setq _obstacleSize (float __obstacleSize))
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
  (:coneDist
   (&optional __coneDist)
   (if __coneDist (setq _coneDist __coneDist)) _coneDist)
  (:bucketDist
   (&optional __bucketDist)
   (if __bucketDist (setq _bucketDist __bucketDist)) _bucketDist)
  (:obstacleDist
   (&optional __obstacleDist)
   (if __obstacleDist (setq _obstacleDist __obstacleDist)) _obstacleDist)
  (:coneSize
   (&optional __coneSize)
   (if __coneSize (setq _coneSize __coneSize)) _coneSize)
  (:bucketSize
   (&optional __bucketSize)
   (if __bucketSize (setq _bucketSize __bucketSize)) _bucketSize)
  (:obstacleSize
   (&optional __obstacleSize)
   (if __obstacleSize (setq _obstacleSize __obstacleSize)) _obstacleSize)
  (:time
   (&optional __time)
   (if __time (setq _time __time)) _time)
  (:serialization-length
   ()
   (+
    ;; int64 _cone
    8
    ;; int64 _bucket
    8
    ;; int64 _obstacle
    8
    ;; float64 _coneDist
    8
    ;; float64 _bucketDist
    8
    ;; float64 _obstacleDist
    8
    ;; float64 _coneSize
    8
    ;; float64 _bucketSize
    8
    ;; float64 _obstacleSize
    8
    ;; float64 _time
    8
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;; int64 _cone
#+(or :alpha :irix6 :x86_64)
       (progn (sys::poke _cone (send s :buffer) (send s :count) :long) (incf (stream-count s) 8))
#-(or :alpha :irix6 :x86_64)
       (cond ((and (class _cone) (= (length (_cone . bv)) 2)) ;; bignum
              (write-long (ash (elt (_cone . bv) 0) 0) s)
              (write-long (ash (elt (_cone . bv) 1) -1) s))
             ((and (class _cone) (= (length (_cone . bv)) 1)) ;; big1
              (write-long (elt (_cone . bv) 0) s)
              (write-long (if (>= _cone 0) 0 #xffffffff) s))
             (t                                         ;; integer
              (write-long _cone s)(write-long (if (>= _cone 0) 0 #xffffffff) s)))
     ;; int64 _bucket
#+(or :alpha :irix6 :x86_64)
       (progn (sys::poke _bucket (send s :buffer) (send s :count) :long) (incf (stream-count s) 8))
#-(or :alpha :irix6 :x86_64)
       (cond ((and (class _bucket) (= (length (_bucket . bv)) 2)) ;; bignum
              (write-long (ash (elt (_bucket . bv) 0) 0) s)
              (write-long (ash (elt (_bucket . bv) 1) -1) s))
             ((and (class _bucket) (= (length (_bucket . bv)) 1)) ;; big1
              (write-long (elt (_bucket . bv) 0) s)
              (write-long (if (>= _bucket 0) 0 #xffffffff) s))
             (t                                         ;; integer
              (write-long _bucket s)(write-long (if (>= _bucket 0) 0 #xffffffff) s)))
     ;; int64 _obstacle
#+(or :alpha :irix6 :x86_64)
       (progn (sys::poke _obstacle (send s :buffer) (send s :count) :long) (incf (stream-count s) 8))
#-(or :alpha :irix6 :x86_64)
       (cond ((and (class _obstacle) (= (length (_obstacle . bv)) 2)) ;; bignum
              (write-long (ash (elt (_obstacle . bv) 0) 0) s)
              (write-long (ash (elt (_obstacle . bv) 1) -1) s))
             ((and (class _obstacle) (= (length (_obstacle . bv)) 1)) ;; big1
              (write-long (elt (_obstacle . bv) 0) s)
              (write-long (if (>= _obstacle 0) 0 #xffffffff) s))
             (t                                         ;; integer
              (write-long _obstacle s)(write-long (if (>= _obstacle 0) 0 #xffffffff) s)))
     ;; float64 _coneDist
       (sys::poke _coneDist (send s :buffer) (send s :count) :double) (incf (stream-count s) 8)
     ;; float64 _bucketDist
       (sys::poke _bucketDist (send s :buffer) (send s :count) :double) (incf (stream-count s) 8)
     ;; float64 _obstacleDist
       (sys::poke _obstacleDist (send s :buffer) (send s :count) :double) (incf (stream-count s) 8)
     ;; float64 _coneSize
       (sys::poke _coneSize (send s :buffer) (send s :count) :double) (incf (stream-count s) 8)
     ;; float64 _bucketSize
       (sys::poke _bucketSize (send s :buffer) (send s :count) :double) (incf (stream-count s) 8)
     ;; float64 _obstacleSize
       (sys::poke _obstacleSize (send s :buffer) (send s :count) :double) (incf (stream-count s) 8)
     ;; float64 _time
       (sys::poke _time (send s :buffer) (send s :count) :double) (incf (stream-count s) 8)
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;; int64 _cone
#+(or :alpha :irix6 :x86_64)
      (setf _cone (prog1 (sys::peek buf ptr- :long) (incf ptr- 8)))
#-(or :alpha :irix6 :x86_64)
      (setf _cone (let ((b0 (prog1 (sys::peek buf ptr- :integer) (incf ptr- 4)))
                  (b1 (prog1 (sys::peek buf ptr- :integer) (incf ptr- 4))))
              (cond ((= b1 -1) b0)
                     ((and (= b1  0)
                           (<= lisp::most-negative-fixnum b0 lisp::most-positive-fixnum))
                      b0)
                    ((= b1  0) (make-instance bignum :size 1 :bv (integer-vector b0)))
                    (t (make-instance bignum :size 2 :bv (integer-vector b0 (ash b1 1)))))))
   ;; int64 _bucket
#+(or :alpha :irix6 :x86_64)
      (setf _bucket (prog1 (sys::peek buf ptr- :long) (incf ptr- 8)))
#-(or :alpha :irix6 :x86_64)
      (setf _bucket (let ((b0 (prog1 (sys::peek buf ptr- :integer) (incf ptr- 4)))
                  (b1 (prog1 (sys::peek buf ptr- :integer) (incf ptr- 4))))
              (cond ((= b1 -1) b0)
                     ((and (= b1  0)
                           (<= lisp::most-negative-fixnum b0 lisp::most-positive-fixnum))
                      b0)
                    ((= b1  0) (make-instance bignum :size 1 :bv (integer-vector b0)))
                    (t (make-instance bignum :size 2 :bv (integer-vector b0 (ash b1 1)))))))
   ;; int64 _obstacle
#+(or :alpha :irix6 :x86_64)
      (setf _obstacle (prog1 (sys::peek buf ptr- :long) (incf ptr- 8)))
#-(or :alpha :irix6 :x86_64)
      (setf _obstacle (let ((b0 (prog1 (sys::peek buf ptr- :integer) (incf ptr- 4)))
                  (b1 (prog1 (sys::peek buf ptr- :integer) (incf ptr- 4))))
              (cond ((= b1 -1) b0)
                     ((and (= b1  0)
                           (<= lisp::most-negative-fixnum b0 lisp::most-positive-fixnum))
                      b0)
                    ((= b1  0) (make-instance bignum :size 1 :bv (integer-vector b0)))
                    (t (make-instance bignum :size 2 :bv (integer-vector b0 (ash b1 1)))))))
   ;; float64 _coneDist
     (setq _coneDist (sys::peek buf ptr- :double)) (incf ptr- 8)
   ;; float64 _bucketDist
     (setq _bucketDist (sys::peek buf ptr- :double)) (incf ptr- 8)
   ;; float64 _obstacleDist
     (setq _obstacleDist (sys::peek buf ptr- :double)) (incf ptr- 8)
   ;; float64 _coneSize
     (setq _coneSize (sys::peek buf ptr- :double)) (incf ptr- 8)
   ;; float64 _bucketSize
     (setq _bucketSize (sys::peek buf ptr- :double)) (incf ptr- 8)
   ;; float64 _obstacleSize
     (setq _obstacleSize (sys::peek buf ptr- :double)) (incf ptr- 8)
   ;; float64 _time
     (setq _time (sys::peek buf ptr- :double)) (incf ptr- 8)
   ;;
   self)
  )

(setf (get object_tracker::Objects :md5sum-) "c409bb10f65ba63532d5faef2c6ec1be")
(setf (get object_tracker::Objects :datatype-) "object_tracker/Objects")
(setf (get object_tracker::Objects :definition-)
      "int64 cone
int64 bucket
int64 obstacle
float64 coneDist
float64 bucketDist
float64 obstacleDist
float64 coneSize
float64 bucketSize
float64 obstacleSize
float64 time

")



(provide :object_tracker/Objects "c409bb10f65ba63532d5faef2c6ec1be")


