# r: Otwiera plik w trybie tylko do odczytu. Rozpoczyna czytanie od początku pliku i jest domyślnym trybem open()funkcji.
# rb: Otwiera plik tylko do odczytu w formacie binarnym i zaczyna czytać od początku pliku. Chociaż format binarny może być używany do różnych celów, zwykle jest używany w przypadku takich rzeczy, jak obrazy, filmy itp.
# r+: Otwiera plik do odczytu i zapisu, umieszczając wskaźnik na początku pliku.
# w: Otwiera się w trybie tylko do zapisu. Wskaźnik jest umieszczony na początku pliku i spowoduje to zastąpienie istniejącego pliku o tej samej nazwie. Utworzy nowy plik, jeśli nie istnieje plik o tej samej nazwie.
# wb: Otwiera plik tylko do zapisu w trybie binarnym.
# w+: Otwiera plik do zapisu i odczytu.
# wb+: Otwiera plik do zapisu i odczytu w trybie binarnym.
# a: Otwiera plik w celu dołączenia do niego nowych informacji. Wskaźnik jest umieszczony na końcu pliku. Nowy plik jest tworzony, jeśli nie istnieje plik o tej samej nazwie.
# ab: Otwiera plik do dołączenia w trybie binarnym.
# a+: Otwiera plik do dołączania i odczytu.
# ab+: Otwiera plik do dołączania i odczytu w trybie binarnym.

def odczytaj_dane():
    with open('log.txt', encoding='UTF') as file:
        tresc = file.read()
    print(tresc)


def zapisz_dane(zmienna):
    with open('log.txt', 'a', encoding='UTF')as file:
        file.write(zmienna)
