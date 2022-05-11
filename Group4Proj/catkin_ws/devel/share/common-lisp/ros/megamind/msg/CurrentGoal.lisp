; Auto-generated. Do not edit!


(cl:in-package megamind-msg)


;//! \htmlinclude CurrentGoal.msg.html

(cl:defclass <CurrentGoal> (roslisp-msg-protocol:ros-message)
  ((currentGoal
    :reader currentGoal
    :initarg :currentGoal
    :type cl:integer
    :initform 0))
)

(cl:defclass CurrentGoal (<CurrentGoal>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <CurrentGoal>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'CurrentGoal)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name megamind-msg:<CurrentGoal> is deprecated: use megamind-msg:CurrentGoal instead.")))

(cl:ensure-generic-function 'currentGoal-val :lambda-list '(m))
(cl:defmethod currentGoal-val ((m <CurrentGoal>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader megamind-msg:currentGoal-val is deprecated.  Use megamind-msg:currentGoal instead.")
  (currentGoal m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <CurrentGoal>) ostream)
  "Serializes a message object of type '<CurrentGoal>"
  (cl:let* ((signed (cl:slot-value msg 'currentGoal)) (unsigned (cl:if (cl:< signed 0) (cl:+ signed 18446744073709551616) signed)))
    (cl:write-byte (cl:ldb (cl:byte 8 0) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 32) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 40) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 48) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 56) unsigned) ostream)
    )
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <CurrentGoal>) istream)
  "Deserializes a message object of type '<CurrentGoal>"
    (cl:let ((unsigned 0))
      (cl:setf (cl:ldb (cl:byte 8 0) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 32) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 40) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 48) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 56) unsigned) (cl:read-byte istream))
      (cl:setf (cl:slot-value msg 'currentGoal) (cl:if (cl:< unsigned 9223372036854775808) unsigned (cl:- unsigned 18446744073709551616))))
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<CurrentGoal>)))
  "Returns string type for a message object of type '<CurrentGoal>"
  "megamind/CurrentGoal")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'CurrentGoal)))
  "Returns string type for a message object of type 'CurrentGoal"
  "megamind/CurrentGoal")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<CurrentGoal>)))
  "Returns md5sum for a message object of type '<CurrentGoal>"
  "0ca78cdf9677c9a77eeaeddd9e2b5143")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'CurrentGoal)))
  "Returns md5sum for a message object of type 'CurrentGoal"
  "0ca78cdf9677c9a77eeaeddd9e2b5143")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<CurrentGoal>)))
  "Returns full string definition for message of type '<CurrentGoal>"
  (cl:format cl:nil "int64 currentGoal~%~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'CurrentGoal)))
  "Returns full string definition for message of type 'CurrentGoal"
  (cl:format cl:nil "int64 currentGoal~%~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <CurrentGoal>))
  (cl:+ 0
     8
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <CurrentGoal>))
  "Converts a ROS message object to a list"
  (cl:list 'CurrentGoal
    (cl:cons ':currentGoal (currentGoal msg))
))
