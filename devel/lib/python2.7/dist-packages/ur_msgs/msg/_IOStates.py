# This Python file uses the following encoding: utf-8
"""autogenerated by genpy from ur_msgs/IOStates.msg. Do not edit."""
import sys
python3 = True if sys.hexversion > 0x03000000 else False
import genpy
import struct

import ur_msgs.msg

class IOStates(genpy.Message):
  _md5sum = "0a5c7b73e3189e9a2caf8583d1bae2e2"
  _type = "ur_msgs/IOStates"
  _has_header = False #flag to mark the presence of a Header object
  _full_text = """Digital[] digital_in_states
Digital[] digital_out_states
Digital[] flag_states
Analog[] analog_in_states
Analog[] analog_out_states

================================================================================
MSG: ur_msgs/Digital
uint8 pin
bool state

================================================================================
MSG: ur_msgs/Analog
uint8 pin
float32 state

"""
  __slots__ = ['digital_in_states','digital_out_states','flag_states','analog_in_states','analog_out_states']
  _slot_types = ['ur_msgs/Digital[]','ur_msgs/Digital[]','ur_msgs/Digital[]','ur_msgs/Analog[]','ur_msgs/Analog[]']

  def __init__(self, *args, **kwds):
    """
    Constructor. Any message fields that are implicitly/explicitly
    set to None will be assigned a default value. The recommend
    use is keyword arguments as this is more robust to future message
    changes.  You cannot mix in-order arguments and keyword arguments.

    The available fields are:
       digital_in_states,digital_out_states,flag_states,analog_in_states,analog_out_states

    :param args: complete set of field values, in .msg order
    :param kwds: use keyword arguments corresponding to message field names
    to set specific fields.
    """
    if args or kwds:
      super(IOStates, self).__init__(*args, **kwds)
      #message fields cannot be None, assign default values for those that are
      if self.digital_in_states is None:
        self.digital_in_states = []
      if self.digital_out_states is None:
        self.digital_out_states = []
      if self.flag_states is None:
        self.flag_states = []
      if self.analog_in_states is None:
        self.analog_in_states = []
      if self.analog_out_states is None:
        self.analog_out_states = []
    else:
      self.digital_in_states = []
      self.digital_out_states = []
      self.flag_states = []
      self.analog_in_states = []
      self.analog_out_states = []

  def _get_types(self):
    """
    internal API method
    """
    return self._slot_types

  def serialize(self, buff):
    """
    serialize message into buffer
    :param buff: buffer, ``StringIO``
    """
    try:
      length = len(self.digital_in_states)
      buff.write(_struct_I.pack(length))
      for val1 in self.digital_in_states:
        _x = val1
        buff.write(_struct_2B.pack(_x.pin, _x.state))
      length = len(self.digital_out_states)
      buff.write(_struct_I.pack(length))
      for val1 in self.digital_out_states:
        _x = val1
        buff.write(_struct_2B.pack(_x.pin, _x.state))
      length = len(self.flag_states)
      buff.write(_struct_I.pack(length))
      for val1 in self.flag_states:
        _x = val1
        buff.write(_struct_2B.pack(_x.pin, _x.state))
      length = len(self.analog_in_states)
      buff.write(_struct_I.pack(length))
      for val1 in self.analog_in_states:
        _x = val1
        buff.write(_struct_Bf.pack(_x.pin, _x.state))
      length = len(self.analog_out_states)
      buff.write(_struct_I.pack(length))
      for val1 in self.analog_out_states:
        _x = val1
        buff.write(_struct_Bf.pack(_x.pin, _x.state))
    except struct.error as se: self._check_types(struct.error("%s: '%s' when writing '%s'" % (type(se), str(se), str(_x))))
    except TypeError as te: self._check_types(ValueError("%s: '%s' when writing '%s'" % (type(te), str(te), str(_x))))

  def deserialize(self, str):
    """
    unpack serialized message in str into this message instance
    :param str: byte array of serialized message, ``str``
    """
    try:
      if self.digital_in_states is None:
        self.digital_in_states = None
      if self.digital_out_states is None:
        self.digital_out_states = None
      if self.flag_states is None:
        self.flag_states = None
      if self.analog_in_states is None:
        self.analog_in_states = None
      if self.analog_out_states is None:
        self.analog_out_states = None
      end = 0
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      self.digital_in_states = []
      for i in range(0, length):
        val1 = ur_msgs.msg.Digital()
        _x = val1
        start = end
        end += 2
        (_x.pin, _x.state,) = _struct_2B.unpack(str[start:end])
        val1.state = bool(val1.state)
        self.digital_in_states.append(val1)
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      self.digital_out_states = []
      for i in range(0, length):
        val1 = ur_msgs.msg.Digital()
        _x = val1
        start = end
        end += 2
        (_x.pin, _x.state,) = _struct_2B.unpack(str[start:end])
        val1.state = bool(val1.state)
        self.digital_out_states.append(val1)
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      self.flag_states = []
      for i in range(0, length):
        val1 = ur_msgs.msg.Digital()
        _x = val1
        start = end
        end += 2
        (_x.pin, _x.state,) = _struct_2B.unpack(str[start:end])
        val1.state = bool(val1.state)
        self.flag_states.append(val1)
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      self.analog_in_states = []
      for i in range(0, length):
        val1 = ur_msgs.msg.Analog()
        _x = val1
        start = end
        end += 5
        (_x.pin, _x.state,) = _struct_Bf.unpack(str[start:end])
        self.analog_in_states.append(val1)
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      self.analog_out_states = []
      for i in range(0, length):
        val1 = ur_msgs.msg.Analog()
        _x = val1
        start = end
        end += 5
        (_x.pin, _x.state,) = _struct_Bf.unpack(str[start:end])
        self.analog_out_states.append(val1)
      return self
    except struct.error as e:
      raise genpy.DeserializationError(e) #most likely buffer underfill


  def serialize_numpy(self, buff, numpy):
    """
    serialize message with numpy array types into buffer
    :param buff: buffer, ``StringIO``
    :param numpy: numpy python module
    """
    try:
      length = len(self.digital_in_states)
      buff.write(_struct_I.pack(length))
      for val1 in self.digital_in_states:
        _x = val1
        buff.write(_struct_2B.pack(_x.pin, _x.state))
      length = len(self.digital_out_states)
      buff.write(_struct_I.pack(length))
      for val1 in self.digital_out_states:
        _x = val1
        buff.write(_struct_2B.pack(_x.pin, _x.state))
      length = len(self.flag_states)
      buff.write(_struct_I.pack(length))
      for val1 in self.flag_states:
        _x = val1
        buff.write(_struct_2B.pack(_x.pin, _x.state))
      length = len(self.analog_in_states)
      buff.write(_struct_I.pack(length))
      for val1 in self.analog_in_states:
        _x = val1
        buff.write(_struct_Bf.pack(_x.pin, _x.state))
      length = len(self.analog_out_states)
      buff.write(_struct_I.pack(length))
      for val1 in self.analog_out_states:
        _x = val1
        buff.write(_struct_Bf.pack(_x.pin, _x.state))
    except struct.error as se: self._check_types(struct.error("%s: '%s' when writing '%s'" % (type(se), str(se), str(_x))))
    except TypeError as te: self._check_types(ValueError("%s: '%s' when writing '%s'" % (type(te), str(te), str(_x))))

  def deserialize_numpy(self, str, numpy):
    """
    unpack serialized message in str into this message instance using numpy for array types
    :param str: byte array of serialized message, ``str``
    :param numpy: numpy python module
    """
    try:
      if self.digital_in_states is None:
        self.digital_in_states = None
      if self.digital_out_states is None:
        self.digital_out_states = None
      if self.flag_states is None:
        self.flag_states = None
      if self.analog_in_states is None:
        self.analog_in_states = None
      if self.analog_out_states is None:
        self.analog_out_states = None
      end = 0
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      self.digital_in_states = []
      for i in range(0, length):
        val1 = ur_msgs.msg.Digital()
        _x = val1
        start = end
        end += 2
        (_x.pin, _x.state,) = _struct_2B.unpack(str[start:end])
        val1.state = bool(val1.state)
        self.digital_in_states.append(val1)
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      self.digital_out_states = []
      for i in range(0, length):
        val1 = ur_msgs.msg.Digital()
        _x = val1
        start = end
        end += 2
        (_x.pin, _x.state,) = _struct_2B.unpack(str[start:end])
        val1.state = bool(val1.state)
        self.digital_out_states.append(val1)
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      self.flag_states = []
      for i in range(0, length):
        val1 = ur_msgs.msg.Digital()
        _x = val1
        start = end
        end += 2
        (_x.pin, _x.state,) = _struct_2B.unpack(str[start:end])
        val1.state = bool(val1.state)
        self.flag_states.append(val1)
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      self.analog_in_states = []
      for i in range(0, length):
        val1 = ur_msgs.msg.Analog()
        _x = val1
        start = end
        end += 5
        (_x.pin, _x.state,) = _struct_Bf.unpack(str[start:end])
        self.analog_in_states.append(val1)
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      self.analog_out_states = []
      for i in range(0, length):
        val1 = ur_msgs.msg.Analog()
        _x = val1
        start = end
        end += 5
        (_x.pin, _x.state,) = _struct_Bf.unpack(str[start:end])
        self.analog_out_states.append(val1)
      return self
    except struct.error as e:
      raise genpy.DeserializationError(e) #most likely buffer underfill

_struct_I = genpy.struct_I
_struct_Bf = struct.Struct("<Bf")
_struct_2B = struct.Struct("<2B")
