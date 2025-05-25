import os
import time
import datetime
from BelfoldiJarat import BelfoldiJarat
from JegyFoglalas import JegyFoglalasiError
from JegyFoglalas import JegyFoglalas
from KulfoldiJarat import KulfoldiJarat
from LegiTarsasag import LegiTarsasag


def feltoltes():
    legi_tarsasag = LegiTarsasag("Gyakorlat Airways")

    jarat1 = BelfoldiJarat("BA101", "Debrecen", 50, 1)
    jarat2 = KulfoldiJarat("NA202", "London", 450, "Egyesult Kiralysag", 3)
    jarat3 = BelfoldiJarat("BA103", "Szeged", 40, 0.5)

    legi_tarsasag.jarat_hozzaad(jarat1)
    legi_tarsasag.jarat_hozzaad(jarat2)
    legi_tarsasag.jarat_hozzaad(jarat3)

    foglalasok = []
    current_date = datetime.date.today()

    foglalasok.append(JegyFoglalas("FOGL001", jarat1, "Kiss Anna", current_date))
    foglalasok.append(JegyFoglalas("FOGL002", jarat2, "Nagy Bence", current_date))
    foglalasok.append(JegyFoglalas("FOGL003", jarat3, "Kovacs Dora", current_date))
    foglalasok.append(JegyFoglalas("FOGL004", jarat1, "Toth Gabor", current_date + datetime.timedelta(days=7)))
    foglalasok.append(JegyFoglalas("FOGL005", jarat2, "Varga Eva", current_date + datetime.timedelta(days=14)))
    foglalasok.append(JegyFoglalas("FOGL006", jarat3, "Papp Marton", current_date + datetime.timedelta(days=3)))

    return legi_tarsasag, foglalasok

def jegy_foglalasa(legi_tarsasag: LegiTarsasag, foglalasok: list):
    print("\n--- Jegy foglalasa ---")
    print("Elérhető jaratok:")
    for jarat in legi_tarsasag.jaratok:
        print(f"  - {jarat}")

    jaratszam = input("Adja meg a jaratszamot, amelyre foglalni szeretne: ").upper()
    jarat = legi_tarsasag.get_jarat_by_number(jaratszam)

    if not jarat:
        print("Hiba: Nincs ilyen jaratszam.")
        return

    utas_neve = input("Adja meg az utas nevet: ")
    while not utas_neve:
        print("Hiba: Az utas neve nem lehet ures.")
        utas_neve = input("Adja meg az utas nevet: ")

    datum_str = input("Adja meg a foglalas datumat (EEEE-HH-NN formatumban): ")
    try:
        datum = datetime.datetime.strptime(datum_str, "%Y-%m-%d").date()
        if datum < datetime.date.today():
            raise JegyFoglalasiError("A foglalas datuma nem lehet a multban.")
    except ValueError:
        print("Hiba: Ervenytelen datumformatum.")
        return
    except JegyFoglalasiError as e:
        print(f"Hiba: {e}")
        return

    foglalasi_azonosito = f"FOGL{len(foglalasok) + 1:03d}"
    uj_foglalas = JegyFoglalas(foglalasi_azonosito, jarat, utas_neve, datum)
    foglalasok.append(uj_foglalas)
    print(f"\nSikeres foglalas! Az On foglalasi azonositoja: {foglalasi_azonosito}")
    print(f"Foglalas ara: {uj_foglalas.get_foglalasi_ar()} Euro")


def foglalas_lemondasa(foglalasok: list):
    print("\n--- Foglalas lemondasa ---")
    if not foglalasok:
        print("Nincsenek aktualis foglalasok.")
        return

    foglalasi_azonosito = input("Adja meg a lemondani kivant foglalas azonositojat: ").upper()

    found_index = -1
    for i, foglalas in enumerate(foglalasok):
        if foglalas.foglalasi_azonosito == foglalasi_azonosito:
            found_index = i
            break

    if found_index != -1:
        lemondott_foglalas = foglalasok.pop(found_index)
        print(f"A(z) {lemondott_foglalas.foglalasi_azonosito} azonositoju foglalas sikeresen lemondva.")
    else:
        print("Hiba: Nincs ilyen foglalasi azonosito.")

def foglalasok_listazasa(foglalasok: list):
    print("\n--- Aktualis foglalasok ---")
    if not foglalasok:
        print("Nincsenek aktualis foglalasok.")
        return
    for foglalas in foglalasok:
        print(f"- {foglalas}")

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def main():
    legi_tarsasag, foglalasok = feltoltes()

    while True:
        clear_screen()
        print("\n--- Repulojegy Foglalasi Rendszer ---")
        print("1. Jegy foglalasa")
        print("2. Foglalas lemondasa")
        print("3. Foglalasok listazasa")
        print("4. Kilepes")

        valasztas = input("Kerem irja be a valasztott opcio szamat: ")

        if valasztas == '1':
            clear_screen()
            (jegy_foglalasa(legi_tarsasag, foglalasok))
            time.sleep(3)
            input("Nyomjon Entert a visszatereshez a menube.")
        elif valasztas == '2':
            clear_screen()
            foglalas_lemondasa(foglalasok)
            time.sleep(3)
            input("Nyomjon Entert a visszatereshez a menube.")
        elif valasztas == '3':
            clear_screen()
            foglalasok_listazasa(foglalasok)
            time.sleep(3)
            input("Nyomjon Entert a visszatereshez a menube.")
        elif valasztas == '4':
            clear_screen()
            print("Viszlat!")
            time.sleep(1)
            break
        else:
            clear_screen()
            print("Ervenytelen valasztas. Kerem, probalja ujra.")
            time.sleep(2)


if __name__ == "__main__":
    main()