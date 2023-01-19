# coding: utf-8

"""
    LUSID API

    FINBOURNE Technology  # noqa: E501

    The version of the OpenAPI document: 0.11.5156
    Contact: info@finbourne.com
    Generated by: https://openapi-generator.tech
"""


try:
    from inspect import getfullargspec
except ImportError:
    from inspect import getargspec as getfullargspec
import pprint
import re  # noqa: F401
import six

from lusid.configuration import Configuration


class StepSchedule(object):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
      required_map (dict): The key is attribute name
                           and the value is whether it is 'required' or 'optional'.
    """
    openapi_types = {
        'level_type': 'str',
        'schedule_type': 'str',
        'step_schedule_type': 'str',
        'steps': 'list[LevelStep]'
    }

    attribute_map = {
        'level_type': 'levelType',
        'schedule_type': 'scheduleType',
        'step_schedule_type': 'stepScheduleType',
        'steps': 'steps'
    }

    required_map = {
        'level_type': 'required',
        'schedule_type': 'required',
        'step_schedule_type': 'required',
        'steps': 'required'
    }

    def __init__(self, level_type=None, schedule_type=None, step_schedule_type=None, steps=None, local_vars_configuration=None):  # noqa: E501
        """StepSchedule - a model defined in OpenAPI"
        
        :param level_type:  The type of shift or adjustment that the quantity represents.    Supported string (enumeration) values are: [Absolute, AbsoluteShift, Percentage, AbsolutePercentage]. (required)
        :type level_type: str
        :param schedule_type:  What type of schedule does this represent.  Supported string (enumeration) values are: [Fixed, Float, Optionality, Step, Payment, Accrual]. (required)
        :type schedule_type: str
        :param step_schedule_type:  The type of step that this schedule is for.  Supported string (enumeration) values are: [Coupon, Notional, Spread]. (required)
        :type step_schedule_type: str
        :param steps:  The level steps which are applied. (required)
        :type steps: list[lusid.LevelStep]

        """  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._level_type = None
        self._schedule_type = None
        self._step_schedule_type = None
        self._steps = None
        self.discriminator = None

        self.level_type = level_type
        self.schedule_type = schedule_type
        self.step_schedule_type = step_schedule_type
        self.steps = steps

    @property
    def level_type(self):
        """Gets the level_type of this StepSchedule.  # noqa: E501

        The type of shift or adjustment that the quantity represents.    Supported string (enumeration) values are: [Absolute, AbsoluteShift, Percentage, AbsolutePercentage].  # noqa: E501

        :return: The level_type of this StepSchedule.  # noqa: E501
        :rtype: str
        """
        return self._level_type

    @level_type.setter
    def level_type(self, level_type):
        """Sets the level_type of this StepSchedule.

        The type of shift or adjustment that the quantity represents.    Supported string (enumeration) values are: [Absolute, AbsoluteShift, Percentage, AbsolutePercentage].  # noqa: E501

        :param level_type: The level_type of this StepSchedule.  # noqa: E501
        :type level_type: str
        """
        if self.local_vars_configuration.client_side_validation and level_type is None:  # noqa: E501
            raise ValueError("Invalid value for `level_type`, must not be `None`")  # noqa: E501

        self._level_type = level_type

    @property
    def schedule_type(self):
        """Gets the schedule_type of this StepSchedule.  # noqa: E501

        What type of schedule does this represent.  Supported string (enumeration) values are: [Fixed, Float, Optionality, Step, Payment, Accrual].  # noqa: E501

        :return: The schedule_type of this StepSchedule.  # noqa: E501
        :rtype: str
        """
        return self._schedule_type

    @schedule_type.setter
    def schedule_type(self, schedule_type):
        """Sets the schedule_type of this StepSchedule.

        What type of schedule does this represent.  Supported string (enumeration) values are: [Fixed, Float, Optionality, Step, Payment, Accrual].  # noqa: E501

        :param schedule_type: The schedule_type of this StepSchedule.  # noqa: E501
        :type schedule_type: str
        """
        if self.local_vars_configuration.client_side_validation and schedule_type is None:  # noqa: E501
            raise ValueError("Invalid value for `schedule_type`, must not be `None`")  # noqa: E501

        self._schedule_type = schedule_type

    @property
    def step_schedule_type(self):
        """Gets the step_schedule_type of this StepSchedule.  # noqa: E501

        The type of step that this schedule is for.  Supported string (enumeration) values are: [Coupon, Notional, Spread].  # noqa: E501

        :return: The step_schedule_type of this StepSchedule.  # noqa: E501
        :rtype: str
        """
        return self._step_schedule_type

    @step_schedule_type.setter
    def step_schedule_type(self, step_schedule_type):
        """Sets the step_schedule_type of this StepSchedule.

        The type of step that this schedule is for.  Supported string (enumeration) values are: [Coupon, Notional, Spread].  # noqa: E501

        :param step_schedule_type: The step_schedule_type of this StepSchedule.  # noqa: E501
        :type step_schedule_type: str
        """
        if self.local_vars_configuration.client_side_validation and step_schedule_type is None:  # noqa: E501
            raise ValueError("Invalid value for `step_schedule_type`, must not be `None`")  # noqa: E501

        self._step_schedule_type = step_schedule_type

    @property
    def steps(self):
        """Gets the steps of this StepSchedule.  # noqa: E501

        The level steps which are applied.  # noqa: E501

        :return: The steps of this StepSchedule.  # noqa: E501
        :rtype: list[lusid.LevelStep]
        """
        return self._steps

    @steps.setter
    def steps(self, steps):
        """Sets the steps of this StepSchedule.

        The level steps which are applied.  # noqa: E501

        :param steps: The steps of this StepSchedule.  # noqa: E501
        :type steps: list[lusid.LevelStep]
        """
        if self.local_vars_configuration.client_side_validation and steps is None:  # noqa: E501
            raise ValueError("Invalid value for `steps`, must not be `None`")  # noqa: E501

        self._steps = steps

    def to_dict(self, serialize=False):
        """Returns the model properties as a dict"""
        result = {}

        def convert(x):
            if hasattr(x, "to_dict"):
                args = getfullargspec(x.to_dict).args
                if len(args) == 1:
                    return x.to_dict()
                else:
                    return x.to_dict(serialize)
            else:
                return x

        for attr, _ in six.iteritems(self.openapi_types):
            value = getattr(self, attr)
            attr = self.attribute_map.get(attr, attr) if serialize else attr
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: convert(x),
                    value
                ))
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], convert(item[1])),
                    value.items()
                ))
            else:
                result[attr] = convert(value)

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, StepSchedule):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, StepSchedule):
            return True

        return self.to_dict() != other.to_dict()
