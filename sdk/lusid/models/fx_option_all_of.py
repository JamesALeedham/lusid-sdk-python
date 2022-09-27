# coding: utf-8

"""
    LUSID API

    FINBOURNE Technology  # noqa: E501

    The version of the OpenAPI document: 0.11.4822
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


class FxOptionAllOf(object):
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
        'start_date': 'datetime',
        'dom_ccy': 'str',
        'dom_amount': 'float',
        'fgn_ccy': 'str',
        'fgn_amount': 'float',
        'strike': 'float',
        'barriers': 'list[Barrier]',
        'exercise_type': 'str',
        'is_call_not_put': 'bool',
        'is_delivery_not_cash': 'bool',
        'is_payoff_digital': 'bool',
        'option_maturity_date': 'datetime',
        'option_settlement_date': 'datetime',
        'payout_style': 'str',
        'premium': 'Premium',
        'touches': 'list[Touch]',
        'instrument_type': 'str'
    }

    attribute_map = {
        'start_date': 'startDate',
        'dom_ccy': 'domCcy',
        'dom_amount': 'domAmount',
        'fgn_ccy': 'fgnCcy',
        'fgn_amount': 'fgnAmount',
        'strike': 'strike',
        'barriers': 'barriers',
        'exercise_type': 'exerciseType',
        'is_call_not_put': 'isCallNotPut',
        'is_delivery_not_cash': 'isDeliveryNotCash',
        'is_payoff_digital': 'isPayoffDigital',
        'option_maturity_date': 'optionMaturityDate',
        'option_settlement_date': 'optionSettlementDate',
        'payout_style': 'payoutStyle',
        'premium': 'premium',
        'touches': 'touches',
        'instrument_type': 'instrumentType'
    }

    required_map = {
        'start_date': 'required',
        'dom_ccy': 'required',
        'dom_amount': 'optional',
        'fgn_ccy': 'required',
        'fgn_amount': 'optional',
        'strike': 'optional',
        'barriers': 'optional',
        'exercise_type': 'optional',
        'is_call_not_put': 'required',
        'is_delivery_not_cash': 'required',
        'is_payoff_digital': 'optional',
        'option_maturity_date': 'required',
        'option_settlement_date': 'required',
        'payout_style': 'optional',
        'premium': 'optional',
        'touches': 'optional',
        'instrument_type': 'required'
    }

    def __init__(self, start_date=None, dom_ccy=None, dom_amount=None, fgn_ccy=None, fgn_amount=None, strike=None, barriers=None, exercise_type=None, is_call_not_put=None, is_delivery_not_cash=None, is_payoff_digital=None, option_maturity_date=None, option_settlement_date=None, payout_style=None, premium=None, touches=None, instrument_type=None, local_vars_configuration=None):  # noqa: E501
        """FxOptionAllOf - a model defined in OpenAPI"
        
        :param start_date:  The start date of the instrument. This is normally synonymous with the trade-date. (required)
        :type start_date: datetime
        :param dom_ccy:  The domestic currency of the instrument. (required)
        :type dom_ccy: str
        :param dom_amount:  The Amount of DomCcy that will be exchanged if the option is exercised.  This amount should be a positive number, with the Call/Put flag used to indicate direction.  The corresponding amount of FgnCcy that will be exchanged is this amount times the strike.  Note there is no rounding performed on this computed value.  This is an optional field, if not set the option ContractSize will default to 1.
        :type dom_amount: float
        :param fgn_ccy:  The foreign currency of the FX. (required)
        :type fgn_ccy: str
        :param fgn_amount:  For a vanilla FxOption contract, FgnAmount cannot be set.  In case of a digital FxOption (IsPayoffDigital==true)  a payoff (if the option is in the money) can be either  in domestic or in foreign currency - for the latter  FgnAmount must be set.  Note: It is invalid to have FgnAmount and DomAmount  at the same time.
        :type fgn_amount: float
        :param strike:  The strike of the option.
        :type strike: float
        :param barriers:  For a barrier option the list should not be empty. Up to two barriers are supported.  An option cannot be at the same time barrier- and touch-option.  One (or both) of the lists must be empty.
        :type barriers: list[lusid.Barrier]
        :param exercise_type:  Type of optionality that is present; European, American.    Supported string (enumeration) values are: [European, American].
        :type exercise_type: str
        :param is_call_not_put:  True if the option is a call, false if the option is a put. (required)
        :type is_call_not_put: bool
        :param is_delivery_not_cash:  True if the option is settled in cash, false if delivery. (required)
        :type is_delivery_not_cash: bool
        :param is_payoff_digital:  By default IsPayoffDigital is false. If IsPayoffDigital=true,  the option is 'digital', and the option payoff is 0 or 1 unit of currency,  instead of a vanilla CallPayoff=max(spot-strike,0) or PutPayoff=max(strike-spot,0).
        :type is_payoff_digital: bool
        :param option_maturity_date:  The maturity date of the option. (required)
        :type option_maturity_date: datetime
        :param option_settlement_date:  The settlement date of the option. (required)
        :type option_settlement_date: datetime
        :param payout_style:  PayoutStyle for touch options.  For options without touch optionality (IsTouch==false),  PayoutStyle should not be set (ot it can be set to None)  For options with touch optionality (IsTouch==true),  PayoutStyle cannot be None.    Supported string (enumeration) values are: [Deferred, Immediate].
        :type payout_style: str
        :param premium: 
        :type premium: lusid.Premium
        :param touches:  For a touch option the list should not be empty. Up to two touches are supported.  An option cannot be at the same time barrier- and touch-option.  One (or both) of the lists must be empty.
        :type touches: list[lusid.Touch]
        :param instrument_type:  The available values are: QuotedSecurity, InterestRateSwap, FxForward, Future, ExoticInstrument, FxOption, CreditDefaultSwap, InterestRateSwaption, Bond, EquityOption, FixedLeg, FloatingLeg, BespokeCashFlowsLeg, Unknown, TermDeposit, ContractForDifference, EquitySwap, CashPerpetual, CapFloor, CashSettled, CdsIndex, Basket, FundingLeg, FxSwap, ForwardRateAgreement, SimpleInstrument, Repo, Equity, ExchangeTradedOption, ReferenceInstrument, ComplexBond, InflationLinkedBond (required)
        :type instrument_type: str

        """  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._start_date = None
        self._dom_ccy = None
        self._dom_amount = None
        self._fgn_ccy = None
        self._fgn_amount = None
        self._strike = None
        self._barriers = None
        self._exercise_type = None
        self._is_call_not_put = None
        self._is_delivery_not_cash = None
        self._is_payoff_digital = None
        self._option_maturity_date = None
        self._option_settlement_date = None
        self._payout_style = None
        self._premium = None
        self._touches = None
        self._instrument_type = None
        self.discriminator = None

        self.start_date = start_date
        self.dom_ccy = dom_ccy
        self.dom_amount = dom_amount
        self.fgn_ccy = fgn_ccy
        self.fgn_amount = fgn_amount
        self.strike = strike
        self.barriers = barriers
        self.exercise_type = exercise_type
        self.is_call_not_put = is_call_not_put
        self.is_delivery_not_cash = is_delivery_not_cash
        if is_payoff_digital is not None:
            self.is_payoff_digital = is_payoff_digital
        self.option_maturity_date = option_maturity_date
        self.option_settlement_date = option_settlement_date
        self.payout_style = payout_style
        if premium is not None:
            self.premium = premium
        self.touches = touches
        self.instrument_type = instrument_type

    @property
    def start_date(self):
        """Gets the start_date of this FxOptionAllOf.  # noqa: E501

        The start date of the instrument. This is normally synonymous with the trade-date.  # noqa: E501

        :return: The start_date of this FxOptionAllOf.  # noqa: E501
        :rtype: datetime
        """
        return self._start_date

    @start_date.setter
    def start_date(self, start_date):
        """Sets the start_date of this FxOptionAllOf.

        The start date of the instrument. This is normally synonymous with the trade-date.  # noqa: E501

        :param start_date: The start_date of this FxOptionAllOf.  # noqa: E501
        :type start_date: datetime
        """
        if self.local_vars_configuration.client_side_validation and start_date is None:  # noqa: E501
            raise ValueError("Invalid value for `start_date`, must not be `None`")  # noqa: E501

        self._start_date = start_date

    @property
    def dom_ccy(self):
        """Gets the dom_ccy of this FxOptionAllOf.  # noqa: E501

        The domestic currency of the instrument.  # noqa: E501

        :return: The dom_ccy of this FxOptionAllOf.  # noqa: E501
        :rtype: str
        """
        return self._dom_ccy

    @dom_ccy.setter
    def dom_ccy(self, dom_ccy):
        """Sets the dom_ccy of this FxOptionAllOf.

        The domestic currency of the instrument.  # noqa: E501

        :param dom_ccy: The dom_ccy of this FxOptionAllOf.  # noqa: E501
        :type dom_ccy: str
        """
        if self.local_vars_configuration.client_side_validation and dom_ccy is None:  # noqa: E501
            raise ValueError("Invalid value for `dom_ccy`, must not be `None`")  # noqa: E501

        self._dom_ccy = dom_ccy

    @property
    def dom_amount(self):
        """Gets the dom_amount of this FxOptionAllOf.  # noqa: E501

        The Amount of DomCcy that will be exchanged if the option is exercised.  This amount should be a positive number, with the Call/Put flag used to indicate direction.  The corresponding amount of FgnCcy that will be exchanged is this amount times the strike.  Note there is no rounding performed on this computed value.  This is an optional field, if not set the option ContractSize will default to 1.  # noqa: E501

        :return: The dom_amount of this FxOptionAllOf.  # noqa: E501
        :rtype: float
        """
        return self._dom_amount

    @dom_amount.setter
    def dom_amount(self, dom_amount):
        """Sets the dom_amount of this FxOptionAllOf.

        The Amount of DomCcy that will be exchanged if the option is exercised.  This amount should be a positive number, with the Call/Put flag used to indicate direction.  The corresponding amount of FgnCcy that will be exchanged is this amount times the strike.  Note there is no rounding performed on this computed value.  This is an optional field, if not set the option ContractSize will default to 1.  # noqa: E501

        :param dom_amount: The dom_amount of this FxOptionAllOf.  # noqa: E501
        :type dom_amount: float
        """

        self._dom_amount = dom_amount

    @property
    def fgn_ccy(self):
        """Gets the fgn_ccy of this FxOptionAllOf.  # noqa: E501

        The foreign currency of the FX.  # noqa: E501

        :return: The fgn_ccy of this FxOptionAllOf.  # noqa: E501
        :rtype: str
        """
        return self._fgn_ccy

    @fgn_ccy.setter
    def fgn_ccy(self, fgn_ccy):
        """Sets the fgn_ccy of this FxOptionAllOf.

        The foreign currency of the FX.  # noqa: E501

        :param fgn_ccy: The fgn_ccy of this FxOptionAllOf.  # noqa: E501
        :type fgn_ccy: str
        """
        if self.local_vars_configuration.client_side_validation and fgn_ccy is None:  # noqa: E501
            raise ValueError("Invalid value for `fgn_ccy`, must not be `None`")  # noqa: E501

        self._fgn_ccy = fgn_ccy

    @property
    def fgn_amount(self):
        """Gets the fgn_amount of this FxOptionAllOf.  # noqa: E501

        For a vanilla FxOption contract, FgnAmount cannot be set.  In case of a digital FxOption (IsPayoffDigital==true)  a payoff (if the option is in the money) can be either  in domestic or in foreign currency - for the latter  FgnAmount must be set.  Note: It is invalid to have FgnAmount and DomAmount  at the same time.  # noqa: E501

        :return: The fgn_amount of this FxOptionAllOf.  # noqa: E501
        :rtype: float
        """
        return self._fgn_amount

    @fgn_amount.setter
    def fgn_amount(self, fgn_amount):
        """Sets the fgn_amount of this FxOptionAllOf.

        For a vanilla FxOption contract, FgnAmount cannot be set.  In case of a digital FxOption (IsPayoffDigital==true)  a payoff (if the option is in the money) can be either  in domestic or in foreign currency - for the latter  FgnAmount must be set.  Note: It is invalid to have FgnAmount and DomAmount  at the same time.  # noqa: E501

        :param fgn_amount: The fgn_amount of this FxOptionAllOf.  # noqa: E501
        :type fgn_amount: float
        """

        self._fgn_amount = fgn_amount

    @property
    def strike(self):
        """Gets the strike of this FxOptionAllOf.  # noqa: E501

        The strike of the option.  # noqa: E501

        :return: The strike of this FxOptionAllOf.  # noqa: E501
        :rtype: float
        """
        return self._strike

    @strike.setter
    def strike(self, strike):
        """Sets the strike of this FxOptionAllOf.

        The strike of the option.  # noqa: E501

        :param strike: The strike of this FxOptionAllOf.  # noqa: E501
        :type strike: float
        """

        self._strike = strike

    @property
    def barriers(self):
        """Gets the barriers of this FxOptionAllOf.  # noqa: E501

        For a barrier option the list should not be empty. Up to two barriers are supported.  An option cannot be at the same time barrier- and touch-option.  One (or both) of the lists must be empty.  # noqa: E501

        :return: The barriers of this FxOptionAllOf.  # noqa: E501
        :rtype: list[lusid.Barrier]
        """
        return self._barriers

    @barriers.setter
    def barriers(self, barriers):
        """Sets the barriers of this FxOptionAllOf.

        For a barrier option the list should not be empty. Up to two barriers are supported.  An option cannot be at the same time barrier- and touch-option.  One (or both) of the lists must be empty.  # noqa: E501

        :param barriers: The barriers of this FxOptionAllOf.  # noqa: E501
        :type barriers: list[lusid.Barrier]
        """

        self._barriers = barriers

    @property
    def exercise_type(self):
        """Gets the exercise_type of this FxOptionAllOf.  # noqa: E501

        Type of optionality that is present; European, American.    Supported string (enumeration) values are: [European, American].  # noqa: E501

        :return: The exercise_type of this FxOptionAllOf.  # noqa: E501
        :rtype: str
        """
        return self._exercise_type

    @exercise_type.setter
    def exercise_type(self, exercise_type):
        """Sets the exercise_type of this FxOptionAllOf.

        Type of optionality that is present; European, American.    Supported string (enumeration) values are: [European, American].  # noqa: E501

        :param exercise_type: The exercise_type of this FxOptionAllOf.  # noqa: E501
        :type exercise_type: str
        """

        self._exercise_type = exercise_type

    @property
    def is_call_not_put(self):
        """Gets the is_call_not_put of this FxOptionAllOf.  # noqa: E501

        True if the option is a call, false if the option is a put.  # noqa: E501

        :return: The is_call_not_put of this FxOptionAllOf.  # noqa: E501
        :rtype: bool
        """
        return self._is_call_not_put

    @is_call_not_put.setter
    def is_call_not_put(self, is_call_not_put):
        """Sets the is_call_not_put of this FxOptionAllOf.

        True if the option is a call, false if the option is a put.  # noqa: E501

        :param is_call_not_put: The is_call_not_put of this FxOptionAllOf.  # noqa: E501
        :type is_call_not_put: bool
        """
        if self.local_vars_configuration.client_side_validation and is_call_not_put is None:  # noqa: E501
            raise ValueError("Invalid value for `is_call_not_put`, must not be `None`")  # noqa: E501

        self._is_call_not_put = is_call_not_put

    @property
    def is_delivery_not_cash(self):
        """Gets the is_delivery_not_cash of this FxOptionAllOf.  # noqa: E501

        True if the option is settled in cash, false if delivery.  # noqa: E501

        :return: The is_delivery_not_cash of this FxOptionAllOf.  # noqa: E501
        :rtype: bool
        """
        return self._is_delivery_not_cash

    @is_delivery_not_cash.setter
    def is_delivery_not_cash(self, is_delivery_not_cash):
        """Sets the is_delivery_not_cash of this FxOptionAllOf.

        True if the option is settled in cash, false if delivery.  # noqa: E501

        :param is_delivery_not_cash: The is_delivery_not_cash of this FxOptionAllOf.  # noqa: E501
        :type is_delivery_not_cash: bool
        """
        if self.local_vars_configuration.client_side_validation and is_delivery_not_cash is None:  # noqa: E501
            raise ValueError("Invalid value for `is_delivery_not_cash`, must not be `None`")  # noqa: E501

        self._is_delivery_not_cash = is_delivery_not_cash

    @property
    def is_payoff_digital(self):
        """Gets the is_payoff_digital of this FxOptionAllOf.  # noqa: E501

        By default IsPayoffDigital is false. If IsPayoffDigital=true,  the option is 'digital', and the option payoff is 0 or 1 unit of currency,  instead of a vanilla CallPayoff=max(spot-strike,0) or PutPayoff=max(strike-spot,0).  # noqa: E501

        :return: The is_payoff_digital of this FxOptionAllOf.  # noqa: E501
        :rtype: bool
        """
        return self._is_payoff_digital

    @is_payoff_digital.setter
    def is_payoff_digital(self, is_payoff_digital):
        """Sets the is_payoff_digital of this FxOptionAllOf.

        By default IsPayoffDigital is false. If IsPayoffDigital=true,  the option is 'digital', and the option payoff is 0 or 1 unit of currency,  instead of a vanilla CallPayoff=max(spot-strike,0) or PutPayoff=max(strike-spot,0).  # noqa: E501

        :param is_payoff_digital: The is_payoff_digital of this FxOptionAllOf.  # noqa: E501
        :type is_payoff_digital: bool
        """

        self._is_payoff_digital = is_payoff_digital

    @property
    def option_maturity_date(self):
        """Gets the option_maturity_date of this FxOptionAllOf.  # noqa: E501

        The maturity date of the option.  # noqa: E501

        :return: The option_maturity_date of this FxOptionAllOf.  # noqa: E501
        :rtype: datetime
        """
        return self._option_maturity_date

    @option_maturity_date.setter
    def option_maturity_date(self, option_maturity_date):
        """Sets the option_maturity_date of this FxOptionAllOf.

        The maturity date of the option.  # noqa: E501

        :param option_maturity_date: The option_maturity_date of this FxOptionAllOf.  # noqa: E501
        :type option_maturity_date: datetime
        """
        if self.local_vars_configuration.client_side_validation and option_maturity_date is None:  # noqa: E501
            raise ValueError("Invalid value for `option_maturity_date`, must not be `None`")  # noqa: E501

        self._option_maturity_date = option_maturity_date

    @property
    def option_settlement_date(self):
        """Gets the option_settlement_date of this FxOptionAllOf.  # noqa: E501

        The settlement date of the option.  # noqa: E501

        :return: The option_settlement_date of this FxOptionAllOf.  # noqa: E501
        :rtype: datetime
        """
        return self._option_settlement_date

    @option_settlement_date.setter
    def option_settlement_date(self, option_settlement_date):
        """Sets the option_settlement_date of this FxOptionAllOf.

        The settlement date of the option.  # noqa: E501

        :param option_settlement_date: The option_settlement_date of this FxOptionAllOf.  # noqa: E501
        :type option_settlement_date: datetime
        """
        if self.local_vars_configuration.client_side_validation and option_settlement_date is None:  # noqa: E501
            raise ValueError("Invalid value for `option_settlement_date`, must not be `None`")  # noqa: E501

        self._option_settlement_date = option_settlement_date

    @property
    def payout_style(self):
        """Gets the payout_style of this FxOptionAllOf.  # noqa: E501

        PayoutStyle for touch options.  For options without touch optionality (IsTouch==false),  PayoutStyle should not be set (ot it can be set to None)  For options with touch optionality (IsTouch==true),  PayoutStyle cannot be None.    Supported string (enumeration) values are: [Deferred, Immediate].  # noqa: E501

        :return: The payout_style of this FxOptionAllOf.  # noqa: E501
        :rtype: str
        """
        return self._payout_style

    @payout_style.setter
    def payout_style(self, payout_style):
        """Sets the payout_style of this FxOptionAllOf.

        PayoutStyle for touch options.  For options without touch optionality (IsTouch==false),  PayoutStyle should not be set (ot it can be set to None)  For options with touch optionality (IsTouch==true),  PayoutStyle cannot be None.    Supported string (enumeration) values are: [Deferred, Immediate].  # noqa: E501

        :param payout_style: The payout_style of this FxOptionAllOf.  # noqa: E501
        :type payout_style: str
        """

        self._payout_style = payout_style

    @property
    def premium(self):
        """Gets the premium of this FxOptionAllOf.  # noqa: E501


        :return: The premium of this FxOptionAllOf.  # noqa: E501
        :rtype: lusid.Premium
        """
        return self._premium

    @premium.setter
    def premium(self, premium):
        """Sets the premium of this FxOptionAllOf.


        :param premium: The premium of this FxOptionAllOf.  # noqa: E501
        :type premium: lusid.Premium
        """

        self._premium = premium

    @property
    def touches(self):
        """Gets the touches of this FxOptionAllOf.  # noqa: E501

        For a touch option the list should not be empty. Up to two touches are supported.  An option cannot be at the same time barrier- and touch-option.  One (or both) of the lists must be empty.  # noqa: E501

        :return: The touches of this FxOptionAllOf.  # noqa: E501
        :rtype: list[lusid.Touch]
        """
        return self._touches

    @touches.setter
    def touches(self, touches):
        """Sets the touches of this FxOptionAllOf.

        For a touch option the list should not be empty. Up to two touches are supported.  An option cannot be at the same time barrier- and touch-option.  One (or both) of the lists must be empty.  # noqa: E501

        :param touches: The touches of this FxOptionAllOf.  # noqa: E501
        :type touches: list[lusid.Touch]
        """

        self._touches = touches

    @property
    def instrument_type(self):
        """Gets the instrument_type of this FxOptionAllOf.  # noqa: E501

        The available values are: QuotedSecurity, InterestRateSwap, FxForward, Future, ExoticInstrument, FxOption, CreditDefaultSwap, InterestRateSwaption, Bond, EquityOption, FixedLeg, FloatingLeg, BespokeCashFlowsLeg, Unknown, TermDeposit, ContractForDifference, EquitySwap, CashPerpetual, CapFloor, CashSettled, CdsIndex, Basket, FundingLeg, FxSwap, ForwardRateAgreement, SimpleInstrument, Repo, Equity, ExchangeTradedOption, ReferenceInstrument, ComplexBond, InflationLinkedBond  # noqa: E501

        :return: The instrument_type of this FxOptionAllOf.  # noqa: E501
        :rtype: str
        """
        return self._instrument_type

    @instrument_type.setter
    def instrument_type(self, instrument_type):
        """Sets the instrument_type of this FxOptionAllOf.

        The available values are: QuotedSecurity, InterestRateSwap, FxForward, Future, ExoticInstrument, FxOption, CreditDefaultSwap, InterestRateSwaption, Bond, EquityOption, FixedLeg, FloatingLeg, BespokeCashFlowsLeg, Unknown, TermDeposit, ContractForDifference, EquitySwap, CashPerpetual, CapFloor, CashSettled, CdsIndex, Basket, FundingLeg, FxSwap, ForwardRateAgreement, SimpleInstrument, Repo, Equity, ExchangeTradedOption, ReferenceInstrument, ComplexBond, InflationLinkedBond  # noqa: E501

        :param instrument_type: The instrument_type of this FxOptionAllOf.  # noqa: E501
        :type instrument_type: str
        """
        if self.local_vars_configuration.client_side_validation and instrument_type is None:  # noqa: E501
            raise ValueError("Invalid value for `instrument_type`, must not be `None`")  # noqa: E501
        allowed_values = ["QuotedSecurity", "InterestRateSwap", "FxForward", "Future", "ExoticInstrument", "FxOption", "CreditDefaultSwap", "InterestRateSwaption", "Bond", "EquityOption", "FixedLeg", "FloatingLeg", "BespokeCashFlowsLeg", "Unknown", "TermDeposit", "ContractForDifference", "EquitySwap", "CashPerpetual", "CapFloor", "CashSettled", "CdsIndex", "Basket", "FundingLeg", "FxSwap", "ForwardRateAgreement", "SimpleInstrument", "Repo", "Equity", "ExchangeTradedOption", "ReferenceInstrument", "ComplexBond", "InflationLinkedBond"]  # noqa: E501
        if self.local_vars_configuration.client_side_validation and instrument_type not in allowed_values:  # noqa: E501
            raise ValueError(
                "Invalid value for `instrument_type` ({0}), must be one of {1}"  # noqa: E501
                .format(instrument_type, allowed_values)
            )

        self._instrument_type = instrument_type

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
        if not isinstance(other, FxOptionAllOf):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, FxOptionAllOf):
            return True

        return self.to_dict() != other.to_dict()
