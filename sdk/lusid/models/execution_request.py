# coding: utf-8

"""
    LUSID API

    FINBOURNE Technology  # noqa: E501

    The version of the OpenAPI document: 0.11.2729
    Contact: info@finbourne.com
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

class ExecutionRequest(object):
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
        'execution_id': 'str',
        'side': 'str',
        'instrument_identifiers': 'dict(str, str)',
        'transaction_time': 'datetime',
        'last_shares': 'float',
        'last_px': 'float',
        'currency': 'str'
    }

    attribute_map = {
        'execution_id': 'executionId',
        'side': 'side',
        'instrument_identifiers': 'instrumentIdentifiers',
        'transaction_time': 'transactionTime',
        'last_shares': 'lastShares',
        'last_px': 'lastPx',
        'currency': 'currency'
    }

    required_map = {
        'execution_id': 'required',
        'side': 'required',
        'instrument_identifiers': 'required',
        'transaction_time': 'required',
        'last_shares': 'required',
        'last_px': 'required',
        'currency': 'required'
    }

    def __init__(self, execution_id=None, side=None, instrument_identifiers=None, transaction_time=None, last_shares=None, last_px=None, currency=None):  # noqa: E501
        """
        ExecutionRequest - a model defined in OpenAPI

        :param execution_id:  The unique identifier of the Execution Report (8) message as assigned by sell-side. FIX field 17. (required)
        :type execution_id: str
        :param side:  The side of the order. FIX field 54. (required)
        :type side: str
        :param instrument_identifiers:  A set of instrument identifiers to use to resolve the execution to a unique instrument. (required)
        :type instrument_identifiers: dict(str, str)
        :param transaction_time:  Time of execution/order creation. FIX field 60. (required)
        :type transaction_time: datetime
        :param last_shares:  Quantity (e.g. shares) bought/sold on this (last) fill. FIX field 32. (required)
        :type last_shares: float
        :param last_px:  Price of this (last) fill. FIX field 31. (required)
        :type last_px: float
        :param currency:  The currency used for the price. FIX field 15. (required)
        :type currency: str

        """  # noqa: E501

        self._execution_id = None
        self._side = None
        self._instrument_identifiers = None
        self._transaction_time = None
        self._last_shares = None
        self._last_px = None
        self._currency = None
        self.discriminator = None

        self.execution_id = execution_id
        self.side = side
        self.instrument_identifiers = instrument_identifiers
        self.transaction_time = transaction_time
        self.last_shares = last_shares
        self.last_px = last_px
        self.currency = currency

    @property
    def execution_id(self):
        """Gets the execution_id of this ExecutionRequest.  # noqa: E501

        The unique identifier of the Execution Report (8) message as assigned by sell-side. FIX field 17.  # noqa: E501

        :return: The execution_id of this ExecutionRequest.  # noqa: E501
        :rtype: str
        """
        return self._execution_id

    @execution_id.setter
    def execution_id(self, execution_id):
        """Sets the execution_id of this ExecutionRequest.

        The unique identifier of the Execution Report (8) message as assigned by sell-side. FIX field 17.  # noqa: E501

        :param execution_id: The execution_id of this ExecutionRequest.  # noqa: E501
        :type: str
        """
        if execution_id is None:
            raise ValueError("Invalid value for `execution_id`, must not be `None`")  # noqa: E501

        self._execution_id = execution_id

    @property
    def side(self):
        """Gets the side of this ExecutionRequest.  # noqa: E501

        The side of the order. FIX field 54.  # noqa: E501

        :return: The side of this ExecutionRequest.  # noqa: E501
        :rtype: str
        """
        return self._side

    @side.setter
    def side(self, side):
        """Sets the side of this ExecutionRequest.

        The side of the order. FIX field 54.  # noqa: E501

        :param side: The side of this ExecutionRequest.  # noqa: E501
        :type: str
        """
        if side is None:
            raise ValueError("Invalid value for `side`, must not be `None`")  # noqa: E501

        self._side = side

    @property
    def instrument_identifiers(self):
        """Gets the instrument_identifiers of this ExecutionRequest.  # noqa: E501

        A set of instrument identifiers to use to resolve the execution to a unique instrument.  # noqa: E501

        :return: The instrument_identifiers of this ExecutionRequest.  # noqa: E501
        :rtype: dict(str, str)
        """
        return self._instrument_identifiers

    @instrument_identifiers.setter
    def instrument_identifiers(self, instrument_identifiers):
        """Sets the instrument_identifiers of this ExecutionRequest.

        A set of instrument identifiers to use to resolve the execution to a unique instrument.  # noqa: E501

        :param instrument_identifiers: The instrument_identifiers of this ExecutionRequest.  # noqa: E501
        :type: dict(str, str)
        """
        if instrument_identifiers is None:
            raise ValueError("Invalid value for `instrument_identifiers`, must not be `None`")  # noqa: E501

        self._instrument_identifiers = instrument_identifiers

    @property
    def transaction_time(self):
        """Gets the transaction_time of this ExecutionRequest.  # noqa: E501

        Time of execution/order creation. FIX field 60.  # noqa: E501

        :return: The transaction_time of this ExecutionRequest.  # noqa: E501
        :rtype: datetime
        """
        return self._transaction_time

    @transaction_time.setter
    def transaction_time(self, transaction_time):
        """Sets the transaction_time of this ExecutionRequest.

        Time of execution/order creation. FIX field 60.  # noqa: E501

        :param transaction_time: The transaction_time of this ExecutionRequest.  # noqa: E501
        :type: datetime
        """
        if transaction_time is None:
            raise ValueError("Invalid value for `transaction_time`, must not be `None`")  # noqa: E501

        self._transaction_time = transaction_time

    @property
    def last_shares(self):
        """Gets the last_shares of this ExecutionRequest.  # noqa: E501

        Quantity (e.g. shares) bought/sold on this (last) fill. FIX field 32.  # noqa: E501

        :return: The last_shares of this ExecutionRequest.  # noqa: E501
        :rtype: float
        """
        return self._last_shares

    @last_shares.setter
    def last_shares(self, last_shares):
        """Sets the last_shares of this ExecutionRequest.

        Quantity (e.g. shares) bought/sold on this (last) fill. FIX field 32.  # noqa: E501

        :param last_shares: The last_shares of this ExecutionRequest.  # noqa: E501
        :type: float
        """
        if last_shares is None:
            raise ValueError("Invalid value for `last_shares`, must not be `None`")  # noqa: E501

        self._last_shares = last_shares

    @property
    def last_px(self):
        """Gets the last_px of this ExecutionRequest.  # noqa: E501

        Price of this (last) fill. FIX field 31.  # noqa: E501

        :return: The last_px of this ExecutionRequest.  # noqa: E501
        :rtype: float
        """
        return self._last_px

    @last_px.setter
    def last_px(self, last_px):
        """Sets the last_px of this ExecutionRequest.

        Price of this (last) fill. FIX field 31.  # noqa: E501

        :param last_px: The last_px of this ExecutionRequest.  # noqa: E501
        :type: float
        """
        if last_px is None:
            raise ValueError("Invalid value for `last_px`, must not be `None`")  # noqa: E501

        self._last_px = last_px

    @property
    def currency(self):
        """Gets the currency of this ExecutionRequest.  # noqa: E501

        The currency used for the price. FIX field 15.  # noqa: E501

        :return: The currency of this ExecutionRequest.  # noqa: E501
        :rtype: str
        """
        return self._currency

    @currency.setter
    def currency(self, currency):
        """Sets the currency of this ExecutionRequest.

        The currency used for the price. FIX field 15.  # noqa: E501

        :param currency: The currency of this ExecutionRequest.  # noqa: E501
        :type: str
        """
        if currency is None:
            raise ValueError("Invalid value for `currency`, must not be `None`")  # noqa: E501

        self._currency = currency

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.openapi_types):
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

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, ExecutionRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
