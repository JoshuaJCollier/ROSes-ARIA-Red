// Generated by gencpp from file object_tracker/Objects.msg
// DO NOT EDIT!


#ifndef OBJECT_TRACKER_MESSAGE_OBJECTS_H
#define OBJECT_TRACKER_MESSAGE_OBJECTS_H


#include <string>
#include <vector>
#include <map>

#include <ros/types.h>
#include <ros/serialization.h>
#include <ros/builtin_message_traits.h>
#include <ros/message_operations.h>


namespace object_tracker
{
template <class ContainerAllocator>
struct Objects_
{
  typedef Objects_<ContainerAllocator> Type;

  Objects_()
    : cone(0)
    , bucket(0)
    , obstacle(0)
    , coneDist(0.0)
    , bucketDist(0.0)
    , obstacleDist(0.0)
    , coneSize(0.0)
    , bucketSize(0.0)
    , obstacleSize(0.0)
    , time(0.0)  {
    }
  Objects_(const ContainerAllocator& _alloc)
    : cone(0)
    , bucket(0)
    , obstacle(0)
    , coneDist(0.0)
    , bucketDist(0.0)
    , obstacleDist(0.0)
    , coneSize(0.0)
    , bucketSize(0.0)
    , obstacleSize(0.0)
    , time(0.0)  {
  (void)_alloc;
    }



   typedef int64_t _cone_type;
  _cone_type cone;

   typedef int64_t _bucket_type;
  _bucket_type bucket;

   typedef int64_t _obstacle_type;
  _obstacle_type obstacle;

   typedef double _coneDist_type;
  _coneDist_type coneDist;

   typedef double _bucketDist_type;
  _bucketDist_type bucketDist;

   typedef double _obstacleDist_type;
  _obstacleDist_type obstacleDist;

   typedef double _coneSize_type;
  _coneSize_type coneSize;

   typedef double _bucketSize_type;
  _bucketSize_type bucketSize;

   typedef double _obstacleSize_type;
  _obstacleSize_type obstacleSize;

   typedef double _time_type;
  _time_type time;





  typedef boost::shared_ptr< ::object_tracker::Objects_<ContainerAllocator> > Ptr;
  typedef boost::shared_ptr< ::object_tracker::Objects_<ContainerAllocator> const> ConstPtr;

}; // struct Objects_

typedef ::object_tracker::Objects_<std::allocator<void> > Objects;

typedef boost::shared_ptr< ::object_tracker::Objects > ObjectsPtr;
typedef boost::shared_ptr< ::object_tracker::Objects const> ObjectsConstPtr;

// constants requiring out of line definition



template<typename ContainerAllocator>
std::ostream& operator<<(std::ostream& s, const ::object_tracker::Objects_<ContainerAllocator> & v)
{
ros::message_operations::Printer< ::object_tracker::Objects_<ContainerAllocator> >::stream(s, "", v);
return s;
}


template<typename ContainerAllocator1, typename ContainerAllocator2>
bool operator==(const ::object_tracker::Objects_<ContainerAllocator1> & lhs, const ::object_tracker::Objects_<ContainerAllocator2> & rhs)
{
  return lhs.cone == rhs.cone &&
    lhs.bucket == rhs.bucket &&
    lhs.obstacle == rhs.obstacle &&
    lhs.coneDist == rhs.coneDist &&
    lhs.bucketDist == rhs.bucketDist &&
    lhs.obstacleDist == rhs.obstacleDist &&
    lhs.coneSize == rhs.coneSize &&
    lhs.bucketSize == rhs.bucketSize &&
    lhs.obstacleSize == rhs.obstacleSize &&
    lhs.time == rhs.time;
}

template<typename ContainerAllocator1, typename ContainerAllocator2>
bool operator!=(const ::object_tracker::Objects_<ContainerAllocator1> & lhs, const ::object_tracker::Objects_<ContainerAllocator2> & rhs)
{
  return !(lhs == rhs);
}


} // namespace object_tracker

namespace ros
{
namespace message_traits
{





template <class ContainerAllocator>
struct IsMessage< ::object_tracker::Objects_<ContainerAllocator> >
  : TrueType
  { };

template <class ContainerAllocator>
struct IsMessage< ::object_tracker::Objects_<ContainerAllocator> const>
  : TrueType
  { };

template <class ContainerAllocator>
struct IsFixedSize< ::object_tracker::Objects_<ContainerAllocator> >
  : TrueType
  { };

template <class ContainerAllocator>
struct IsFixedSize< ::object_tracker::Objects_<ContainerAllocator> const>
  : TrueType
  { };

template <class ContainerAllocator>
struct HasHeader< ::object_tracker::Objects_<ContainerAllocator> >
  : FalseType
  { };

template <class ContainerAllocator>
struct HasHeader< ::object_tracker::Objects_<ContainerAllocator> const>
  : FalseType
  { };


template<class ContainerAllocator>
struct MD5Sum< ::object_tracker::Objects_<ContainerAllocator> >
{
  static const char* value()
  {
    return "c409bb10f65ba63532d5faef2c6ec1be";
  }

  static const char* value(const ::object_tracker::Objects_<ContainerAllocator>&) { return value(); }
  static const uint64_t static_value1 = 0xc409bb10f65ba635ULL;
  static const uint64_t static_value2 = 0x32d5faef2c6ec1beULL;
};

template<class ContainerAllocator>
struct DataType< ::object_tracker::Objects_<ContainerAllocator> >
{
  static const char* value()
  {
    return "object_tracker/Objects";
  }

  static const char* value(const ::object_tracker::Objects_<ContainerAllocator>&) { return value(); }
};

template<class ContainerAllocator>
struct Definition< ::object_tracker::Objects_<ContainerAllocator> >
{
  static const char* value()
  {
    return "int64 cone\n"
"int64 bucket\n"
"int64 obstacle\n"
"float64 coneDist\n"
"float64 bucketDist\n"
"float64 obstacleDist\n"
"float64 coneSize\n"
"float64 bucketSize\n"
"float64 obstacleSize\n"
"float64 time\n"
;
  }

  static const char* value(const ::object_tracker::Objects_<ContainerAllocator>&) { return value(); }
};

} // namespace message_traits
} // namespace ros

namespace ros
{
namespace serialization
{

  template<class ContainerAllocator> struct Serializer< ::object_tracker::Objects_<ContainerAllocator> >
  {
    template<typename Stream, typename T> inline static void allInOne(Stream& stream, T m)
    {
      stream.next(m.cone);
      stream.next(m.bucket);
      stream.next(m.obstacle);
      stream.next(m.coneDist);
      stream.next(m.bucketDist);
      stream.next(m.obstacleDist);
      stream.next(m.coneSize);
      stream.next(m.bucketSize);
      stream.next(m.obstacleSize);
      stream.next(m.time);
    }

    ROS_DECLARE_ALLINONE_SERIALIZER
  }; // struct Objects_

} // namespace serialization
} // namespace ros

namespace ros
{
namespace message_operations
{

template<class ContainerAllocator>
struct Printer< ::object_tracker::Objects_<ContainerAllocator> >
{
  template<typename Stream> static void stream(Stream& s, const std::string& indent, const ::object_tracker::Objects_<ContainerAllocator>& v)
  {
    s << indent << "cone: ";
    Printer<int64_t>::stream(s, indent + "  ", v.cone);
    s << indent << "bucket: ";
    Printer<int64_t>::stream(s, indent + "  ", v.bucket);
    s << indent << "obstacle: ";
    Printer<int64_t>::stream(s, indent + "  ", v.obstacle);
    s << indent << "coneDist: ";
    Printer<double>::stream(s, indent + "  ", v.coneDist);
    s << indent << "bucketDist: ";
    Printer<double>::stream(s, indent + "  ", v.bucketDist);
    s << indent << "obstacleDist: ";
    Printer<double>::stream(s, indent + "  ", v.obstacleDist);
    s << indent << "coneSize: ";
    Printer<double>::stream(s, indent + "  ", v.coneSize);
    s << indent << "bucketSize: ";
    Printer<double>::stream(s, indent + "  ", v.bucketSize);
    s << indent << "obstacleSize: ";
    Printer<double>::stream(s, indent + "  ", v.obstacleSize);
    s << indent << "time: ";
    Printer<double>::stream(s, indent + "  ", v.time);
  }
};

} // namespace message_operations
} // namespace ros

#endif // OBJECT_TRACKER_MESSAGE_OBJECTS_H