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

class CurrentGoal {
  constructor(initObj={}) {
    if (initObj === null) {
      // initObj === null is a special case for deserialization where we don't initialize fields
      this.currentGoal = null;
    }
    else {
      if (initObj.hasOwnProperty('currentGoal')) {
        this.currentGoal = initObj.currentGoal
      }
      else {
        this.currentGoal = 0;
      }
    }
  }

  static serialize(obj, buffer, bufferOffset) {
    // Serializes a message object of type CurrentGoal
    // Serialize message field [currentGoal]
    bufferOffset = _serializer.int64(obj.currentGoal, buffer, bufferOffset);
    return bufferOffset;
  }

  static deserialize(buffer, bufferOffset=[0]) {
    //deserializes a message object of type CurrentGoal
    let len;
    let data = new CurrentGoal(null);
    // Deserialize message field [currentGoal]
    data.currentGoal = _deserializer.int64(buffer, bufferOffset);
    return data;
  }

  static getMessageSize(object) {
    return 8;
  }

  static datatype() {
    // Returns string type for a message object
    return 'megamind/CurrentGoal';
  }

  static md5sum() {
    //Returns md5sum for a message object
    return '0ca78cdf9677c9a77eeaeddd9e2b5143';
  }

  static messageDefinition() {
    // Returns full string definition for message
    return `
    int64 currentGoal
    
    `;
  }

  static Resolve(msg) {
    // deep-construct a valid message object instance of whatever was passed in
    if (typeof msg !== 'object' || msg === null) {
      msg = {};
    }
    const resolved = new CurrentGoal(null);
    if (msg.currentGoal !== undefined) {
      resolved.currentGoal = msg.currentGoal;
    }
    else {
      resolved.currentGoal = 0
    }

    return resolved;
    }
};

module.exports = CurrentGoal;
