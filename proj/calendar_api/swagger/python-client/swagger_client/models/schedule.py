# coding: utf-8

"""
    Prison Guard Scheduling API

    This API manages the schedules of prison guards, ensuring a guard cannot be scheduled to be in two places at the same time. It supports querying schedules by guard ID and location name.  # noqa: E501

    OpenAPI spec version: 1.0.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class Schedule(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'id': 'str',
        'guard_id': 'str',
        'time': 'datetime',
        'location_id': 'str'
    }

    attribute_map = {
        'id': 'id',
        'guard_id': 'guardId',
        'time': 'time',
        'location_id': 'locationId'
    }

    def __init__(self, id=None, guard_id=None, time=None, location_id=None):  # noqa: E501
        """Schedule - a model defined in Swagger"""  # noqa: E501
        self._id = None
        self._guard_id = None
        self._time = None
        self._location_id = None
        self.discriminator = None
        if id is not None:
            self.id = id
        self.guard_id = guard_id
        self.time = time
        self.location_id = location_id

    @property
    def id(self):
        """Gets the id of this Schedule.  # noqa: E501

        The unique identifier of the schedule.  # noqa: E501

        :return: The id of this Schedule.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this Schedule.

        The unique identifier of the schedule.  # noqa: E501

        :param id: The id of this Schedule.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def guard_id(self):
        """Gets the guard_id of this Schedule.  # noqa: E501

        The unique identifier of the guard.  # noqa: E501

        :return: The guard_id of this Schedule.  # noqa: E501
        :rtype: str
        """
        return self._guard_id

    @guard_id.setter
    def guard_id(self, guard_id):
        """Sets the guard_id of this Schedule.

        The unique identifier of the guard.  # noqa: E501

        :param guard_id: The guard_id of this Schedule.  # noqa: E501
        :type: str
        """
        if guard_id is None:
            raise ValueError("Invalid value for `guard_id`, must not be `None`")  # noqa: E501

        self._guard_id = guard_id

    @property
    def time(self):
        """Gets the time of this Schedule.  # noqa: E501

        The scheduled start time, with conflict checks.  # noqa: E501

        :return: The time of this Schedule.  # noqa: E501
        :rtype: datetime
        """
        return self._time

    @time.setter
    def time(self, time):
        """Sets the time of this Schedule.

        The scheduled start time, with conflict checks.  # noqa: E501

        :param time: The time of this Schedule.  # noqa: E501
        :type: datetime
        """
        if time is None:
            raise ValueError("Invalid value for `time`, must not be `None`")  # noqa: E501

        self._time = time

    @property
    def location_id(self):
        """Gets the location_id of this Schedule.  # noqa: E501

        The unique identifier of the location, referencing the Location schema.  # noqa: E501

        :return: The location_id of this Schedule.  # noqa: E501
        :rtype: str
        """
        return self._location_id

    @location_id.setter
    def location_id(self, location_id):
        """Sets the location_id of this Schedule.

        The unique identifier of the location, referencing the Location schema.  # noqa: E501

        :param location_id: The location_id of this Schedule.  # noqa: E501
        :type: str
        """
        if location_id is None:
            raise ValueError("Invalid value for `location_id`, must not be `None`")  # noqa: E501

        self._location_id = location_id

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value
        if issubclass(Schedule, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, Schedule):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other