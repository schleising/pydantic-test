import json
from typing import Any

from rich import print
from pydantic import ValidationError

from model import DateModel

def parse_data(entry: dict[str, Any]) -> bool:
    try:
        # Attempt to parse the data
        validatedData = DateModel(**entry)
    except ValidationError as e:
        # If there is a validation error, print it and return false
        print(f'[red]{e}[/]')
        return False
    else:
        # If the data validated OK, print it and the json representation and return True
        print(f'[blue]{validatedData}[/]')
        print(f'[green]{validatedData.model_dump_json()}[/]')
        return True

if __name__ == '__main__':
    print()

    # Simulate receiving data
    with open('inputs/test1.json', 'r', encoding='utf8') as inputFile:
        strIn = inputFile.read()

    dataIn: list[dict[str, str]] = json.loads(strIn)

    # Iterate through the data parsing it into a Pydantic class
    for item in dataIn:
        print(item)
        print(f'Data validation {"Passed" if parse_data(item) else "Failed"}')
        print('----------------------')
        print()

    # Output the schema
    print(json.dumps(DateModel.model_json_schema(), indent=2))
