Python project - web scrap

Tento program umožňuje stažení výsledků voleb z roku 2017. Projekt byl vytvořen v rámci kurzu Engeto. 

Data jsou stahována z této webové stránky (https://volby.cz/pls/ps2017nss/ps3?xjazyk=CZ). Link na stránku není potřeba zadávat ručně, je již uveden v kódu. 
Program umožňuje vybrat jeden z okresů a do souboru *.csv jsou poté uloženy výsledky za každou obec v tom zvoleném okrese. 

Program lze otevřít například pomocí příkazového řádku. Tam je potřeba zadat název souboru a uvést 2 argumenty hlavní funkce (1. argument - přesný název okresu, 2. argument - název, pod kterým chceš, aby byl soubor uložen), příklad: Projekt_3.py Praha Praha_data
Je důležité, aby byl zadán přesný název okresu. 

Zde je seznam okresů:
Praha, Benešov, Beroun, Kladno, Kolín, Kutná Hora, Mělník, Mladá Boleslav, Nymburk, Praha-východ, Praha-západ, Příbram, Rakovník, České Budějovice, Český Krumlov, Jindřichův Hradec, Písek, Prachatice, Strakonice, Tábor, Domažlice, Klatovy, Plzeň-město, Plzeň-jih, Plzeň-sever, Rokycany, Tachov, Cheb, Karlovy Vary, Sokolov, Děčín, Chomutov, Litoměřice, Louny, Most, Teplice, Ústí nad Labem, Česká Lípa, Jablonec nad Nisou, Liberec, Semily, Hradec Králové, Jičín, Náchod, Rychnov nad Kněžnou, Trutnov, Chrudim, Pardubice, Svitavy, Ústí nad Orlicí, Havlíčkův Brod, Jihlava, Pelhřimov, Třebíč, Žďár nad Sázavou, Blansko, Brno-město, Brno-venkov, Břeclav, Hodonín, Vyškov, Znojmo, Jeseník, Olomouc, Prostějov, Přerov, Šumperk, Kroměříž, Uherské Hradiště, Vsetín, Zlín, Bruntál, Frýdek-Místek, Karviná, Nový Jičín, Opava, Ostrava-město
