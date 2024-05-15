# Engeto-projekt-3
Projekt 3 - web scrap
Tento program umožňuje stažení výsledků voleb z roku 2017. 
Data jsou stahována z této webové stránky (https://volby.cz/pls/ps2017nss/ps3?xjazyk=CZ). Link na stránku není potřeba zadávat ručně, je již uveden v kódu. 
Program umožňuje vybrat jeden z okresů a do souboru *.csv jsou poté uloženy výsledky za každou obec v tom zvoleném okrese. 
Musíš scrolovat až dolů na konec kódu, kde na konci kódu je spuštění funkce, kde je potřeba zadat 2 argumenty: prvním argumentem je název okresu, jehož data chceme stáhnout, a název souboru, do kterého budou data uložena (je na každém, jak si soubor nazve). 
Je důležité, aby byly zadány oba argumenty. 
Zde je seznam okresů (je nutné zadat přesný název):
Praha, Benešov, Beroun, Kladno, Kolín, Kutná Hora, Mělník, Mladá Boleslav, Nymburk, Praha-východ, Praha-západ, Příbram, Rakovník, České Budějovice, Český Krumlov, Jindřichův Hradec, Písek, Prachatice, Strakonice, Tábor, Domažlice, Klatovy, Plzeň-město, Plzeň-jih, Plzeň-sever, Rokycany, Tachov, Cheb, Karlovy Vary, Sokolov, Děčín, Chomutov, Litoměřice, Louny, Most, Teplice, Ústí nad Labem, Česká Lípa, Jablonec nad Nisou, Liberec, Semily, Hradec Králové, Jičín, Náchod, Rychnov nad Kněžnou, Trutnov, Chrudim, Pardubice, Svitavy, Ústí nad Orlicí, Havlíčkův Brod, Jihlava, Pelhřimov, Třebíč, Žďár nad Sázavou, Blansko, Brno-město, Brno-venkov, Břeclav, Hodonín, Vyškov, Znojmo, Jeseník, Olomouc, Prostějov, Přerov, Šumperk, Kroměříž, Uherské Hradiště, Vsetín, Zlín, Bruntál, Frýdek-Místek, Karviná, Nový Jičín, Opava, Ostrava-město
Po zadání obou argumentů  stačí kliknout na spuštění kódu a během několika vteřin nebo desítek vteřin bude vytvořen soubor s daty. Některé okresy obsahují docela dost obcí a tudíž stahování dat může chvíli trvat. 
Příklad, jak spustit kód: zpracuj_vybrany_okres("Plzeň-město", "Výsledky_voleb_Plzeň-město") - program vytvoří soubor Výsledky_voleb_Plzeň-město.csv, kde budou uložena data (ukázka na přiloženém souboru Výsledky_voleb_Plzeň-město.csv).
Stejným způsobem lze stáhnout data z dalších okresů. 
