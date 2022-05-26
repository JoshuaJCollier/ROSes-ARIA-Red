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
      this.coneDist = null;
      this.bucketDist = null;
      this.obstacleDist = null;
      this.coneSize = null;
      this.bucketSize = null;
      this.obstacleSize = null;
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
      if (initObj.hasOwnProperty('coneDist')) {
        this.coneDist = initObj.coneDist
      }
      else {
        this.coneDist = 0.0;
      }
      if (initObj.hasOwnProperty('bucketDist')) {
        this.bucketDist = initObj.bucketDist
      }
      else {
        this.bucketDist = 0.0;
      }
      if (initObj.hasOwnProperty('obstacleDist')) {
        this.obstacleDist = initObj.obstacleDist
      }
      else {
        this.obstacleDist = 0.0;
      }
      if (initObj.hasOwnProperty('coneSize')) {
        this.coneSize = initObj.coneSize
      }
      else {
        this.coneSize = 0.0;
      }
      if (initObj.hasOwnProperty('bucketSize')) {
        this.bucketSize = initObj.bucketSize
      }
      else {
        this.bucketSize = 0.0;
      }
      if (initObj.hasOwnProperty('obstacleSize')) {
        this.obstacleSize = initObj.obstacleSize
      }
      else {
        this.obstacleSize = 0.0;
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
    bufferOffset = _serializer.int64(obj.cone, buffer, bufferOffset);
    // Serialize message field [bucket]
    bufferOffset = _serializer.int64(obj.bucket, buffer, bufferOffset);
    // Serialize message field [obstacle]
    bufferOffset = _serializer.int64(obj.obstacle, buffer, bufferOffset);
    // Serialize message field [coneDist]
    bufferOffset = _serializer.float64(obj.coneDist, buffer, bufferOffset);
    // Serialize message field [bucketDist]
    bufferOffset = _serializer.float64(obj.bucketDist, buffer, bufferOffset);
    // Serialize message field [obstacleDist]
    bufferOffset = _serializer.float64(obj.obstacleDist, buffer, bufferOffset);
    // Serialize message field [coneSize]
    bufferOffset = _serializer.float64(obj.coneSize, buffer, bufferOffset);
    // Serialize message field [bucketSize]
    bufferOffset = _serializer.float64(obj.bucketSize, buffer, bufferOffset);
    // Serialize message field [obstacleSize]
    bufferOffset = _serializer.float64(obj.obstacleSize, buffer, bufferOffset);
    // Serialize message field [time]
    bufferOffset = _serializer.float64(obj.time, buffer, bufferOffset);
    return bufferOffset;
  }

  static deserialize(buffer, bufferOffset=[0]) {
    //deserializes a message object of type Objects
    let len;
    let data = new Objects(null);
    // Deserialize message field [cone]
    data.cone = _deserializer.int64(buffer, bufferOffset);
    // Deserialize message field [bucket]
    data.bucket = _deserializer.int64(buffer, bufferOffset);
    // Deserialize message field [obstacle]
    data.obstacle = _deserializer.int64(buffer, bufferOffset);
    // Deserialize message field [coneDist]
    data.coneDist = _deserializer.float64(buffer, bufferOffset);
    // Deserialize message field [bucketDist]
    data.bucketDist = _deserializer.float64(buffer, bufferOffset);
    // Deserialize message field [obstacleDist]
    data.obstacleDist = _deserializer.float64(buffer, bufferOffset);
    // Deserialize message field [coneSize]
    data.coneSize = _deserializer.float64(buffer, bufferOffset);
    // Deserialize message field [bucketSize]
    data.bucketSize = _deserializer.float64(buffer, bufferOffset);
    // Deserialize message field [obstacleSize]
    data.obstacleSize = _deserializer.float64(buffer, bufferOffset);
    // Deserialize message field [time]
    data.time = _deserializer.float64(buffer, bufferOffset);
    return data;
  }

  static getMessageSize(object) {
    return 80;
  }

  static datatype() {
    // Returns string type for a message object
    return 'object_tracker/Objects';
  }

  static md5sum() {
    //Returns md5sum for a message object
    return 'c409bb10f65ba63532d5faef2c6ec1be';
  }

  static messageDefinition() {
    // Returns full string definition for message
    return `
    int64 cone
    int64 bucket
    int64 obstacle
    float64 coneDist
    float64 bucketDist
    float64 obstacleDist
    float64 coneSize
    float64 bucketSize
    float64 obstacleSize
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

    if (msg.coneDist !== undefined) {
      resolved.coneDist = msg.coneDist;
    }
    else {
      resolved.coneDist = 0.0
    }

    if (msg.bucketDist !== undefined) {
      resolved.bucketDist = msg.bucketDist;
    }
    else {
      resolved.bucketDist = 0.0
    }

    if (msg.obstacleDist !== undefined) {
      resolved.obstacleDist = msg.obstacleDist;
    }
    else {
      resolved.obstacleDist = 0.0
    }

    if (msg.coneSize !== undefined) {
      resolved.coneSize = msg.coneSize;
    }
    else {
      resolved.coneSize = 0.0
    }

    if (msg.bucketSize !== undefined) {
      resolved.bucketSize = msg.bucketSize;
    }
    else {
      resolved.bucketSize = 0.0
    }

    if (msg.obstacleSize !== undefined) {
      resolved.obstacleSize = msg.obstacleSize;
    }
    else {
      resolved.obstacleSize = 0.0
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
