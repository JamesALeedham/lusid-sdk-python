# coding: utf-8

"""
    LUSID API

    FINBOURNE Technology  # noqa: E501

    The version of the OpenAPI document: 0.11.5240
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


class LifeCycleEventLineage(object):
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
        'event_type': 'str',
        'instrument_type': 'str',
        'instrument_id': 'str',
        'leg_id': 'str',
        'source_transaction_id': 'str'
    }

    attribute_map = {
        'event_type': 'eventType',
        'instrument_type': 'instrumentType',
        'instrument_id': 'instrumentId',
        'leg_id': 'legId',
        'source_transaction_id': 'sourceTransactionId'
    }

    required_map = {
        'event_type': 'optional',
        'instrument_type': 'optional',
        'instrument_id': 'optional',
        'leg_id': 'optional',
        'source_transaction_id': 'optional'
    }

    def __init__(self, event_type=None, instrument_type=None, instrument_id=None, leg_id=None, source_transaction_id=None, local_vars_configuration=None):  # noqa: E501
        """LifeCycleEventLineage - a model defined in OpenAPI"
        
        :param event_type:  The type of the event
        :type event_type: str
        :param instrument_type:  The instrument type of the instrument for the event.
        :type instrument_type: str
        :param instrument_id:  The LUID of the instrument for the event.
        :type instrument_id: str
        :param leg_id:  Leg id for the event.
        :type leg_id: str
        :param source_transaction_id:  The source transaction of the instrument for the event.
        :type source_transaction_id: str

        """  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._event_type = None
        self._instrument_type = None
        self._instrument_id = None
        self._leg_id = None
        self._source_transaction_id = None
        self.discriminator = None

        self.event_type = event_type
        self.instrument_type = instrument_type
        self.instrument_id = instrument_id
        self.leg_id = leg_id
        self.source_transaction_id = source_transaction_id

    @property
    def event_type(self):
        """Gets the event_type of this LifeCycleEventLineage.  # noqa: E501

        The type of the event  # noqa: E501

        :return: The event_type of this LifeCycleEventLineage.  # noqa: E501
        :rtype: str
        """
        return self._event_type

    @event_type.setter
    def event_type(self, event_type):
        """Sets the event_type of this LifeCycleEventLineage.

        The type of the event  # noqa: E501

        :param event_type: The event_type of this LifeCycleEventLineage.  # noqa: E501
        :type event_type: str
        """

        self._event_type = event_type

    @property
    def instrument_type(self):
        """Gets the instrument_type of this LifeCycleEventLineage.  # noqa: E501

        The instrument type of the instrument for the event.  # noqa: E501

        :return: The instrument_type of this LifeCycleEventLineage.  # noqa: E501
        :rtype: str
        """
        return self._instrument_type

    @instrument_type.setter
    def instrument_type(self, instrument_type):
        """Sets the instrument_type of this LifeCycleEventLineage.

        The instrument type of the instrument for the event.  # noqa: E501

        :param instrument_type: The instrument_type of this LifeCycleEventLineage.  # noqa: E501
        :type instrument_type: str
        """

        self._instrument_type = instrument_type

    @property
    def instrument_id(self):
        """Gets the instrument_id of this LifeCycleEventLineage.  # noqa: E501

        The LUID of the instrument for the event.  # noqa: E501

        :return: The instrument_id of this LifeCycleEventLineage.  # noqa: E501
        :rtype: str
        """
        return self._instrument_id

    @instrument_id.setter
    def instrument_id(self, instrument_id):
        """Sets the instrument_id of this LifeCycleEventLineage.

        The LUID of the instrument for the event.  # noqa: E501

        :param instrument_id: The instrument_id of this LifeCycleEventLineage.  # noqa: E501
        :type instrument_id: str
        """

        self._instrument_id = instrument_id

    @property
    def leg_id(self):
        """Gets the leg_id of this LifeCycleEventLineage.  # noqa: E501

        Leg id for the event.  # noqa: E501

        :return: The leg_id of this LifeCycleEventLineage.  # noqa: E501
        :rtype: str
        """
        return self._leg_id

    @leg_id.setter
    def leg_id(self, leg_id):
        """Sets the leg_id of this LifeCycleEventLineage.

        Leg id for the event.  # noqa: E501

        :param leg_id: The leg_id of this LifeCycleEventLineage.  # noqa: E501
        :type leg_id: str
        """

        self._leg_id = leg_id

    @property
    def source_transaction_id(self):
        """Gets the source_transaction_id of this LifeCycleEventLineage.  # noqa: E501

        The source transaction of the instrument for the event.  # noqa: E501

        :return: The source_transaction_id of this LifeCycleEventLineage.  # noqa: E501
        :rtype: str
        """
        return self._source_transaction_id

    @source_transaction_id.setter
    def source_transaction_id(self, source_transaction_id):
        """Sets the source_transaction_id of this LifeCycleEventLineage.

        The source transaction of the instrument for the event.  # noqa: E501

        :param source_transaction_id: The source_transaction_id of this LifeCycleEventLineage.  # noqa: E501
        :type source_transaction_id: str
        """

        self._source_transaction_id = source_transaction_id

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
        if not isinstance(other, LifeCycleEventLineage):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, LifeCycleEventLineage):
            return True

        return self.to_dict() != other.to_dict()
