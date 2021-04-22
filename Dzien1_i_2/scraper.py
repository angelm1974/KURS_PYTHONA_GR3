from urllib.request import urlopen
import pliki
link = "https://www.onet.pl"
f = urlopen(link)
plik=f.read()
plik=str(plik)
pliki.zapisz_dane(plik)
