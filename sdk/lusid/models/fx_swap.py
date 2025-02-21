# coding: utf-8

"""
    LUSID API

    FINBOURNE Technology  # noqa: E501

    Contact: info@finbourne.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""


from __future__ import annotations
import pprint
import re  # noqa: F401
import json


from typing import Any, Dict, Optional
from pydantic import Field, StrictStr, validator
from lusid.models.fx_forward import FxForward
from lusid.models.lusid_instrument import LusidInstrument

class FxSwap(LusidInstrument):
    """
    LUSID representation of an FX Swap. Composed of two FX Forwards.                This instrument has multiple legs, to see how legs are used in LUSID see [knowledge base article KA-02252](https://support.lusid.com/knowledgebase/article/KA-02252).                | Leg Index | Leg Identifier | Description |  | --------- | -------------- | ----------- |  | 1 | NearDomesticLeg | Cash flows in the domestic currency for the near forward. |  | 2 | NearForeignLeg | Cash flows in the foreign currency for the near forward (not present for non-deliverable forwards). |  | 3 | FarDomesticLeg | Cash flows in the domestic currency for the far forward. |  | 4 | FarForeignLeg | Cash flows in the foreign currency for the far forward (not present for non-deliverable forwards). |  # noqa: E501
    """
    near_fx_forward: FxForward = Field(..., alias="nearFxForward")
    far_fx_forward: FxForward = Field(..., alias="farFxForward")
    notional_symmetry: Optional[StrictStr] = Field(None, alias="notionalSymmetry", description="The NotionalSymmetry allows for even and uneven FxSwaps to be supported.  An even FxSwap is one where the near and far fx forwards have the same notional value on at least one of the  legs. An uneven FxSwap is one where near and far fx forwards don't have the same notional on both the  domestic and foreign legs.  By default NotionalSymmetry will be set as even.    Supported string (enumeration) values are: [Even, Uneven].")
    instrument_type: StrictStr = Field(..., alias="instrumentType", description="The available values are: QuotedSecurity, InterestRateSwap, FxForward, Future, ExoticInstrument, FxOption, CreditDefaultSwap, InterestRateSwaption, Bond, EquityOption, FixedLeg, FloatingLeg, BespokeCashFlowsLeg, Unknown, TermDeposit, ContractForDifference, EquitySwap, CashPerpetual, CapFloor, CashSettled, CdsIndex, Basket, FundingLeg, FxSwap, ForwardRateAgreement, SimpleInstrument, Repo, Equity, ExchangeTradedOption, ReferenceInstrument, ComplexBond, InflationLinkedBond, InflationSwap, SimpleCashFlowLoan, TotalReturnSwap, InflationLeg")
    additional_properties: Dict[str, Any] = {}
    __properties = ["instrumentType", "nearFxForward", "farFxForward", "notionalSymmetry"]

    @validator('instrument_type')
    def instrument_type_validate_enum(cls, value):
        """Validates the enum"""
        if value not in ('QuotedSecurity', 'InterestRateSwap', 'FxForward', 'Future', 'ExoticInstrument', 'FxOption', 'CreditDefaultSwap', 'InterestRateSwaption', 'Bond', 'EquityOption', 'FixedLeg', 'FloatingLeg', 'BespokeCashFlowsLeg', 'Unknown', 'TermDeposit', 'ContractForDifference', 'EquitySwap', 'CashPerpetual', 'CapFloor', 'CashSettled', 'CdsIndex', 'Basket', 'FundingLeg', 'FxSwap', 'ForwardRateAgreement', 'SimpleInstrument', 'Repo', 'Equity', 'ExchangeTradedOption', 'ReferenceInstrument', 'ComplexBond', 'InflationLinkedBond', 'InflationSwap', 'SimpleCashFlowLoan', 'TotalReturnSwap', 'InflationLeg'):
            raise ValueError("must be one of enum values ('QuotedSecurity', 'InterestRateSwap', 'FxForward', 'Future', 'ExoticInstrument', 'FxOption', 'CreditDefaultSwap', 'InterestRateSwaption', 'Bond', 'EquityOption', 'FixedLeg', 'FloatingLeg', 'BespokeCashFlowsLeg', 'Unknown', 'TermDeposit', 'ContractForDifference', 'EquitySwap', 'CashPerpetual', 'CapFloor', 'CashSettled', 'CdsIndex', 'Basket', 'FundingLeg', 'FxSwap', 'ForwardRateAgreement', 'SimpleInstrument', 'Repo', 'Equity', 'ExchangeTradedOption', 'ReferenceInstrument', 'ComplexBond', 'InflationLinkedBond', 'InflationSwap', 'SimpleCashFlowLoan', 'TotalReturnSwap', 'InflationLeg')")
        return value

    class Config:
        """Pydantic configuration"""
        allow_population_by_field_name = True
        validate_assignment = True

    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.dict(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> FxSwap:
        """Create an instance of FxSwap from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                            "additional_properties"
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of near_fx_forward
        if self.near_fx_forward:
            _dict['nearFxForward'] = self.near_fx_forward.to_dict()
        # override the default output from pydantic by calling `to_dict()` of far_fx_forward
        if self.far_fx_forward:
            _dict['farFxForward'] = self.far_fx_forward.to_dict()
        # puts key-value pairs in additional_properties in the top level
        if self.additional_properties is not None:
            for _key, _value in self.additional_properties.items():
                _dict[_key] = _value

        # set to None if notional_symmetry (nullable) is None
        # and __fields_set__ contains the field
        if self.notional_symmetry is None and "notional_symmetry" in self.__fields_set__:
            _dict['notionalSymmetry'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> FxSwap:
        """Create an instance of FxSwap from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return FxSwap.parse_obj(obj)

        _obj = FxSwap.parse_obj({
            "instrument_type": obj.get("instrumentType"),
            "near_fx_forward": FxForward.from_dict(obj.get("nearFxForward")) if obj.get("nearFxForward") is not None else None,
            "far_fx_forward": FxForward.from_dict(obj.get("farFxForward")) if obj.get("farFxForward") is not None else None,
            "notional_symmetry": obj.get("notionalSymmetry")
        })
        # store additional fields in additional_properties
        for _key in obj.keys():
            if _key not in cls.__properties:
                _obj.additional_properties[_key] = obj.get(_key)

        return _obj
