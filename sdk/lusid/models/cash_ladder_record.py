# coding: utf-8

"""
    LUSID API

    FINBOURNE Technology  # noqa: E501

    The version of the OpenAPI document: 1.0.35
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


class CashLadderRecord(object):
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
        'effective_date': 'datetime',
        'open': 'float',
        'activities': 'dict(str, float)',
        'close': 'float'
    }

    attribute_map = {
        'effective_date': 'effectiveDate',
        'open': 'open',
        'activities': 'activities',
        'close': 'close'
    }

    required_map = {
        'effective_date': 'optional',
        'open': 'required',
        'activities': 'required',
        'close': 'required'
    }

    def __init__(self, effective_date=None, open=None, activities=None, close=None, local_vars_configuration=None):  # noqa: E501
        """CashLadderRecord - a model defined in OpenAPI"
        
        :param effective_date: 
        :type effective_date: datetime
        :param open:  (required)
        :type open: float
        :param activities:  (required)
        :type activities: dict(str, float)
        :param close:  (required)
        :type close: float

        """  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._effective_date = None
        self._open = None
        self._activities = None
        self._close = None
        self.discriminator = None

        if effective_date is not None:
            self.effective_date = effective_date
        self.open = open
        self.activities = activities
        self.close = close

    @property
    def effective_date(self):
        """Gets the effective_date of this CashLadderRecord.  # noqa: E501


        :return: The effective_date of this CashLadderRecord.  # noqa: E501
        :rtype: datetime
        """
        return self._effective_date

    @effective_date.setter
    def effective_date(self, effective_date):
        """Sets the effective_date of this CashLadderRecord.


        :param effective_date: The effective_date of this CashLadderRecord.  # noqa: E501
        :type effective_date: datetime
        """

        self._effective_date = effective_date

    @property
    def open(self):
        """Gets the open of this CashLadderRecord.  # noqa: E501


        :return: The open of this CashLadderRecord.  # noqa: E501
        :rtype: float
        """
        return self._open

    @open.setter
    def open(self, open):
        """Sets the open of this CashLadderRecord.


        :param open: The open of this CashLadderRecord.  # noqa: E501
        :type open: float
        """
        if self.local_vars_configuration.client_side_validation and open is None:  # noqa: E501
            raise ValueError("Invalid value for `open`, must not be `None`")  # noqa: E501

        self._open = open

    @property
    def activities(self):
        """Gets the activities of this CashLadderRecord.  # noqa: E501


        :return: The activities of this CashLadderRecord.  # noqa: E501
        :rtype: dict(str, float)
        """
        return self._activities

    @activities.setter
    def activities(self, activities):
        """Sets the activities of this CashLadderRecord.


        :param activities: The activities of this CashLadderRecord.  # noqa: E501
        :type activities: dict(str, float)
        """
        if self.local_vars_configuration.client_side_validation and activities is None:  # noqa: E501
            raise ValueError("Invalid value for `activities`, must not be `None`")  # noqa: E501

        self._activities = activities

    @property
    def close(self):
        """Gets the close of this CashLadderRecord.  # noqa: E501


        :return: The close of this CashLadderRecord.  # noqa: E501
        :rtype: float
        """
        return self._close

    @close.setter
    def close(self, close):
        """Sets the close of this CashLadderRecord.


        :param close: The close of this CashLadderRecord.  # noqa: E501
        :type close: float
        """
        if self.local_vars_configuration.client_side_validation and close is None:  # noqa: E501
            raise ValueError("Invalid value for `close`, must not be `None`")  # noqa: E501

        self._close = close

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
        if not isinstance(other, CashLadderRecord):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, CashLadderRecord):
            return True

        return self.to_dict() != other.to_dict()
