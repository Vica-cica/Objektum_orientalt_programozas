from Jarat import Jarat

class LegiTarsasag:
    def __init__(self, nev):
        self.nev = nev
        self.jaratok = []

    def jarat_hozzaad(self, jarat: Jarat):
        self.jaratok.append(jarat)

    def get_jarat_by_number(self, jaratszam) -> Jarat:
        for jarat in self.jaratok:
            if jarat.jaratszam == jaratszam:
                return jarat
        return None


    def __str__(self):
        return f"Legitarsasag: {self.nev}, Jaratok: {self.jaratok}"