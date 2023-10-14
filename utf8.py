import json
from pydantic import BaseModel, Field

class IntegerField(BaseModel):
    intIn: int

class StringModel(BaseModel):
    strIn: str
    integer: IntegerField

# Create a string with a nbsp in it
strIn = 'Non-breaking space: :-:🏈:'

print(f'Unencoded                 : {strIn}')
print(f'Encoded                   : {strIn.encode()}')
print(f'Encoded Utf8              : {strIn.encode("utf-8")}')
print(f'Encoded Unicode Escape    : {strIn.encode("unicode_escape")}')
print(f'Encoded Raw Unicode Escape: {strIn.encode("raw_unicode_escape")}')
print(f'Encoded Latin-1           : {strIn.encode("latin_1", errors="replace")}')
print(f'Encoded Ascii             : {strIn.encode("ascii", errors="replace")}')
print(f'Encoded Cp1252            : {strIn.encode("cp1252", errors="replace")}')

model = StringModel(strIn=strIn, integer=IntegerField(intIn=1))

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
    'strIn': strIn,
    'integer': {
        'intIn': 1
    }
}

print(dictIn)
print(json.dumps(dictIn))
print()