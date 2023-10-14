import json
from pydantic import BaseModel, Field, ConfigDict

class AliasModel(BaseModel):
    model_config: ConfigDict = ConfigDict(populate_by_name=True)
    human_readable_field_name: str = Field(..., alias=str('customfield_12345'))

print('Construct by Name')
print('-----------------')

model = AliasModel(human_readable_field_name='normal')

print(f'Model Dump by Name : {model.model_dump_json()}')
print(f'Model Dump by Alias: {model.model_dump_json(by_alias=True)}')
print(f'Access by Name     : {model.human_readable_field_name}')

print()
print('Populate by Alias')
print('-----------------')

data = {
    'customfield_12345': 'alias'
}

json_data = json.dumps(data)

model = AliasModel.model_validate_json(json_data)

print(f'Model Dump by Name : {model.model_dump_json()}')
print(f'Model Dump by Alias: {model.model_dump_json(by_alias=True)}')
print(f'Access by Name     : {model.human_readable_field_name}')

print()
print('Populate by Name')
print('----------------')

data = {
    'human_readable_field_name': 'normal',
}

json_data = json.dumps(data)

model = AliasModel.model_validate_json(json_data)

print(f'Model Dump by Name : {model.model_dump_json()}')
print(f'Model Dump by Alias: {model.model_dump_json(by_alias=True)}')
print(f'Access by Name     : {model.human_readable_field_name}')

print()
print('Modify by Name')
print('--------------')

model.human_readable_field_name = 'modified'

print(f'Model Dump by Name : {model.model_dump_json()}')
print(f'Model Dump by Alias: {model.model_dump_json(by_alias=True)}')
print(f'Access by Name     : {model.human_readable_field_name}')
