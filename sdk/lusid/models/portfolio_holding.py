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


from typing import Any, Dict, Optional, Union
from pydantic import BaseModel, Field, StrictFloat, StrictInt, StrictStr, constr
from lusid.models.currency_and_amount import CurrencyAndAmount
from lusid.models.model_property import ModelProperty
from lusid.models.perpetual_property import PerpetualProperty
from lusid.models.transaction import Transaction

class PortfolioHolding(BaseModel):
    """
    A list of holdings.  # noqa: E501
    """
    instrument_scope: Optional[StrictStr] = Field(None, alias="instrumentScope", description="The scope in which the holding's instrument is in.")
    instrument_uid: constr(strict=True, min_length=1) = Field(..., alias="instrumentUid", description="The unique Lusid Instrument Id (LUID) of the instrument that the holding is in.")
    sub_holding_keys: Optional[Dict[str, PerpetualProperty]] = Field(None, alias="subHoldingKeys", description="The sub-holding properties which identify the holding. Each property will be from the 'Transaction' domain. These are configured on a transaction portfolio.")
    properties: Optional[Dict[str, ModelProperty]] = Field(None, description="The properties which have been requested to be decorated onto the holding. These will be from the 'Instrument' or 'Holding' domain.")
    holding_type: constr(strict=True, min_length=1) = Field(..., alias="holdingType", description="The code for the type of the holding e.g. P, B, C, R, F etc.")
    units: Union[StrictFloat, StrictInt] = Field(..., description="The total number of units of the holding.")
    settled_units: Union[StrictFloat, StrictInt] = Field(..., alias="settledUnits", description="The total number of settled units of the holding.")
    cost: CurrencyAndAmount = Field(...)
    cost_portfolio_ccy: CurrencyAndAmount = Field(..., alias="costPortfolioCcy")
    transaction: Optional[Transaction] = None
    currency: Optional[StrictStr] = Field(None, description="The holding currency.")
    holding_type_name: Optional[StrictStr] = Field(None, alias="holdingTypeName", description="The decoded type of the holding e.g. Position, Balance, CashCommitment, Receivable, ForwardFX etc.")
    holding_id: Optional[StrictInt] = Field(None, alias="holdingId", description="A single identifier for the holding within the portfolio. The holdingId is constructed from the LusidInstrumentId, sub-holding keys and currrency and is unique within the portfolio.")
    __properties = ["instrumentScope", "instrumentUid", "subHoldingKeys", "properties", "holdingType", "units", "settledUnits", "cost", "costPortfolioCcy", "transaction", "currency", "holdingTypeName", "holdingId"]

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
    def from_json(cls, json_str: str) -> PortfolioHolding:
        """Create an instance of PortfolioHolding from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of each value in sub_holding_keys (dict)
        _field_dict = {}
        if self.sub_holding_keys:
            for _key in self.sub_holding_keys:
                if self.sub_holding_keys[_key]:
                    _field_dict[_key] = self.sub_holding_keys[_key].to_dict()
            _dict['subHoldingKeys'] = _field_dict
        # override the default output from pydantic by calling `to_dict()` of each value in properties (dict)
        _field_dict = {}
        if self.properties:
            for _key in self.properties:
                if self.properties[_key]:
                    _field_dict[_key] = self.properties[_key].to_dict()
            _dict['properties'] = _field_dict
        # override the default output from pydantic by calling `to_dict()` of cost
        if self.cost:
            _dict['cost'] = self.cost.to_dict()
        # override the default output from pydantic by calling `to_dict()` of cost_portfolio_ccy
        if self.cost_portfolio_ccy:
            _dict['costPortfolioCcy'] = self.cost_portfolio_ccy.to_dict()
        # override the default output from pydantic by calling `to_dict()` of transaction
        if self.transaction:
            _dict['transaction'] = self.transaction.to_dict()
        # set to None if instrument_scope (nullable) is None
        # and __fields_set__ contains the field
        if self.instrument_scope is None and "instrument_scope" in self.__fields_set__:
            _dict['instrumentScope'] = None

        # set to None if sub_holding_keys (nullable) is None
        # and __fields_set__ contains the field
        if self.sub_holding_keys is None and "sub_holding_keys" in self.__fields_set__:
            _dict['subHoldingKeys'] = None

        # set to None if properties (nullable) is None
        # and __fields_set__ contains the field
        if self.properties is None and "properties" in self.__fields_set__:
            _dict['properties'] = None

        # set to None if currency (nullable) is None
        # and __fields_set__ contains the field
        if self.currency is None and "currency" in self.__fields_set__:
            _dict['currency'] = None

        # set to None if holding_type_name (nullable) is None
        # and __fields_set__ contains the field
        if self.holding_type_name is None and "holding_type_name" in self.__fields_set__:
            _dict['holdingTypeName'] = None

        # set to None if holding_id (nullable) is None
        # and __fields_set__ contains the field
        if self.holding_id is None and "holding_id" in self.__fields_set__:
            _dict['holdingId'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> PortfolioHolding:
        """Create an instance of PortfolioHolding from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return PortfolioHolding.parse_obj(obj)

        _obj = PortfolioHolding.parse_obj({
            "instrument_scope": obj.get("instrumentScope"),
            "instrument_uid": obj.get("instrumentUid"),
            "sub_holding_keys": dict(
                (_k, PerpetualProperty.from_dict(_v))
                for _k, _v in obj.get("subHoldingKeys").items()
            )
            if obj.get("subHoldingKeys") is not None
            else None,
            "properties": dict(
                (_k, ModelProperty.from_dict(_v))
                for _k, _v in obj.get("properties").items()
            )
            if obj.get("properties") is not None
            else None,
            "holding_type": obj.get("holdingType"),
            "units": obj.get("units"),
            "settled_units": obj.get("settledUnits"),
            "cost": CurrencyAndAmount.from_dict(obj.get("cost")) if obj.get("cost") is not None else None,
            "cost_portfolio_ccy": CurrencyAndAmount.from_dict(obj.get("costPortfolioCcy")) if obj.get("costPortfolioCcy") is not None else None,
            "transaction": Transaction.from_dict(obj.get("transaction")) if obj.get("transaction") is not None else None,
            "currency": obj.get("currency"),
            "holding_type_name": obj.get("holdingTypeName"),
            "holding_id": obj.get("holdingId")
        })
        return _obj
