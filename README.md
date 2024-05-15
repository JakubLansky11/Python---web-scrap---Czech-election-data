# Engeto-projekt-3
Projekt 3 - web scrap
Tento program umožňuje stažení výsledků voleb z roku 2017. 
Data jsou stahována z této webové stránky (https://volby.cz/pls/ps2017nss/ps3?xjazyk=CZ). Link na stránku není potřeba zadávat ručně, je již uveden v kódu. 
Program umožňuje vybrat jeden z okresů a do souboru *.csv jsou poté uloženy výsledky za každou obec v tom zvoleném okrese. 
Na konci kódu je spuštění funkce, kde je potřeba zadat 2 argumenty: prvním argumentem je název okresu, jehož data chceme stáhnout, a název souboru, do kterého budou data uložena (je na každém, jak si soubor nazve). 
Je důležité, aby byly zadány oba argumenty. 
Zde je seznam okresů (je nutné zadat přesný název):
Praha, Benešov, Beroun, Kladno, Kolín, Kutná Hora, Mělník, Mladá Boleslav, Nymburk, Praha-východ, Praha-západ, Příbram, Rakovník, České Budějovice, Český Krumlov, Jindřichův Hradec, Písek, Prachatice, Strakonice, Tábor, Domažlice, Klatovy, Plzeň-město, Plzeň-jih, Plzeň-sever, Rokycany, 'Tachov', 'Cheb', 'Karlovy Vary', 'Sokolov', 'Děčín', 'Chomutov', 'Litoměřice', 'Louny', Most, Teplice, Ústí nad Labem, Česká Lípa, Jablonec nad Nisou, Liberec, Semily, Hradec Králové, Jičín, Náchod, Rychnov nad Kněžnou, Trutnov, Chrudim, Pardubice, Svitavy, Ústí nad Orlicí, Havlíčkův Brod, Jihlava, Pelhřimov, Třebíč, Žďár nad Sázavou, Blansko, Brno-město, Brno-venkov, Břeclav, Hodonín, Vyškov, Znojmo, Jeseník, Olomouc, Prostějov, Přerov, Šumperk, Kroměříž, Uherské Hradiště, Vsetín, Zlín, Bruntál, Frýdek-Místek, Karviná, Nový Jičín, Opava, Ostrava-město
Po zadání obou argumentů  stačí kliknout na spuštění kódu (např. v Jupiter notebooku) a během několika vteřin nebo desítek vteřin bude vytvořen soubor s daty. Některé okresy obsahují desítky obcí a tudíž stahování dat může chvíli trvat. 
příklad: zpracuj_vybrany_okres("Plzeň-město", "Výsledky_voleb_Plzeň-město") - program vytvoří soubor Výsledky_voleb_Plzeň.město.csv, kde budou uložena tato data:
Kód obce	Název obce	Registrovaní voliči	Vydané obálky	Platné hlasy	Občanská demokratická strana	Řád národa - Vlastenecká unie	CESTA ODPOVĚDNÉ SPOLEČNOSTI	Česká str.sociálně demokrat.	Radostné Česko	STAROSTOVÉ A NEZÁVISLÍ	Komunistická str.Čech a Moravy	Strana zelených	ROZUMNÍ-stop migraci,diktát.EU	Strana svobodných občanů	Blok proti islam.-Obran.domova	Občanská demokratická aliance	Česká pirátská strana	OBČANÉ 2011-SPRAVEDL. PRO LIDI	Referendum o Evropské unii	TOP 09	ANO 2011	SPR-Republ.str.Čsl. M.Sládka	Křesť.demokr.unie-Čs.str.lid.	Česká strana národně sociální	REALISTÉ	SPORTOVCI	Dělnic.str.sociální spravedl.	Svob.a př.dem.-T.Okamura (SPD)	Strana Práv Občanů	
558851	Dýšina	1 349	858	853	114	0	0	48	0	52	41	10	5	16	1	2	119	0	3	45	269	5	34	0	3	2	1	80	3	-
558966	Chrást	1 429	1 002	999	151	1	1	51	1	31	63	8	4	15	1	2	111	1	1	45	354	1	24	0	11	5	2	114	1	-
557846	Chválenice	561	369	369	50	3	0	21	0	13	21	7	7	7	1	1	52	0	0	38	104	0	8	0	3	2	0	29	2	-
559130	Kyšice	734	508	506	87	1	0	39	0	23	32	5	3	12	0	0	52	2	0	22	153	0	24	0	8	2	1	38	2	-
540561	Letkov	510	410	409	74	0	0	21	0	16	19	6	2	6	2	6	41	0	0	34	126	0	15	0	3	0	0	37	1	-
578606	Lhůta	144	114	114	16	0	0	9	0	8	13	4	1	2	0	2	6	0	0	4	31	0	1	0	3	0	0	13	1	-
558001	Losiná	1 051	665	659	115	0	0	32	2	26	48	8	4	15	1	1	70	0	0	28	218	2	15	0	8	1	0	63	2	-
540641	Mokrouše	191	139	138	19	1	0	14	0	7	12	2	1	1	0	0	15	0	0	7	36	0	5	0	2	2	1	13	0	-
553590	Nezbavětice	181	135	135	17	0	0	11	0	2	13	0	1	2	0	0	10	0	0	1	48	0	2	0	5	1	2	20	0	-
558141	Nezvěstice	1 156	770	767	72	0	0	85	1	33	56	10	3	7	2	4	77	0	0	41	270	3	28	0	5	1	0	68	1	-
554791	Plzeň	131 457	79 229	78 723	11 331	146	70	5 989	88	3 076	5 050	1 209	445	1 622	86	299	9 186	52	63	5 685	22 347	157	2 999	31	739	289	155	7 365	244	-
558371	Starý Plzenec	4 038	2 781	2 758	387	10	5	181	5	163	160	38	19	41	3	9	281	2	4	195	798	4	85	0	26	15	4	315	8	-
558427	Šťáhlavy	2 096	1 417	1 414	199	3	2	129	3	103	78	26	13	32	2	9	128	0	1	88	430	3	32	0	11	11	1	104	6	-
539741	Štěnovický Borek	436	313	313	58	2	1	27	1	21	15	4	4	7	2	0	24	2	0	20	74	1	8	0	0	4	3	34	1	-
558460	Tymákov	740	495	492	54	3	0	37	0	31	28	4	1	5	0	1	56	0	0	26	172	1	19	0	5	3	0	41	5	-

Stejným způsobem lze stáhnout data z dalších okresů. 
