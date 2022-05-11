;; Auto-generated. Do not edit!


(when (boundp 'megamind::CurrentGoal)
  (if (not (find-package "MEGAMIND"))
    (make-package "MEGAMIND"))
  (shadow 'CurrentGoal (find-package "MEGAMIND")))
(unless (find-package "MEGAMIND::CURRENTGOAL")
  (make-package "MEGAMIND::CURRENTGOAL"))

(in-package "ROS")
;;//! \htmlinclude CurrentGoal.msg.html


(defclass megamind::CurrentGoal
  :super ros::object
  :slots (_currentGoal ))

(defmethod megamind::CurrentGoal
  (:init
   (&key
    ((:currentGoal __currentGoal) 0)
    )
   (send-super :init)
   (setq _currentGoal (round __currentGoal))
   self)
  (:currentGoal
   (&optional __currentGoal)
   (if __currentGoal (setq _currentGoal __currentGoal)) _currentGoal)
  (:serialization-length
   ()
   (+
    ;; int64 _currentGoal
    8
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;; int64 _currentGoal
#+(or :alpha :irix6 :x86_64)
       (progn (sys::poke _currentGoal (send s :buffer) (send s :count) :long) (incf (stream-count s) 8))
#-(or :alpha :irix6 :x86_64)
       (cond ((and (class _currentGoal) (= (length (_currentGoal . bv)) 2)) ;; bignum
              (write-long (ash (elt (_currentGoal . bv) 0) 0) s)
              (write-long (ash (elt (_currentGoal . bv) 1) -1) s))
             ((and (class _currentGoal) (= (length (_currentGoal . bv)) 1)) ;; big1
              (write-long (elt (_currentGoal . bv) 0) s)
              (write-long (if (>= _currentGoal 0) 0 #xffffffff) s))
             (t                                         ;; integer
              (write-long _currentGoal s)(write-long (if (>= _currentGoal 0) 0 #xffffffff) s)))
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;; int64 _currentGoal
#+(or :alpha :irix6 :x86_64)
      (setf _currentGoal (prog1 (sys::peek buf ptr- :long) (incf ptr- 8)))
#-(or :alpha :irix6 :x86_64)
      (setf _currentGoal (let ((b0 (prog1 (sys::peek buf ptr- :integer) (incf ptr- 4)))
                  (b1 (prog1 (sys::peek buf ptr- :integer) (incf ptr- 4))))
              (cond ((= b1 -1) b0)
                     ((and (= b1  0)
                           (<= lisp::most-negative-fixnum b0 lisp::most-positive-fixnum))
                      b0)
                    ((= b1  0) (make-instance bignum :size 1 :bv (integer-vector b0)))
                    (t (make-instance bignum :size 2 :bv (integer-vector b0 (ash b1 1)))))))
   ;;
   self)
  )

(setf (get megamind::CurrentGoal :md5sum-) "0ca78cdf9677c9a77eeaeddd9e2b5143")
(setf (get megamind::CurrentGoal :datatype-) "megamind/CurrentGoal")
(setf (get megamind::CurrentGoal :definition-)
      "int64 currentGoal

")



(provide :megamind/CurrentGoal "0ca78cdf9677c9a77eeaeddd9e2b5143")


