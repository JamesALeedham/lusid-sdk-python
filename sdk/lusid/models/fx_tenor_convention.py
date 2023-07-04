# coding: utf-8

"""
    LUSID API

    FINBOURNE Technology  # noqa: E501

    The version of the OpenAPI document: 1.0.308
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


class FxTenorConvention(object):
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
        'calendar_code': 'str',
        'spot_days': 'int'
    }

    attribute_map = {
        'calendar_code': 'calendarCode',
        'spot_days': 'spotDays'
    }

    required_map = {
        'calendar_code': 'required',
        'spot_days': 'required'
    }

    def __init__(self, calendar_code=None, spot_days=None, local_vars_configuration=None):  # noqa: E501
        """FxTenorConvention - a model defined in OpenAPI"
        
        :param calendar_code:  The code of the holiday calendar that should be used when interpreting FX tenors. (required)
        :type calendar_code: str
        :param spot_days:  The minimum number of business days that must pass within this calendar when calculating the spot date. (required)
        :type spot_days: int

        """  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._calendar_code = None
        self._spot_days = None
        self.discriminator = None

        self.calendar_code = calendar_code
        self.spot_days = spot_days

    @property
    def calendar_code(self):
        """Gets the calendar_code of this FxTenorConvention.  # noqa: E501

        The code of the holiday calendar that should be used when interpreting FX tenors.  # noqa: E501

        :return: The calendar_code of this FxTenorConvention.  # noqa: E501
        :rtype: str
        """
        return self._calendar_code

    @calendar_code.setter
    def calendar_code(self, calendar_code):
        """Sets the calendar_code of this FxTenorConvention.

        The code of the holiday calendar that should be used when interpreting FX tenors.  # noqa: E501

        :param calendar_code: The calendar_code of this FxTenorConvention.  # noqa: E501
        :type calendar_code: str
        """
        if self.local_vars_configuration.client_side_validation and calendar_code is None:  # noqa: E501
            raise ValueError("Invalid value for `calendar_code`, must not be `None`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                calendar_code is not None and len(calendar_code) > 64):
            raise ValueError("Invalid value for `calendar_code`, length must be less than or equal to `64`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                calendar_code is not None and len(calendar_code) < 0):
            raise ValueError("Invalid value for `calendar_code`, length must be greater than or equal to `0`")  # noqa: E501

        self._calendar_code = calendar_code

    @property
    def spot_days(self):
        """Gets the spot_days of this FxTenorConvention.  # noqa: E501

        The minimum number of business days that must pass within this calendar when calculating the spot date.  # noqa: E501

        :return: The spot_days of this FxTenorConvention.  # noqa: E501
        :rtype: int
        """
        return self._spot_days

    @spot_days.setter
    def spot_days(self, spot_days):
        """Sets the spot_days of this FxTenorConvention.

        The minimum number of business days that must pass within this calendar when calculating the spot date.  # noqa: E501

        :param spot_days: The spot_days of this FxTenorConvention.  # noqa: E501
        :type spot_days: int
        """
        if self.local_vars_configuration.client_side_validation and spot_days is None:  # noqa: E501
            raise ValueError("Invalid value for `spot_days`, must not be `None`")  # noqa: E501

        self._spot_days = spot_days

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
        if not isinstance(other, FxTenorConvention):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, FxTenorConvention):
            return True

        return self.to_dict() != other.to_dict()
