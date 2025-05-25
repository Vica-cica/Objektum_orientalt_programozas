import datetime
from Jarat import Jarat

class JegyFoglalasiError(Exception):
    pass

class JegyFoglalas:
    def __init__(self, foglalasi_azonosito, jarat: Jarat, utas_neve, datum: datetime.date):
        self.foglalasi_azonosito = foglalasi_azonosito
        self.jarat = jarat
        self.utas_neve = utas_neve
        self.datum = datum

    def get_foglalasi_ar(self) -> float:
        return self.jarat.jegyar

    def __str__(self):
        return (f"Foglalas ID: {self.foglalasi_azonosito}, Jarat: {self.jarat.jaratszam}, "
                f"Utas: {self.utas_neve}, Datum: {self.datum.strftime('%Y-%m-%d')}, "
                f"Ar: {self.get_foglalasi_ar()} Euro")