import phone_country as phc
from phone_country import HungaryPhoneManager
from phone_country import PhoneCountry

mobile_operators_counter: dict[str, int] = {"Yettel": 0, "Telekom": 0, "Digi": 0, "Vodafone": 0, "Unknown": 0}

class Phonenumber:
    def __init__(self, phone_number: str):
        self.phone_number: str = phone_number
        self.original_phone_number = phone_number;
        if self.phone_number.startswith("06") and len(self.phone_number.replace("06", "", 1)) in phc.phone_countries['HU'].phoneLength:
            self.phone_number: str = self.phone_number.replace("06", "+36", 1)
        

        self.instant_invalid: bool = False
        if not self.phone_number.startswith("+"):
            print(f"A telefonszámnak + jellel kell kezdődnie.")
            self.instant_invalid = True
            return
        
        self.phone_number: str = self.phone_number.replace("+", "", 1)

        if not self.phone_number.strip().isdecimal():
            self.instant_invalid: bool = True

            if not self.phone_number.isdecimal():
                print(f"A + jel után szám kell legyen a(z) '{self.original_phone_number}' telefonszámnál.")
            else:
                print(f"Hibás telefonszám: {self.original_phone_number}")

        self.phone_country: PhoneCountry | None = phc.get_phone_country(self.phone_number)

    def record(self):
        if self.instant_invalid:
            return
        
        if self.is_hungary():
            hpm: HungaryPhoneManager = HungaryPhoneManager(self.phone_number)
            if not hpm.is_valid(): return
            szolgaltato: str = hpm.get_szolgaltato()
            if szolgaltato is None: return

            mobile_operators_counter[szolgaltato] += 1
            if szolgaltato == "Unknown":
                print(f"A(z) '{self.original_phone_number}' telefonszám szolgáltatója nem található.")
                return
                
            print(f"A(z) '{self.original_phone_number}' telefonszám szolgáltatója a {szolgaltato}.")
            return
        
        print(f"Érvénytelen magyar telefonszám: {self.original_phone_number} ({self.phone_country.name if self.is_international() else 'Nem található'})")

    def is_international(self) -> bool:
        return not self.phone_country is None and not self.is_hungary()

    def is_hungary(self) -> bool:
        return not self.phone_country is None and self.phone_country.is_hungary()