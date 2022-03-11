# coding: utf-8

"""
    LUSID API

    FINBOURNE Technology  # noqa: E501

    The version of the OpenAPI document: 0.11.4092
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


class PortfolioCashFlow(object):
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
        'group_by_id': 'int',
        'sequence_number': 'int',
        'effective_date': 'datetime',
        'sub_holding_keys': 'dict(str, PerpetualProperty)',
        'type': 'str',
        'movement_name': 'str',
        'cashflow': 'CurrencyAndAmount',
        'balance': 'CurrencyAndAmount',
        'fx_rate': 'float',
        'cashflow_reporting_currency': 'CurrencyAndAmount',
        'balance_reporting_currency': 'CurrencyAndAmount',
        'translation_gain_loss': 'CurrencyAndAmount',
        'cost_basis_reporting_currency': 'CurrencyAndAmount',
        'transaction': 'Transaction',
        'unrealised_gain_loss_reporting_currency': 'CurrencyAndAmount',
        'links': 'list[Link]'
    }

    attribute_map = {
        'group_by_id': 'groupById',
        'sequence_number': 'sequenceNumber',
        'effective_date': 'effectiveDate',
        'sub_holding_keys': 'subHoldingKeys',
        'type': 'type',
        'movement_name': 'movementName',
        'cashflow': 'cashflow',
        'balance': 'balance',
        'fx_rate': 'fxRate',
        'cashflow_reporting_currency': 'cashflowReportingCurrency',
        'balance_reporting_currency': 'balanceReportingCurrency',
        'translation_gain_loss': 'translationGainLoss',
        'cost_basis_reporting_currency': 'costBasisReportingCurrency',
        'transaction': 'transaction',
        'unrealised_gain_loss_reporting_currency': 'unrealisedGainLossReportingCurrency',
        'links': 'links'
    }

    required_map = {
        'group_by_id': 'required',
        'sequence_number': 'required',
        'effective_date': 'optional',
        'sub_holding_keys': 'optional',
        'type': 'required',
        'movement_name': 'required',
        'cashflow': 'required',
        'balance': 'required',
        'fx_rate': 'required',
        'cashflow_reporting_currency': 'required',
        'balance_reporting_currency': 'required',
        'translation_gain_loss': 'required',
        'cost_basis_reporting_currency': 'required',
        'transaction': 'optional',
        'unrealised_gain_loss_reporting_currency': 'required',
        'links': 'optional'
    }

    def __init__(self, group_by_id=None, sequence_number=None, effective_date=None, sub_holding_keys=None, type=None, movement_name=None, cashflow=None, balance=None, fx_rate=None, cashflow_reporting_currency=None, balance_reporting_currency=None, translation_gain_loss=None, cost_basis_reporting_currency=None, transaction=None, unrealised_gain_loss_reporting_currency=None, links=None, local_vars_configuration=None):  # noqa: E501
        """PortfolioCashFlow - a model defined in OpenAPI"
        
        :param group_by_id:  The groupBy subHoldings and currency. (required)
        :type group_by_id: int
        :param sequence_number:  Sequence number determining the order of the cash flow records. (required)
        :type sequence_number: int
        :param effective_date:  Indicates the date when the cash-flow settles.
        :type effective_date: datetime
        :param sub_holding_keys:  The sub-holding properties which identify the holding. Each property will be from the 'Transaction' domain. These are configured on a transaction portfolio.
        :type sub_holding_keys: dict[str, lusid.PerpetualProperty]
        :param type:  Indicates the record type (Closed, Open, Activity). (required)
        :type type: str
        :param movement_name:  Indicates the specific movement of the transaction that generated this cash flow. (required)
        :type movement_name: str
        :param cashflow:  (required)
        :type cashflow: lusid.CurrencyAndAmount
        :param balance:  (required)
        :type balance: lusid.CurrencyAndAmount
        :param fx_rate:  Exchange rate between the currency of this cash flow and the reporting currency. (required)
        :type fx_rate: float
        :param cashflow_reporting_currency:  (required)
        :type cashflow_reporting_currency: lusid.CurrencyAndAmount
        :param balance_reporting_currency:  (required)
        :type balance_reporting_currency: lusid.CurrencyAndAmount
        :param translation_gain_loss:  (required)
        :type translation_gain_loss: lusid.CurrencyAndAmount
        :param cost_basis_reporting_currency:  (required)
        :type cost_basis_reporting_currency: lusid.CurrencyAndAmount
        :param transaction: 
        :type transaction: lusid.Transaction
        :param unrealised_gain_loss_reporting_currency:  (required)
        :type unrealised_gain_loss_reporting_currency: lusid.CurrencyAndAmount
        :param links:  Collection of links.
        :type links: list[lusid.Link]

        """  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._group_by_id = None
        self._sequence_number = None
        self._effective_date = None
        self._sub_holding_keys = None
        self._type = None
        self._movement_name = None
        self._cashflow = None
        self._balance = None
        self._fx_rate = None
        self._cashflow_reporting_currency = None
        self._balance_reporting_currency = None
        self._translation_gain_loss = None
        self._cost_basis_reporting_currency = None
        self._transaction = None
        self._unrealised_gain_loss_reporting_currency = None
        self._links = None
        self.discriminator = None

        self.group_by_id = group_by_id
        self.sequence_number = sequence_number
        if effective_date is not None:
            self.effective_date = effective_date
        self.sub_holding_keys = sub_holding_keys
        self.type = type
        self.movement_name = movement_name
        self.cashflow = cashflow
        self.balance = balance
        self.fx_rate = fx_rate
        self.cashflow_reporting_currency = cashflow_reporting_currency
        self.balance_reporting_currency = balance_reporting_currency
        self.translation_gain_loss = translation_gain_loss
        self.cost_basis_reporting_currency = cost_basis_reporting_currency
        if transaction is not None:
            self.transaction = transaction
        self.unrealised_gain_loss_reporting_currency = unrealised_gain_loss_reporting_currency
        self.links = links

    @property
    def group_by_id(self):
        """Gets the group_by_id of this PortfolioCashFlow.  # noqa: E501

        The groupBy subHoldings and currency.  # noqa: E501

        :return: The group_by_id of this PortfolioCashFlow.  # noqa: E501
        :rtype: int
        """
        return self._group_by_id

    @group_by_id.setter
    def group_by_id(self, group_by_id):
        """Sets the group_by_id of this PortfolioCashFlow.

        The groupBy subHoldings and currency.  # noqa: E501

        :param group_by_id: The group_by_id of this PortfolioCashFlow.  # noqa: E501
        :type group_by_id: int
        """
        if self.local_vars_configuration.client_side_validation and group_by_id is None:  # noqa: E501
            raise ValueError("Invalid value for `group_by_id`, must not be `None`")  # noqa: E501

        self._group_by_id = group_by_id

    @property
    def sequence_number(self):
        """Gets the sequence_number of this PortfolioCashFlow.  # noqa: E501

        Sequence number determining the order of the cash flow records.  # noqa: E501

        :return: The sequence_number of this PortfolioCashFlow.  # noqa: E501
        :rtype: int
        """
        return self._sequence_number

    @sequence_number.setter
    def sequence_number(self, sequence_number):
        """Sets the sequence_number of this PortfolioCashFlow.

        Sequence number determining the order of the cash flow records.  # noqa: E501

        :param sequence_number: The sequence_number of this PortfolioCashFlow.  # noqa: E501
        :type sequence_number: int
        """
        if self.local_vars_configuration.client_side_validation and sequence_number is None:  # noqa: E501
            raise ValueError("Invalid value for `sequence_number`, must not be `None`")  # noqa: E501

        self._sequence_number = sequence_number

    @property
    def effective_date(self):
        """Gets the effective_date of this PortfolioCashFlow.  # noqa: E501

        Indicates the date when the cash-flow settles.  # noqa: E501

        :return: The effective_date of this PortfolioCashFlow.  # noqa: E501
        :rtype: datetime
        """
        return self._effective_date

    @effective_date.setter
    def effective_date(self, effective_date):
        """Sets the effective_date of this PortfolioCashFlow.

        Indicates the date when the cash-flow settles.  # noqa: E501

        :param effective_date: The effective_date of this PortfolioCashFlow.  # noqa: E501
        :type effective_date: datetime
        """

        self._effective_date = effective_date

    @property
    def sub_holding_keys(self):
        """Gets the sub_holding_keys of this PortfolioCashFlow.  # noqa: E501

        The sub-holding properties which identify the holding. Each property will be from the 'Transaction' domain. These are configured on a transaction portfolio.  # noqa: E501

        :return: The sub_holding_keys of this PortfolioCashFlow.  # noqa: E501
        :rtype: dict[str, lusid.PerpetualProperty]
        """
        return self._sub_holding_keys

    @sub_holding_keys.setter
    def sub_holding_keys(self, sub_holding_keys):
        """Sets the sub_holding_keys of this PortfolioCashFlow.

        The sub-holding properties which identify the holding. Each property will be from the 'Transaction' domain. These are configured on a transaction portfolio.  # noqa: E501

        :param sub_holding_keys: The sub_holding_keys of this PortfolioCashFlow.  # noqa: E501
        :type sub_holding_keys: dict[str, lusid.PerpetualProperty]
        """

        self._sub_holding_keys = sub_holding_keys

    @property
    def type(self):
        """Gets the type of this PortfolioCashFlow.  # noqa: E501

        Indicates the record type (Closed, Open, Activity).  # noqa: E501

        :return: The type of this PortfolioCashFlow.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this PortfolioCashFlow.

        Indicates the record type (Closed, Open, Activity).  # noqa: E501

        :param type: The type of this PortfolioCashFlow.  # noqa: E501
        :type type: str
        """
        if self.local_vars_configuration.client_side_validation and type is None:  # noqa: E501
            raise ValueError("Invalid value for `type`, must not be `None`")  # noqa: E501

        self._type = type

    @property
    def movement_name(self):
        """Gets the movement_name of this PortfolioCashFlow.  # noqa: E501

        Indicates the specific movement of the transaction that generated this cash flow.  # noqa: E501

        :return: The movement_name of this PortfolioCashFlow.  # noqa: E501
        :rtype: str
        """
        return self._movement_name

    @movement_name.setter
    def movement_name(self, movement_name):
        """Sets the movement_name of this PortfolioCashFlow.

        Indicates the specific movement of the transaction that generated this cash flow.  # noqa: E501

        :param movement_name: The movement_name of this PortfolioCashFlow.  # noqa: E501
        :type movement_name: str
        """
        if self.local_vars_configuration.client_side_validation and movement_name is None:  # noqa: E501
            raise ValueError("Invalid value for `movement_name`, must not be `None`")  # noqa: E501

        self._movement_name = movement_name

    @property
    def cashflow(self):
        """Gets the cashflow of this PortfolioCashFlow.  # noqa: E501


        :return: The cashflow of this PortfolioCashFlow.  # noqa: E501
        :rtype: lusid.CurrencyAndAmount
        """
        return self._cashflow

    @cashflow.setter
    def cashflow(self, cashflow):
        """Sets the cashflow of this PortfolioCashFlow.


        :param cashflow: The cashflow of this PortfolioCashFlow.  # noqa: E501
        :type cashflow: lusid.CurrencyAndAmount
        """
        if self.local_vars_configuration.client_side_validation and cashflow is None:  # noqa: E501
            raise ValueError("Invalid value for `cashflow`, must not be `None`")  # noqa: E501

        self._cashflow = cashflow

    @property
    def balance(self):
        """Gets the balance of this PortfolioCashFlow.  # noqa: E501


        :return: The balance of this PortfolioCashFlow.  # noqa: E501
        :rtype: lusid.CurrencyAndAmount
        """
        return self._balance

    @balance.setter
    def balance(self, balance):
        """Sets the balance of this PortfolioCashFlow.


        :param balance: The balance of this PortfolioCashFlow.  # noqa: E501
        :type balance: lusid.CurrencyAndAmount
        """
        if self.local_vars_configuration.client_side_validation and balance is None:  # noqa: E501
            raise ValueError("Invalid value for `balance`, must not be `None`")  # noqa: E501

        self._balance = balance

    @property
    def fx_rate(self):
        """Gets the fx_rate of this PortfolioCashFlow.  # noqa: E501

        Exchange rate between the currency of this cash flow and the reporting currency.  # noqa: E501

        :return: The fx_rate of this PortfolioCashFlow.  # noqa: E501
        :rtype: float
        """
        return self._fx_rate

    @fx_rate.setter
    def fx_rate(self, fx_rate):
        """Sets the fx_rate of this PortfolioCashFlow.

        Exchange rate between the currency of this cash flow and the reporting currency.  # noqa: E501

        :param fx_rate: The fx_rate of this PortfolioCashFlow.  # noqa: E501
        :type fx_rate: float
        """
        if self.local_vars_configuration.client_side_validation and fx_rate is None:  # noqa: E501
            raise ValueError("Invalid value for `fx_rate`, must not be `None`")  # noqa: E501

        self._fx_rate = fx_rate

    @property
    def cashflow_reporting_currency(self):
        """Gets the cashflow_reporting_currency of this PortfolioCashFlow.  # noqa: E501


        :return: The cashflow_reporting_currency of this PortfolioCashFlow.  # noqa: E501
        :rtype: lusid.CurrencyAndAmount
        """
        return self._cashflow_reporting_currency

    @cashflow_reporting_currency.setter
    def cashflow_reporting_currency(self, cashflow_reporting_currency):
        """Sets the cashflow_reporting_currency of this PortfolioCashFlow.


        :param cashflow_reporting_currency: The cashflow_reporting_currency of this PortfolioCashFlow.  # noqa: E501
        :type cashflow_reporting_currency: lusid.CurrencyAndAmount
        """
        if self.local_vars_configuration.client_side_validation and cashflow_reporting_currency is None:  # noqa: E501
            raise ValueError("Invalid value for `cashflow_reporting_currency`, must not be `None`")  # noqa: E501

        self._cashflow_reporting_currency = cashflow_reporting_currency

    @property
    def balance_reporting_currency(self):
        """Gets the balance_reporting_currency of this PortfolioCashFlow.  # noqa: E501


        :return: The balance_reporting_currency of this PortfolioCashFlow.  # noqa: E501
        :rtype: lusid.CurrencyAndAmount
        """
        return self._balance_reporting_currency

    @balance_reporting_currency.setter
    def balance_reporting_currency(self, balance_reporting_currency):
        """Sets the balance_reporting_currency of this PortfolioCashFlow.


        :param balance_reporting_currency: The balance_reporting_currency of this PortfolioCashFlow.  # noqa: E501
        :type balance_reporting_currency: lusid.CurrencyAndAmount
        """
        if self.local_vars_configuration.client_side_validation and balance_reporting_currency is None:  # noqa: E501
            raise ValueError("Invalid value for `balance_reporting_currency`, must not be `None`")  # noqa: E501

        self._balance_reporting_currency = balance_reporting_currency

    @property
    def translation_gain_loss(self):
        """Gets the translation_gain_loss of this PortfolioCashFlow.  # noqa: E501


        :return: The translation_gain_loss of this PortfolioCashFlow.  # noqa: E501
        :rtype: lusid.CurrencyAndAmount
        """
        return self._translation_gain_loss

    @translation_gain_loss.setter
    def translation_gain_loss(self, translation_gain_loss):
        """Sets the translation_gain_loss of this PortfolioCashFlow.


        :param translation_gain_loss: The translation_gain_loss of this PortfolioCashFlow.  # noqa: E501
        :type translation_gain_loss: lusid.CurrencyAndAmount
        """
        if self.local_vars_configuration.client_side_validation and translation_gain_loss is None:  # noqa: E501
            raise ValueError("Invalid value for `translation_gain_loss`, must not be `None`")  # noqa: E501

        self._translation_gain_loss = translation_gain_loss

    @property
    def cost_basis_reporting_currency(self):
        """Gets the cost_basis_reporting_currency of this PortfolioCashFlow.  # noqa: E501


        :return: The cost_basis_reporting_currency of this PortfolioCashFlow.  # noqa: E501
        :rtype: lusid.CurrencyAndAmount
        """
        return self._cost_basis_reporting_currency

    @cost_basis_reporting_currency.setter
    def cost_basis_reporting_currency(self, cost_basis_reporting_currency):
        """Sets the cost_basis_reporting_currency of this PortfolioCashFlow.


        :param cost_basis_reporting_currency: The cost_basis_reporting_currency of this PortfolioCashFlow.  # noqa: E501
        :type cost_basis_reporting_currency: lusid.CurrencyAndAmount
        """
        if self.local_vars_configuration.client_side_validation and cost_basis_reporting_currency is None:  # noqa: E501
            raise ValueError("Invalid value for `cost_basis_reporting_currency`, must not be `None`")  # noqa: E501

        self._cost_basis_reporting_currency = cost_basis_reporting_currency

    @property
    def transaction(self):
        """Gets the transaction of this PortfolioCashFlow.  # noqa: E501


        :return: The transaction of this PortfolioCashFlow.  # noqa: E501
        :rtype: lusid.Transaction
        """
        return self._transaction

    @transaction.setter
    def transaction(self, transaction):
        """Sets the transaction of this PortfolioCashFlow.


        :param transaction: The transaction of this PortfolioCashFlow.  # noqa: E501
        :type transaction: lusid.Transaction
        """

        self._transaction = transaction

    @property
    def unrealised_gain_loss_reporting_currency(self):
        """Gets the unrealised_gain_loss_reporting_currency of this PortfolioCashFlow.  # noqa: E501


        :return: The unrealised_gain_loss_reporting_currency of this PortfolioCashFlow.  # noqa: E501
        :rtype: lusid.CurrencyAndAmount
        """
        return self._unrealised_gain_loss_reporting_currency

    @unrealised_gain_loss_reporting_currency.setter
    def unrealised_gain_loss_reporting_currency(self, unrealised_gain_loss_reporting_currency):
        """Sets the unrealised_gain_loss_reporting_currency of this PortfolioCashFlow.


        :param unrealised_gain_loss_reporting_currency: The unrealised_gain_loss_reporting_currency of this PortfolioCashFlow.  # noqa: E501
        :type unrealised_gain_loss_reporting_currency: lusid.CurrencyAndAmount
        """
        if self.local_vars_configuration.client_side_validation and unrealised_gain_loss_reporting_currency is None:  # noqa: E501
            raise ValueError("Invalid value for `unrealised_gain_loss_reporting_currency`, must not be `None`")  # noqa: E501

        self._unrealised_gain_loss_reporting_currency = unrealised_gain_loss_reporting_currency

    @property
    def links(self):
        """Gets the links of this PortfolioCashFlow.  # noqa: E501

        Collection of links.  # noqa: E501

        :return: The links of this PortfolioCashFlow.  # noqa: E501
        :rtype: list[lusid.Link]
        """
        return self._links

    @links.setter
    def links(self, links):
        """Sets the links of this PortfolioCashFlow.

        Collection of links.  # noqa: E501

        :param links: The links of this PortfolioCashFlow.  # noqa: E501
        :type links: list[lusid.Link]
        """

        self._links = links

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
        if not isinstance(other, PortfolioCashFlow):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, PortfolioCashFlow):
            return True

        return self.to_dict() != other.to_dict()
