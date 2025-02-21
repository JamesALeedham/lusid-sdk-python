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


from typing import Any, Dict, List, Union
from pydantic import BaseModel, Field, StrictFloat, StrictInt, StrictStr, conlist, constr
from lusid.models.model_property import ModelProperty

class ComplianceRuleBreakdown(BaseModel):
    """
    ComplianceRuleBreakdown
    """
    group_status: constr(strict=True, min_length=1) = Field(..., alias="groupStatus", description="The status of this subset of results.")
    results_used: Dict[str, Union[StrictFloat, StrictInt]] = Field(..., alias="resultsUsed", description="Dictionary of AddressKey (as string) and their corresponding decimal values, that were used in this rule.")
    properties_used: Dict[str, conlist(ModelProperty)] = Field(..., alias="propertiesUsed", description="Dictionary of PropertyKey (as string) and their corresponding Properties, that were used in this rule")
    missing_data_information: conlist(StrictStr) = Field(..., alias="missingDataInformation", description="List of string information detailing data that was missing from contributions processed in this rule")
    __properties = ["groupStatus", "resultsUsed", "propertiesUsed", "missingDataInformation"]

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
    def from_json(cls, json_str: str) -> ComplianceRuleBreakdown:
        """Create an instance of ComplianceRuleBreakdown from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of each value in properties_used (dict of array)
        _field_dict_of_array = {}
        if self.properties_used:
            for _key in self.properties_used:
                if self.properties_used[_key]:
                    _field_dict_of_array[_key] = [
                        _item.to_dict() for _item in self.properties_used[_key]
                    ]
            _dict['propertiesUsed'] = _field_dict_of_array
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> ComplianceRuleBreakdown:
        """Create an instance of ComplianceRuleBreakdown from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return ComplianceRuleBreakdown.parse_obj(obj)

        _obj = ComplianceRuleBreakdown.parse_obj({
            "group_status": obj.get("groupStatus"),
            "results_used": obj.get("resultsUsed"),
            "properties_used": dict(
                (_k,
                        [ModelProperty.from_dict(_item) for _item in _v]
                        if _v is not None
                        else None
                )
                for _k, _v in obj.get("propertiesUsed").items()
            ),
            "missing_data_information": obj.get("missingDataInformation")
        })
        return _obj
