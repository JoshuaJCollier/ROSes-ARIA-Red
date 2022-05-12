// Auto-generated. Do not edit!

// (in-package megamind.msg)


"use strict";

const _serializer = _ros_msg_utils.Serialize;
const _arraySerializer = _serializer.Array;
const _deserializer = _ros_msg_utils.Deserialize;
const _arrayDeserializer = _deserializer.Array;
const _finder = _ros_msg_utils.Find;
const _getByteLength = _ros_msg_utils.getByteLength;

//-----------------------------------------------------------

class Decision {
  constructor(initObj={}) {
    if (initObj === null) {
      // initObj === null is a special case for deserialization where we don't initialize fields
      this.currentGoal = null;
      this.startHeading = null;
      this.startTime = null;
      this.gps_travel_on = null;
    }
    else {
      if (initObj.hasOwnProperty('currentGoal')) {
        this.currentGoal = initObj.currentGoal
      }
      else {
        this.currentGoal = 0;
      }
      if (initObj.hasOwnProperty('startHeading')) {
        this.startHeading = initObj.startHeading
      }
      else {
        this.startHeading = 0.0;
      }
      if (initObj.hasOwnProperty('startTime')) {
        this.startTime = initObj.startTime
      }
      else {
        this.startTime = 0.0;
      }
      if (initObj.hasOwnProperty('gps_travel_on')) {
        this.gps_travel_on = initObj.gps_travel_on
      }
      else {
        this.gps_travel_on = 0;
      }
    }
  }

  static serialize(obj, buffer, bufferOffset) {
    // Serializes a message object of type Decision
    // Serialize message field [currentGoal]
    bufferOffset = _serializer.int32(obj.currentGoal, buffer, bufferOffset);
    // Serialize message field [startHeading]
    bufferOffset = _serializer.float32(obj.startHeading, buffer, bufferOffset);
    // Serialize message field [startTime]
    bufferOffset = _serializer.float32(obj.startTime, buffer, bufferOffset);
    // Serialize message field [gps_travel_on]
    bufferOffset = _serializer.int32(obj.gps_travel_on, buffer, bufferOffset);
    return bufferOffset;
  }

  static deserialize(buffer, bufferOffset=[0]) {
    //deserializes a message object of type Decision
    let len;
    let data = new Decision(null);
    // Deserialize message field [currentGoal]
    data.currentGoal = _deserializer.int32(buffer, bufferOffset);
    // Deserialize message field [startHeading]
    data.startHeading = _deserializer.float32(buffer, bufferOffset);
    // Deserialize message field [startTime]
    data.startTime = _deserializer.float32(buffer, bufferOffset);
    // Deserialize message field [gps_travel_on]
    data.gps_travel_on = _deserializer.int32(buffer, bufferOffset);
    return data;
  }

  static getMessageSize(object) {
    return 16;
  }

  static datatype() {
    // Returns string type for a message object
    return 'megamind/Decision';
  }

  static md5sum() {
    //Returns md5sum for a message object
    return '64f33f84960e1def33c8809e718d04ee';
  }

  static messageDefinition() {
    // Returns full string definition for message
    return `
    int32 currentGoal
    float32 startHeading
    float32 startTime
    int32 gps_travel_on
    
    `;
  }

  static Resolve(msg) {
    // deep-construct a valid message object instance of whatever was passed in
    if (typeof msg !== 'object' || msg === null) {
      msg = {};
    }
    const resolved = new Decision(null);
    if (msg.currentGoal !== undefined) {
      resolved.currentGoal = msg.currentGoal;
    }
    else {
      resolved.currentGoal = 0
    }

    if (msg.startHeading !== undefined) {
      resolved.startHeading = msg.startHeading;
    }
    else {
      resolved.startHeading = 0.0
    }

    if (msg.startTime !== undefined) {
      resolved.startTime = msg.startTime;
    }
    else {
      resolved.startTime = 0.0
    }

    if (msg.gps_travel_on !== undefined) {
      resolved.gps_travel_on = msg.gps_travel_on;
    }
    else {
      resolved.gps_travel_on = 0
    }

    return resolved;
    }
};

module.exports = Decision;
