# 3. projekt - kurz Python - Engeto - Web scrap
# Autor - Jakub Lánský
# Emil - kubik.langos@seznam.cz
# Discord - Kuba L. 11

from requests import get
from bs4 import BeautifulSoup as bs
import csv
import sys

# Hlavní odkaz, ze kterého budou stahovány další odkazy, které poskytnou potřebné údaje. 
url_hlavni = "https://volby.cz/pls/ps2017nss/ps3?xjazyk=CZ"
seznam_obci = get(url_hlavni)
soup1 = bs(seznam_obci.text)
url_zahranici = "https://volby.cz/pls/ps2017nss/ps36?xjazyk=CZ"

# Nejprve je potřeba získat názvy jednotlivých okresů a jejich kódy. Ty lze nalézt dle označení "td". Ne všechny "td" využijeme, proto je potřeba vybrat jen názvy a kódy (použít striding). 
seznam_okresu = soup1.find_all("td")
okresy_vsechny = []
for na_radek in seznam_okresu:
    okresy_vsechny.append(na_radek.text)
okresy_nazvy = okresy_vsechny[1::4]
okresy_kody = okresy_vsechny[0::4]

# Vymazat z okresů zahraničí.
index_zahranici = okresy_nazvy.index("Zahraničí")
l = okresy_nazvy.pop(index_zahranici)
k = okresy_kody.pop(index_zahranici)

# Stáhnout odkazy z hlavní stránky, upravit do požadovaného stavu a vybrat jen ty odkazy na jednotlivé okresy (= odkazy obsahující "ps32").
odkazy_vsechny = []
for odkaz in soup1.find_all("a", href=True):
    if len(odkaz["href"]) > 34:
        odkazy_vsechny.append(odkaz["href"])
odkazy_na_okresy = []
for odkaz in odkazy_vsechny:
    cely_odkaz = "https://volby.cz/pls/ps2017nss/" + odkaz
    odkazy_na_okresy.append(cely_odkaz)
odkazy_vybrane = []
for odkaz in odkazy_na_okresy:
    if "ps32" in odkaz:
        odkazy_vybrane.append(odkaz)

# Definovat funkci na stažení dat z vybraného okresu.
def zpracuj_vybrany_okres(nazev_okresu, nazev_souboru):
    """
    Tato funkce vytáhne údaje z vybraného okresu a z každého okresu vypíše jednotlivé obce, které jsou v daném okresu, a výsledky voleb ze všech obcí. Následně tyto údaje uloží do souboru csv. 
    Prvním argumentem je přesný název okresu a druhým argumentem je název souboru, do kterého se data uloží (s příponou csv, tu není nutné do názvu zapisovat).
    Funkce nejprve načte vybraný okres, stáhne ze stránky okresu odkazy na jednotlivé obce. Dále stáhne názvy jednotlivých obcí, jejich kódy, názvy politických stran, které byly v okrese voleny. 
    Poté bude vytvořen soubor s příponou .csv, do kterého budou postupně ukládána data. 
    Nejprve budou uloženy názvy obcí, jejich kódů, politických stran a poté počty voličů v jednotlivých obcích, počet platných hlasů a počet hlasů, které dostaly jednotlivé politické strany v každé obci. 
    Například, pokud budeme chtít stáhnout výsledky voleb z okresu Plzeň-město, bude příkaz vypadat takto:
    >>> zpracuj_vybrany_okres("Plzeň-město", "výsledky_voleb_Plzeň-město")
    Program stáhne data a uloží je do souboru podle zadaného názvu. 
    Pokud nebudou zadány oba argumenty nebo pokud nebude zadán správný název okresu, tak program napíše chybu "Špatné zadání" a ukončí se. 
    """
    try:
        index = okresy_nazvy.index(nazev_okresu)
        url = odkazy_vybrane[index]
        jednotlivy_okres = get(url)
        soup_okres = bs(jednotlivy_okres.text, "html.parser")
    except:
        print("Špatné zadání")
        sys.exit()

# Stáhnout odkazy na jednotlivé obce ze stránky vybraného okresu (jsou zde i další odkazy, které nechceme, odkazy na jednotlivé obce obsahují v názvu "ps311", podle kterého tyto odkazy najdeme).
    odkazy_vsechny_2 = []
    for odkaz in soup_okres.find_all("a", href=True):
        if odkaz["href"] not in odkazy_vsechny_2:
            if "ps311" in odkaz["href"]:
               odkazy_vsechny_2.append(odkaz["href"])
            else:
                continue
    odkazy_na_obce = []
    for odkaz in odkazy_vsechny_2:
        cely_odkaz = "https://volby.cz/pls/ps2017nss/" + odkaz
        odkazy_na_obce.append(cely_odkaz)

# Z vybraného okresu stáhnout názvy obcí a jejich kódy. Z jedné obce stáhnout názvy stran, které jsou pro každou obec v okresu stejné. Vytvořit soubor csv a uložit do něj názvy sloupců. 
    nazvy_obci_okres = soup_okres.find_all("td")
    vsechna_td = []
    for na_radek in nazvy_obci_okres:
        vsechna_td.append(na_radek.text)
    list_nazvy_obci = vsechna_td[1::3]
    for na_radek in nazvy_obci_okres:
        list_nazvy_obci.append(na_radek.text)
    kod_obec = soup_okres.find_all("td", {"class": "cislo"})
    list_kody = []
    for na_radek in kod_obec:
        list_kody.append(na_radek.text)
    odkazy = odkazy_na_obce
    nazev = nazev_souboru + ".csv"
    soubor = open(nazev, mode="w", newline="")
    zapisovac = csv.writer(soubor, delimiter = ";") 
    seznam_stran = get(odkazy_na_obce[0])
    soup_seznam = bs(seznam_stran.text, "html.parser")
    nazvy_sloupcu = ["Kód obce", "Název obce", "Registrovaní voliči", "Odevzdané obálky", "Platné hlasy"]
    nazvy_stran = soup_seznam.find_all("td", {"class": "overflow_name"})
    for na_radek in nazvy_stran:
        nazvy_sloupcu.append(na_radek.text)
    zapisovac.writerow(nazvy_sloupcu)   

# Nejprve stáhnout všechna "h3" ze stránky a vybrat jen ta "h3", která obsahují název obce a osekat, abychom dostali jen ten název (použit slicing). Potom z částí "table" a "td" stáhnout potřebná data a zapsat do souboru.
    for odkaz in odkazy:
        url_obce = odkaz
        volby_obce = get(url_obce)
        soup_obce = bs(volby_obce.text, "html.parser")
        obec = []
        for na_radek in soup_obce.find_all("h3"):
            obec.append(na_radek.text)
        jen_nazev_obce = obec[-3]
        index_aktualni_obce = list_nazvy_obci.index(jen_nazev_obce[7:-1])
        kod_aktualni_obce = list_kody[index_aktualni_obce]
        souhrn_obec = soup_obce.find("table", {"class": "table"})
        vysledky_obec = []
        vysledky_obec.append(kod_aktualni_obce)
        vysledky_obec.append(jen_nazev_obce[7:-1])                                # osekat, aby zbyl jen název obce
        vysledky_obec.append(souhrn_obec.contents[5].contents[7].contents[0])     # Registrovaní voliči
        vysledky_obec.append(souhrn_obec.contents[5].contents[13].contents[0])    # Odevzdané obálky
        vysledky_obec.append(souhrn_obec.contents[5].contents[15].contents[0])    # Platné hlasy
        volici_stran_1 = soup_obce.find_all("td", {"headers": "t1sa2 t1sb3"})
        for na_radek in volici_stran_1:
            vysledky_obec.append(na_radek.text)
        volici_stran_2 = soup_obce.find_all("td", {"headers": "t2sa2 t2sb3"})
        for na_radek in volici_stran_2:  
            vysledky_obec.append(na_radek.text)
        zapisovac.writerow(vysledky_obec)
    soubor.close()

# Vyber okres a zapni funkci, výsledky se uloží do souboru dle zadaného názvu. Je potřeba zapsat nejprve název okresu a poté požadovaný název souboru. 

vyber_okres = input("Prosím, vyber název okresu, jehož data ohledně voleb chceš stáhnout ")
vyber_nazev = input("Teď vyber, jak se bude jmenovat soubor, do kterého budou data uložena ")
print("Chviličku strpení. Ukládám data....")
zpracuj_vybrany_okres(vyber_okres, vyber_nazev)