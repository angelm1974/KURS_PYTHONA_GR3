import abc


class Ptak(abc.ABC):
    @abc.abstractmethod
    def lata(self):
        pass


class Papuga(Ptak):
    def __init__(self):
        self.kolor = ""

    def lata(self):
        super(Papuga, self).__init__()
        print(f'Lata do 30m i ma kolor {self.kolor}')


class Czlowiek():
    def __init__(self, imie, nazwisko, wiek):
        self.imie = imie
        self.nazwisko = nazwisko
        self.wiek = wiek
        self.drugieimie = ""


class CzlowiekPapuga(Czlowiek, Papuga ):
    def __init__(self, imie, nazwisko, wiek):
       super(CzlowiekPapuga, self).__init__(imie, nazwisko, wiek)


JanPapuga = CzlowiekPapuga("jan", "Papuga", 23)
JanPapuga.kolor= "czerwony"
JanPapuga.lata()
