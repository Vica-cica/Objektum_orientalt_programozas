class Jarat:
    def __init__(self, jaratszam, celallomas, jegyar):
        self.jaratszam = jaratszam
        self.celallomas = celallomas
        self.jegyar = jegyar

    def get_jarat_tipus(self):
        pass

    def __str__(self):
        return f"Jarat: {self.jaratszam}, Celallomas: {self.celallomas}, Jegyar: {self.jegyar}Euro"