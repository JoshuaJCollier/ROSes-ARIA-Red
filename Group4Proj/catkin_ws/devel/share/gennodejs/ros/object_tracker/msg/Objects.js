// Auto-generated. Do not edit!

// (in-package object_tracker.msg)


"use strict";

const _serializer = _ros_msg_utils.Serialize;
const _arraySerializer = _serializer.Array;
const _deserializer = _ros_msg_utils.Deserialize;
const _arrayDeserializer = _deserializer.Array;
const _finder = _ros_msg_utils.Find;
const _getByteLength = _ros_msg_utils.getByteLength;

//-----------------------------------------------------------

class Objects {
  constructor(initObj={}) {
    if (initObj === null) {
      // initObj === null is a special case for deserialization where we don't initialize fields
      this.cone = null;
      this.bucket = null;
      this.obstacle = null;
      this.bucketDist = null;
      this.time = null;
    }
    else {
      if (initObj.hasOwnProperty('cone')) {
        this.cone = initObj.cone
      }
      else {
        this.cone = 0;
      }
      if (initObj.hasOwnProperty('bucket')) {
        this.bucket = initObj.bucket
      }
      else {
        this.bucket = 0;
      }
      if (initObj.hasOwnProperty('obstacle')) {
        this.obstacle = initObj.obstacle
      }
      else {
        this.obstacle = 0;
      }
      if (initObj.hasOwnProperty('bucketDist')) {
        this.bucketDist = initObj.bucketDist
      }
      else {
        this.bucketDist = 0.0;
      }
      if (initObj.hasOwnProperty('time')) {
        this.time = initObj.time
      }
      else {
        this.time = 0.0;
      }
    }
  }

  static serialize(obj, buffer, bufferOffset) {
    // Serializes a message object of type Objects
    // Serialize message field [cone]
    bufferOffset = _serializer.int32(obj.cone, buffer, bufferOffset);
    // Serialize message field [bucket]
    bufferOffset = _serializer.int32(obj.bucket, buffer, bufferOffset);
    // Serialize message field [obstacle]
    bufferOffset = _serializer.int32(obj.obstacle, buffer, bufferOffset);
    // Serialize message field [bucketDist]
    bufferOffset = _serializer.float64(obj.bucketDist, buffer, bufferOffset);
    // Serialize message field [time]
    bufferOffset = _serializer.float64(obj.time, buffer, bufferOffset);
    return bufferOffset;
  }

  static deserialize(buffer, bufferOffset=[0]) {
    //deserializes a message object of type Objects
    let len;
    let data = new Objects(null);
    // Deserialize message field [cone]
    data.cone = _deserializer.int32(buffer, bufferOffset);
    // Deserialize message field [bucket]
    data.bucket = _deserializer.int32(buffer, bufferOffset);
    // Deserialize message field [obstacle]
    data.obstacle = _deserializer.int32(buffer, bufferOffset);
    // Deserialize message field [bucketDist]
    data.bucketDist = _deserializer.float64(buffer, bufferOffset);
    // Deserialize message field [time]
    data.time = _deserializer.float64(buffer, bufferOffset);
    return data;
  }

  static getMessageSize(object) {
    return 28;
  }

  static datatype() {
    // Returns string type for a message object
    return 'object_tracker/Objects';
  }

  static md5sum() {
    //Returns md5sum for a message object
    return '57c2ce73fa9cbfd6f321f8c8cacc21d6';
  }

  static messageDefinition() {
    // Returns full string definition for message
    return `
    int32 cone
    int32 bucket
    int32 obstacle
    float64 bucketDist
    float64 time
    
    `;
  }

  static Resolve(msg) {
    // deep-construct a valid message object instance of whatever was passed in
    if (typeof msg !== 'object' || msg === null) {
      msg = {};
    }
    const resolved = new Objects(null);
    if (msg.cone !== undefined) {
      resolved.cone = msg.cone;
    }
    else {
      resolved.cone = 0
    }

    if (msg.bucket !== undefined) {
      resolved.bucket = msg.bucket;
    }
    else {
      resolved.bucket = 0
    }

    if (msg.obstacle !== undefined) {
      resolved.obstacle = msg.obstacle;
    }
    else {
      resolved.obstacle = 0
    }

    if (msg.bucketDist !== undefined) {
      resolved.bucketDist = msg.bucketDist;
    }
    else {
      resolved.bucketDist = 0.0
    }

    if (msg.time !== undefined) {
      resolved.time = msg.time;
    }
    else {
      resolved.time = 0.0
    }

    return resolved;
    }
};

module.exports = Objects;
