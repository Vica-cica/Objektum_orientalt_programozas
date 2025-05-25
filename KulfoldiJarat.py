from Jarat import Jarat

class KulfoldiJarat(Jarat):
    def __init__(self, jaratszam, celallomas, jegyar, orszag, utazasi_ido):
        super().__init__(jaratszam,celallomas,jegyar)
        self.orszag = orszag
        self.utazasi_ido = utazasi_ido

    def get_jarat_tipus(self):
        return "Nemzetkozi"

    def __str__(self):
        return f"Nemzetkozi {super().__str__()}, {self.orszag}, {self.utazasi_ido} ora"