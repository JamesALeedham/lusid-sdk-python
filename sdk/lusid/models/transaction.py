# coding: utf-8

"""
    LUSID API

    FINBOURNE Technology  # noqa: E501

    The version of the OpenAPI document: 0.11.5204
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


class Transaction(object):
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
        'transaction_id': 'str',
        'type': 'str',
        'instrument_identifiers': 'dict(str, str)',
        'instrument_scope': 'str',
        'instrument_uid': 'str',
        'transaction_date': 'datetime',
        'settlement_date': 'datetime',
        'units': 'float',
        'transaction_price': 'TransactionPrice',
        'total_consideration': 'CurrencyAndAmount',
        'exchange_rate': 'float',
        'transaction_currency': 'str',
        'properties': 'dict(str, PerpetualProperty)',
        'counterparty_id': 'str',
        'source': 'str',
        'entry_date_time': 'datetime',
        'otc_confirmation': 'OtcConfirmation',
        'transaction_status': 'str',
        'cancel_date_time': 'datetime',
        'order_id': 'ResourceId',
        'allocation_id': 'ResourceId'
    }

    attribute_map = {
        'transaction_id': 'transactionId',
        'type': 'type',
        'instrument_identifiers': 'instrumentIdentifiers',
        'instrument_scope': 'instrumentScope',
        'instrument_uid': 'instrumentUid',
        'transaction_date': 'transactionDate',
        'settlement_date': 'settlementDate',
        'units': 'units',
        'transaction_price': 'transactionPrice',
        'total_consideration': 'totalConsideration',
        'exchange_rate': 'exchangeRate',
        'transaction_currency': 'transactionCurrency',
        'properties': 'properties',
        'counterparty_id': 'counterpartyId',
        'source': 'source',
        'entry_date_time': 'entryDateTime',
        'otc_confirmation': 'otcConfirmation',
        'transaction_status': 'transactionStatus',
        'cancel_date_time': 'cancelDateTime',
        'order_id': 'orderId',
        'allocation_id': 'allocationId'
    }

    required_map = {
        'transaction_id': 'required',
        'type': 'required',
        'instrument_identifiers': 'optional',
        'instrument_scope': 'optional',
        'instrument_uid': 'required',
        'transaction_date': 'required',
        'settlement_date': 'required',
        'units': 'required',
        'transaction_price': 'optional',
        'total_consideration': 'required',
        'exchange_rate': 'optional',
        'transaction_currency': 'optional',
        'properties': 'optional',
        'counterparty_id': 'optional',
        'source': 'optional',
        'entry_date_time': 'optional',
        'otc_confirmation': 'optional',
        'transaction_status': 'optional',
        'cancel_date_time': 'optional',
        'order_id': 'optional',
        'allocation_id': 'optional'
    }

    def __init__(self, transaction_id=None, type=None, instrument_identifiers=None, instrument_scope=None, instrument_uid=None, transaction_date=None, settlement_date=None, units=None, transaction_price=None, total_consideration=None, exchange_rate=None, transaction_currency=None, properties=None, counterparty_id=None, source=None, entry_date_time=None, otc_confirmation=None, transaction_status=None, cancel_date_time=None, order_id=None, allocation_id=None, local_vars_configuration=None):  # noqa: E501
        """Transaction - a model defined in OpenAPI"
        
        :param transaction_id:  The unique identifier for the transaction. (required)
        :type transaction_id: str
        :param type:  The type of the transaction e.g. 'Buy', 'Sell'. The transaction type should have been pre-configured via the System Configuration API endpoint. (required)
        :type type: str
        :param instrument_identifiers:  A set of instrument identifiers that can resolve the transaction to a unique instrument.
        :type instrument_identifiers: dict(str, str)
        :param instrument_scope:  The scope in which the transaction's instrument lies.
        :type instrument_scope: str
        :param instrument_uid:  The unqiue Lusid Instrument Id (LUID) of the instrument that the transaction is in. (required)
        :type instrument_uid: str
        :param transaction_date:  The date of the transaction. (required)
        :type transaction_date: datetime
        :param settlement_date:  The settlement date of the transaction. (required)
        :type settlement_date: datetime
        :param units:  The number of units transacted in the associated instrument. (required)
        :type units: float
        :param transaction_price: 
        :type transaction_price: lusid.TransactionPrice
        :param total_consideration:  (required)
        :type total_consideration: lusid.CurrencyAndAmount
        :param exchange_rate:  The exchange rate between the transaction and settlement currency (settlement currency being represented by the TotalConsideration.Currency). For example if the transaction currency is in USD and the settlement currency is in GBP this this the USD/GBP rate.
        :type exchange_rate: float
        :param transaction_currency:  The transaction currency.
        :type transaction_currency: str
        :param properties:  Set of unique transaction properties and associated values to stored with the transaction. Each property will be from the 'Transaction' domain.
        :type properties: dict[str, lusid.PerpetualProperty]
        :param counterparty_id:  The identifier for the counterparty of the transaction.
        :type counterparty_id: str
        :param source:  The source of the transaction. This is used to look up the appropriate transaction group set in the transaction type configuration.
        :type source: str
        :param entry_date_time:  The asAt datetime that the transaction was added to LUSID.
        :type entry_date_time: datetime
        :param otc_confirmation: 
        :type otc_confirmation: lusid.OtcConfirmation
        :param transaction_status:  The status of the transaction. The available values are: Active, Amended, Cancelled
        :type transaction_status: str
        :param cancel_date_time:  If the transaction has been cancelled, the asAt datetime that the transaction was cancelled.
        :type cancel_date_time: datetime
        :param order_id: 
        :type order_id: lusid.ResourceId
        :param allocation_id: 
        :type allocation_id: lusid.ResourceId

        """  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._transaction_id = None
        self._type = None
        self._instrument_identifiers = None
        self._instrument_scope = None
        self._instrument_uid = None
        self._transaction_date = None
        self._settlement_date = None
        self._units = None
        self._transaction_price = None
        self._total_consideration = None
        self._exchange_rate = None
        self._transaction_currency = None
        self._properties = None
        self._counterparty_id = None
        self._source = None
        self._entry_date_time = None
        self._otc_confirmation = None
        self._transaction_status = None
        self._cancel_date_time = None
        self._order_id = None
        self._allocation_id = None
        self.discriminator = None

        self.transaction_id = transaction_id
        self.type = type
        self.instrument_identifiers = instrument_identifiers
        self.instrument_scope = instrument_scope
        self.instrument_uid = instrument_uid
        self.transaction_date = transaction_date
        self.settlement_date = settlement_date
        self.units = units
        if transaction_price is not None:
            self.transaction_price = transaction_price
        self.total_consideration = total_consideration
        self.exchange_rate = exchange_rate
        self.transaction_currency = transaction_currency
        self.properties = properties
        self.counterparty_id = counterparty_id
        self.source = source
        if entry_date_time is not None:
            self.entry_date_time = entry_date_time
        if otc_confirmation is not None:
            self.otc_confirmation = otc_confirmation
        if transaction_status is not None:
            self.transaction_status = transaction_status
        self.cancel_date_time = cancel_date_time
        if order_id is not None:
            self.order_id = order_id
        if allocation_id is not None:
            self.allocation_id = allocation_id

    @property
    def transaction_id(self):
        """Gets the transaction_id of this Transaction.  # noqa: E501

        The unique identifier for the transaction.  # noqa: E501

        :return: The transaction_id of this Transaction.  # noqa: E501
        :rtype: str
        """
        return self._transaction_id

    @transaction_id.setter
    def transaction_id(self, transaction_id):
        """Sets the transaction_id of this Transaction.

        The unique identifier for the transaction.  # noqa: E501

        :param transaction_id: The transaction_id of this Transaction.  # noqa: E501
        :type transaction_id: str
        """
        if self.local_vars_configuration.client_side_validation and transaction_id is None:  # noqa: E501
            raise ValueError("Invalid value for `transaction_id`, must not be `None`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                transaction_id is not None and len(transaction_id) < 1):
            raise ValueError("Invalid value for `transaction_id`, length must be greater than or equal to `1`")  # noqa: E501

        self._transaction_id = transaction_id

    @property
    def type(self):
        """Gets the type of this Transaction.  # noqa: E501

        The type of the transaction e.g. 'Buy', 'Sell'. The transaction type should have been pre-configured via the System Configuration API endpoint.  # noqa: E501

        :return: The type of this Transaction.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this Transaction.

        The type of the transaction e.g. 'Buy', 'Sell'. The transaction type should have been pre-configured via the System Configuration API endpoint.  # noqa: E501

        :param type: The type of this Transaction.  # noqa: E501
        :type type: str
        """
        if self.local_vars_configuration.client_side_validation and type is None:  # noqa: E501
            raise ValueError("Invalid value for `type`, must not be `None`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                type is not None and len(type) < 1):
            raise ValueError("Invalid value for `type`, length must be greater than or equal to `1`")  # noqa: E501

        self._type = type

    @property
    def instrument_identifiers(self):
        """Gets the instrument_identifiers of this Transaction.  # noqa: E501

        A set of instrument identifiers that can resolve the transaction to a unique instrument.  # noqa: E501

        :return: The instrument_identifiers of this Transaction.  # noqa: E501
        :rtype: dict(str, str)
        """
        return self._instrument_identifiers

    @instrument_identifiers.setter
    def instrument_identifiers(self, instrument_identifiers):
        """Sets the instrument_identifiers of this Transaction.

        A set of instrument identifiers that can resolve the transaction to a unique instrument.  # noqa: E501

        :param instrument_identifiers: The instrument_identifiers of this Transaction.  # noqa: E501
        :type instrument_identifiers: dict(str, str)
        """

        self._instrument_identifiers = instrument_identifiers

    @property
    def instrument_scope(self):
        """Gets the instrument_scope of this Transaction.  # noqa: E501

        The scope in which the transaction's instrument lies.  # noqa: E501

        :return: The instrument_scope of this Transaction.  # noqa: E501
        :rtype: str
        """
        return self._instrument_scope

    @instrument_scope.setter
    def instrument_scope(self, instrument_scope):
        """Sets the instrument_scope of this Transaction.

        The scope in which the transaction's instrument lies.  # noqa: E501

        :param instrument_scope: The instrument_scope of this Transaction.  # noqa: E501
        :type instrument_scope: str
        """

        self._instrument_scope = instrument_scope

    @property
    def instrument_uid(self):
        """Gets the instrument_uid of this Transaction.  # noqa: E501

        The unqiue Lusid Instrument Id (LUID) of the instrument that the transaction is in.  # noqa: E501

        :return: The instrument_uid of this Transaction.  # noqa: E501
        :rtype: str
        """
        return self._instrument_uid

    @instrument_uid.setter
    def instrument_uid(self, instrument_uid):
        """Sets the instrument_uid of this Transaction.

        The unqiue Lusid Instrument Id (LUID) of the instrument that the transaction is in.  # noqa: E501

        :param instrument_uid: The instrument_uid of this Transaction.  # noqa: E501
        :type instrument_uid: str
        """
        if self.local_vars_configuration.client_side_validation and instrument_uid is None:  # noqa: E501
            raise ValueError("Invalid value for `instrument_uid`, must not be `None`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                instrument_uid is not None and len(instrument_uid) < 1):
            raise ValueError("Invalid value for `instrument_uid`, length must be greater than or equal to `1`")  # noqa: E501

        self._instrument_uid = instrument_uid

    @property
    def transaction_date(self):
        """Gets the transaction_date of this Transaction.  # noqa: E501

        The date of the transaction.  # noqa: E501

        :return: The transaction_date of this Transaction.  # noqa: E501
        :rtype: datetime
        """
        return self._transaction_date

    @transaction_date.setter
    def transaction_date(self, transaction_date):
        """Sets the transaction_date of this Transaction.

        The date of the transaction.  # noqa: E501

        :param transaction_date: The transaction_date of this Transaction.  # noqa: E501
        :type transaction_date: datetime
        """
        if self.local_vars_configuration.client_side_validation and transaction_date is None:  # noqa: E501
            raise ValueError("Invalid value for `transaction_date`, must not be `None`")  # noqa: E501

        self._transaction_date = transaction_date

    @property
    def settlement_date(self):
        """Gets the settlement_date of this Transaction.  # noqa: E501

        The settlement date of the transaction.  # noqa: E501

        :return: The settlement_date of this Transaction.  # noqa: E501
        :rtype: datetime
        """
        return self._settlement_date

    @settlement_date.setter
    def settlement_date(self, settlement_date):
        """Sets the settlement_date of this Transaction.

        The settlement date of the transaction.  # noqa: E501

        :param settlement_date: The settlement_date of this Transaction.  # noqa: E501
        :type settlement_date: datetime
        """
        if self.local_vars_configuration.client_side_validation and settlement_date is None:  # noqa: E501
            raise ValueError("Invalid value for `settlement_date`, must not be `None`")  # noqa: E501

        self._settlement_date = settlement_date

    @property
    def units(self):
        """Gets the units of this Transaction.  # noqa: E501

        The number of units transacted in the associated instrument.  # noqa: E501

        :return: The units of this Transaction.  # noqa: E501
        :rtype: float
        """
        return self._units

    @units.setter
    def units(self, units):
        """Sets the units of this Transaction.

        The number of units transacted in the associated instrument.  # noqa: E501

        :param units: The units of this Transaction.  # noqa: E501
        :type units: float
        """
        if self.local_vars_configuration.client_side_validation and units is None:  # noqa: E501
            raise ValueError("Invalid value for `units`, must not be `None`")  # noqa: E501

        self._units = units

    @property
    def transaction_price(self):
        """Gets the transaction_price of this Transaction.  # noqa: E501


        :return: The transaction_price of this Transaction.  # noqa: E501
        :rtype: lusid.TransactionPrice
        """
        return self._transaction_price

    @transaction_price.setter
    def transaction_price(self, transaction_price):
        """Sets the transaction_price of this Transaction.


        :param transaction_price: The transaction_price of this Transaction.  # noqa: E501
        :type transaction_price: lusid.TransactionPrice
        """

        self._transaction_price = transaction_price

    @property
    def total_consideration(self):
        """Gets the total_consideration of this Transaction.  # noqa: E501


        :return: The total_consideration of this Transaction.  # noqa: E501
        :rtype: lusid.CurrencyAndAmount
        """
        return self._total_consideration

    @total_consideration.setter
    def total_consideration(self, total_consideration):
        """Sets the total_consideration of this Transaction.


        :param total_consideration: The total_consideration of this Transaction.  # noqa: E501
        :type total_consideration: lusid.CurrencyAndAmount
        """
        if self.local_vars_configuration.client_side_validation and total_consideration is None:  # noqa: E501
            raise ValueError("Invalid value for `total_consideration`, must not be `None`")  # noqa: E501

        self._total_consideration = total_consideration

    @property
    def exchange_rate(self):
        """Gets the exchange_rate of this Transaction.  # noqa: E501

        The exchange rate between the transaction and settlement currency (settlement currency being represented by the TotalConsideration.Currency). For example if the transaction currency is in USD and the settlement currency is in GBP this this the USD/GBP rate.  # noqa: E501

        :return: The exchange_rate of this Transaction.  # noqa: E501
        :rtype: float
        """
        return self._exchange_rate

    @exchange_rate.setter
    def exchange_rate(self, exchange_rate):
        """Sets the exchange_rate of this Transaction.

        The exchange rate between the transaction and settlement currency (settlement currency being represented by the TotalConsideration.Currency). For example if the transaction currency is in USD and the settlement currency is in GBP this this the USD/GBP rate.  # noqa: E501

        :param exchange_rate: The exchange_rate of this Transaction.  # noqa: E501
        :type exchange_rate: float
        """

        self._exchange_rate = exchange_rate

    @property
    def transaction_currency(self):
        """Gets the transaction_currency of this Transaction.  # noqa: E501

        The transaction currency.  # noqa: E501

        :return: The transaction_currency of this Transaction.  # noqa: E501
        :rtype: str
        """
        return self._transaction_currency

    @transaction_currency.setter
    def transaction_currency(self, transaction_currency):
        """Sets the transaction_currency of this Transaction.

        The transaction currency.  # noqa: E501

        :param transaction_currency: The transaction_currency of this Transaction.  # noqa: E501
        :type transaction_currency: str
        """

        self._transaction_currency = transaction_currency

    @property
    def properties(self):
        """Gets the properties of this Transaction.  # noqa: E501

        Set of unique transaction properties and associated values to stored with the transaction. Each property will be from the 'Transaction' domain.  # noqa: E501

        :return: The properties of this Transaction.  # noqa: E501
        :rtype: dict[str, lusid.PerpetualProperty]
        """
        return self._properties

    @properties.setter
    def properties(self, properties):
        """Sets the properties of this Transaction.

        Set of unique transaction properties and associated values to stored with the transaction. Each property will be from the 'Transaction' domain.  # noqa: E501

        :param properties: The properties of this Transaction.  # noqa: E501
        :type properties: dict[str, lusid.PerpetualProperty]
        """

        self._properties = properties

    @property
    def counterparty_id(self):
        """Gets the counterparty_id of this Transaction.  # noqa: E501

        The identifier for the counterparty of the transaction.  # noqa: E501

        :return: The counterparty_id of this Transaction.  # noqa: E501
        :rtype: str
        """
        return self._counterparty_id

    @counterparty_id.setter
    def counterparty_id(self, counterparty_id):
        """Sets the counterparty_id of this Transaction.

        The identifier for the counterparty of the transaction.  # noqa: E501

        :param counterparty_id: The counterparty_id of this Transaction.  # noqa: E501
        :type counterparty_id: str
        """

        self._counterparty_id = counterparty_id

    @property
    def source(self):
        """Gets the source of this Transaction.  # noqa: E501

        The source of the transaction. This is used to look up the appropriate transaction group set in the transaction type configuration.  # noqa: E501

        :return: The source of this Transaction.  # noqa: E501
        :rtype: str
        """
        return self._source

    @source.setter
    def source(self, source):
        """Sets the source of this Transaction.

        The source of the transaction. This is used to look up the appropriate transaction group set in the transaction type configuration.  # noqa: E501

        :param source: The source of this Transaction.  # noqa: E501
        :type source: str
        """

        self._source = source

    @property
    def entry_date_time(self):
        """Gets the entry_date_time of this Transaction.  # noqa: E501

        The asAt datetime that the transaction was added to LUSID.  # noqa: E501

        :return: The entry_date_time of this Transaction.  # noqa: E501
        :rtype: datetime
        """
        return self._entry_date_time

    @entry_date_time.setter
    def entry_date_time(self, entry_date_time):
        """Sets the entry_date_time of this Transaction.

        The asAt datetime that the transaction was added to LUSID.  # noqa: E501

        :param entry_date_time: The entry_date_time of this Transaction.  # noqa: E501
        :type entry_date_time: datetime
        """

        self._entry_date_time = entry_date_time

    @property
    def otc_confirmation(self):
        """Gets the otc_confirmation of this Transaction.  # noqa: E501


        :return: The otc_confirmation of this Transaction.  # noqa: E501
        :rtype: lusid.OtcConfirmation
        """
        return self._otc_confirmation

    @otc_confirmation.setter
    def otc_confirmation(self, otc_confirmation):
        """Sets the otc_confirmation of this Transaction.


        :param otc_confirmation: The otc_confirmation of this Transaction.  # noqa: E501
        :type otc_confirmation: lusid.OtcConfirmation
        """

        self._otc_confirmation = otc_confirmation

    @property
    def transaction_status(self):
        """Gets the transaction_status of this Transaction.  # noqa: E501

        The status of the transaction. The available values are: Active, Amended, Cancelled  # noqa: E501

        :return: The transaction_status of this Transaction.  # noqa: E501
        :rtype: str
        """
        return self._transaction_status

    @transaction_status.setter
    def transaction_status(self, transaction_status):
        """Sets the transaction_status of this Transaction.

        The status of the transaction. The available values are: Active, Amended, Cancelled  # noqa: E501

        :param transaction_status: The transaction_status of this Transaction.  # noqa: E501
        :type transaction_status: str
        """
        allowed_values = ["Active", "Amended", "Cancelled"]  # noqa: E501
        if self.local_vars_configuration.client_side_validation and transaction_status not in allowed_values:  # noqa: E501
            raise ValueError(
                "Invalid value for `transaction_status` ({0}), must be one of {1}"  # noqa: E501
                .format(transaction_status, allowed_values)
            )

        self._transaction_status = transaction_status

    @property
    def cancel_date_time(self):
        """Gets the cancel_date_time of this Transaction.  # noqa: E501

        If the transaction has been cancelled, the asAt datetime that the transaction was cancelled.  # noqa: E501

        :return: The cancel_date_time of this Transaction.  # noqa: E501
        :rtype: datetime
        """
        return self._cancel_date_time

    @cancel_date_time.setter
    def cancel_date_time(self, cancel_date_time):
        """Sets the cancel_date_time of this Transaction.

        If the transaction has been cancelled, the asAt datetime that the transaction was cancelled.  # noqa: E501

        :param cancel_date_time: The cancel_date_time of this Transaction.  # noqa: E501
        :type cancel_date_time: datetime
        """

        self._cancel_date_time = cancel_date_time

    @property
    def order_id(self):
        """Gets the order_id of this Transaction.  # noqa: E501


        :return: The order_id of this Transaction.  # noqa: E501
        :rtype: lusid.ResourceId
        """
        return self._order_id

    @order_id.setter
    def order_id(self, order_id):
        """Sets the order_id of this Transaction.


        :param order_id: The order_id of this Transaction.  # noqa: E501
        :type order_id: lusid.ResourceId
        """

        self._order_id = order_id

    @property
    def allocation_id(self):
        """Gets the allocation_id of this Transaction.  # noqa: E501


        :return: The allocation_id of this Transaction.  # noqa: E501
        :rtype: lusid.ResourceId
        """
        return self._allocation_id

    @allocation_id.setter
    def allocation_id(self, allocation_id):
        """Sets the allocation_id of this Transaction.


        :param allocation_id: The allocation_id of this Transaction.  # noqa: E501
        :type allocation_id: lusid.ResourceId
        """

        self._allocation_id = allocation_id

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
        if not isinstance(other, Transaction):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, Transaction):
            return True

        return self.to_dict() != other.to_dict()
