# coding: utf-8

"""
    LUSID API

    FINBOURNE Technology  # noqa: E501

    The version of the OpenAPI document: 0.11.4906
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


class FxSwapAllOf(object):
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
        'near_fx_forward': 'FxForward',
        'far_fx_forward': 'FxForward',
        'notional_symmetry': 'str',
        'instrument_type': 'str'
    }

    attribute_map = {
        'near_fx_forward': 'nearFxForward',
        'far_fx_forward': 'farFxForward',
        'notional_symmetry': 'notionalSymmetry',
        'instrument_type': 'instrumentType'
    }

    required_map = {
        'near_fx_forward': 'required',
        'far_fx_forward': 'required',
        'notional_symmetry': 'optional',
        'instrument_type': 'required'
    }

    def __init__(self, near_fx_forward=None, far_fx_forward=None, notional_symmetry=None, instrument_type=None, local_vars_configuration=None):  # noqa: E501
        """FxSwapAllOf - a model defined in OpenAPI"
        
        :param near_fx_forward:  (required)
        :type near_fx_forward: lusid.FxForward
        :param far_fx_forward:  (required)
        :type far_fx_forward: lusid.FxForward
        :param notional_symmetry:  The NotionalSymmetry allows for even and uneven FxSwaps to be supported.  An even FxSwap is one where the near and far fx forwards have the same notional value on at least one of the  legs. An uneven FxSwap is one where near and far fx forwards don't have the same notional on both the  domestic and foreign legs.  By default NotionalSymmetry will be set as even.    Supported string (enumeration) values are: [Even, Uneven].
        :type notional_symmetry: str
        :param instrument_type:  The available values are: QuotedSecurity, InterestRateSwap, FxForward, Future, ExoticInstrument, FxOption, CreditDefaultSwap, InterestRateSwaption, Bond, EquityOption, FixedLeg, FloatingLeg, BespokeCashFlowsLeg, Unknown, TermDeposit, ContractForDifference, EquitySwap, CashPerpetual, CapFloor, CashSettled, CdsIndex, Basket, FundingLeg, FxSwap, ForwardRateAgreement, SimpleInstrument, Repo, Equity, ExchangeTradedOption, ReferenceInstrument, ComplexBond, InflationLinkedBond, InflationSwap (required)
        :type instrument_type: str

        """  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._near_fx_forward = None
        self._far_fx_forward = None
        self._notional_symmetry = None
        self._instrument_type = None
        self.discriminator = None

        self.near_fx_forward = near_fx_forward
        self.far_fx_forward = far_fx_forward
        self.notional_symmetry = notional_symmetry
        self.instrument_type = instrument_type

    @property
    def near_fx_forward(self):
        """Gets the near_fx_forward of this FxSwapAllOf.  # noqa: E501


        :return: The near_fx_forward of this FxSwapAllOf.  # noqa: E501
        :rtype: lusid.FxForward
        """
        return self._near_fx_forward

    @near_fx_forward.setter
    def near_fx_forward(self, near_fx_forward):
        """Sets the near_fx_forward of this FxSwapAllOf.


        :param near_fx_forward: The near_fx_forward of this FxSwapAllOf.  # noqa: E501
        :type near_fx_forward: lusid.FxForward
        """
        if self.local_vars_configuration.client_side_validation and near_fx_forward is None:  # noqa: E501
            raise ValueError("Invalid value for `near_fx_forward`, must not be `None`")  # noqa: E501

        self._near_fx_forward = near_fx_forward

    @property
    def far_fx_forward(self):
        """Gets the far_fx_forward of this FxSwapAllOf.  # noqa: E501


        :return: The far_fx_forward of this FxSwapAllOf.  # noqa: E501
        :rtype: lusid.FxForward
        """
        return self._far_fx_forward

    @far_fx_forward.setter
    def far_fx_forward(self, far_fx_forward):
        """Sets the far_fx_forward of this FxSwapAllOf.


        :param far_fx_forward: The far_fx_forward of this FxSwapAllOf.  # noqa: E501
        :type far_fx_forward: lusid.FxForward
        """
        if self.local_vars_configuration.client_side_validation and far_fx_forward is None:  # noqa: E501
            raise ValueError("Invalid value for `far_fx_forward`, must not be `None`")  # noqa: E501

        self._far_fx_forward = far_fx_forward

    @property
    def notional_symmetry(self):
        """Gets the notional_symmetry of this FxSwapAllOf.  # noqa: E501

        The NotionalSymmetry allows for even and uneven FxSwaps to be supported.  An even FxSwap is one where the near and far fx forwards have the same notional value on at least one of the  legs. An uneven FxSwap is one where near and far fx forwards don't have the same notional on both the  domestic and foreign legs.  By default NotionalSymmetry will be set as even.    Supported string (enumeration) values are: [Even, Uneven].  # noqa: E501

        :return: The notional_symmetry of this FxSwapAllOf.  # noqa: E501
        :rtype: str
        """
        return self._notional_symmetry

    @notional_symmetry.setter
    def notional_symmetry(self, notional_symmetry):
        """Sets the notional_symmetry of this FxSwapAllOf.

        The NotionalSymmetry allows for even and uneven FxSwaps to be supported.  An even FxSwap is one where the near and far fx forwards have the same notional value on at least one of the  legs. An uneven FxSwap is one where near and far fx forwards don't have the same notional on both the  domestic and foreign legs.  By default NotionalSymmetry will be set as even.    Supported string (enumeration) values are: [Even, Uneven].  # noqa: E501

        :param notional_symmetry: The notional_symmetry of this FxSwapAllOf.  # noqa: E501
        :type notional_symmetry: str
        """

        self._notional_symmetry = notional_symmetry

    @property
    def instrument_type(self):
        """Gets the instrument_type of this FxSwapAllOf.  # noqa: E501

        The available values are: QuotedSecurity, InterestRateSwap, FxForward, Future, ExoticInstrument, FxOption, CreditDefaultSwap, InterestRateSwaption, Bond, EquityOption, FixedLeg, FloatingLeg, BespokeCashFlowsLeg, Unknown, TermDeposit, ContractForDifference, EquitySwap, CashPerpetual, CapFloor, CashSettled, CdsIndex, Basket, FundingLeg, FxSwap, ForwardRateAgreement, SimpleInstrument, Repo, Equity, ExchangeTradedOption, ReferenceInstrument, ComplexBond, InflationLinkedBond, InflationSwap  # noqa: E501

        :return: The instrument_type of this FxSwapAllOf.  # noqa: E501
        :rtype: str
        """
        return self._instrument_type

    @instrument_type.setter
    def instrument_type(self, instrument_type):
        """Sets the instrument_type of this FxSwapAllOf.

        The available values are: QuotedSecurity, InterestRateSwap, FxForward, Future, ExoticInstrument, FxOption, CreditDefaultSwap, InterestRateSwaption, Bond, EquityOption, FixedLeg, FloatingLeg, BespokeCashFlowsLeg, Unknown, TermDeposit, ContractForDifference, EquitySwap, CashPerpetual, CapFloor, CashSettled, CdsIndex, Basket, FundingLeg, FxSwap, ForwardRateAgreement, SimpleInstrument, Repo, Equity, ExchangeTradedOption, ReferenceInstrument, ComplexBond, InflationLinkedBond, InflationSwap  # noqa: E501

        :param instrument_type: The instrument_type of this FxSwapAllOf.  # noqa: E501
        :type instrument_type: str
        """
        if self.local_vars_configuration.client_side_validation and instrument_type is None:  # noqa: E501
            raise ValueError("Invalid value for `instrument_type`, must not be `None`")  # noqa: E501
        allowed_values = ["QuotedSecurity", "InterestRateSwap", "FxForward", "Future", "ExoticInstrument", "FxOption", "CreditDefaultSwap", "InterestRateSwaption", "Bond", "EquityOption", "FixedLeg", "FloatingLeg", "BespokeCashFlowsLeg", "Unknown", "TermDeposit", "ContractForDifference", "EquitySwap", "CashPerpetual", "CapFloor", "CashSettled", "CdsIndex", "Basket", "FundingLeg", "FxSwap", "ForwardRateAgreement", "SimpleInstrument", "Repo", "Equity", "ExchangeTradedOption", "ReferenceInstrument", "ComplexBond", "InflationLinkedBond", "InflationSwap"]  # noqa: E501
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
        if not isinstance(other, FxSwapAllOf):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, FxSwapAllOf):
            return True

        return self.to_dict() != other.to_dict()
