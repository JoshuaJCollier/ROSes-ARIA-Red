; Auto-generated. Do not edit!


(cl:in-package megamind-msg)


;//! \htmlinclude Decision.msg.html

(cl:defclass <Decision> (roslisp-msg-protocol:ros-message)
  ((currentGoal
    :reader currentGoal
    :initarg :currentGoal
    :type cl:integer
    :initform 0)
   (startHeading
    :reader startHeading
    :initarg :startHeading
    :type cl:float
    :initform 0.0)
   (startTime
    :reader startTime
    :initarg :startTime
    :type cl:float
    :initform 0.0)
   (gps_travel_on
    :reader gps_travel_on
    :initarg :gps_travel_on
    :type cl:integer
    :initform 0)
   (mindState
    :reader mindState
    :initarg :mindState
    :type cl:integer
    :initform 0))
)

(cl:defclass Decision (<Decision>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <Decision>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'Decision)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name megamind-msg:<Decision> is deprecated: use megamind-msg:Decision instead.")))

(cl:ensure-generic-function 'currentGoal-val :lambda-list '(m))
(cl:defmethod currentGoal-val ((m <Decision>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader megamind-msg:currentGoal-val is deprecated.  Use megamind-msg:currentGoal instead.")
  (currentGoal m))

(cl:ensure-generic-function 'startHeading-val :lambda-list '(m))
(cl:defmethod startHeading-val ((m <Decision>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader megamind-msg:startHeading-val is deprecated.  Use megamind-msg:startHeading instead.")
  (startHeading m))

(cl:ensure-generic-function 'startTime-val :lambda-list '(m))
(cl:defmethod startTime-val ((m <Decision>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader megamind-msg:startTime-val is deprecated.  Use megamind-msg:startTime instead.")
  (startTime m))

(cl:ensure-generic-function 'gps_travel_on-val :lambda-list '(m))
(cl:defmethod gps_travel_on-val ((m <Decision>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader megamind-msg:gps_travel_on-val is deprecated.  Use megamind-msg:gps_travel_on instead.")
  (gps_travel_on m))

(cl:ensure-generic-function 'mindState-val :lambda-list '(m))
(cl:defmethod mindState-val ((m <Decision>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader megamind-msg:mindState-val is deprecated.  Use megamind-msg:mindState instead.")
  (mindState m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <Decision>) ostream)
  "Serializes a message object of type '<Decision>"
  (cl:let* ((signed (cl:slot-value msg 'currentGoal)) (unsigned (cl:if (cl:< signed 0) (cl:+ signed 4294967296) signed)))
    (cl:write-byte (cl:ldb (cl:byte 8 0) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) unsigned) ostream)
    )
  (cl:let ((bits (roslisp-utils:encode-single-float-bits (cl:slot-value msg 'startHeading))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) bits) ostream))
  (cl:let ((bits (roslisp-utils:encode-single-float-bits (cl:slot-value msg 'startTime))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) bits) ostream))
  (cl:let* ((signed (cl:slot-value msg 'gps_travel_on)) (unsigned (cl:if (cl:< signed 0) (cl:+ signed 4294967296) signed)))
    (cl:write-byte (cl:ldb (cl:byte 8 0) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) unsigned) ostream)
    )
  (cl:let* ((signed (cl:slot-value msg 'mindState)) (unsigned (cl:if (cl:< signed 0) (cl:+ signed 4294967296) signed)))
    (cl:write-byte (cl:ldb (cl:byte 8 0) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) unsigned) ostream)
    )
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <Decision>) istream)
  "Deserializes a message object of type '<Decision>"
    (cl:let ((unsigned 0))
      (cl:setf (cl:ldb (cl:byte 8 0) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) unsigned) (cl:read-byte istream))
      (cl:setf (cl:slot-value msg 'currentGoal) (cl:if (cl:< unsigned 2147483648) unsigned (cl:- unsigned 4294967296))))
    (cl:let ((bits 0))
      (cl:setf (cl:ldb (cl:byte 8 0) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) bits) (cl:read-byte istream))
    (cl:setf (cl:slot-value msg 'startHeading) (roslisp-utils:decode-single-float-bits bits)))
    (cl:let ((bits 0))
      (cl:setf (cl:ldb (cl:byte 8 0) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) bits) (cl:read-byte istream))
    (cl:setf (cl:slot-value msg 'startTime) (roslisp-utils:decode-single-float-bits bits)))
    (cl:let ((unsigned 0))
      (cl:setf (cl:ldb (cl:byte 8 0) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) unsigned) (cl:read-byte istream))
      (cl:setf (cl:slot-value msg 'gps_travel_on) (cl:if (cl:< unsigned 2147483648) unsigned (cl:- unsigned 4294967296))))
    (cl:let ((unsigned 0))
      (cl:setf (cl:ldb (cl:byte 8 0) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) unsigned) (cl:read-byte istream))
      (cl:setf (cl:slot-value msg 'mindState) (cl:if (cl:< unsigned 2147483648) unsigned (cl:- unsigned 4294967296))))
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<Decision>)))
  "Returns string type for a message object of type '<Decision>"
  "megamind/Decision")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'Decision)))
  "Returns string type for a message object of type 'Decision"
  "megamind/Decision")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<Decision>)))
  "Returns md5sum for a message object of type '<Decision>"
  "af844dac541f02d8db9a23f015cc9488")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'Decision)))
  "Returns md5sum for a message object of type 'Decision"
  "af844dac541f02d8db9a23f015cc9488")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<Decision>)))
  "Returns full string definition for message of type '<Decision>"
  (cl:format cl:nil "int32 currentGoal~%float32 startHeading~%float32 startTime~%int32 gps_travel_on~%int32 mindState~%~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'Decision)))
  "Returns full string definition for message of type 'Decision"
  (cl:format cl:nil "int32 currentGoal~%float32 startHeading~%float32 startTime~%int32 gps_travel_on~%int32 mindState~%~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <Decision>))
  (cl:+ 0
     4
     4
     4
     4
     4
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <Decision>))
  "Converts a ROS message object to a list"
  (cl:list 'Decision
    (cl:cons ':currentGoal (currentGoal msg))
    (cl:cons ':startHeading (startHeading msg))
    (cl:cons ':startTime (startTime msg))
    (cl:cons ':gps_travel_on (gps_travel_on msg))
    (cl:cons ':mindState (mindState msg))
))
