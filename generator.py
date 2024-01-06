import random
from phone_country import phone_countries

hungary = 20
international = 20

class PhonenumberGenerator:
    def __init__(self):
        self.mobile_operators: dict[str, int] = {"Yettel": 20, "Telekom": 30, "Digi": 50, "Vodafone": 70}
        self.random_international_phone_numbers: dict[str, bool] = {}
        self.random_hungary_phone_numbers: dict[str, bool] = {}


    def generate_invalid_international(self):
        randomCountry = phone_countries[random.choice(list(phone_countries))]
        phone_number = f"+{max(int(randomCountry.phone), random.randrange(999))}{''.join([str(random.randrange(10)) for i in range(max(randomCountry.phoneLength) + 1)])}"
        self.random_international_phone_numbers[phone_number] = False


    def generate_valid_international(self):
        randomCountry = phone_countries[random.choice(list(phone_countries))]
        while randomCountry.code == "HU":
            randomCountry = phone_countries[random.choice(list(phone_countries))]

        phone_number = f"+{randomCountry.phone}{''.join([str(random.randrange(10)) for i in range(random.choice(randomCountry.phoneLength))])}"
        self.random_international_phone_numbers[phone_number] = True


    def generate_invalid_hungary(self):
        phone_number = f"+36{random.choice([10, 15, 35, 66, 88, 90, 47])}{''.join(str(random.randrange(10)) for i in range(7))}"
        self.random_hungary_phone_numbers[phone_number] = False


    def generate_valid_hungary(self):
        phone_number = f"+36{random.choice([20, 30, 50, 70])}{''.join(str(random.randrange(10)) for i in range(7))}"
        self.random_hungary_phone_numbers[phone_number] = True
    

    def write_to_file(self):
        print(f"Érvénytelen telefonszámok: {len([k for k, v in self.random_international_phone_numbers.items() if not v])}")
        print(f"Érvényes nem magyar telefonszámok: {len([k for k, v in self.random_international_phone_numbers.items() if v])}")

        print(f"Érvénytelen magyar telefonszámok: {len([k for k, v in self.random_hungary_phone_numbers.items() if not v])}")
        print(f"Érvényes magyar telefonszámok: {len([k for k, v in self.random_hungary_phone_numbers.items() if v])}")
        
        with open("autogenerated.txt", "w") as f:
            f.write('\n'.join(self.random_international_phone_numbers) + "\n")
            f.write('\n'.join(self.random_hungary_phone_numbers))