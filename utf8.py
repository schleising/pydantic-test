import json

from pydantic import BaseModel
from rich import print

class IntegerField(BaseModel):
    int_in: int

class StringModel(BaseModel):
    str_in: str
    integer: IntegerField

# Create a string with a nbsp in it
str_in = 'Non-breaking space: :-:🏈:'

print(f'Unencoded                 : {str_in}')
print(f'Encoded                   : {str_in.encode()}')
print(f'Encoded Utf8              : {str_in.encode("utf-8")}')
print(f'Encoded Unicode Escape    : {str_in.encode("unicode_escape")}')
print(f'Encoded Raw Unicode Escape: {str_in.encode("raw_unicode_escape")}')
print(f'Encoded Latin-1           : {str_in.encode("latin_1", errors="replace")}')
print(f'Encoded Ascii             : {str_in.encode("ascii", errors="replace")}')
print(f'Encoded Cp1252            : {str_in.encode("cp1252", errors="replace")}')

model = StringModel(str_in=str_in, integer=IntegerField(int_in=1))

model_dump = model.model_dump()
model_dump_json = model.model_dump_json()

print(model_dump)
print(model_dump_json)
print()
print(json.dumps(model_dump))
print(json.dumps(model_dump_json))
print()

# Create a dict similar to the pydantic model
dictIn = {
    'str_in': str_in,
    'integer': {
        'int_in': 1
    }
}

print(dictIn)
print(json.dumps(dictIn))
