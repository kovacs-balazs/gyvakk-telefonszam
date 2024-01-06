class PhoneCountry:
    def __init__(self, code: str, name: str, phone: str, phoneLength: int | list[int]):
        self.code: str = code
        self.name: str = name
        self.phone: int = phone.replace("-", "")

        self.phoneLength: list[int] = (phoneLength if isinstance(phoneLength, list) else [phoneLength])


    # Ellenőrzi, hogy a telefonszám a megadott országé-e
    def is_number(self, phone_number: str) -> bool:
        if not phone_number.isdecimal():
            return False
        
        if not phone_number.startswith(self.phone):
            return False

        if not len(phone_number.replace(self.phone, "", 1)) in self.phoneLength:
            return False
        return True
    

    # Magyar-e az ország
    def is_hungary(self):
        return self.code == "HU"


phone_countries: dict[str, PhoneCountry] = {}
mobile_operators: dict[str, int] = {"Yettel": 20, "Telekom": 30, "Digi": 50, "Vodafone": 70}


class HungaryPhoneManager:
    def __init__(self, phone_number: str):
        self.hungary: PhoneCountry = phone_countries['HU']
        self.phone_number: str = phone_number
        self.original_phone_number: str = "+" + phone_number
        self.phone_country: PhoneCountry | None = get_phone_country(self.phone_number)
        self.phone_number_short: str = self.phone_number.replace(self.phone_country.phone, "", 1)


    def is_valid(self) -> bool:
        if self.phone_country is None or self.phone_country.code != "HU":
            return False
        
        if not self.phone_number.isdecimal():
            print(f"A + jel után szám kell legyen a(z) '{self.original_phone_number}' telefonszámnál.")
            return False
        
        if not self.phone_number.startswith("36") or not self.phone_country.is_hungary():
            print(f"Érvénytelen magyar telefonszám: {self.original_phone_number} ({self.phone_country.name if self.phone_country else 'Nem található'})")
            return False
        
        if len(self.phone_number) != 11:
            print(f"Érvénytelen hosszúságú telefonszám: {self.original_phone_number} ({len(self.original_phone_number)})")
            return False
        
        try:
            assert int(self.phone_number_short[0:2])
        except AssertionError:
            print(f"Hibás telefonszám: {self.original_phone_number}")
            return False
        return True


    def get_szolgaltato(self) -> str | None:
        if self.phone_country.code != "HU":
            return None
        
        operator: int = int(self.phone_number_short[0:2])
        if not operator in mobile_operators.values() and self.phone_country.is_hungary():
            return "Unknown"
        
        if not self.is_valid():
            return None
        
        return list(mobile_operators.keys())[[str(operator == v) for v in mobile_operators.values()].index("True")]


def get_phone_country(phone_number: str) -> PhoneCountry | None:
    for country in phone_countries.values():
        if country.is_number(phone_number):
            return country
    return None


def get_sorted_countries():
    return dict(sorted(phone_countries.items(), key=lambda item: len(str(item[1].phone)), reverse=True))