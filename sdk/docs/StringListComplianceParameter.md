# StringListComplianceParameter


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**ResourceId**](ResourceId.md) |  | 
**compliance_parameter_type** | **str** | The parameter type. The available values are: BoolComplianceParameter, StringComplianceParameter, DecimalComplianceParameter, DateTimeComplianceParameter, PropertyKeyComplianceParameter, AddressKeyComplianceParameter, PortfolioIdComplianceParameter, PortfolioGroupIdComplianceParameter, StringListComplianceParameter, BoolListComplianceParameter, DateTimeListComplianceParameter, DecimalListComplianceParameter, PropertyKeyListComplianceParameter, AddressKeyListComplianceParameter, PortfolioIdListComplianceParameter, PortfolioGroupIdListComplianceParameter, InstrumentListComplianceParameter, FilterPredicateComplianceParameter | 

## Example

```python
from lusid.models.string_list_compliance_parameter import StringListComplianceParameter

# TODO update the JSON string below
json = "{}"
# create an instance of StringListComplianceParameter from a JSON string
string_list_compliance_parameter_instance = StringListComplianceParameter.from_json(json)
# print the JSON string representation of the object
print StringListComplianceParameter.to_json()

# convert the object into a dict
string_list_compliance_parameter_dict = string_list_compliance_parameter_instance.to_dict()
# create an instance of StringListComplianceParameter from a dict
string_list_compliance_parameter_form_dict = string_list_compliance_parameter.from_dict(string_list_compliance_parameter_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


