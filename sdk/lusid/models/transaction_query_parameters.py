# coding: utf-8

"""
    LUSID API

    FINBOURNE Technology  # noqa: E501

    The version of the OpenAPI document: 0.11.3234
    Contact: info@finbourne.com
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

class TransactionQueryParameters(object):
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
        'start_date': 'str',
        'end_date': 'str',
        'query_mode': 'str',
        'show_cancelled_transactions': 'bool'
    }

    attribute_map = {
        'start_date': 'startDate',
        'end_date': 'endDate',
        'query_mode': 'queryMode',
        'show_cancelled_transactions': 'showCancelledTransactions'
    }

    required_map = {
        'start_date': 'required',
        'end_date': 'required',
        'query_mode': 'optional',
        'show_cancelled_transactions': 'optional'
    }

    def __init__(self, start_date=None, end_date=None, query_mode=None, show_cancelled_transactions=None):  # noqa: E501
        """
        TransactionQueryParameters - a model defined in OpenAPI

        :param start_date:  The lower bound effective datetime or cut label (inclusive) from which to build the transactions. (required)
        :type start_date: str
        :param end_date:  The upper bound effective datetime or cut label (inclusive) from which to retrieve transactions. (required)
        :type end_date: str
        :param query_mode:  The date to compare against the upper and lower bounds for the effective datetime or cut label. Defaults to 'TradeDate' if not specified. The available values are: TradeDate, SettleDate
        :type query_mode: str
        :param show_cancelled_transactions:  Option to specify whether or not to include cancelled transactions in the output. Defaults to False if not specified.
        :type show_cancelled_transactions: bool

        """  # noqa: E501

        self._start_date = None
        self._end_date = None
        self._query_mode = None
        self._show_cancelled_transactions = None
        self.discriminator = None

        self.start_date = start_date
        self.end_date = end_date
        if query_mode is not None:
            self.query_mode = query_mode
        if show_cancelled_transactions is not None:
            self.show_cancelled_transactions = show_cancelled_transactions

    @property
    def start_date(self):
        """Gets the start_date of this TransactionQueryParameters.  # noqa: E501

        The lower bound effective datetime or cut label (inclusive) from which to build the transactions.  # noqa: E501

        :return: The start_date of this TransactionQueryParameters.  # noqa: E501
        :rtype: str
        """
        return self._start_date

    @start_date.setter
    def start_date(self, start_date):
        """Sets the start_date of this TransactionQueryParameters.

        The lower bound effective datetime or cut label (inclusive) from which to build the transactions.  # noqa: E501

        :param start_date: The start_date of this TransactionQueryParameters.  # noqa: E501
        :type: str
        """
        if start_date is None:
            raise ValueError("Invalid value for `start_date`, must not be `None`")  # noqa: E501

        self._start_date = start_date

    @property
    def end_date(self):
        """Gets the end_date of this TransactionQueryParameters.  # noqa: E501

        The upper bound effective datetime or cut label (inclusive) from which to retrieve transactions.  # noqa: E501

        :return: The end_date of this TransactionQueryParameters.  # noqa: E501
        :rtype: str
        """
        return self._end_date

    @end_date.setter
    def end_date(self, end_date):
        """Sets the end_date of this TransactionQueryParameters.

        The upper bound effective datetime or cut label (inclusive) from which to retrieve transactions.  # noqa: E501

        :param end_date: The end_date of this TransactionQueryParameters.  # noqa: E501
        :type: str
        """
        if end_date is None:
            raise ValueError("Invalid value for `end_date`, must not be `None`")  # noqa: E501

        self._end_date = end_date

    @property
    def query_mode(self):
        """Gets the query_mode of this TransactionQueryParameters.  # noqa: E501

        The date to compare against the upper and lower bounds for the effective datetime or cut label. Defaults to 'TradeDate' if not specified. The available values are: TradeDate, SettleDate  # noqa: E501

        :return: The query_mode of this TransactionQueryParameters.  # noqa: E501
        :rtype: str
        """
        return self._query_mode

    @query_mode.setter
    def query_mode(self, query_mode):
        """Sets the query_mode of this TransactionQueryParameters.

        The date to compare against the upper and lower bounds for the effective datetime or cut label. Defaults to 'TradeDate' if not specified. The available values are: TradeDate, SettleDate  # noqa: E501

        :param query_mode: The query_mode of this TransactionQueryParameters.  # noqa: E501
        :type: str
        """
        allowed_values = ["TradeDate", "SettleDate"]  # noqa: E501
        if query_mode not in allowed_values:
            raise ValueError(
                "Invalid value for `query_mode` ({0}), must be one of {1}"  # noqa: E501
                .format(query_mode, allowed_values)
            )

        self._query_mode = query_mode

    @property
    def show_cancelled_transactions(self):
        """Gets the show_cancelled_transactions of this TransactionQueryParameters.  # noqa: E501

        Option to specify whether or not to include cancelled transactions in the output. Defaults to False if not specified.  # noqa: E501

        :return: The show_cancelled_transactions of this TransactionQueryParameters.  # noqa: E501
        :rtype: bool
        """
        return self._show_cancelled_transactions

    @show_cancelled_transactions.setter
    def show_cancelled_transactions(self, show_cancelled_transactions):
        """Sets the show_cancelled_transactions of this TransactionQueryParameters.

        Option to specify whether or not to include cancelled transactions in the output. Defaults to False if not specified.  # noqa: E501

        :param show_cancelled_transactions: The show_cancelled_transactions of this TransactionQueryParameters.  # noqa: E501
        :type: bool
        """

        self._show_cancelled_transactions = show_cancelled_transactions

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
        if not isinstance(other, TransactionQueryParameters):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
