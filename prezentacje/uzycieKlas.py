from mojeklasy import Budynek, Willa, Osiedle   
       
domArka=Budynek("rodzinny")
domArka.temparatura=30
domArka.rokOddania=2019
domArka.iloscPieter=4
domArka.zmienTemperature(18)        

mojaWilla=Willa("willa")
mojaWilla.rokOddania=2020
mojaWilla.iloscPieter=10
mojaWilla.basen=False
# mojaWilla.zmienTemperature()
 
osiedleZabawne=Osiedle(mojaWilla)
osiedleZabawne.rozmiar=200
osiedleZabawne.rokOddania=2019
osiedleZabawne.lawka=33
osiedleZabawne.jakasWilla.zmienTemperature()

ilL=osiedleZabawne.podajIloscLawek()
print(f"Na naszym osiedlu jest {ilL} ławek")