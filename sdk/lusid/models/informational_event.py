# coding: utf-8

"""
    LUSID API

    FINBOURNE Technology  # noqa: E501

    The version of the OpenAPI document: 1.0.154
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


class InformationalEvent(object):
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
        'event_status': 'str',
        'anchor_date': 'datetime',
        'event_window_end': 'datetime',
        'diagnostics': 'ResultValueDictionary',
        'instrument_event_type': 'str'
    }

    attribute_map = {
        'event_type': 'eventType',
        'event_status': 'eventStatus',
        'anchor_date': 'anchorDate',
        'event_window_end': 'eventWindowEnd',
        'diagnostics': 'diagnostics',
        'instrument_event_type': 'instrumentEventType'
    }

    required_map = {
        'event_type': 'required',
        'event_status': 'required',
        'anchor_date': 'required',
        'event_window_end': 'optional',
        'diagnostics': 'optional',
        'instrument_event_type': 'required'
    }

    def __init__(self, event_type=None, event_status=None, anchor_date=None, event_window_end=None, diagnostics=None, instrument_event_type=None, local_vars_configuration=None):  # noqa: E501
        """InformationalEvent - a model defined in OpenAPI"
        
        :param event_type:  What type of internal event does this represent; reset, exercise, amortisation etc. (required)
        :type event_type: str
        :param event_status:  What is the event status, is it a known (ie historic) or unknown (ie projected) event? (required)
        :type event_status: str
        :param anchor_date:  In the case of a point event, the single date on which the event occurs. In the case of an event which is  spread over a window, e.g. a barrier or American option, the start of that window. (required)
        :type anchor_date: datetime
        :param event_window_end:  In the case of a point event this is identical to the anchor date. In the case of an event that is spread over a window,  this is the end of that window.
        :type event_window_end: datetime
        :param diagnostics: 
        :type diagnostics: lusid.ResultValueDictionary
        :param instrument_event_type:  The Type of Event. The available values are: TransitionEvent, InformationalEvent, OpenEvent, CloseEvent, StockSplitEvent, BondDefaultEvent, CashDividendEvent, AmortisationEvent, CashFlowEvent, ExerciseEvent, ResetEvent, TriggerEvent, RawVendorEvent, InformationalErrorEvent (required)
        :type instrument_event_type: str

        """  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._event_type = None
        self._event_status = None
        self._anchor_date = None
        self._event_window_end = None
        self._diagnostics = None
        self._instrument_event_type = None
        self.discriminator = None

        self.event_type = event_type
        self.event_status = event_status
        self.anchor_date = anchor_date
        if event_window_end is not None:
            self.event_window_end = event_window_end
        if diagnostics is not None:
            self.diagnostics = diagnostics
        self.instrument_event_type = instrument_event_type

    @property
    def event_type(self):
        """Gets the event_type of this InformationalEvent.  # noqa: E501

        What type of internal event does this represent; reset, exercise, amortisation etc.  # noqa: E501

        :return: The event_type of this InformationalEvent.  # noqa: E501
        :rtype: str
        """
        return self._event_type

    @event_type.setter
    def event_type(self, event_type):
        """Sets the event_type of this InformationalEvent.

        What type of internal event does this represent; reset, exercise, amortisation etc.  # noqa: E501

        :param event_type: The event_type of this InformationalEvent.  # noqa: E501
        :type event_type: str
        """
        if self.local_vars_configuration.client_side_validation and event_type is None:  # noqa: E501
            raise ValueError("Invalid value for `event_type`, must not be `None`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                event_type is not None and len(event_type) < 1):
            raise ValueError("Invalid value for `event_type`, length must be greater than or equal to `1`")  # noqa: E501

        self._event_type = event_type

    @property
    def event_status(self):
        """Gets the event_status of this InformationalEvent.  # noqa: E501

        What is the event status, is it a known (ie historic) or unknown (ie projected) event?  # noqa: E501

        :return: The event_status of this InformationalEvent.  # noqa: E501
        :rtype: str
        """
        return self._event_status

    @event_status.setter
    def event_status(self, event_status):
        """Sets the event_status of this InformationalEvent.

        What is the event status, is it a known (ie historic) or unknown (ie projected) event?  # noqa: E501

        :param event_status: The event_status of this InformationalEvent.  # noqa: E501
        :type event_status: str
        """
        if self.local_vars_configuration.client_side_validation and event_status is None:  # noqa: E501
            raise ValueError("Invalid value for `event_status`, must not be `None`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                event_status is not None and len(event_status) < 1):
            raise ValueError("Invalid value for `event_status`, length must be greater than or equal to `1`")  # noqa: E501

        self._event_status = event_status

    @property
    def anchor_date(self):
        """Gets the anchor_date of this InformationalEvent.  # noqa: E501

        In the case of a point event, the single date on which the event occurs. In the case of an event which is  spread over a window, e.g. a barrier or American option, the start of that window.  # noqa: E501

        :return: The anchor_date of this InformationalEvent.  # noqa: E501
        :rtype: datetime
        """
        return self._anchor_date

    @anchor_date.setter
    def anchor_date(self, anchor_date):
        """Sets the anchor_date of this InformationalEvent.

        In the case of a point event, the single date on which the event occurs. In the case of an event which is  spread over a window, e.g. a barrier or American option, the start of that window.  # noqa: E501

        :param anchor_date: The anchor_date of this InformationalEvent.  # noqa: E501
        :type anchor_date: datetime
        """
        if self.local_vars_configuration.client_side_validation and anchor_date is None:  # noqa: E501
            raise ValueError("Invalid value for `anchor_date`, must not be `None`")  # noqa: E501

        self._anchor_date = anchor_date

    @property
    def event_window_end(self):
        """Gets the event_window_end of this InformationalEvent.  # noqa: E501

        In the case of a point event this is identical to the anchor date. In the case of an event that is spread over a window,  this is the end of that window.  # noqa: E501

        :return: The event_window_end of this InformationalEvent.  # noqa: E501
        :rtype: datetime
        """
        return self._event_window_end

    @event_window_end.setter
    def event_window_end(self, event_window_end):
        """Sets the event_window_end of this InformationalEvent.

        In the case of a point event this is identical to the anchor date. In the case of an event that is spread over a window,  this is the end of that window.  # noqa: E501

        :param event_window_end: The event_window_end of this InformationalEvent.  # noqa: E501
        :type event_window_end: datetime
        """

        self._event_window_end = event_window_end

    @property
    def diagnostics(self):
        """Gets the diagnostics of this InformationalEvent.  # noqa: E501


        :return: The diagnostics of this InformationalEvent.  # noqa: E501
        :rtype: lusid.ResultValueDictionary
        """
        return self._diagnostics

    @diagnostics.setter
    def diagnostics(self, diagnostics):
        """Sets the diagnostics of this InformationalEvent.


        :param diagnostics: The diagnostics of this InformationalEvent.  # noqa: E501
        :type diagnostics: lusid.ResultValueDictionary
        """

        self._diagnostics = diagnostics

    @property
    def instrument_event_type(self):
        """Gets the instrument_event_type of this InformationalEvent.  # noqa: E501

        The Type of Event. The available values are: TransitionEvent, InformationalEvent, OpenEvent, CloseEvent, StockSplitEvent, BondDefaultEvent, CashDividendEvent, AmortisationEvent, CashFlowEvent, ExerciseEvent, ResetEvent, TriggerEvent, RawVendorEvent, InformationalErrorEvent  # noqa: E501

        :return: The instrument_event_type of this InformationalEvent.  # noqa: E501
        :rtype: str
        """
        return self._instrument_event_type

    @instrument_event_type.setter
    def instrument_event_type(self, instrument_event_type):
        """Sets the instrument_event_type of this InformationalEvent.

        The Type of Event. The available values are: TransitionEvent, InformationalEvent, OpenEvent, CloseEvent, StockSplitEvent, BondDefaultEvent, CashDividendEvent, AmortisationEvent, CashFlowEvent, ExerciseEvent, ResetEvent, TriggerEvent, RawVendorEvent, InformationalErrorEvent  # noqa: E501

        :param instrument_event_type: The instrument_event_type of this InformationalEvent.  # noqa: E501
        :type instrument_event_type: str
        """
        if self.local_vars_configuration.client_side_validation and instrument_event_type is None:  # noqa: E501
            raise ValueError("Invalid value for `instrument_event_type`, must not be `None`")  # noqa: E501
        allowed_values = ["TransitionEvent", "InformationalEvent", "OpenEvent", "CloseEvent", "StockSplitEvent", "BondDefaultEvent", "CashDividendEvent", "AmortisationEvent", "CashFlowEvent", "ExerciseEvent", "ResetEvent", "TriggerEvent", "RawVendorEvent", "InformationalErrorEvent"]  # noqa: E501
        if self.local_vars_configuration.client_side_validation and instrument_event_type not in allowed_values:  # noqa: E501
            raise ValueError(
                "Invalid value for `instrument_event_type` ({0}), must be one of {1}"  # noqa: E501
                .format(instrument_event_type, allowed_values)
            )

        self._instrument_event_type = instrument_event_type

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
        if not isinstance(other, InformationalEvent):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, InformationalEvent):
            return True

        return self.to_dict() != other.to_dict()
