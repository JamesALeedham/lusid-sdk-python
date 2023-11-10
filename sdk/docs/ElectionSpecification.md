# ElectionSpecification


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**election_type** | **str** |  | 
**cardinality** | **List[str]** |  | 
**referenced_as** | **List[str]** |  | 

## Example

```python
from lusid.models.election_specification import ElectionSpecification

# TODO update the JSON string below
json = "{}"
# create an instance of ElectionSpecification from a JSON string
election_specification_instance = ElectionSpecification.from_json(json)
# print the JSON string representation of the object
print ElectionSpecification.to_json()

# convert the object into a dict
election_specification_dict = election_specification_instance.to_dict()
# create an instance of ElectionSpecification from a dict
election_specification_form_dict = election_specification.from_dict(election_specification_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


