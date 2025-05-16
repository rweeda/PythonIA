###SQL Basthon

<h4>ALGEMENE INLEIDING</h4>

<div class="activity-item time-block">
    <div class="fa fa-clock-o fa-3x"><br></div>
    <br>XX uur
</div>

<p><span lang="nl">Dit domein gaat over gestructureerde data, oftewel
databases…</p>

<p>Databases zijn overal. Wist je dat alle grote bedrijven zeer intensief van
databases gebruik maken om informatie op te slaan? Spotify gebruikt het om
elke dag nieuwe daily mixes samen te stellen die jouw favoriete muziek
bijhouden. Google gebruikt het om je het zoeken gemakkelijker te maken door
bij te houden wat jouw interesses zijn (waar zoek je vaak naar). Maar ook
veel reclames en advertenties worden gepersonaliseerd op basis van gegevens
die worden opgeslagen als jij op je computer of telefoon zit… </p>

<p>Al deze bedrijven, programma’s en apps maken gebruik van zogeheten
databases, waar je in deze lessenserie over zult leren. Relationele databases
zijn databases met meerdere tabellen die onderling relaties hebben. Dat wil
zeggen de gegevens van de ene tabel horen bij gegevens uit een andere tabel.
Deze databases worden beheerd door een database management systeem (DBMS) die
er voor zorgt dat de data betrouwbaar en correct blijft, en dat wij op een
gemakkelijk manier verzoeken kunnen indien om informatie die we nodig hebben
op te halen. </p>

<p>Zo’n verzoek noem je een query en daarvoor heb je een speciale vraagtaak
nodig: SQL. Dat staat voor Structured Query Language. De komende 2 weken leer
je de basis van SQL. Daarnaast is er (voor vwo) een verdieping waarin je
leert informatie uit verschillende tabellen te combineren.</p>

TODO Toelichting: inhoud van het lesmateriaal is deels overgenomen uit het Co-Teach lesmateriaal ontwikkeld door...



###Overzicht Hoofdstuk 1: Je eerste query
 <div class="activity-item time-block">
    <div class="fa fa-clock-o fa-3x"><br></div>
    <br>XX uur
</div>



<p>We beginnen met het kennismaken met databases. Wat zijn het, waar vind je
ze, hoe zitten ze in elkaar en hoe kunnen we er dan nuttige informatie uit
halen? Voor deze lessenserie maken we gebruik van SQL Online. Om dit
programma te kunnen gebruiken moet je elke keer als je de website opent de
juiste database importeren. Dat lijkt onhandig, maar als je (per ongeluk)
iets verandert in de database, kan je zo weer opnieuw beginnen door de
website opnieuw te laden en de database opnieuw in te lezen. Wees dus niet
bang om iets verkeerd te doen.</p>

[IMG: H1_overzicht.png]

<p>Leerdoelen</p>

In dit onderwerp:
<ul> 
<li>Je hebt kennis van de volgende begrippen: query, data(base) en SQL.</li>
<li> TODO: CREATE, UPDATE, DELETE???
<li>Je kan een SELECT - FROM toepassen voor het ophalen van informatie uit een tabel.</li>
<li>Je kan uitleggen wat een voorwaarde is en deze gebruiken in een WHERE clausule om informatie te filteren. </li>
</ul>


## 1.1. Introductie databases

## Introductie
<p>Het is vrijdagavond. Je weet nog niet wat je wilt eten maar hebt gehoord dat een nieuwe
pizzeria – Pizzeria Danilo, net geopend om de hoek – hele lekkere pizza’s maakt.
Als je een pizza bestelt, moet je natuurlijk wel eerst weten 
welke je wilt hebben. Als je de website van je plaatselijke 
pizzeria erbij hebt gepakt word je overweldigd door de 
hoeveelheid opties. Al deze opties staan in een 
<b>database</b>.</p>
[IMG H1_1_pizzabezorger]
<!--    <img src="https://raw.githubusercontent.com/rweeda/PythonIA/main/img/dicitonary_gamescores.png" width="300"> -->

<p>Maar wat is een database? En hoe ziet zoiets eruit?
Danilo moet veel <b>gegevens</b> bijhouden. Zoals bijvoorbeeld, de 
naam van de pizza's, de prijs en de ingredienten. Maar ook de
namen en adressen van klanten en gegevens over 
bestellingen en bezorgers. 


Die gegevens worden bewaard in tabellen. En tabellen bestaan weer uit 
rijen en kolommen met gegevens die opgeslagen worden. Die gegevens noemen we 
<b>data</b>. Gestructureerde data is informatie die op een vaste, georganiseerde manier is opgeslagen, zodat computers die makkelijk kunnen lezen, begrijpen en verwerken. 


## Ontwerp van een tabel

Op de webpagina hieronder worden gegevens gevraagd. Deze gegevens worden opgeslagen in een database. We gaan nu kijken hoe de achterliggende database eruit ziet.

[IMG H1_H1_H1_webform.png]

We maken een tabel waarin we de contactgegevens opslaan. Zo kunnen we makkelijk de gegevens van klanten terugvinden als ze een bestelling plaatsen.
<ol style="list-style-type: lower-alpha">
<li>Wat betekent het sterretje, bijvoorbeeld achter 'Voornaam'?
<li>Wat gebeurt er als er twee verschillende mensen zijn met dezelfde naam waarvan je het adres wilt opzoeken? Wat voor oplossing hebben we op school hiervoor? Bedenk een oplossing voor Danilo's pizzeria voor het eenduidig opslaan van klantgegevens.

<li>Sleep de kolomnamen naarWelke kolomnamen kies je? Vul die in het strokendiagram hieronder in. De kolom met `Achternaam' is voor je gedaan. 
<li>Geef de tabel een naam.
<li>Geef bij elke kolom aan welk van de volgende type gegevens het bevat:
  <ul>
  <li>TEXT: een tekst
  <li>INTEGER: een geheel getal
  <li>REAL: een kommagetal
  </ul>

<li>Geef bij elke kolom aan of er speciale eisen aan gesteld zijn:
  <ul>
  <li>PRIMARY KEY: een unieke waarde (in het Nederlands <i>primaire sleutel</i>)
  <li>NOT NULL: mag niet leeg zijn
  </ul>
</ol>



ANTWOORDEN:
<ol style="list-style-type: lower-alpha">
<li>Dat is een veld dat verplicht ingevuld moet worden.</li>
<li>Als twee klanten dezelfde naam hebben kun je ze niet uit elkaar halen, je kunt dan niet hun juiste adres opzoeken. Als oplossing gebruiken we een unieke waarde waarvan er maar één is, zoals een leerlingnummer op school, of een BSN. Voor Danilo's pizzeria zou een unieke nummer een klantnummer kunnen zijn.
<li>Zie hieronder
<li>tabelnaam: klanten

</ol>


TABEL: klanten
<table>
  <thead>
    <tr>
      <th>klantnummer<br>INTEGER PRIMARY KEY NOT NULL</th>
      <th>voornaam<br>TEXT NOT NULL</th>
      <th>tussenvoegsel</th>
      <th>achternaam<br>TEXT NOT NULL</th>
      <th>straat + huisnummer<br>TEXT NOT NULL</th>
      <th>postcode<br>TEXT NOT NULL</th>
      <th>woonplaats<br>TEXT NOT NULL</th>
      <th>telefoonnummer<br>TEXT NOT NULL</th>
      <th>e-mailadres<br>TEXT NOT NULL</th>
      <th>geboortedatum</th>
    </tr>
  </thead>
</table>




## Terugblik

Bij het maken van de vorige opdracht heb je veel geleerd over gestructureerde data. We vatten dat nu samen.

Voordat je gegevens op kan slaan, moet je eerst opgeven wat de vorm is van die gegevens. Daarvoor maak je een tabellen aan met verschillende kolommen waarin je 
<b>records</b> (oftewel 'gegevens') kunt opslaan.

<b>Primary key</b>:
Elke tabel heeft een kolom hebben waarmee je records kan aanwijzen: een <b>primary key</b>. Deze kolom moet <b>unieke</b> gegevens hebben, een kolom waar nooit twee keer hetzelfde waarde voor mag komen.
Een voorbeeld is leerlingnummer. Er kunnen geen twee leerlingen dezelfde leerlingnummer hebben. Terwijl er misschien wel twee leerlingen met dezelfde naam zijn, bijvoorbeeld Tom Janssen. Met een leerlingnummer weet je zeker over wie je het hebt. Een andervoorbeeld is een gebruikersnaam in een spel, daar mag er maar één van zijn.

(<i>Toelichting: een primary key kan uit meerdere kolommen samen bestaan, maar dat behandelen we in deze cursus niet.</i>)

<b>Soorten data</b>:
Met een database sla je gestructureerde data op. Daarvoor moet je voor iedere kolom het datatype aangeven, oftewel, wat voor soort gegevens je wilt opslaan.

In SQLite zijn er drie <b>datatypen</b>, oftelwel soorten data: 
<ul>
<li><b>INTEGER</b>: een geheel getal. Bijvoorbeeld: 4
<li><b>TEXT</b>: een stuk tekst. Bijvoorbeeld: 'Jaap'
<li><b>REAL</b>: een kommagetal. Bijvoorbeeld: 2.50
</ul>
  
Omdat er maar drie datatypen zijn zul je sommige gegevens als een TEXT opslaan. Bijvoorbeeld, een datum sla je in de vorm jjjj-mm-dd (j: jaar, m: maand, d:dag) op als een tekst, bijvoorbeeld: "2025-04-20". Een telefoonnummer zul je ook als een tekst opslaan, omdat anders de voorloop nul wegvalt, bijvoorbeeld: "0688567389".

<b>Eisen</b>:
Je kunt ook eisen geven aan waarden in een bepaald kolom:
<ul>
  <li>PRIMARY KEY: unieke waarde
  <li>NOT NULL: mag niet leeg zijn

####################



## Databases: Waarom?


[![Watch the video](https://www.youtube.com/watch?v=t8jgX1f8kc4/hqdefault.jpg)](https://www.youtube.com/watch?v=t8jgX1f8kc4)


<p>Je kunt je voorstellen dat Danilo graag een goed overzicht wil houden van alle verzamelde gegevens. 
Daarom gebruikt hij een <b>database</b>. Een database is een gestructureerde manier om gegevens op te
slaan. Met een database is het mogelijk om door middel van een speciale vraagtaal gegevens op te 
vragen en te combineren tot nuttige informatie.</p>

<p>Data is overal, niet alleen in de pizzeria van Danilo. Zodra jij je op het internet begeeft laat je een 
spoor van gegevens achter en die data moet ergens heen. Terwijl jij, bijvoorbeeld, gebruik maakt van 
YouTube worden verschillende gegevens verzameld die hergebruikt kunnen worden om een 
gepersonaliseerde ervaring mogelijk te maken aan te bieden. Denk hierbij aan hoe lang je naar een video kijkt, naar 
welke video’s je zoekt of op welke video’s die aangeraden worden jij ook echt doorklikt. Ook moet er 
veel informatie over de video’s zelf opgeslagen worden zoals de titel, de thema’s, de lengte, etc. Je 
kunt je voorstellen dat via het internet zo een enorme hoeveelheid data verzameld wordt.</p>


<p>Jouw school maakt ook gebruik van databases. Gebruikt je school Magister of Somtoday? Deze 
programma's slaan informatie over jou als leerling op in een database. Hiermee kan je docent 
huiswerk opgeven en toetscijfers inzien en invoeren, kan de schoolleiding zien hoe het met 
verschillende klassen gaat en kan jij zien hoe je er voor staat met al je vakken of opdrachten 
inleveren.</p>

###Databasemanagementsysteem (DBMS)
<p>Een database kan al snel heel groot worden. Er wordt niet alleen data in opgeslagen, maar er wordt 
ook data veranderd of verwijderd. Een andere belangrijke functie van een database is de mogelijkheid
tot het opvragen en combineren van data. Tenslotte heeft niet iedereen dezelfde toegang tot een 
database. Als leerling kan jij alleen jouw eigen gegevens lezen, maar een docent kan dat van al zijn 
leerlingen zien en bovendien kan hij cijfers veranderen en toevoegen.</p>

[IMG]
<p>Dat moet natuurlijk allemaal goede bewaakt en geregeld worden. En daarvoor wordt een <b>databasemanagementsysteem</b> of kort gezegd DBMS 
gebruikt.</p>

<p>Dit is software die er voor zorgt dat iemand met de juiste 
rechten toegang krijgt, dat data altijd correct wordt 
opgeslagen, ook als deze wordt aangepast of (deels) 
verwijderd.</p>





### Opdracht 1.1:  Wat zijn databases?

<p>Stiekem heb je al eerder gebruik gemaakt van een database zonder dat je dat wist. Laten we eens op
onderzoek uit gaan en kijken of we nog meer databases kunnen vinden.</p>

<ol style="list-style-type: lower-alpha">
<li>Bedenk nog een voorbeeld van een website die, naar jouw verwachting, gebruik maakt van een 
database. </li>
<li>Wat voor soort data zou opgeslagen worden in deze database?</li>
</ol>

<p>Bekijk <a href="https://rweeda.github.io/PythonIA/docs/IA_H5_oplossingen.html#opgave532" target="_blank">hier</a> de voorbeelduitwerking.</p>



<!--
Voorbeelden van antwoorden: 
<ol style="list-style-type: lower-alpha">
<li>
  <li>Webwinkel</li>
  <li>Social media platform</li>
</li>
<li>
  <li>Bij webwinkel: productenlijst</li>
  <li>Bij social media platform: posts</li>
</li>
</ul>
-->

### Opdracht 1.2: Gegevens, data en informatie


<p>Woorden als <i>gegevens</i>, <i>data</i>, en <i>informatie</i> worden vaak 
door elkaar gehaald. Is dat terecht of niet? Betekenen ze allemaal hetzelfde 
of is er toch een verschil? Dat ga jij in deze opdracht uitzoeken.</p>


<ol style="list-style-type: lower-alpha">


<li>Zoek op internet naar de definitie van gegevens. Wat zijn gegevens?</li>
<li>Zoek op internet naar de definitie van data. Wat is data?</li>
<li>Zoek op internet naar de definitie van informatie. Wat is informatie?</li>
<li>Bepaal welk van de volgende woorden <i>gegevens</i>, <i>data</i> en <i>informatie</i> bij ieder van de onderstaand thuishoren:
  <ul>
  <li>Het weerbericht
  <li>Windsnelheid gemeten met een windmolentje
  <li>Temperatuur gedurende de dag op elk uur gemeten.
  </ul>


</ol>


<!-- Mogelijke antwoorden:
<ol style="list-style-type: lower-alpha">
<li>chatGPT: "Gegevens zijn feiten, cijfers en andere waarnemingen die verzameld 
en opgeslagen kunnen worden om te worden geanalyseerd, geïnterpreteerd of 
gebruikt voor besluitvorming." Met andere woorden, allerlei eigenschappen van 
mensen en objecten die je kunt verzamelen en opslaan om later te gebruiken 
en/of te combineren tot nuttige informatie.</li>

<li>chatGPT: "Data bestaat uit feiten, cijfers en waarnemingen die worden verzameld uit verschillende 
bronnen en die nog moeten worden geanalyseerd of geïnterpreteerd om betekenis of waarde te 
krijgen."
Met andere woorden, opgeslagen eigenschappen van mensen en objecten die je kunt verzamelen 
en opslaan om later te gebruiken en/of te combineren tot nuttige informatie.</li>

<li>chatGPT: "Informatie is de kennis, inzichten, of betekenis die wordt verkregen door het verzamelen,
verwerken, analyseren en interpreteren van ruwe feiten en cijfers. Het is georganiseerd en 
gestructureerd zodanig dat het begrijpelijk en nuttig is voor de ontvanger, en het wordt gebruikt om 
beslissingen te nemen, problemen op te lossen of communicatie te verbeteren"
Met andere woorden, informatie bestaat uit het (slim) combineren van data (gegevens) om zo tot 
nuttige kennis te komen. Bijvoorbeeld het opstellen van een profiel van iemand om een 
persoonlijke advertentie, advies of muziekkeuze te kunnen geven.</li>

<li>

  <ul>
    <li>Het weerbericht bestaat uit een combinatie van gegevens en data  en dus is het informatie.
    <li>Windsnelheid die wordt gemeten en afgelezen is een gegeven is dat nog niet is opgeslagen. Dus zijn 
    het gegevens.
    <li>"Temperatuur gedurende de dag" zijn metingen die elk uur zijn gedaan en zijn opgeslagen. Dus is 
    het data.
  </ul>
In de praktijk worden de woorden data en gegevens veel door elkaar gebruikt.
</ol>

-->


### SQL
SQL (Structured Query Language) is een standaardtaal om data in een database op te slaan, te bewerken en op te halen. In deze cursus leer je hoe je SQL gebruikt binnen een SQLite databasesysteem. 
Het woord query betekent letterlijk ‘vraag’ in het Engels. Als je een query maakt, stel je dus eigenlijk een vraag aan de database. Bijvoorbeeld: “Welke klanten wonen in Amsterdam?”

In deze cursus leer je hoe je met SQL een SQLlite-database maakt, maar ook hoe je daar gegevens uit opvraagt of die aanpast.




De taal voor het ophalen van informatie bestaat uit slechts 6 commando’s waarmee je in de volgende lessen
leert werken. De commando’s zijn

[IMG H1_commandos.png]

Je hoeft niet alle commando's te gebruiken, maar ze staan welk altijd in deze volgorde.


## 1.2: Gegevens ophalen

<p>Met een query kun je gegevens uit een tabel ophalen. Met SELECT kun je data selecteren van een database en in een overzicht tonen. 
Met FROM geef je aan uit welke tabel de informatie gehaald moet worden.</p>




<p>Bij de volgende opgaven maken we gebruik van de tabel <i>pizza</i> uit Danilo's pizzeria. De afbeelding hieronder toont de kolommen van tabel <i>pizza</i>:
[img ERD_pizza]

Hieronder zie je hoe de tabel <i>pizza</i> er uitziet met de gegevens van een aantal pizza's erin.
[IMG H1_tabel_pizza]




### Alle gegevens van een tabel ophalen

<p>Om alle kolommen met gegevens van een tabel op te halen, gebruik je de volgende query:</p>
 
<code>SELECT * 
FROM tabelnaam;</code>

### Opdracht 1.3: Alle gegevens van tabel pizza ophalen

Toon alle kolommen met gegevens van tabel <i>pizza</i>.

<!-- ANTWOORD:
SELECT *
FROM pizza
-->

### Eén kolom uit een tabel halen

Je kunt ook maar één kolom ophalen. Dat doe je als volgt:
 
SELECT kolomnaam
FROM tabelnaam;


Bijvoorbeeld:
SELECT naam 
FROM pizza;

### Opdracht 1.4: Pizzacodes
<ol style="list-style-type: lower-alpha">
<li>Toon alle pizzacodes (kolom <i>pizzacode</i>) in tabel <i>pizza</i>.
<li>Wat zie je als je naar de pizzacodes kijkt? Leg uit wat dat te maken heeft met de 'primary key'.
</ol>



<ol style="list-style-type: lower-alpha">
<li>
<!-- SELECT pizzacode 
FROM pizza;
-->
<li>Elke pizzacode komt maar één keer voor. Dat betekent dat elke pizza een unieke code heeft. Zo’n unieke code noemen we een primary key. Een primary key zorgt ervoor dat je elk record in een tabel kunt herkennen. In dit geval herken je elke pizza aan zijn pizzacode.
</ol>


### Sommige kolommen uit een tabel halen
Je kunt ook een beperkt aantal kolommen ophalen. Dat doe je als volgt:
 
SELECT kolom1, kolom2, ...
FROM tabelnaam;

### Opdracht 1.4: Menu printen

Maak een menu door de pizzanamen (kolom <i>naam</i>), <i>omschrijving</i> en de prijs (kolom <i>basisprijs</i> uit het tabel <i>pizza</i> te halen.

<!-- ANTWOORD:
SELECT naam, omschrijving, basisprijs 
FROM pizza;
-->


## 1.3: Commentaar

Net als bij programmeren, kun je in SQL ook commentaar opnemen in je code. Dit doe je 
door twee streepjes ‘--’ ervoor te zetten. Dat ziet er dan zo uit (zie regel 2):</p>
SELECT * 
FROM pizza; -- dit is de tabelnaam

<p>Je kunt ook <code>/*</code> ervoor en <code>*/</code> erna zetten. Dat ziet er dan zo uit (zie regel 2):</p>
SELECT * 
FROM pizza; /* dit is de tabelnaam */


## 1.4: Nette code
<p>Net als andere programmeertalen, zijn er afspraken om nette en leesbare queries 
te schrijven.</p>


  
<ol>
<li>Schrijf de SQL opdrachten altijd met HOOFDLETTERS.
<li>Schrijf elke opdracht op een nieuwe regel.
<li>Als je meerdere items achter een SELECT of FROM opdracht hebt staan dan moet je deze scheiden met een komma.
<li>Gebruik spaties om de leesbaarheid tussen items te vergroten.
<li>Schrijf commentaar in je query om uit te leggen wat je doet (vooral bij WHERE en GROUP BY).
<li>Je mag een query afsluiten met een puntkomma (;), maar dat hoeft bij eenvoudige queries niet.
</ol>

Hieronder een voorbeeld van nette code:
<code>
SELECT naam, basisprijs
FROM pizza
-- Alleen pizza's bekijken die goedkoper zijn dan 10 euro
-- EN duurder dan 8 euro 50
WHERE basisprijs <= 10 AND basisprijs >= 8.50;
</code>  

### Opdracht 1.5: Nette code
<ol style="list-style-type: lower-alpha">
De query hieronder is niet zo netjes opgeschreven.
<li>Voer de onderstaande query uit, dan zul je zien dat de query het gewoon doet. Bekijk de uitkomst.
<li>Pas deze query aan zodat hij voldoet aan alle voorwaarden van nette code.
<li>Voeg bij elke regel commentaar toe om aan te geven voor welk voorwaarde je het hebt aangepast.
</ol> 


naam,basisprijs From pizza wHERe basisprijs<8



<!--ANTWOORD
-- (1) SQL commando in hoofdletters, (4) spatie na de komma
SELECT naam, basisprijs
-- (2) Elke SQL commando op een nieuwe regel (en in hoofdletters)
FROM pizza
-- (4) spaties in de voorwaarde zodat het beter leesbaar is
-- (6) en afsluiten met een ; (maar dat hoeft niet)
WHERE basisprijs < 8;
-->



#TODO DEBUGGEN - code met fout laten runnen en fout opsporen, evt mbv commentaar



## 1.4: Aantal rijen
<p>Met LIMIT kun je bepalen hoeveel rijen er getoond moeten worden.</p>

<p>Met de volgende code toon je alleen de eerste vijf rijen:</p>

SELECT *
FROM pizza
LIMIT 5;


### Opdracht 1.6 LIMIT
Toon de naam (<i>pizzanaam</i>) en prijs (<i>basisprijs</i>) van de eerste drie pizza's.


ANTWOORD:

SELECT pizzanaam, basisprijs
FROM pizza
LIMIT 3;



## Voorwaarden: WHERE
<p>Met WHERE kun je een voorwaarde aangeven zodat alleen een deel van de informatie opgehaald wordt: ’waarbij de informatie voldoet aan ...’</p>

<p>Je geeft altijd eerst een SELECT op voor de gegevens die opgehaald moeten worden, dan met FROM de tabel waaruit de gegevens moeten komen, en met WHERE welke beperking er is.</p>


Bijvoorbeeld, met de volgende query tonen we alle pizza's die precies 8 euro kosten:
SELECT *
FROM pizza
WHERE basisprijs=8

### Opdracht: Omschrijving van een Inferno pizza
Schrijf een query om de omschrijving van de pizza 'Inferno' te tonen.


ANTWOORD:
SELECT omschrijving
FROM pizza
WHERE naam='Inferno'


## Operatoren

Behalve de '='-teken kun ook andere operatoren in de WHERE gebruiken. Hier is een overzicht:

|---------|-----------------------------|
| Operator| Betekenis                   |
|---------|-----------------------------|
| =       | gelijk aan                  |
| >       | groter dan                  |
| >=      | groter dan of gelijk aan    |
| <       | kleiner dan                 |
| <=      | kleiner dan of gelijk aan   |
| <>      | ongelijk aan                |
|---------|-----------------------------|

Bijvoorbeeld, met de volgende query tonen we alle pizza's die niet de naam 'Inferno' hebben:
SELECT *
FROM pizza
WHERE naam<>'Inferno'


### Opdracht: Dure pizza's
Toon de namen en prijzen van de pizza's die 9,50 euro kosten of meer.


ANTWOORD:
SELECT naam, basisprijs
FROM pizza
WHERE basisprijs>=9.50;



### Opdracht: Dure pizza's
Toon de namen en prijzen van de pizza's die <b>niet</b> 8 euro kosten.


ANTWOORD:
SELECT naam, basisprijs
FROM pizza
WHERE basisprijs<>8;



## WHERE met LIKE

TODO: _ weghalen

<p>LIKE maakt gebruikt van jokers. Dat gebruik om te zoeken naar delen van 
teksten, of wanneer je iets ongeveer wilt zoeken, dus niet exact zoals met 
<code>=</code>. Met de joker geef je aan welke teken(s) anders mogen zijn.</p> <p>Er zijn twee soorten jokers: procent 
teken <code>%</code> voor meerdere tekens en <code>_</code> voor één teken: </ul> 

| Joker | Betekenis                  | Voorbeeld                                                          |
|--------|----------------------------|---------------------------------------------------------------------|
| `%`    | Vervangt 0 of meer tekens  | `naam LIKE 'J%'` → alle namen die beginnen met ‘J’ (zoals Jan, Julia) |
| `_`    | Vervangt exact één teken   | `naam LIKE '_an'` → Jan, Ian, Han                                   |
|--------|----------------------------|---------------------------------------------------------------------|


Je mag de jokers ook combineren.

### De <code>%</code> joker
Met de <code>%</code> geef je een zoekvraag waarbij er meerdere tekens anders mogen zijn.

Bijvoorbeeld, met de volgende query tonen we de pizza's met een naam die begint met 'Quattro':

SELECT naam
FROM pizza
WHERE naam LIKE 'Quattro%';

Of die eindigen met 'arma':

SELECT naam
FROM pizza
WHERE naam LIKE '%arma';

Of waarbij de letter 'e' erin voorkomt:

SELECT naam
FROM pizza
WHERE naam LIKE '%e%';






### Opdracht: Alle pizza's waarvan de naam met 'Ca' begint

Toon een overzicht van alle pizza's waarvan de naam met 'Ca' begint.


ANTWOORD: 
SELECT naam
FROM pizza
WHERE naam LIKE 'Ca%';







## Booleanse operatoren
Je kunt de voorwaarde ook uitbreiden met de booleaanse operatoren AND, OR, NOT of combinaties daarvan. 


Bijvoorbeeld, met de volgende query tonen we de pizza's die tussen de €8,50 en €10,- kosten:

SELECT naam, basisprijs
FROM pizza
WHERE basisprijs>=8.50 AND basisprijs<=10;



Of waar de letter 'a' er niet in voorkomt:

SELECT naam
FROM pizza
WHERE NOT naam LIKE '%a%';



### Opdracht: Alle goedkope of gezonde pizza's
Maak een overzicht van alle pizza's goedkoper zijn dan €7,50 of fruit bevatten.

ANTWOORD:
SELECT *
FROM pizza
WHERE basisprijs<7.50 OR omschrijving LIKE '%fruit%';




### Opdracht: Alle pizza's zonder paprika

Toon een overzicht van alle pizza's waar <b>geen</b> paprika op zit. Toon zowel de <i>pizzanaam</i> als de <i>omschrijving</i>.


ANTWOORD: 
SELECT naam, omschrijving
FROM pizza
WHERE NOT omschrijving LIKE '%paprika%';






### Opdracht: Alle pizza's 

## Meerdere operatoren combineren
Als je de AND, OR en NOT combineert moet je gebruik maken van haakjes voor de gewenste uitkomst.

Bijvoorbeeld, met de volgende query tonen we de pizza's die tussen de  €8,50 en €10,- kosten, of pizza's die geen salami bevatten:

SELECT naam, omschrijving, basisprijs
FROM pizza
WHERE (basisprijs>=8.50 AND basisprijs<=10) OR NOT omschrijving LIKE '%salami%';



### Opdracht: Toon pizza's gefiltererd op meerdere voorwaarden

Toon alle pizza's die minder dan €7,50 kosten, en met de letter M beginnen of letter A eindigen. 

ANTWOORD:
SELECT *
FROM pizza
WHERE basisprijs < 7.5 AND (naam LIKE 'M%' OR naam LIKE '%A') AND ;



## Kennis maken met de andere tabellen

ERD

Danilo's pizzeria database bestaat uit meer tabellen dan alleen pizza's. Er wordt ook bijvoorbeeld ook informatie opgeslagen over klanten, berzorgers en bestellingen. In de afbeelding hieronder zie je alle 7 tabellen.



### Opdracht: Alle klanten uit Enschede


Toon het adres, de postcode en de plaats van alle klanten die in Enschede wonen.


ANTWOORD:

SELECT adres, postcode, plaats
FROM klant
WHERE plaats='Enschede';


### Opdracht: Wachtwoord uit tabel bezorger.
Toon het wachtwoord van de bezorger met de naam Ronald Marbus.

ANTWOORD
SELECT wachtwoord
FROM bezorger
WHERE naam = 'Ronald Marbus';


### Opdracht: Bestellingen met bestelcode
Toon alle informatie over zowel bestellingen bestelcode 13 en die met bestelcode 30.


ANTWOORD:
SELECT *
FROM bestelling
WHERE bestelcode = 13 OR bestelcode = 30;


## Resulaten sorteren

Met ORDER BY kun je resultaten sorteren.
Hierbij moet je aangeven op welke kolom er gesorteerd moet worden en of het oplopend ('ASC') of juist 
aflopend ('DESC') moet zijn. Geef altijd eerst de SELECT en FROM aan, en daarna de ORDER BY.



Bijvoorbeeld, om de pizza's op oplopend op prijs te sorteren, dus met de goedkoopste pizza bovenaan:
SELECT naam, basisprijs
FROM pizza
ORDER BY basisprijs ASC;


Of om de bezorgers te aflopende sorteren op geboortedaum, dus met de jongste bezorger bovenaaan:
SELECT naam, geboortedatum
FROM bezorger
ORDER BY gebdatum DESC;


### Opdracht: de drie duurste pizza's
Geef een overzicht van de duurste drie pizza's. Tip: eerst aflopend sorteren, dan met LIMIT de bovenste drie pizza's tonen.

ANTWOORD: 
SELECT naam, basisprijs
FROM pizza
ORDER BY basisprijs DESC
LIMIT 3;


### Opdracht: de vijf laatste bezorgingen


ANTWOORD: 
SELECT bestelcode, datum
FROM bestelling
ORDER BY datum ASC
LIMIT 5;


### Kolom hernoemen met 'AS`

Met `AS` kan je een kolomnaam hernoemen.

Bijvoorbeeld, hieronder wordt de kolom `naam` getoond als `pizzanaam`



SELECT naam AS pizzanaam
FROM pizza;


| pizzanaam   |
|-------------|
| Margherita  |
| Napoletana  |
| Prosciutto  |
| Funghi      |
| Salame      |


### Opdracht: kolom 'naam' veranderen in 'bezorgernaam'
Toon een overzicht van alle namen van de bezorgers. Noem het kolom `bezorgernaam`.


ANTWOORD:

SELECT naam AS bezorgernaam
FROM bezorger;



### AFSLUITENDE OPDRACHTEN



### Afsluitende opdracht

Toon van alle pizza's de omschrijving en de naam (in die volgorde).
<!-- ANTWOORD
SELECT omschrijving, naam
FROM pizza;
-->





## Gegevens beheren

Het beheren van gegevens kan je opdelen in vier categorieen: Create, Read, Update, Delete, afgekort tot CRUD:

<ul> 

<li><b>Create</b>: Nieuwe tabellen aanmaken (met CREATE TABLE), of gegevens toevoegen (met INSERT INTO);

<li><b>Read</b>: Opgeslagen gegevens bekijken (met SELECT);

<li><b>Update</b>: Opgeslagen gegevens bewerken (met UPDATE);

<li><b>Delete</b>: Opgeslagen gegevens verwijderen (met DELETE). 
</ul> 


Een DBMS zorgt ervoor dat een beheerder al deze dingen kan doen bij alle 
gegevens. Als je een programma met meerdere gebruikers maakt, bepaal je per gebruiker wat ze 
mogen. De gebruiker mag bijvoorbeeld alleen zijn eigen 
wachtwoord bewerken (Update), niet dat van andere gebruikers. 

De app van Danilo's Pizzeria heeft verschillende gebruikers:
<ul>
<li>Klanten – bestellen pizza’s
<li>Medewerkers – maken pizza’s klaar
<li>Beheerders – beheren de hele database
</ul>

TODO ERD
### Opdracht CRUD rechten van klanten bepalen

Een klant plaatst een bestelling via de app van Danilo's Pizzeria. 
<ol type="a">
<li>Welke acties (Create, Read, Update, Delete) moet een klant kunnen uitvoeren op de tabel <code>besteldePizza</code>?
<li>Licht je antwoord toe: waarom is het logisch dat een klant sommige dingen wel en andere dingen niet mag? 
</ol>

ANTWOORDEN:
<ol type="a">
<li>Acties:
	<ul>
	<li>Create: Ja, een klant moet nieuwe bestellingen kunnen plaatsen.
	<li>Read: Ja, maar alleen de eigen bestellingen.
	<li>Update: Nee, een bestelling aanpassen na plaatsing kan leiden tot verwarring in de keuken of bezorging.
	<li>Delete: Nee, want verwijderen van bestellingen kan misbruik veroorzaken of onduidelijkheid voor medewerkers.
	</ul>
<li>Toelichting:
Klanten mogen alleen hun eigen gegevens zien en invoeren, maar niet wijzigen of verwijderen. Dit voorkomt fouten en misbruik, en beschermt de privacy van andere klanten.
</ol>



### Opdracht CRUD Rechten van de bezorger bepalen
Een bezorger krijgt een overzicht van de pizza’s die hij moet afleveren. Na bezorging vinkt hij in het systeem aan dat de bestelling is bezorgd, daarmee wordt de bezorgtijd vastgelegd.
<ol type="a">
<li>Welke rechten heeft een bezorger nodig op de tabel besteldePizza?
<li>Welke informatie moet hij kunnen zien, en welke mag hij aanpassen?
<li>Waarom is het belangrijk dat een bezorger geen toegang heeft tot bepaalde gegevens?
</ol>


ANTWOORDEN:
<ol type="a">
<li>Acties:
<ul>
<li>Read: Ja, om te kunnen zien welke bestellingen hij moet bezorgen, inclusief adresinformatie.
<li>Update: Ja, om de status van een bestelling te markeren als "bezorgd", waardoor de bezorgtijd wordt vastgelegd.
<li>Create/Delete: Nee, een bezorger mag geen bestellingen invoeren of verwijderen.
</ul>
<li>Toelichting: De bezorger heeft beperkte toegang. Hij mag alleen de status aanpassen, bijvoorbeeld een vinkje bij "bezorgd". Andere gegevens zijn niet zijn verantwoordelijkheid en moeten dus beschermd blijven.
</ol>

### Opdracht CRUD Rechten van de databasebeheerder bepalen
De beheerder moet het hele systeem kunnen beheren, ook als er iets fout is gegaan.
<ol type="a">
<li>Welke CRUD-rechten heeft een beheerder?
<li>Wat zijn de voor- en nadelen van het geven van volledige CRUD-rechten aan een beheerder?
<li>Zou je alle beheerders dezelfde rechten geven, of verschillende rollen aanmaken?
</ol>

ANTWOORDEN
<ol type="a">
<li>Acties: Create, Read, Update, Delete: een beheerder heeft alle rechten.
<li>Voor- en nadelen:
<ul>
<li>Voordelen: De beheerder kan fouten corrigeren, testgegevens verwijderen, of het systeem onderhouden.
<li>Nadelen: Volledige rechten zijn gevoelig voor fouten of misbruik. Eén verkeerde DELETE-query kan veel gegevens verwijderen.
</ul>
<li>Overweging:
Je kunt overwegen om meerdere beheerdersrollen aan te maken, bijvoorbeeld een “technisch beheerder” (volledige toegang) en een “functioneel beheerder” (alleen lezen en bewerken, geen verwijderen).
</ol>

### Opdracht Fouten voorkomen
Stel dat je per ongeluk een Delete-recht geeft aan klanten op de tabel besteldePizza.

<ol type="a">
<li>Wat zou er kunnen gebeuren als een klant zijn eigen of andermans bestellingen kon verwijderen?
<li>Hoe kun je dit voorkomen?
</ol>


ANTWOORDEN
<ol type="a">
<li>Gevolgen van verkeerde Delete-rechten bij klanten:
<ul>
<li>Klanten kunnen elkaars of hun eigen bestellingen verwijderen.
<li>Hierdoor kunnen bezorgers en keukenpersoneel hun werk niet goed doen.
<li>Er ontstaat chaos in de bestelgeschiedenis, en klantenservice moet fouten oplossen.
</ul>
<li>Oplossing:
<ul>
<li>Gebruik rolgebaseerde toegang (bijv. alleen de beheerder mag DELETE uitvoeren).
<li>Voeg controlemechanismen toe in de applicatie: de knop ‘verwijderen’ is niet zichtbaar voor klanten.
<li>Extra: in een geavanceerde DBMS kun je databasepermissies aanpassen, bijvoorbeeld met GRANT/REVOKE.
</ul>
</ol>


## Tabel aanmaken in een database

Met CREATE TABLE kun je een nieuwe tabel aanmaken. Je geeft dan de naam van de nieuwe tabel op met daarachter tussen haakjes ieder kolomnaam en de bijbehorende datatype.

Elk tabel heeft een primary key. In die kolom mag een waarde maar een keer voorkomen. Dat kan je zelf bijhouden, maar de database kan ook automatische voor je doortellen als een record wordt toegevoegd. Dat doe je met: INTEGER PRIMARY KEY AUTOINCREMENT



Hieronder een voorbeeld voor het maken van tabel <i>pizza</i>:

CREATE TABLE pizza (
  pizzacode INTEGER PRIMARY KEY AUTOINCREMENT, 
  naam TEXT,
  omschrijving TEXT,
  basisprijs REAL)
  ;
  



### Opdracht tabel aanmaken


TODO: MOGELIJK? COTEACH 3.3 Laat leelring juist de tabel Bezorger zelf bedenken
FILMPJE OVERNEMEN


Je gaat een nieuw onderdeel toevoegen aan de pizzadatabase: een tabel voor *kortingsbonnen*. Deze tabel moet informatie bevatten over de kortingsbonnen die in omloop zijn: hoeveel korting ze geven en op welk datum de bon geldig is.


Schrijf zelf een CREATE TABLE-statement voor de tabel <code>kortingsbonnen</code>. Bedenk welke kolommen je nodig hebt, en welke typen data je gebruikt. Denk aan:
<ul>
<li>AUTOINCREMENT voor een uniek boncode
<li>Zinnige datatypen (zoals TEXT, INTEGER, REAL, …)
<li>Een primary key
</ul>


<!-- ANTWOORD:

CREATE TABLE kortingsbonnen (
    boncode INTEGER PRIMARY KEY AUTOINCREMENT,
    korting REAL,
    datum TEXT
);
-->



 


## Gegevens in een tabel invoeren

Met INSERT INTO kun je gegevens in een tabel invoeren. Je geeft dan de naam van de tabel aan, en tussen haakjes de gegevens voor elke kolom in de tabel.
Let er op dat tekst tussen aanhalingstekens gezet moet worden. Bij getallen of kommagetallen hoeft dat niet.

Bij een AUTOINCREMENT wordt automatisch een unieke primary key bepaald, daarom geef je daar de waarde <code>NULL</code> op.


INSERT INTO pizza VALUES (NULL, 'Pizza Hawaii', 'Ham en ananas', 8.50);


### Opdracht gegevens invullen aanmaken

Voeg een kortingsbon toe aan tabel <i>kortingsbonnen</i> met een korting van 0.50 euro en de datum 2025-12-20.

De kolom boncode heeft een AUTOINCREMENT. Deze wordt automatisch bepaald, geef daarom daar de waarde <code>NULL</code> op.


GEGEVEN:
CREATE TABLE kortingsbonnen (
    boncode INTEGER PRIMARY KEY AUTOINCREMENT,
    korting REAL,
    datum TEXT
);

<!-- ANTWOORD:
INSERT INTO kortingsbonnen VALUES (NULL,0.50,"2025-12-20");
-->




## Gegevens in een tabel aanpassen

Met UPDATE kun je gegevens in een tabel aanpassen. Je geeft dan de naam van de tabel aan. Daarna geeft je met SET aan wat de nieuwe waarde moet worden. Met WHERE geef je aan welke records aangepast moeten worden. Om één specifiek record aan te passen kun je hier het beste de 'primary key' gebruiken.

Bijvoorbeeld, met de volgende query wordt de pizzanaam van de pizza met code 1 aangepast naar "Hawaii"

UPDATE pizza
SET pizzanaam = "Hawaii"
WHERE pizzacode = 1;




### Opdracht: pas de prijs van een pizza aan

Schrijf een query die de prijs van de pizza met code 1 aanpast naar 9.50.

<!-- ANTWOORD

UPDATE pizza
SET basisprijs = 9.50
WHERE pizzacode = 1;
-->



## Record uit een tabel verwijderen
Om een hele rij van gegevens uit een tabel te verwijderen, gebruik je DELETE FROM. Met WHERE geef je aan welk records verwijderd moeten worden. Om één specifiek record te verwijderen kun je hier het beste de 'primary key' gebruiken.



DELETE FROM Pizza
WHERE pizza_code = 1;

## Een tabel verwijderen
DROP TABLE klant



# H4: 

## Overzicht van alle tabellen
In de schema hieronder zie je een overzicht van de tabellen.
[DaniloIA_ERD.png]
[ERDtoelichting.png]

De pijlen geven koppelingen tussen de tabellen aan. Een bestelling heeft een klantnummer. Aan het pijltje kun je zien dat de gegevens over de klant te vinden zijn in tabel <code>klanten</code>.

<p>
Extra:
De tekens bij de pijlen geven ook een relatie aan. De relatie tussen tabel <i>klant</i> en <i>bestelling</i> is een één-op-veel-relatie omdat 1 klant meerdere bestelling kan hebben, maar een bestelling altijd maar 1 klant heeft.
</p>



## Tabellen koppelen

In een vorige opdracht heb je een nieuwe tabel ontworpen om van kortingsbonnen de waarde en geldigheidsdatum bij te houden:


CREATE TABLE kortingsbonnen (
    boncode INTEGER PRIMARY KEY AUTOINCREMENT,
    korting REAL,
    datum TEXT
);

[picture ERD kortingsbonnen]

Als je bij een bestelling wilt bijhouden welke kortingsbon gebruikt, dan moet je de tabel <code>besteldePizza</code> uitbreiden met een kolom die verwijst naar <code>kortingsbonnen</code>.

Dit doe je met een *foreign key*. Een foreign key is een kolom in een tabel die verwijst naar een primary key in een andere tabel. Zo leg je een relatie tussen twee tabellen.


Waarom doe je dit?
<ul>
<li>Je legt een relatie tussen twee tabellen: een bestelling kan een kortingsbon gebruiken.
<li>Je voorkomt fouten, zoals het invullen van een boncode die niet bestaat.
<li>Je kunt makkelijk gegevens opvragen, bijvoorbeeld welke bestellingen hebben welke bon gebruikt, en hoeveel korting er in totaal is gegeven is.
</ul>

In het voorbeeld hieronder zie je hoe je tabel <code>besteldePizza</code> kunt uitbreiden met een foreign key die verwijst naar de primary key <code>boncode</code> van tabel <code>kortingsbonnen</code>.


CREATE TABLE besteldePizza (
    besteldePizzaID INTEGER PRIMARY KEY AUTOINCREMENT,
    pizzacode INTEGER,
    bestelcode INTEGER,
    boncode INTEGER,
    FOREIGN KEY (boncode) REFERENCES kortingsbonnen(boncode)
);

Toelichting: 
<ul>
<li>Kolom <code>boncode</code> is aan tabel <code>besteldePizza</code> toegevoegd. Hier staat de gebruikte boncode uit tabel <code>kortingsbonnen</code> in.
<li>Met de onderste regel geven we aan dat de nieuwe kolom <code>boncode</code> uit <code>besteldePizza</code> verwijst naar (`REFERENCES`) naar tabel de primary key <code>boncode</code> uit tabel <code>kortingsbonnen</code> met: <code>kortingsbonnen(boncode)</code>.
</ul>


### Opdracht Foreign keys bij Danilo's Pizzeria

Bekijk het overzicht van de tabellen en beantwoord de volgende vragen:
[DaniloIA_ERD.png]

<ol type="a">
<li>Hoeveel foreign keys heeft tabel <code>besteldepizza</code>? Benoem voor elk de tabel waar naar verwezen wordt en de bijbehorende kolomnaam.
<li>Hoeveel foreign keys heeft tabel <code>formaat</code>?
<li>Leg in je eigen woorden wat de volgende code betekent: <code>FOREIGN KEY (formaatcode) REFERENCES formaat(formaatcode)</code>.
<li>Leg in je eigen woorden wat er mis is aan de volgende code: <code>FOREIGN KEY (formaatcode) REFERENCES formaat(omschrijving)</code>.
</ol>


ANTWOORDEN:
<ol type="a">
<li>Tabel <code>besteldepizza</code> heeft vier foreign keys, namelijk:
	<ol><li><code>bestelcode</code> uit tabel <code>bestelling</code> 
	<ol><li><code>pizzacode</code> uit tabel <code>pizza</code> 
	<ol><li><code>bodemcode</code> uit tabel <code>bodem</code> 
	<ol><li><code>formaatcode</code> uit tabel <code>formaat</code> 
	</ol>
<li>Tabel <code>formaat</code> heeft *geen* foreign key. Die heeft een primary key <code>formaatcode</code> die vanuit tabel <code>besteldePizza</code> als foreign key gebruikt wordt, maar die verwijst zelf niet naar een ander tabel en heeft dus geen foreign key.
<li>Tabel <code>besteldePizza</code> heeft een kolom formaatcode. Daarvoor komen de gegevens uit tabel <code>formaat</code> en kolom <code>formaatcode</code>.
<li>De foreign key verwijst naar kolom <code>omschrijving</code> uit tabel <code>formaat</code>. Dit is niet goed, want het moet verwijzen naar de primary key van tabel <code>formaat</code>, en dus <code>formaatcode</code>.
</ol>



## UITLEG UITVRAGEN OVER MEERDERE TABELLEN MET WHERE (GEEN JOIN)

<p>In een database zijn gegevens vaak verdeeld over meerdere tabellen. Maar soms wil je juist gegevens uit meerdere tabellen tegelijk zien — bijvoorbeeld: Bij Danilo's pizzeria, welke bodem er in een bestelling gekozen is. Je wilt dus de tabel <code>besteldePizza</code> koppelen aan tabel <code>bodem</code>.


Tabel: `besteldePizza`

| besteldePizzaCode | pizzacode | bodemcode |
|------------------|-----------|-----------|
| 9011             | 101       | 2         |
| 9012             | 102       | 1         |

Tabel: `bodem`

| bodemcode | beschrijving |
|-----------|--------------|
| 1         | dun          |
| 2         | dik          |

Je ziet dat de bestelde pizza met besteldePizzaCode 9011 een bodemcode van 2 heeft, dus een dikke bodem. Als we nu deze gegevens samen in 1 overzicht willen, dan moet je in de <code>FROM</code> alle tabellen gegeven is waar de gegevens uitkomen. In de <code>WHERE</code> geeft je aan welke twee kolommen aan elkaar gekoppeld zijn.
In dit geval verwijst kolom `bodemcode` van tabel `besteldePizzaCode` naar kolom  `bodemcode` van tabel `bodem`. Dat doe je zo: <code>WHERE besteldePizza.bodemcode = bodem.bodemcode</code>. 

Met de volgende code krijg je dus een overzicht van de beschrijving die bij de bestelde pizza hoort:


SELECT besteldePizzaCode, omschrijving
FROM besteldePizza, bodem
WHERE besteldePizza.bodemcode = bodem.bodemcode;


Uitvoer:

| besteldePizzaCode | omschrijving   |
|-------------------|----------------|
| 1                 | American style |
| 2                 | American style |
| 3                 | American style |
| 4                 | American style |
| 5                 | American style |

    
    
Als je een kolom wilt zien die in twee tabellen voorkomt, dan moet je in de SELECT aangeven uit welk tabel de gegevens moeten komen. Dat doe je door de tabelnaam aan te geven, dan een '.' en dan de kolomnaan.

In het voorbeeld hieronder willen we bodemcode zien.  Met `bodem.bodemcode` geven we aan dat `bodemcode' uit tabel `bodem` komt:   


SELECT besteldePizza.besteldePizzaCode, bodem.bodemcode, bodem.omschrijving
FROM besteldePizza, bodem
WHERE besteldePizza.bodemcode = bodem.bodemcode;


Uitvoer:

| besteldePizzaCode | bodemcode | omschrijving   |
|-------------------|-----------|----------------|
| 1                 | 2         | American style |
| 2                 | 2         | American style |
| 3                 | 2         | American style |
| 4                 | 2         | American style |
| 5                 | 2         | American style |




N.B.: Omdat `bodemcode' ook een kolom in `besteldePizza' is, had je ook `besteldePizza.bodemcode` kunnen gebruiken.



### Opdracht: maak een overzicht van de bestelde pizza en het formaat

### Opdracht: maak eene overzicht voor de besteldePizza en datum en bezorg tijd



# TODO 3 tabellen:

### Opdracht: naam van de bezorger en bijbehorende de klantgegevens: naam adres, postcode, plaats,


### Opdracht: overzicht van alle bestellingen: pizzanaam, formaat, bodem


#TODO -	FUNCTIES: min, max,sum,avg, count(*), distinct, wiskundige functies +,-,....


### Opdracht: Aantal pizza's in totaal besteld
Toon het aantal pizza's dat er in totaal zijn besteld.

ANTWOORD:

SELECT COUNT(*) 
FROM besteldepizza;

### Opdracht: Toon van alle bestellingen: pizzanaam, formaat, bodem + basisprijs +plusprijs formaat, plusprijs bodem, Totaal pijs

### Opdracht: Toon alle kortingen die bij een bestelling horen






## TODO DISTINCT
Toon een overzicht van alle plaatsnamen (<i>plaats</i>) waar klanten wonen. Toon elk plaats maar een keer.

SELECT DISTINCT(plaats)
FROM klant;


### Opdracht

Toon unieke combinaties van bodemcode en omschrijving.

ANTWOORD
SELECT DISTINCT bodemcode, omschrijving 
FROM besteldepizza;


#TODO UITLEG	GROUP BY

GROUP BY groepeert rijen die dezelfde waarde hebben in één of meer kolommen. Je kunt daarna functies zoals COUNT(), SUM(), AVG() of MAX() gebruiken op elke groep.

Bijvoorbeeld, met de code hieronder krijg je een overzicht van hoe vaak elke bodemcode is besteld:

SELECT bodemcode, COUNT(*) as aantal_besteld
FROM besteldepizza
GROUP BY bodemcode;

| bodemcode | aantal_besteld |
|-----------|----------------|
| 1         | 2788           |
| 2         | 2905           |
| 3         | 140            |


## Volgorde van keywords

De volgorde van de keywords is altijd:

SELECT ...
FROM ...
WHERE ...
GROUP BY ...
HAVING ...
ORDER BY ... DESC/ASC
LIMIT ... ;





# VRAGEN GROUP BY


### Opdracht
Toon hoeveel pizza’s er zijn besteld per omschrijving.



| bodemcode | omschrijving   | aantal |
| --------- | -------------- | ------ |
| 2         | American style | 3      |
| 3         | Italian style  | 2      |


ANTWOORD: SELECT omschrijving, COUNT(*) AS aantal
FROM besteldepizza
GROUP BY omschrijving;

### Opdracht:
Tel het aantal bestellingen per bodemcode.


| bodemcode | aantal_besteld |
|-----------|----------------|
| 1         | 2788           |
| 2         | 2905           |
| 3         | 140            |


ANTWOORD:

SELECT bodemcode, COUNT(*) 
FROM besteldepizza 
GROUP BY bodemcode;




### Opdracht:
Welk bodem komt het vaakst voor bij pizza’s met de omschrijving 'American style'? Toon de bodemcode, omschrijving en het aantal keer dat die besteld is.

| bodemcode | omschrijving   | aantal_besteld |
|-----------|----------------|----------------|
| 2         | American style | 3              |


ANTWOORD:

SELECT bodemcode, omschrijving, COUNT(*) AS aantal_besteld
FROM besteldepizza
WHERE omschrijving = 'American style'
GROUP BY bodemcode, omschrijving
ORDER BY aantal_besteld DESC
LIMIT 1;



#TODO UITLEG GROUP BY HAVING

Om maar bepaalde gegevens te tonen *nadat* je een GROUP BY gebruikt, kun je gebruik maken van HAVING. Deze werkt op waarden zoals COUNT(*), AVG(), SUM()...

Bijvoorbeeld, de volgende query toont alleen bodems die meer dan 1 keer zijn besteld. HAVING filtert op het aantal per groep.

SELECT bodemcode, COUNT(*) as aantal_besteld_per_bodem
FROM besteldepizza
GROUP BY bodemcode
HAVING COUNT(*) > 1;

| bodemcode | aantal_besteld_per_bodem |
|-----------|---------------------------|
| 1         | 2788                      |
| 2         | 2905                      |



#VRAGEN GROUP BY HAVING


### Opdracht
Toon alleen combinaties van bodemcode en omschrijving die meer dan 2 keer voorkomen.

| bodemcode | omschrijving   | aantal |
| --------- | -------------- | ------ |
| 2         | American style | 3      |



SELECT bodemcode, omschrijving, COUNT(*) AS aantal
FROM besteldepizza
GROUP BY bodemcode, omschrijving
HAVING COUNT(*) > 2;



#Verschil tussen WHERE en HAVING
Er is een verschil tssen WHERE en HAVING:
<ul>
<li>WHERE werkt op individuele rijen.
<li>HAVING werkt op een groep gegevens, dus *na* een GROUP BY.
</ul>

### Opdracht: verschil tussen WHERE en HAVING

<ol type="a">
<li>Schrijf een query met WHERE die alleen bestellingen met omschrijving 'American style' toont.

<li>Schrijf een query met GROUP BY en HAVING die alleen bodems toont die meer dan 1 keer zijn besteld.

<li>Vergelijk de resultaten en leg in je eigen woorden uit wat het verschil is.
</ol>

ANTWOORD:
<ol type="a">
<li>WHERE-filter op rij-niveau:<br>
SELECT * FROM besteldepizza
WHERE omschrijving = 'American style';

<li>HAVING-filter op groep-niveau<br>
SELECT bodemcode, COUNT(*) AS aantal
FROM besteldepizza
GROUP BY bodemcode
HAVING COUNT(*) > 1;

<li>Her verschil tussen WHERE en HAVING:
<ul>"
<li>HERE gebruik je als je rijen wilt uitsluiten voordat je gaat tellen of groeperen.
<li>HAVING gebruik je als je groepen wilt filteren nadat je hebt geteld of iets hebt samengevat.
</ul>
</ol>

### Opdracht:


Wat is de meest bestelde pizzabodem met de omschrijving 'American style', als die vaker dan één keer is besteld?"

ANTWOORD:
SELECT bodemcode, omschrijving, COUNT(*) AS aantal_besteld
FROM besteldepizza
WHERE omschrijving = 'American style'
GROUP BY bodemcode, omschrijving
HAVING COUNT(*) > 1
ORDER BY aantal_besteld DESC
LIMIT 1;




### AFLSUITENDE OPDRACHT
Schrijf een query die de meest bestelde pizzabodem toont.

ANTWOORD:
SELECT bodemcode, COUNT(*)
FROM besteldepizza
GROUP BY bodemcode
ORDER BY aantal_besteld DESC
LIMIT 1;


### AFSLUITENDE OPDRACHT
Schrijf een query om een nieuwe bestelling toe te voegen met besteldePizzaCode = 6, bodemcode 2, omschrijving 'American style'.


ANTWOORD:
INSERT INTO besteldepizza (besteldePizzaCode, bodemcode, omschrijving)
VALUES (6, 2, 'American style');

### AFSLUITENDE OPDRACHT
Stel dat er een andere tabel is met `pizzabodemprijzen`. 


Voeg die tabel toe en schrijf een query die de totale prijs per bestelling toont.
CREATE TABLE bodem (
    bodemcode INTEGER PRIMARY KEY,
    prijs REAL
);







