import json
from phone_number import Phonenumber
from phone_number import mobile_operators_counter
from generator import PhonenumberGenerator
from phone_country import PhoneCountry
import phone_country as phc

import argparse

my_parser = argparse.ArgumentParser()
my_parser.add_argument("--nogui", action="store_true", help="konzol használata")
my_parser.add_argument("--autogenerate", action="store_true", help="Telefonszámok generálása")
my_parser.add_argument("--file", action="store", type=argparse.FileType('r'), help="File megadása")

# setup countires (exclude hungary)
with open("phone_number_countries.json") as f:
    countries_json = json.loads(f.read())
    for country in countries_json:
        phone_c: PhoneCountry = PhoneCountry(country["code"], country["label"], country["phone"], country['phoneLength'])
        phc.phone_countries[phone_c.code] = phone_c

phc.phone_countries: dict[str, PhoneCountry] = phc.get_sorted_countries()

args = my_parser.parse_args()
if args.autogenerate:
    phoneGen = PhonenumberGenerator()
    phoneGen.generate_invalid_international()
    phoneGen.generate_valid_international()
    phoneGen.generate_invalid_hungary()
    phoneGen.generate_valid_hungary()
    phoneGen.write_to_file()

if not args.file is None:
    for line in args.file:
        phonenumber: Phonenumber = Phonenumber(line.strip("\n"))
        phonenumber.record()

if args.nogui:
    while True:
        input_phone_number: str = input("Adj meg egy telefonszámot.\n")
        if input_phone_number.lower().strip() == "exit":
            exit()
        elif input_phone_number.lower().strip() == "list":
            print(mobile_operators_counter)
        else:
            phonenumber: str = Phonenumber(input_phone_number.strip("\n"))
            phonenumber.record()
else:
    import gui
    gui.open_gui()