# coding: utf-8

"""
    LUSID API

    FINBOURNE Technology  # noqa: E501

    The version of the OpenAPI document: 1.0.535
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


class PlacementRequest(object):
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
        'id': 'ResourceId',
        'parent_placement_id': 'ResourceId',
        'block_ids': 'list[ResourceId]',
        'properties': 'dict(str, PerpetualProperty)',
        'instrument_identifiers': 'dict(str, str)',
        'quantity': 'float',
        'state': 'str',
        'side': 'str',
        'time_in_force': 'str',
        'type': 'str',
        'created_date': 'datetime',
        'limit_price': 'CurrencyAndAmount',
        'stop_price': 'CurrencyAndAmount',
        'counterparty': 'str',
        'execution_system': 'str',
        'entry_type': 'str'
    }

    attribute_map = {
        'id': 'id',
        'parent_placement_id': 'parentPlacementId',
        'block_ids': 'blockIds',
        'properties': 'properties',
        'instrument_identifiers': 'instrumentIdentifiers',
        'quantity': 'quantity',
        'state': 'state',
        'side': 'side',
        'time_in_force': 'timeInForce',
        'type': 'type',
        'created_date': 'createdDate',
        'limit_price': 'limitPrice',
        'stop_price': 'stopPrice',
        'counterparty': 'counterparty',
        'execution_system': 'executionSystem',
        'entry_type': 'entryType'
    }

    required_map = {
        'id': 'required',
        'parent_placement_id': 'optional',
        'block_ids': 'required',
        'properties': 'optional',
        'instrument_identifiers': 'required',
        'quantity': 'required',
        'state': 'required',
        'side': 'required',
        'time_in_force': 'required',
        'type': 'required',
        'created_date': 'required',
        'limit_price': 'optional',
        'stop_price': 'optional',
        'counterparty': 'optional',
        'execution_system': 'optional',
        'entry_type': 'optional'
    }

    def __init__(self, id=None, parent_placement_id=None, block_ids=None, properties=None, instrument_identifiers=None, quantity=None, state=None, side=None, time_in_force=None, type=None, created_date=None, limit_price=None, stop_price=None, counterparty=None, execution_system=None, entry_type=None, local_vars_configuration=None):  # noqa: E501
        """PlacementRequest - a model defined in OpenAPI"
        
        :param id:  (required)
        :type id: lusid.ResourceId
        :param parent_placement_id: 
        :type parent_placement_id: lusid.ResourceId
        :param block_ids:  The IDs of the Blocks associated with this placement. (required)
        :type block_ids: list[lusid.ResourceId]
        :param properties:  Client-defined properties associated with this order.
        :type properties: dict[str, lusid.PerpetualProperty]
        :param instrument_identifiers:  The instrument ordered. (required)
        :type instrument_identifiers: dict(str, str)
        :param quantity:  The quantity of given instrument ordered. (required)
        :type quantity: float
        :param state:  The state of this placement (typically a FIX state; Open, Filled, etc). (required)
        :type state: str
        :param side:  The side (Buy, Sell, ...) of this placement. (required)
        :type side: str
        :param time_in_force:  The time in force applicable to this placement (GTC, FOK, Day, etc) (required)
        :type time_in_force: str
        :param type:  The type of this placement (Market, Limit, etc). (required)
        :type type: str
        :param created_date:  The active date of this placement. (required)
        :type created_date: datetime
        :param limit_price: 
        :type limit_price: lusid.CurrencyAndAmount
        :param stop_price: 
        :type stop_price: lusid.CurrencyAndAmount
        :param counterparty:  Optionally specifies the market entity this placement is placed with.
        :type counterparty: str
        :param execution_system:  Optionally specifies the execution system in use.
        :type execution_system: str
        :param entry_type:  Optionally specifies the entry type of this placement.
        :type entry_type: str

        """  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._id = None
        self._parent_placement_id = None
        self._block_ids = None
        self._properties = None
        self._instrument_identifiers = None
        self._quantity = None
        self._state = None
        self._side = None
        self._time_in_force = None
        self._type = None
        self._created_date = None
        self._limit_price = None
        self._stop_price = None
        self._counterparty = None
        self._execution_system = None
        self._entry_type = None
        self.discriminator = None

        self.id = id
        if parent_placement_id is not None:
            self.parent_placement_id = parent_placement_id
        self.block_ids = block_ids
        self.properties = properties
        self.instrument_identifiers = instrument_identifiers
        self.quantity = quantity
        self.state = state
        self.side = side
        self.time_in_force = time_in_force
        self.type = type
        self.created_date = created_date
        if limit_price is not None:
            self.limit_price = limit_price
        if stop_price is not None:
            self.stop_price = stop_price
        self.counterparty = counterparty
        self.execution_system = execution_system
        self.entry_type = entry_type

    @property
    def id(self):
        """Gets the id of this PlacementRequest.  # noqa: E501


        :return: The id of this PlacementRequest.  # noqa: E501
        :rtype: lusid.ResourceId
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this PlacementRequest.


        :param id: The id of this PlacementRequest.  # noqa: E501
        :type id: lusid.ResourceId
        """
        if self.local_vars_configuration.client_side_validation and id is None:  # noqa: E501
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501

        self._id = id

    @property
    def parent_placement_id(self):
        """Gets the parent_placement_id of this PlacementRequest.  # noqa: E501


        :return: The parent_placement_id of this PlacementRequest.  # noqa: E501
        :rtype: lusid.ResourceId
        """
        return self._parent_placement_id

    @parent_placement_id.setter
    def parent_placement_id(self, parent_placement_id):
        """Sets the parent_placement_id of this PlacementRequest.


        :param parent_placement_id: The parent_placement_id of this PlacementRequest.  # noqa: E501
        :type parent_placement_id: lusid.ResourceId
        """

        self._parent_placement_id = parent_placement_id

    @property
    def block_ids(self):
        """Gets the block_ids of this PlacementRequest.  # noqa: E501

        The IDs of the Blocks associated with this placement.  # noqa: E501

        :return: The block_ids of this PlacementRequest.  # noqa: E501
        :rtype: list[lusid.ResourceId]
        """
        return self._block_ids

    @block_ids.setter
    def block_ids(self, block_ids):
        """Sets the block_ids of this PlacementRequest.

        The IDs of the Blocks associated with this placement.  # noqa: E501

        :param block_ids: The block_ids of this PlacementRequest.  # noqa: E501
        :type block_ids: list[lusid.ResourceId]
        """
        if self.local_vars_configuration.client_side_validation and block_ids is None:  # noqa: E501
            raise ValueError("Invalid value for `block_ids`, must not be `None`")  # noqa: E501

        self._block_ids = block_ids

    @property
    def properties(self):
        """Gets the properties of this PlacementRequest.  # noqa: E501

        Client-defined properties associated with this order.  # noqa: E501

        :return: The properties of this PlacementRequest.  # noqa: E501
        :rtype: dict[str, lusid.PerpetualProperty]
        """
        return self._properties

    @properties.setter
    def properties(self, properties):
        """Sets the properties of this PlacementRequest.

        Client-defined properties associated with this order.  # noqa: E501

        :param properties: The properties of this PlacementRequest.  # noqa: E501
        :type properties: dict[str, lusid.PerpetualProperty]
        """

        self._properties = properties

    @property
    def instrument_identifiers(self):
        """Gets the instrument_identifiers of this PlacementRequest.  # noqa: E501

        The instrument ordered.  # noqa: E501

        :return: The instrument_identifiers of this PlacementRequest.  # noqa: E501
        :rtype: dict(str, str)
        """
        return self._instrument_identifiers

    @instrument_identifiers.setter
    def instrument_identifiers(self, instrument_identifiers):
        """Sets the instrument_identifiers of this PlacementRequest.

        The instrument ordered.  # noqa: E501

        :param instrument_identifiers: The instrument_identifiers of this PlacementRequest.  # noqa: E501
        :type instrument_identifiers: dict(str, str)
        """
        if self.local_vars_configuration.client_side_validation and instrument_identifiers is None:  # noqa: E501
            raise ValueError("Invalid value for `instrument_identifiers`, must not be `None`")  # noqa: E501

        self._instrument_identifiers = instrument_identifiers

    @property
    def quantity(self):
        """Gets the quantity of this PlacementRequest.  # noqa: E501

        The quantity of given instrument ordered.  # noqa: E501

        :return: The quantity of this PlacementRequest.  # noqa: E501
        :rtype: float
        """
        return self._quantity

    @quantity.setter
    def quantity(self, quantity):
        """Sets the quantity of this PlacementRequest.

        The quantity of given instrument ordered.  # noqa: E501

        :param quantity: The quantity of this PlacementRequest.  # noqa: E501
        :type quantity: float
        """
        if self.local_vars_configuration.client_side_validation and quantity is None:  # noqa: E501
            raise ValueError("Invalid value for `quantity`, must not be `None`")  # noqa: E501

        self._quantity = quantity

    @property
    def state(self):
        """Gets the state of this PlacementRequest.  # noqa: E501

        The state of this placement (typically a FIX state; Open, Filled, etc).  # noqa: E501

        :return: The state of this PlacementRequest.  # noqa: E501
        :rtype: str
        """
        return self._state

    @state.setter
    def state(self, state):
        """Sets the state of this PlacementRequest.

        The state of this placement (typically a FIX state; Open, Filled, etc).  # noqa: E501

        :param state: The state of this PlacementRequest.  # noqa: E501
        :type state: str
        """
        if self.local_vars_configuration.client_side_validation and state is None:  # noqa: E501
            raise ValueError("Invalid value for `state`, must not be `None`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                state is not None and len(state) < 1):
            raise ValueError("Invalid value for `state`, length must be greater than or equal to `1`")  # noqa: E501

        self._state = state

    @property
    def side(self):
        """Gets the side of this PlacementRequest.  # noqa: E501

        The side (Buy, Sell, ...) of this placement.  # noqa: E501

        :return: The side of this PlacementRequest.  # noqa: E501
        :rtype: str
        """
        return self._side

    @side.setter
    def side(self, side):
        """Sets the side of this PlacementRequest.

        The side (Buy, Sell, ...) of this placement.  # noqa: E501

        :param side: The side of this PlacementRequest.  # noqa: E501
        :type side: str
        """
        if self.local_vars_configuration.client_side_validation and side is None:  # noqa: E501
            raise ValueError("Invalid value for `side`, must not be `None`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                side is not None and len(side) < 1):
            raise ValueError("Invalid value for `side`, length must be greater than or equal to `1`")  # noqa: E501

        self._side = side

    @property
    def time_in_force(self):
        """Gets the time_in_force of this PlacementRequest.  # noqa: E501

        The time in force applicable to this placement (GTC, FOK, Day, etc)  # noqa: E501

        :return: The time_in_force of this PlacementRequest.  # noqa: E501
        :rtype: str
        """
        return self._time_in_force

    @time_in_force.setter
    def time_in_force(self, time_in_force):
        """Sets the time_in_force of this PlacementRequest.

        The time in force applicable to this placement (GTC, FOK, Day, etc)  # noqa: E501

        :param time_in_force: The time_in_force of this PlacementRequest.  # noqa: E501
        :type time_in_force: str
        """
        if self.local_vars_configuration.client_side_validation and time_in_force is None:  # noqa: E501
            raise ValueError("Invalid value for `time_in_force`, must not be `None`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                time_in_force is not None and len(time_in_force) < 1):
            raise ValueError("Invalid value for `time_in_force`, length must be greater than or equal to `1`")  # noqa: E501

        self._time_in_force = time_in_force

    @property
    def type(self):
        """Gets the type of this PlacementRequest.  # noqa: E501

        The type of this placement (Market, Limit, etc).  # noqa: E501

        :return: The type of this PlacementRequest.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this PlacementRequest.

        The type of this placement (Market, Limit, etc).  # noqa: E501

        :param type: The type of this PlacementRequest.  # noqa: E501
        :type type: str
        """
        if self.local_vars_configuration.client_side_validation and type is None:  # noqa: E501
            raise ValueError("Invalid value for `type`, must not be `None`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                type is not None and len(type) < 1):
            raise ValueError("Invalid value for `type`, length must be greater than or equal to `1`")  # noqa: E501

        self._type = type

    @property
    def created_date(self):
        """Gets the created_date of this PlacementRequest.  # noqa: E501

        The active date of this placement.  # noqa: E501

        :return: The created_date of this PlacementRequest.  # noqa: E501
        :rtype: datetime
        """
        return self._created_date

    @created_date.setter
    def created_date(self, created_date):
        """Sets the created_date of this PlacementRequest.

        The active date of this placement.  # noqa: E501

        :param created_date: The created_date of this PlacementRequest.  # noqa: E501
        :type created_date: datetime
        """
        if self.local_vars_configuration.client_side_validation and created_date is None:  # noqa: E501
            raise ValueError("Invalid value for `created_date`, must not be `None`")  # noqa: E501

        self._created_date = created_date

    @property
    def limit_price(self):
        """Gets the limit_price of this PlacementRequest.  # noqa: E501


        :return: The limit_price of this PlacementRequest.  # noqa: E501
        :rtype: lusid.CurrencyAndAmount
        """
        return self._limit_price

    @limit_price.setter
    def limit_price(self, limit_price):
        """Sets the limit_price of this PlacementRequest.


        :param limit_price: The limit_price of this PlacementRequest.  # noqa: E501
        :type limit_price: lusid.CurrencyAndAmount
        """

        self._limit_price = limit_price

    @property
    def stop_price(self):
        """Gets the stop_price of this PlacementRequest.  # noqa: E501


        :return: The stop_price of this PlacementRequest.  # noqa: E501
        :rtype: lusid.CurrencyAndAmount
        """
        return self._stop_price

    @stop_price.setter
    def stop_price(self, stop_price):
        """Sets the stop_price of this PlacementRequest.


        :param stop_price: The stop_price of this PlacementRequest.  # noqa: E501
        :type stop_price: lusid.CurrencyAndAmount
        """

        self._stop_price = stop_price

    @property
    def counterparty(self):
        """Gets the counterparty of this PlacementRequest.  # noqa: E501

        Optionally specifies the market entity this placement is placed with.  # noqa: E501

        :return: The counterparty of this PlacementRequest.  # noqa: E501
        :rtype: str
        """
        return self._counterparty

    @counterparty.setter
    def counterparty(self, counterparty):
        """Sets the counterparty of this PlacementRequest.

        Optionally specifies the market entity this placement is placed with.  # noqa: E501

        :param counterparty: The counterparty of this PlacementRequest.  # noqa: E501
        :type counterparty: str
        """

        self._counterparty = counterparty

    @property
    def execution_system(self):
        """Gets the execution_system of this PlacementRequest.  # noqa: E501

        Optionally specifies the execution system in use.  # noqa: E501

        :return: The execution_system of this PlacementRequest.  # noqa: E501
        :rtype: str
        """
        return self._execution_system

    @execution_system.setter
    def execution_system(self, execution_system):
        """Sets the execution_system of this PlacementRequest.

        Optionally specifies the execution system in use.  # noqa: E501

        :param execution_system: The execution_system of this PlacementRequest.  # noqa: E501
        :type execution_system: str
        """
        if (self.local_vars_configuration.client_side_validation and
                execution_system is not None and len(execution_system) > 256):
            raise ValueError("Invalid value for `execution_system`, length must be less than or equal to `256`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                execution_system is not None and len(execution_system) < 1):
            raise ValueError("Invalid value for `execution_system`, length must be greater than or equal to `1`")  # noqa: E501

        self._execution_system = execution_system

    @property
    def entry_type(self):
        """Gets the entry_type of this PlacementRequest.  # noqa: E501

        Optionally specifies the entry type of this placement.  # noqa: E501

        :return: The entry_type of this PlacementRequest.  # noqa: E501
        :rtype: str
        """
        return self._entry_type

    @entry_type.setter
    def entry_type(self, entry_type):
        """Sets the entry_type of this PlacementRequest.

        Optionally specifies the entry type of this placement.  # noqa: E501

        :param entry_type: The entry_type of this PlacementRequest.  # noqa: E501
        :type entry_type: str
        """
        if (self.local_vars_configuration.client_side_validation and
                entry_type is not None and len(entry_type) > 256):
            raise ValueError("Invalid value for `entry_type`, length must be less than or equal to `256`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                entry_type is not None and len(entry_type) < 1):
            raise ValueError("Invalid value for `entry_type`, length must be greater than or equal to `1`")  # noqa: E501

        self._entry_type = entry_type

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
        if not isinstance(other, PlacementRequest):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, PlacementRequest):
            return True

        return self.to_dict() != other.to_dict()
