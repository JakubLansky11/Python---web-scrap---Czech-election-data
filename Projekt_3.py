# 3. projekt - kurz Python - Engeto - Web scrap
# Autor - Jakub Lánský
# Emil - kubik.langos@seznam.cz
# Discord - Kuba L. 11

from requests import get
from bs4 import BeautifulSoup as bs
import csv
import sys
# Hlavní odkaz, ze kterého budou stahovány další odkazy, které poskytnou potřebné údaje. Pozdrav od programu. 
url_hlavni = "https://volby.cz/pls/ps2017nss/ps3?xjazyk=CZ"
seznam_obci = get(url_hlavni)
soup1 = bs(seznam_obci.text, "html.parser")

print("Ahoj. Vítej v tomto programu, který ti stáhne data ohledně voleb z roku 2017.")
print("Prvotním zdrojem je tato stránka: ", url_hlavni)
print("Program stáhne data z některého z okresů, který byl vybrán")
print("(seznam okresů a jejich přesné názvy viz soubor readme)")
print("Chviličku strpení. Stahuji data....")

# Nejprve je potřeba získat názvy jednotlivých okresů a jejich kódy. Ty lze nalézt dle označení "td". Ne všechny "td" využijeme, proto je potřeba vybrat jen názvy a kódy (použít striding). Z okresů vymazat zahraničí.
def ziskat_okresy(soup, nazvy):
    seznam_okresu = soup.find_all("td")
    vsechen_text = []
    for na_radek in seznam_okresu:
        vsechen_text.append(na_radek.text)
    nazvy_vsechny = vsechen_text[1::4]
    kody_vsechny = vsechen_text[0::4]

    index_zahranici = nazvy_vsechny.index("Zahraničí")
    l = nazvy_vsechny.pop(index_zahranici)
    k = kody_vsechny.pop(index_zahranici)
    for nazev in nazvy_vsechny:
        nazvy.append(nazev)
    return None

# Stáhnout odkazy z hlavní stránky, upravit do požadovaného stavu a vybrat jen ty odkazy na jednotlivé okresy (= odkazy obsahující "ps32").
def stahni_odkazy_okresy(soup, odkazy):
    odkazy_vsechny = []
    for odkaz in soup.find_all("a", href=True):
        if len(odkaz["href"]) > 34:
            odkazy_vsechny.append(odkaz["href"])
    for odkaz in odkazy_vsechny:
        if "ps32" in odkaz:
            cely_odkaz = "https://volby.cz/pls/ps2017nss/" + odkaz
            odkazy.append(cely_odkaz)
    return None

# Stáhnout odkazy na jednotlivé obce ze stránky vybraného okresu (jsou zde i další odkazy, které nechceme, odkazy na jednotlivé obce obsahují v názvu "ps311", podle kterého tyto odkazy najdeme).
def stahni_odkazy_obce(soup, odkazy):
    odkazy_vsechny = []
    for odkaz in soup.find_all("a", href=True):
        if odkaz["href"] not in odkazy_vsechny:
            if "ps311" in odkaz["href"]:
               odkazy_vsechny.append(odkaz["href"])
            else:
                continue
    for odkaz in odkazy_vsechny:
        cely_odkaz = "https://volby.cz/pls/ps2017nss/" + odkaz
        odkazy.append(cely_odkaz)

# Tato funkce stáhne potřebná data. Z vybraného okresu stáhnout názvy obcí a jejich kódy. Z jedné obce stáhnout názvy stran, které jsou pro každou obec v okresu stejné. Uložit názvy sloupců do souboru.
def stahni_data(soup, url, nazev_souboru):
    nazev = nazev_souboru + ".csv"
    soubor = open(nazev, mode="w", newline="")
    zapisovac = csv.writer(soubor, delimiter = ";") 
    nazvy_obci_okres = soup.find_all("td")
    vsechna_td = []
    for na_radek in nazvy_obci_okres:
        vsechna_td.append(na_radek.text)
    list_nazvy_obci = vsechna_td[1::3]
    for na_radek in nazvy_obci_okres:
        list_nazvy_obci.append(na_radek.text)
    kod_obec = soup.find_all("td", {"class": "cislo"})
    list_kody = []
    for na_radek in kod_obec:
        list_kody.append(na_radek.text)
    seznam_stran = get(url[0])
    soup_seznam = bs(seznam_stran.text, "html.parser")
    nazvy_sloupcu = ["Kód obce", "Název obce", "Registrovaní voliči", "Odevzdané obálky", "Platné hlasy"]
    nazvy_stran = soup_seznam.find_all("td", {"class": "overflow_name"})
    for na_radek in nazvy_stran:
        nazvy_sloupcu.append(na_radek.text)
    zapisovac.writerow(nazvy_sloupcu) 
# Stáhnout všechna "h3" ze stránky a vybrat jen ta "h3", která obsahují název obce a osekat, abychom dostali jen ten název (použit slicing). Potom z částí "table" a "td" stáhnout potřebná data a zapsat do souboru.
    for odkaz in url:
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
        data_2 = []
        data_2.append(kod_aktualni_obce)
        data_2.append(jen_nazev_obce[7:-1])                                # osekat, aby zbyl jen název obce
        data_2.append(souhrn_obec.contents[5].contents[7].contents[0])     # Registrovaní voliči
        data_2.append(souhrn_obec.contents[5].contents[13].contents[0])    # Odevzdané obálky
        data_2.append(souhrn_obec.contents[5].contents[15].contents[0])    # Platné hlasy
        volici_stran_1 = soup_obce.find_all("td", {"headers": "t1sa2 t1sb3"})
        for na_radek in volici_stran_1:
            data_2.append(na_radek.text)
        volici_stran_2 = soup_obce.find_all("td", {"headers": "t2sa2 t2sb3"})
        for na_radek in volici_stran_2:  
            data_2.append(na_radek.text)
        zapisovac.writerow(data_2)
    soubor.close()

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
        nazvy_okresu = []
        odkazy_okresy = []
        ziskat_okresy(soup1, nazvy_okresu)
        stahni_odkazy_okresy(soup1, odkazy_okresy)

        index = nazvy_okresu.index(nazev_okresu)
        url = odkazy_okresy[index]
        jednotlivy_okres = get(url)
        soup_okres = bs(jednotlivy_okres.text, "html.parser")
        odkazy_obce = []
        stahni_odkazy_obce(soup_okres, odkazy_obce)
        stahni_data(soup_okres, odkazy_obce, nazev_souboru)
    except:
        print("Špatné zadání! Zadal jsi správný název okresu?")
        sys.exit(1)
if len(sys.argv) != 3:
    print("Nebyl zadán správný počet argumentů! Je nutné zadat 2 argumenty: název okresu, požadovaný název souboru")
    sys.exit(1)
else:	
    vyber_okres = sys.argv[1]
    vyber_nazev = sys.argv[2]
    zpracuj_vybrany_okres(vyber_okres, vyber_nazev)
