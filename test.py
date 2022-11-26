import json
from datetime import date
from typing import Any

from colorama import Fore
from pydantic import BaseModel, ValidationError


class Address(BaseModel):
    number: int
    street: str
    city: str

class DateModel(BaseModel):
    id: int
    inputDate: date
    name : str = 'Hello'
    address: Address


def parse_data(entry: dict[str, Any]) -> bool:
    try:
        # Attempt to parse the data
        validatedData = DateModel(**entry)
    except ValidationError as e:
        # If there is a validation error, print it and return false
        print(f'{Fore.RED}{e}')
        return False
    else:
        # If the data validated OK, print it and the json representation and return True
        print(f'{Fore.BLUE}{validatedData}')
        print(f'{Fore.GREEN}{validatedData.json()}')
        return True
    finally:
        # Either way reset the output colour
        print(Fore.RESET)

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
    print(DateModel.schema_json(indent=2))
