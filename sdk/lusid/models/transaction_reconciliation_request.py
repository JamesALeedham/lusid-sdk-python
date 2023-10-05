# coding: utf-8

"""
    LUSID API

    FINBOURNE Technology  # noqa: E501

    The version of the OpenAPI document: 1.0.571
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


class TransactionReconciliationRequest(object):
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
        'left_portfolio_id': 'ResourceId',
        'right_portfolio_id': 'ResourceId',
        'mapping_id': 'ResourceId',
        'from_transaction_date': 'datetime',
        'to_transaction_date': 'datetime',
        'as_at': 'datetime',
        'property_keys': 'list[str]'
    }

    attribute_map = {
        'left_portfolio_id': 'leftPortfolioId',
        'right_portfolio_id': 'rightPortfolioId',
        'mapping_id': 'mappingId',
        'from_transaction_date': 'fromTransactionDate',
        'to_transaction_date': 'toTransactionDate',
        'as_at': 'asAt',
        'property_keys': 'propertyKeys'
    }

    required_map = {
        'left_portfolio_id': 'required',
        'right_portfolio_id': 'required',
        'mapping_id': 'optional',
        'from_transaction_date': 'required',
        'to_transaction_date': 'required',
        'as_at': 'optional',
        'property_keys': 'optional'
    }

    def __init__(self, left_portfolio_id=None, right_portfolio_id=None, mapping_id=None, from_transaction_date=None, to_transaction_date=None, as_at=None, property_keys=None, local_vars_configuration=None):  # noqa: E501
        """TransactionReconciliationRequest - a model defined in OpenAPI"
        
        :param left_portfolio_id:  (required)
        :type left_portfolio_id: lusid.ResourceId
        :param right_portfolio_id:  (required)
        :type right_portfolio_id: lusid.ResourceId
        :param mapping_id: 
        :type mapping_id: lusid.ResourceId
        :param from_transaction_date:  (required)
        :type from_transaction_date: datetime
        :param to_transaction_date:  (required)
        :type to_transaction_date: datetime
        :param as_at: 
        :type as_at: datetime
        :param property_keys: 
        :type property_keys: list[str]

        """  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._left_portfolio_id = None
        self._right_portfolio_id = None
        self._mapping_id = None
        self._from_transaction_date = None
        self._to_transaction_date = None
        self._as_at = None
        self._property_keys = None
        self.discriminator = None

        self.left_portfolio_id = left_portfolio_id
        self.right_portfolio_id = right_portfolio_id
        if mapping_id is not None:
            self.mapping_id = mapping_id
        self.from_transaction_date = from_transaction_date
        self.to_transaction_date = to_transaction_date
        self.as_at = as_at
        self.property_keys = property_keys

    @property
    def left_portfolio_id(self):
        """Gets the left_portfolio_id of this TransactionReconciliationRequest.  # noqa: E501


        :return: The left_portfolio_id of this TransactionReconciliationRequest.  # noqa: E501
        :rtype: lusid.ResourceId
        """
        return self._left_portfolio_id

    @left_portfolio_id.setter
    def left_portfolio_id(self, left_portfolio_id):
        """Sets the left_portfolio_id of this TransactionReconciliationRequest.


        :param left_portfolio_id: The left_portfolio_id of this TransactionReconciliationRequest.  # noqa: E501
        :type left_portfolio_id: lusid.ResourceId
        """
        if self.local_vars_configuration.client_side_validation and left_portfolio_id is None:  # noqa: E501
            raise ValueError("Invalid value for `left_portfolio_id`, must not be `None`")  # noqa: E501

        self._left_portfolio_id = left_portfolio_id

    @property
    def right_portfolio_id(self):
        """Gets the right_portfolio_id of this TransactionReconciliationRequest.  # noqa: E501


        :return: The right_portfolio_id of this TransactionReconciliationRequest.  # noqa: E501
        :rtype: lusid.ResourceId
        """
        return self._right_portfolio_id

    @right_portfolio_id.setter
    def right_portfolio_id(self, right_portfolio_id):
        """Sets the right_portfolio_id of this TransactionReconciliationRequest.


        :param right_portfolio_id: The right_portfolio_id of this TransactionReconciliationRequest.  # noqa: E501
        :type right_portfolio_id: lusid.ResourceId
        """
        if self.local_vars_configuration.client_side_validation and right_portfolio_id is None:  # noqa: E501
            raise ValueError("Invalid value for `right_portfolio_id`, must not be `None`")  # noqa: E501

        self._right_portfolio_id = right_portfolio_id

    @property
    def mapping_id(self):
        """Gets the mapping_id of this TransactionReconciliationRequest.  # noqa: E501


        :return: The mapping_id of this TransactionReconciliationRequest.  # noqa: E501
        :rtype: lusid.ResourceId
        """
        return self._mapping_id

    @mapping_id.setter
    def mapping_id(self, mapping_id):
        """Sets the mapping_id of this TransactionReconciliationRequest.


        :param mapping_id: The mapping_id of this TransactionReconciliationRequest.  # noqa: E501
        :type mapping_id: lusid.ResourceId
        """

        self._mapping_id = mapping_id

    @property
    def from_transaction_date(self):
        """Gets the from_transaction_date of this TransactionReconciliationRequest.  # noqa: E501


        :return: The from_transaction_date of this TransactionReconciliationRequest.  # noqa: E501
        :rtype: datetime
        """
        return self._from_transaction_date

    @from_transaction_date.setter
    def from_transaction_date(self, from_transaction_date):
        """Sets the from_transaction_date of this TransactionReconciliationRequest.


        :param from_transaction_date: The from_transaction_date of this TransactionReconciliationRequest.  # noqa: E501
        :type from_transaction_date: datetime
        """
        if self.local_vars_configuration.client_side_validation and from_transaction_date is None:  # noqa: E501
            raise ValueError("Invalid value for `from_transaction_date`, must not be `None`")  # noqa: E501

        self._from_transaction_date = from_transaction_date

    @property
    def to_transaction_date(self):
        """Gets the to_transaction_date of this TransactionReconciliationRequest.  # noqa: E501


        :return: The to_transaction_date of this TransactionReconciliationRequest.  # noqa: E501
        :rtype: datetime
        """
        return self._to_transaction_date

    @to_transaction_date.setter
    def to_transaction_date(self, to_transaction_date):
        """Sets the to_transaction_date of this TransactionReconciliationRequest.


        :param to_transaction_date: The to_transaction_date of this TransactionReconciliationRequest.  # noqa: E501
        :type to_transaction_date: datetime
        """
        if self.local_vars_configuration.client_side_validation and to_transaction_date is None:  # noqa: E501
            raise ValueError("Invalid value for `to_transaction_date`, must not be `None`")  # noqa: E501

        self._to_transaction_date = to_transaction_date

    @property
    def as_at(self):
        """Gets the as_at of this TransactionReconciliationRequest.  # noqa: E501


        :return: The as_at of this TransactionReconciliationRequest.  # noqa: E501
        :rtype: datetime
        """
        return self._as_at

    @as_at.setter
    def as_at(self, as_at):
        """Sets the as_at of this TransactionReconciliationRequest.


        :param as_at: The as_at of this TransactionReconciliationRequest.  # noqa: E501
        :type as_at: datetime
        """

        self._as_at = as_at

    @property
    def property_keys(self):
        """Gets the property_keys of this TransactionReconciliationRequest.  # noqa: E501


        :return: The property_keys of this TransactionReconciliationRequest.  # noqa: E501
        :rtype: list[str]
        """
        return self._property_keys

    @property_keys.setter
    def property_keys(self, property_keys):
        """Sets the property_keys of this TransactionReconciliationRequest.


        :param property_keys: The property_keys of this TransactionReconciliationRequest.  # noqa: E501
        :type property_keys: list[str]
        """

        self._property_keys = property_keys

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
        if not isinstance(other, TransactionReconciliationRequest):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, TransactionReconciliationRequest):
            return True

        return self.to_dict() != other.to_dict()
