import abc


class Czlowiek():
    imie = "Jan"


kowalski = Czlowiek()
print(kowalski.imie, 'Kowalski')


class Czlowiek_A():
    def __init__(self, imie, nazwisko, wiek):
        self.imie = imie
        self.nazwisko = nazwisko
        self.wiek = wiek
        self.drugieimie = ""


osoba = Czlowiek_A('Tomasz', 'Kowalski', 20)

print(osoba.wiek, osoba.nazwisko, osoba.imie, osoba.drugieimie)


class Czlowiek_B():
    def __init__(self, imie, nazwisko, wiek):
        self.imie = imie
        self.nazwisko = nazwisko
        self.wiek = wiek
        self.drugieimie = ""

    def moja_funkcja(self):
        print(f"Drugie imię: {self.drugieimie}")


osoba2 = Czlowiek_B("Adam", "Głowa", 33)
osoba2.drugieimie = "Oskar"
print(osoba2.imie)
osoba2.moja_funkcja()


class Czlowiek_P(abc.ABC):
    @abc.abstractmethod
    def podaj_imie(self, str_imie):
        pass

    @abc.abstractmethod
    def podaj_nazwisko(self, str_nazwisko):
        pass


class Kierownik(Czlowiek_P):
    def __init__(self):
        self.Imie = ""
        self.Nazwisko = ""

    def podaj_imie(self, str_imie):
        self.Imie = str_imie
        super(Kierownik, self).__init__()
        print(str_imie)

    def podaj_nazwisko(self, str_nazwisko):
        self.Nazwisko = str_nazwisko
        super(Kierownik, self).__init__()
        print(str_nazwisko)


k = Kierownik()
k.podaj_imie("Rafał")
k.podaj_nazwisko("Rasz")
k.Nazwisko = "Bułka"
print(k.Nazwisko)
