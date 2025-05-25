from Jarat import Jarat

class BelfoldiJarat(Jarat):
    def __init__(self, jaratszam, celallomas, jegyar, utazasi_ido):
        super().__init__(jaratszam, celallomas, jegyar)
        self.utazasi_ido = utazasi_ido

    def get_jarat_tipus(self):
        return "Belfoldi"

    def __str__(self):
        return f"Belfoldi {super().__str__()}, {self.utazasi_ido} ora"