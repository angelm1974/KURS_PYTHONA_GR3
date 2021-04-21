import random

class Gracz():

    def __init__(self, imie, nazwisko):
        self.imie = imie
        self.nazwisko = nazwisko
        self.ilosc_zyc = 3
        self.koniec = False

    def utrata_zycia(self):
        self.ilosc_zyc -= 1
        if(self.ilosc_zyc <= 0):
            self.koniec = True
            print("Koniec GRY")
        else:
            print(f"Masz obecnie: {self.ilosc_zyc} żyć")

    def graj(self):
        wynik = random.randrange(1, 3)
        if (self.koniec == True):
            wynik = -1

        if(wynik == 1):
            self.utrata_zycia()
        elif(wynik == 2):
            self.ilosc_zyc += 1
            print(f'wynik: {wynik}, ilość żyć: {self.ilosc_zyc}')
        else:
            print(f'Zakończyłeś już grę!!!')


adam = Gracz("Adam", "Bułka")
for a in range(10):
    adam.graj()
