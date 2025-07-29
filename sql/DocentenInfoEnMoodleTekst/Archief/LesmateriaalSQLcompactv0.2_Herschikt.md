###SQL Basthon

<h4>ALGEMENE INLEIDING</h4>

<div class="activity-item time-block">
    <div class="fa fa-clock-o fa-3x"><br></div>
    <br>XX uur
</div>

<p><span lang="nl">Dit domein gaat over gestructureerde data, oftewel
databases…</p>

<p>Databases zijn overal. Wist je dat bijna alle grote bedrijven intensief 
gebruikmaken van databases om informatie op te slaan? Spotify gebruikt 
databases om dagelijks nieuwe *Daily Mixes* samen te stellen op basis van 
jouw favoriete muziek. Google houdt in databases bij waar jij vaak naar 
zoekt, zodat zoeken sneller en relevanter wordt. Ook veel reclames en 
advertenties worden gepersonaliseerd op basis van gegevens die worden 
opgeslagen terwijl jij je computer of telefoon gebruikt.</p> 


<p>Al deze 
bedrijven, programma’s en apps maken gebruik van zogeheten databases — en 
daar ga je in deze cursus meer over leren. Een veelgebruikte soort is de 
relationele database: een database die bestaat uit meerdere tabellen die met 
elkaar in verband staan. Dat betekent dat gegevens uit de ene tabel gekoppeld 
zijn aan gegevens in een andere tabel. Deze databases worden beheerd door een 
databasebeheersysteem (*Database Management System*, of DBMS). Zo’n systeem 
zorgt ervoor dat de data betrouwbaar en correct blijft, en dat wij op een 
eenvoudige manier informatie kunnen opvragen wanneer we die nodig hebben.</p> 


<p>Zo’n verzoek noem je een <b>query</b> en daarvoor heb je een speciale vraagtaal
nodig: <b>SQL</b>. Dat staat voor <i>Structured Query Language</i>. Dat is de standaardtaal om met databases te werken.
In deze onderwerp gebruik je <b>SQLite</b> — een eenvoudige, lichtgewicht database — om SQL te leren.
In de komende weken leer je hoe je met SQL data uit een SQLite-database opvraagt, opslaat en zelfs hoe je zelf tabellen aanmaakt.</p>

TODO Toelichting: inhoud van het lesmateriaal is deels overgenomen uit het Co-Teach lesmateriaal ontwikkeld door...



###Overzicht Hoofdstuk 1: Je eerste query
 <div class="activity-item time-block">
    <div class="fa fa-clock-o fa-3x"><br></div>
    <br>XX uur
</div>


<p>We beginnen met het verkennen van databases. Wat zijn het, waar kom je ze 
tegen, hoe zijn ze opgebouwd en hoe kun je er nuttige informatie uit halen? 
In deze onderwerp werk je met een database van Pizzeria Danilo.</p>

<p>Elke keer als je Informatica-Actief opnieuw opstart, wordt de 
oorspronkelijke database hersteld. Je hoeft dus niet bang te zijn om iets 
fout te doen — experimenteren mag!</p> 

[IMG: H1_overzicht.png]

<img src="https://raw.githubusercontent.com/rweeda/PythonIA/main/sql/img/H1_overzicht.png" width="100">



<p>Leerdoelen</p>

In dit onderwerp:
<ul> 
<li>Je hebt kennis van de volgende begrippen: query, data(base) en SQL.</li>
<li> TODO: CREATE, UPDATE, DELETE
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

<img src="https://raw.githubusercontent.com/rweeda/PythonIA/main/sql/img/H1_1_pizzabezorger.png" alt="afbeelding van een bezorger" width="300">


<p>Maar wat is een database? En hoe ziet zoiets eruit? Danilo moet veel 
<b>gegevens</b> bijhouden. Zoals bijvoorbeeld, de naam van de pizza's, de 
prijs en de ingredienten. Maar ook de namen en adressen van klanten en 
gegevens over bestellingen en bezorgers. </p> 


<p>Die gegevens worden bewaard in tabellen. En tabellen bestaan weer uit 
rijen en kolommen met gegevens die opgeslagen worden. Die gegevens noemen we 
<b>data</b>. Gestructureerde data is informatie die op een vaste, 
georganiseerde manier is opgeslagen, zodat computers die makkelijk kunnen 
lezen, begrijpen en verwerken.</p>


## Ontwerp van een tabel: kolommen kiezen

Stel dat jij bij Danilo's Pizzeria wilt bestellen. Om de contactgegevens op 
te slaan in een database moet je het webformulier hieronder invullen. 

Bekijk het webformulier goed.



<p><img src="https://raw.githubusercontent.com/rweeda/PythonIA/main/sql/img/H1_webform.png" alt="webformulier" width="600"></p>


We maken een tabel waarin we de contactgegevens opslaan. Zo kunnen we 
makkelijk de gegevens van klanten terugvinden als ze een bestelling plaatsen. 
<ol style="list-style-type: lower-alpha"> 

<li>Welke gegevens worden verzameld? Noem alle velden.

<li>Wat betekent het sterretje, bijvoorbeeld 
achter 'Voornaam'? 

<li>Wat gebeurt er als er twee verschillende mensen zijn 
met dezelfde voornaam en achternaam waarvan je het adres wilt opzoeken? Wat voor oplossing 
hebben we op school hiervoor? 

<li>Bedenk een oplossing voor Danilo's pizzeria 
voor het eenduidig opslaan van klantgegevens. 

<li>Hieronder staat een tabel om de gegevens op te slaan. Geef de kolommen namen (bij 'A' t/m 'H'). Geef de tabel ook een naam.

</ol>
|   A   |   B   |   C   |   D   |   E   |   F   |   G   |   H   |
|-------|-------|-------|-------|-------|-------|-------|-------|
|       |       |       |       |       |       |       |       |


ANTWOORDEN: <ol style="list-style-type: lower-alpha"> 

<li>Deze gegevens worden verzameld: voornaam, tussenvoegsel, achternaam, adres, postcode, plaats en telefoon.
      
<li>Dat is een veld dat verplicht ingevuld moet worden.</li> 

<li>Als 
twee klanten dezelfde naam hebben kun je ze niet uit elkaar halen, je kunt 
dan niet hun juiste adres opzoeken. Als oplossing gebruiken we een unieke 
waarde waarvan er maar één is, zoals een leerlingnummer op school, of een 
BSN. 

<li>Voor Danilo's pizzeria zou een unieke nummer een klantnummer kunnen 
zijn. 

<li>Zie hieronder <li>tabelnaam: klanten 

</ol>


TABEL: klanten
<table>
  <thead>
    <tr>
      <th>klantnummer</th>
      <th>voornaam</th>
      <th>tussenvoegsel</th>
      <th>achternaam</th>
      <th>adres</th>
      <th>postcode</th>
      <th>plaats</th>
      <th>telefoon/th>
    </tr>
  </thead>
</table>



## UITLEG Verschillende soorten data
Met een database sla je gestructureerde data op. Daarvoor moet je voor iedere kolom aangeven wat voor soort gegevens je wilt opslaan, oftewel het <b>datatype</b>. 

In SQLite zijn er drie datatypen: 
<ul>
<li><b>INTEGER</b>: een geheel getal. Bijvoorbeeld: 4
<li><b>TEXT</b>: een stuk tekst. Bijvoorbeeld: 'Jaap'
<li><b>REAL</b>: een kommagetal. Bijvoorbeeld: 2.50
</ul>



### Alle gegevens van een tabel ophalen

<p>Om alle kolommen met gegevens van een tabel op te halen, gebruik je de volgende query:</p>
 
<code>SELECT * 
FROM tabelnaam;</code>



### Eén kolom uit een tabel halen

Je kunt ook maar één kolom ophalen. Dat doe je als volgt:
 
SELECT kolomnaam
FROM tabelnaam;


Bijvoorbeeld:
SELECT naam 
FROM pizza;

Daarmee krijg je de volgende overzicht:

| naam                    |
|-------------------------|
| Margherita              |
| Napoletana              |
| Prosciutto              |
| Funghi                  |
| Salame                  |
| ...                     |
| Combinazione            |





### Sommige kolommen uit een tabel halen
Je kunt ook een beperkt aantal kolommen ophalen. Dat doe je als volgt:
 
SELECT kolom1, kolom2, ...
FROM tabelnaam;



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





### AND (EN)
Met *AND* moet aan alle voorwaarden worden voldaan om een resultaat te krijgen. 

Bijvoorbeeld, met de volgende query tonen we alle klanten die in Enschede wonen en een naam hebben die met 'H' begint:


SELECT *
FROM klant
WHERE plaats = 'Enschede' AND naam LIKE 'H%';

| klantnummer | wachtwoord     | naam                  | adres                | postcode | plaats    | telefoon     |
|-------------|----------------|------------------------|----------------------|----------|-----------|--------------|
| 101         | uqOpgECQ_      | Hanneke Bolier         | Gladioolstraat 11    | 3742TC   | Enschede  | 06-169X5427  |
| 209         | m1nbsrweOFJxu5 | Hermina de Pater       | Koekoeksbloemlaan 40 | 3742EK   | Enschede  | 06-6255X908  |
| 221         | Qe4W6Xf70D_YlHR| Heleen  van Harberden  | Acacialaan 27        | 3741WB   | Enschede  | 035-85X3955  |
| 401         | dJiorsEkNLE    | Henrike Teeuw          | Dahliastraat 17      | 3742RK   | Enschede  | 035-8X94605  |





### OR (OF)

Met *OR* moet aan één van de voorwaarden voldaan worden.

Bijvoorbeeld, de volgende query toont alle pizza's die met 'M' beginnen OF een basisprijs onder de 7euro hebben:

SELECT naam, basisprijs
FROM pizza
WHERE naam LIKE 'M%' OR basisprijs < 7;



| naam       | basisprijs |
| ---------- | ---------- |
| Margherita | 6.0        |
| Cippola    | 6.5        |
| Marinara   | 8.5        |
| Mozzarella | 8.5        |









### NOT
Met `NOT` mag er aan géén van de voorwaarden voldaan worden.

Bijvoorbeeld, alle klanten die *niet* in Hengelo wonen:

SELECT *
FROM klanten
WHERE NOT plaats = 'Hengelo'


Bijvoorbeeld, alle pizza's waarbij de letter 'e' er <b>niet</b> in voorkomt:

SELECT naam
FROM pizza
WHERE naam NOT LIKE '%e%';






### Tabel: `besteldepizza`

| besteldepizzacode | pizzacode |
|-------------------|-----------|
| 1                 | 101       |
| 2                 | 102       |
| 3                 | 103       |
|-------------------|-----------|

De namen van de pizza’s staan in een andere tabel: `pizza`.




### Tabel: `pizza`

| pizzacode | naam               |
|-----------|--------------------|
| 101       | Margherita         |
| 102       | Quattro Formaggi   |
| 103       | Salami             |
|-----------|--------------------|

Als je wilt weten **welke pizza’s** er precies besteld zijn, moet je gegevens **uit beide tabellen combineren**.



Zoals je ziet:
- `besteldepizza` weet wél dat pizzacode 101 besteld is,  
- maar **alleen** `pizza` weet dat dit de *Margherita* is.

---

## Wat doet een JOIN?

Met een JOIN **koppel je de rijen van twee tabellen aan elkaar**, op basis van een overeenkomstige waarde. In dit geval: `pizzacode`.

```sql
SELECT besteldepizza.besteldepizzacode, pizza.naam
FROM besteldepizza
JOIN pizza ON besteldepizza.pizzacode = pizza.pizzacode;
```

De uitvoer van deze query is:
| besteldepizzacode | naam             |
| ----------------- | ---------------- |
| 1                 | Margherita       |
| 2                 | Quattro Formaggi |
| 3                 | Salami           |
| ----------------- | ---------------- |






### SAMENVATTING JOIN
JOIN is nodig om betekenisvolle combinaties van data uit verschillende tabellen te maken.



#TODO -	FUNCTIES: min, max,sum,avg, count(*), distinct, wiskundige functies +,-,....

# SQL Functies

In deze onderwerp leer je hoe je met SQL berekeningen en samenvattingen kunt maken uit je database.  
We behandelen de volgende functies:

- `MIN()`
- `MAX()`
- `SUM()`
- `AVG()`
- `COUNT(*)`
- `DISTINCT`
- Rekenen met `+`, `-`, `*`, `/`

---

## 1. `MIN()` – Minimumwaarde



### Uitleg
`MIN(kolom)` geeft de **laagste waarde** in een kolom terug.  
Bijvoorbeeld: de goedkoopste pizza.



### Voorbeeldquery
```sql
SELECT MIN(basisprijs) AS goedkoopste_pizza
FROM pizza;
```



### Voorbeeld uitvoer

| goedkoopste_pizza |
|-------------------|
| 6.50              |



### Uitleg
`MAX(kolom)` geeft de **hoogste waarde** in een kolom terug.  
Bijvoorbeeld: de duurste pizza.



### Voorbeeldquery
```sql
SELECT MAX(basisprijs) AS duurste_pizza
FROM pizza;
```



### Voorbeeld uitvoer

| duurste_pizza |
|----------------|
| 10.00          |



### Uitleg
`SUM(kolom)` telt **alle waarden in een kolom op**.  
Bijvoorbeeld: de totale waarde van alle pizza’s samen.



### Voorbeeldquery
```sql
SELECT SUM(basisprijs) AS totaal_waarde
FROM pizza;
```



### Voorbeeld uitvoer

| totaal_waarde |
|---------------|
| 98.50         |



### Uitleg
`AVG(kolom)` geeft het **gemiddelde** van de waarden in een kolom.  
Bijvoorbeeld: de gemiddelde prijs van een pizza.



### Voorbeeldquery
```sql
SELECT AVG(basisprijs) AS gemiddelde_pizza_prijs
FROM pizza;
```



### Voorbeeld uitvoer

| gemiddelde_pizza_prijs |
|-------------------------|
| 8.21                    |



### Uitleg
`COUNT(*)` telt **het aantal rijen** in een tabel.  
Wil je alleen unieke waarden tellen? Dan gebruik je `COUNT(DISTINCT kolom)`.



### Voorbeeldquery
```sql
SELECT COUNT(*) AS aantal_pizza’s
FROM pizza;
```



### Voorbeeld uitvoer

| aantal_pizza’s |
|----------------|
| 12             |



###  Voorbeeldquery
```sql
SELECT DISTINCT plaats
FROM klant;
```

| plaats     |
|------------|
| Enschede   |
| Hengelo    |




###  Uitleg
Je kunt met SQL rekenen in je SELECT-statement.  



| Symbool | Betekenis             | Voorbeeld                         | Uitleg                                |
|---------|------------------------|-----------------------------------|----------------------------------------|
| `+`     | Optellen               | `basisprijs + 1.00`               | Tel 1 euro bij de basisprijs op        |
| `-`     | Aftrekken              | `basisprijs - 0.50`               | Trek 50 cent van de basisprijs af      |
| `*`     | Vermenigvuldigen       | `basisprijs * 2`                  | Verdubbel de prijs                     |
| `/`     | Delen                  | `basisprijs / 2`                  | Deel de prijs door twee                |




Bijvoorbeeld: basisprijs + toeslagen voor formaat en bodem.



### Voorbeeldquery
```sql
SELECT naam, basisprijs + 1.00 AS totaalprijs
FROM pizza;
```



### Voorbeeld uitvoer

| naam        | totaalprijs |
|-------------|-------------|
| Margherita  | 7.50        |
| Salami      | 8.90        |



### ANTWOORD:
<ol type="alpha">
<li>
```sql
SELECT besteldepizza.bestelcode, pizza.naam AS pizzanaam, bodem.omschrijving AS bodembeschrijving
FROM besteldepizza
JOIN pizza ON besteldepizza.pizzacode = pizza.pizzacode
JOIN bodem ON besteldepizza.bodemcode = bodem.bodemcode;
```
</li>
<li>
Je kunt dit niet doen zonder JOIN, omdat de informatie die je nodig hebt verspreid is over meerdere tabellen.<br>
In de tabel <code>besteldepizza</code> staat de <code>pizzacode</code> en de <code>bodemcode</code>,
maar de naam van de pizza staat in de tabel <code>pizza</code>,
en de omschrijving van de bodem staat in de tabel <code>bodem</code>.
</li>
</ol>



</li>


# TODO 3 tabellen:



### Opdracht: ontwerp van een tabel: data types
Ga verder met het tabel uit de vorige opdracht. <br>Geef bij elke kolom 'A' t/m 'H' aan welk van de volgende type gegevens het bevat:
  <ul>
  <li>TEXT: een tekst
  <li>INTEGER: een geheel getal
  <li>REAL: een kommagetal
  </ul>
  
 
  
Omdat er maar drie datatypen zijn zul je sommige gegevens als een TEXT opslaan. Bijvoorbeeld, een datum sla je in de vorm jjjj-mm-dd (j: jaar, m: maand, d:dag) op als een tekst, bijvoorbeeld: "2025-04-20". Een telefoonnummer zul je ook als een tekst opslaan, omdat anders de voorloop nul wegvalt, bijvoorbeeld: "0688567389".


## UITLEG PRIMARY KEY
Elke tabel heeft een kolom hebben waarmee je records kan aanwijzen: een <b>primary key</b>. Deze kolom moet <b>unieke</b> gegevens hebben, een kolom waar nooit twee keer hetzelfde waarde voor mag komen.
Een voorbeeld is leerlingnummer. Er kunnen geen twee leerlingen dezelfde leerlingnummer hebben. Terwijl er misschien wel twee leerlingen met dezelfde naam zijn, bijvoorbeeld Tom Janssen. Met een leerlingnummer weet je zeker over wie je het hebt. Een andervoorbeeld is een gebruikersnaam in een spel, daar mag er maar één van zijn.

(<i>Toelichting: een primary key kan uit meerdere kolommen samen bestaan, maar dat behandelen we in deze cursus niet.</i>)



### OPDRACHT PRIMARY KEY

Welke van de volgende uitspraken over primary keys is correct?
A. Een primary key mag leeg zijn
B. Een primary key mag dubbel voorkomen
C. Een primary key identificeert elke rij uniek
D. Een primary key is altijd tekst

ANTWOORD:
Antwoord C is juist


## UITLEG Eisen stellen aan data
Naast dat data van een bepaald type is, kun je nog anderen eisen stellen aan waarden in een bepaald kolom, bijvoorbeeld:
<ul>
  <li>PRIMARY KEY: unieke waarde
  <li>NOT NULL: mag niet leeg zijn



### Opdracht: ontwerp van een tabel: Eisen aan data
Ga verder met het tabel uit de vorige opdracht. <br>

Geef bij elke kolom aan of er speciale eisen aan gesteld zijn:
  <ul>
  <li>PRIMARY KEY: een unieke waarde (in het Nederlands <i>primaire sleutel</i>)
  <li>NOT NULL: mag niet leeg zijn
  </ul>


ANTWOORD:
TABEL: klanten
<table>
  <thead>
    <tr>
      <th>klantnummer<br>INTEGER PRIMARY KEY NOT NULL</th>
      <th>voornaam<br>TEXT NOT NULL</th>
      <th>tussenvoegsel<br>TEXT</th>
      <th>achternaam<br>TEXT NOT NULL</th>
      <th>adres<br>TEXT NOT NULL</th>
      <th>postcode<br>TEXT NOT NULL</th>
      <th>plaats<br>TEXT NOT NULL</th>
      <th>telefoon<br>TEXT NOT NULL</th>
    </tr>
  </thead>
</table>




## Terugblik

Bij het maken van de vorige opdracht heb je veel geleerd over gestructureerde data. We vatten dat nu samen.

<ul>
<li><b>Database</b>: Een georganiseerde verzameling gegevens, opgeslagen in tabellen met rijen en kolommen.
<li>SQL (Structured Query Language): De standaardtaal om gegevens in een database op te slaan, te bewerken en op te halen. In deze cursus gebruiken we <b>SQLite</b>: Een eenvoudige, lichtgewicht databasei
<li><b>Datatypes</b> in SQLite:  INTEGER - Gehele getallen (bijv. 4), TEXT - Tekstuele gegevens (bijv. 'Jaap') en REAL - Kommagetallen (bijv. 2.50)
<li><b>Primary Key</b>: Een kolom die elke rij uniek identificeert; moet uniek en niet leeg zijn.
</ul>




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
gepersonaliseerde ervaring aan te kunnen bieden. Denk hierbij aan hoe lang je naar een video kijkt, naar 
welke video’s je zoekt of op welke video’s die aangeraden worden jij ook echt doorklikt. Ook moet er 
veel informatie over de video’s zelf opgeslagen worden zoals de titel, de thema’s, de lengte, etc. Je 
kunt je voorstellen dat via het internet zo een enorme hoeveelheid data verzameld wordt.</p>


<p>Jouw school maakt ook gebruik van databases. Gebruikt je school Magister of Somtoday? Deze 
programma's slaan informatie over jou als leerling op in een database. Hiermee kan je docent 
huiswerk opgeven en toetscijfers inzien en invoeren, kan de schoolleiding zien hoe het met 
verschillende klassen gaat en kan jij zien hoe je er voor staat met al je vakken of opdrachten 
inleveren.</p>

###Databasemanagementsysteem (DBMS) <p>Een database kan al snel heel groot 
worden. Er wordt niet alleen data in opgeslagen, maar ook data gewijzigd of 
verwijderd. Een andere belangrijke functie is het opvragen en combineren van 
gegevens. Bovendien heeft niet iedereen dezelfde toegang: als leerling kun je 
alleen je eigen gegevens zien, terwijl een docent bijvoorbeeld de cijfers van 
alle leerlingen kan bekijken, aanpassen of toevoegen.</p> <p>Al deze 
bedrijven, programma’s en apps maken gebruik van zogeheten databases. Een 
veelgebruikte soort is de relationele database: een database die bestaat uit 
meerdere tabellen die met elkaar in verband staan. Dat betekent dat gegevens 
uit de ene tabel gekoppeld zijn aan gegevens in een andere tabel. Deze 
databases worden beheerd door een databasebeheersysteem (*Database Management 
System*, of DBMS). 


[IMG]


<p>Zo’n systeem zorgt ervoor dat de data betrouwbaar en 
correct blijft, en dat wij op een eenvoudige manier informatie kunnen 
opvragen wanneer we die nodig hebben.</p> </p>








### Opdracht 1.1:  Wat zijn databases?

<p>Waarschijnlijk heb je al eerder gebruik gemaakt van een database, misschien zonder dat je dat wist. Laten we eens op
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
  <li>Magister of SOMtoday</li>
</li>
<li>
  <li>Bij webwinkel: productenlijst</li>
  <li>Bij social media platform: posts</li>
  <li>Bij school database: gegevens over leerlingen zoals adres, cijfers en rooster</li>
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


## SQL 

<p>SQL staat voor <i>Structured Query Language</i>. Het is de 
standaardtaal om data in een database op te slaan, te bewerken en op te 
halen. Zo’n verzoek aan de database noem je een <b>query</b>, wat letterlijk 
‘vraag’ betekent in het Engels. Als je een query schrijft, stel je dus 
eigenlijk een vraag aan de database. Bijvoorbeeld: “Welke klanten wonen in 
Amsterdam?”</p>

<p>In deze cursus leer je hoe je SQL gebruikt binnen 
<b>SQLite</b> — een eenvoudige, lichtgewicht databasesysteem. We beginnen met 
leren hoe je informatie kunt ophalen. Daarna leer je ook hoe je gegevens kunt 
opslaan, aanpassen en verwijderen. Tot slot ga je zelfs je eigen tabellen 
aanmaken.</p> 





## 1.2: Gegevens ophalen

De taal voor het ophalen van informatie bestaat uit slechts 6 commando’s waarmee je 
leert werken. De commando’s zijn:


<p><img src="https://raw.githubusercontent.com/rweeda/PythonIA/main/sql/img/H1_commandos.png]" alt="Commando's voor het ophalen van informatie" width="600"></p>


Je hoeft niet alle commando's te gebruiken, maar ze staan welk altijd in deze volgorde.

<p>Met een query kun je gegevens uit een tabel ophalen. Met SELECT kun je data selecteren van een database en in een overzicht tonen. 
Met FROM geef je aan uit welke tabel de informatie gehaald moet worden.</p>




<p>Bij de volgende opgaven maken we gebruik van de tabel <i>pizza</i> uit Danilo's pizzeria. De afbeelding hieronder toont de kolommen van tabel <i>pizza</i>:

<p><img src="https://raw.githubusercontent.com/rweeda/PythonIA/main/sql/img/ERD_pizza.png]" alt="Tabel pizza" width="600"></p>


Hieronder zie je hoe de tabel <i>pizza</i> er uitziet met de gegevens van een aantal pizza's erin.


<p><img src="https://raw.githubusercontent.com/rweeda/PythonIA/main/sql/img/H1_tabel_pizza.png]" alt="Tabel pizza" width="600"></p>


| pizzacode | naam                  | omschrijving                                                             | basisprijs |
|-----------|-----------------------|---------------------------------------------------------------------------|------------|
| 1         | Margherita            | Tomaat,kaas en oregano                                                    | 6.0        |
| 2         | Napoletana            | Tomaat, kaas, ansjovis, olijven, kappertjes en oregano                   | 7.5        |
| 3         | Prosciutto            | Tomaat, kaas, ham en oregano                                              | 7.5        |
| 4         | Funghi                | Tomaat, kaas, champignons en oregano                                     | 7.5        |
| ...       | ...                   | ...                                                                       | ...        |
| 36        | Combinazione          | Eigen keuze pizza                                                        | 10.5       |






### Opdracht 1.3: Alle gegevens van tabel pizza ophalen

Toon alle kolommen met gegevens van tabel <i>pizza</i>, zoals in het voorbeeld hieronder: 

| pizzacode | naam                  | omschrijving                                                             | basisprijs |
|-----------|-----------------------|---------------------------------------------------------------------------|------------|
| 1         | Margherita            | Tomaat,kaas en oregano                                                    | 6.0        |
| 2         | Napoletana            | Tomaat, kaas, ansjovis, olijven, kappertjes en oregano                   | 7.5        |
| 3         | Prosciutto            | Tomaat, kaas, ham en oregano                                              | 7.5        |
| 4         | Funghi                | Tomaat, kaas, champignons en oregano                                     | 7.5        |
| ...       | ...                   | ...                                                                       | ...        |
| 36        | Combinazione          | Eigen keuze pizza                                                        | 10.5       |


<!-- ANTWOORD:
SELECT *
FROM pizza
-->



### Opdracht 1.4: Pizzacodes
<ol style="list-style-type: lower-alpha">
<li>Toon alle pizzacodes (kolom <i>pizzacode</i>) in tabel <i>pizza</i>.
<li>Wat zie je als je naar de pizzacodes kijkt? Leg uit wat dat te maken heeft met de 'primary key'.
</ol>

| pizzacode |
|-----------|
| 1         |
| 2         |
| 3         |
| 4         |
| ...       |
| 36        |




<ol style="list-style-type: lower-alpha">
<li>
<!-- SELECT pizzacode 
FROM pizza;
-->
<li>Elke pizzacode komt maar één keer voor. Dat betekent dat elke pizza een unieke code heeft. Zo’n unieke code noemen we een primary key. Een primary key zorgt ervoor dat je elk record in een tabel kunt herkennen. In dit geval herken je elke pizza aan zijn pizzacode.
</ol>




### Opdracht 1.4: Menu printen

Maak een menu door de pizzanamen (kolom <i>naam</i>), <i>omschrijving</i> en de prijs (kolom <i>basisprijs</i> uit het tabel <i>pizza</i> te halen.


| naam                   | omschrijving                                                             | basisprijs |
|------------------------|----------------------------------------------------------------------------|------------|
| Margherita             | Tomaat,kaas en oregano                                                    | 6.0        |
| Napoletana             | Tomaat, kaas, ansjovis, olijven, kappertjes en oregano                   | 7.5        |
| Prosciutto             | Tomaat, kaas, ham en oregano                                              | 7.5        |
| Funghi                 | Tomaat, kaas, champignons en oregano                                     | 7.5        |
| ...                    | ...                                                                      | ...        |
| Combinazione           | Eigen keuze pizza                                                        | 10.5       |


<!-- ANTWOORD:
SELECT naam, omschrijving, basisprijs 
FROM pizza;
-->


## Voorwaarden met de WHERE

Met WHERE kun je beperken welke rijen getoond moet worden. Met WHERE kun je een voorwaarde aangeven, bijvoorbeeld: ’waarbij de informatie voldoet aan ...’</p>

<p>Je geeft altijd eerst een SELECT op voor de gegevens die opgehaald moeten worden, dan met FROM de tabel waaruit de gegevens moeten komen, en met WHERE welke beperking er is.</p>


Bijvoorbeeld, met de volgende query tonen we alle pizza's die precies 8 euro kosten:
SELECT *
FROM pizza
WHERE basisprijs=8

| pizzacode | naam           | omschrijving                                                             | basisprijs |
|-----------|----------------|----------------------------------------------------------------------------|------------|
| 10        | Capricciosa    | Tomaat, kaas, ham, champignons, paprika, artisjokken en oregano          | 8.0        |
| 11        | Primavera      | Tomaat, kaas, ham, salami en oregano                                     | 8.0        |
| 12        | Venezia        | Tomaat, kaas, ham, champignons, ananas en oregano                        | 8.0        |
| ...       | ...            | ...                                                                      | 8.0        |
| 30        | Romana         | Tomaat, kaas, spek, uien, champignons, ei en oregano                     | 8.0        |






### Opdracht: Omschrijving van een Inferno pizza
Schrijf een query om de omschrijving van de pizza 'Inferno' te tonen, zoals in het voorbeeld hieronder.

| omschrijving |
|--------------|
| Tomaat, kaas, ham, spaanse peper, kappertjes, salami, olijven en oregano  |



ANTWOORD:
SELECT omschrijving
FROM pizza
WHERE naam='Inferno'




## Kennis maken met de andere tabellen


Danilo's pizzeria database bestaat uit meer tabellen dan alleen pizza's. Er wordt ook bijvoorbeeld ook informatie opgeslagen over klanten, berzorgers en bestellingen. In de afbeelding hieronder zie je alle 7 tabellen.


<p><img src="https://raw.githubusercontent.com/rweeda/PythonIA/main/sql/img/DaniloIA_ERD.png]" alt="Alle tabellen" width="1000"></p>




### Opdracht: Alle klanten uit Enschede


Toon het adres, de postcode en de plaats van alle klanten die in Enschede wonen, zoals hieronder.
| Adres              | Postcode | Plaats    |
|--------------------|----------|-----------|
| Gladioolstraat 11  | 3742TC   | Enschede  |
| Banckertlaan 7     | 3742MG   | Enschede  |
| Talmalaan 11       | 3741TX   | Enschede  |
| Krugerlaan 9       | 3743CJ   | Enschede  |
| Zandvoortweg 199   | 3741BE   | Enschede  |




ANTWOORD:

SELECT adres, postcode, plaats
FROM klant
WHERE plaats='Enschede';




### Opdracht: Wachtwoord uit tabel bezorger.
Toon het wachtwoord van de bezorger met de naam Ronald Marbus, zoals hieronder.

| wachtwoord  |
|-------------|
| R0nalt      |



ANTWOORD
SELECT wachtwoord
FROM bezorger
WHERE naam = 'Ronald Marbus';




### Opdracht: Bestellingen met bestelcode
Toon alle informatie over zowel bestellingen bestelcode 13 en die met bestelcode 30, zoals hieronder.

| bestelcode | datum       | bestel_tijd | bezorg_tijd | bezorgernummer | klantnummer | korting |
| ---------- | ----------- | ----------- | ----------- | -------------- | ----------- | ------- |
| 13         | 2021-12-03  | 17:33:00    | 17:48:00    | 5              | 279         | 0.0     |
| 30         | 2021-12-05  | 17:55:00    | 18:11:00    | 8              | 376         | 0.0     |



ANTWOORD:
SELECT *
FROM bestelling
WHERE bestelcode = 13 OR bestelcode = 30;







## Wiskundige operatoren

Naast de '='-teken kun ook andere operatoren in de WHERE gebruiken. Hier is een overzicht:

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


Bijvoorbeeld, met de volgende query laten we de gegevens zien van klanten die <i>niet</i> in Enschede wonen:
```sql 
SELECT *
FROM klant
WHERE plaats <> 'Enschede';
```

| klantnummer | wachtwoord | naam             | adres                | postcode | plaats  | telefoon    |
|-------------|------------|------------------|----------------------|----------|---------|-------------|
| 107         | OjhTVw4PIT | Josette Soede    | Varenstraat 190      | 3765WR   | Hengelo | 06-56X49758 |
| 123         | XwNRl      | Miranda LeBlanche| Verlengde Talmalaan 9| 3762AA   | Hengelo | 035-1791X17 |
| 124         | TP_OicB    | Peter van Tol    | Kerkpad ZZ 49        | 3764AN   | Hengelo | 06-5X038039 |
| 156         | oeJqdsJ    | Jeroen Voskuil   | Smitsweg 519         | 3765CP   | Hengelo | 035-569X542 |
| ...         | ...        | ...              | ...                  | ...      | ...     | ...         |
| 463         | 3srxf41bnK | Jurgen Brug      | Heideweg 40          | 3768BC   | Hengelo | 035-4X02016






### Opdracht: Fout in query voor goedkope pizza's
Piet wil een overzicht van alle pizza's die minder dan 7 euro kosten. Wat is de fout in deze query? Los die op.
``` sql
SELECT naam basisprijs < 7.0 FROM WHERE pizza;
```

ANTWOORD:
SELECT naam 
FROM pizza
WHERE basispijs < 7.0;



### Opdracht: Dure pizza's
Toon de namen en prijzen van de pizza's die 9,50 euro kosten of meer, zoals in het overzicht hieronder.


| naam                  | basisprijs |
|-----------------------|-------------|
| Specialità di Danilo | 9.5         |
| Combinazione          | 10.5        |


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




## 1.3: Commentaar

Net als bij programmeren, kun je in SQL ook commentaar opnemen in je code. Dit doe je 
door twee streepjes ‘--’ ervoor te zetten. Dat ziet er dan zo uit (zie regel 2):</p>
SELECT * 
FROM pizza; -- dit is de tabelnaam


<!--
<p>Je kunt ook <code>/*</code> ervoor en <code>*/</code> erna zetten. Dat ziet er dan zo uit (zie regel 2):</p>
SELECT * 
FROM pizza; /* dit is de tabelnaam */
-->

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






### Opdracht: kolom 'naam' veranderen in 'bezorgernaam'
Toon een overzicht van alle namen van de bezorgers. Noem het kolom `bezorgernaam`.


ANTWOORD:

SELECT naam AS bezorgernaam
FROM bezorger;


## 1.4: Beperkt aantal rijen tonen
<p>Met LIMIT kun je bepalen hoeveel rijen er getoond moeten worden.</p>

<p>Met de volgende code toon je alleen de eerste vijf rijen:</p>

SELECT *
FROM pizza
LIMIT 5;




### Opdracht 1.6 Alleen de eerste drie pizza's
Toon de naam (<i>pizzanaam</i>) en prijs (<i>basisprijs</i>) van de eerste drie pizza's.


ANTWOORD:

SELECT pizzanaam, basisprijs
FROM pizza
LIMIT 3;






## WHERE met LIKE


<p>In de WHERE gebruik je een LIKE om te zoeken naar delen van 
teksten, of wanneer je iets ongeveer wilt zoeken. Met de joker geef je aan welke teken(s) anders mogen zijn. De procent 
teken <code>%</code> vervangt nul of meerdere tekens.

Let op:
- De LIKE gebruik je in de where
- De joker zet je in ter vervanging van nul of meerdere tekens
- Je moet bij de LIKE aanhalingstekens gebruiken


Bijvoorbeeld, om alle namen te die beginnen met ‘Jo’ (zoals Josette, Johan) gebruik je:

SELECT naam
FROM klant
WHERE naam LIKE 'J%';

| naam                      |
|---------------------------|
| Josette Soede             |
| Jolanda Budding-Doornbos  |
| Joanne Vlastuin           |
| Jolanda Knoop - Hoek      |
| Joost Nieuwboer           |
| Johan van Nierop          |






Bijvoorbeeld, met de volgende query tonen we de pizza's met een naam die <i>begint met</i> 'Quattro':

SELECT naam
FROM pizza
WHERE naam LIKE 'Quattro%';

Of die <i>eindigd op</i> 'arma':

SELECT naam
FROM pizza
WHERE naam LIKE '%arma';

Of waarbij de letter 'e' <i>erin voorkomt</i>:

SELECT naam
FROM pizza
WHERE naam LIKE '%e%';





### Opdracht: Alle pizza's waar de letter 'a' in voorkomt
Toon een overzicht van alle pizza's waar de letter 'a' in voorkomt:

SELECT naam
FROM pizza
WHERE naam LIKE '%a%';




### Opdracht: Alle klanten met een mobiele telefoonnummer.
Toon een overzicht van alle klanten die een 06-nummer hebben opgegeven.

SELECT *
FROM klant
WHERE telefoon LIKE '06%';




## Logische operatoren
Je kunt de WHERE voorwaarde ook uitbreiden met de logische operatoren AND, OR, NOT of combinaties daarvan. 




### OPDRACHT

Toon alle pizza's die tussen de €8,50 en €10,- kosten:

| naam                   | basisprijs |
|------------------------|-------------|
| Calzone (dichte pizza) | 9.0         |
| Marinara               | 8.5         |
| Mozzarella             | 8.5         |
| Quattro stragioni      | 8.5         |
| Americana              | 8.5         |
| Shoarma                | 9.0         |
| Pollo                  | 9.0         |
| Salmone                | 8.5         |
| Fantasia               | 9.0         |
| Parma                  | 8.5         |
| Pazza                  | 8.5         |
| Inferno                | 8.5         |
| Tropicana              | 8.5         |
| Della Casa             | 8.5         |
| Specialità di Danilo   | 9.5         |

Tip: de basisprijs is meer dan 8.50 en minder dan 10 euro.


ANTWOORD

SELECT naam, basisprijs
FROM pizza
WHERE basisprijs>=8.50 AND basisprijs<=10;






### Opdracht: Alle goedkope of gezonde pizza's
Maak een overzicht van alle pizza's goedkoper zijn dan €7,50 of fruit bevatten.

ANTWOORD:
SELECT *
FROM pizza
WHERE basisprijs<7.50 OR omschrijving LIKE '%fruit%';




### Opdracht: Alle pizza's zonder kip

Toon een overzicht van alle pizza's waar <b>geen</b> kip op zit, dus ook geen kipfilet, zoals in het voorbeeld hieronder.

| pizzanaam   | omschrijving                                                       |
|-------------|---------------------------------------------------------------------|
| Margherita  | Tomaat, kaas en oregano                                            |
| Napoletana  | Tomaat, kaas, ansjovis, olijven, kappertjes en oregano            |
| Prosciutto  | Tomaat, kaas, ham en oregano                                       |
| Funghi      | Tomaat, kaas, champignons en oregano                               |
| Salame      | Tomaat, kaas, salami en oregano                                    |




ANTWOORD: 
SELECT naam AS pizzanaam, omschrijving
FROM pizza
WHERE omschrijving NOT LIKE '%kip%';


ook goed:

ANTWOORD: 
SELECT naam, omschrijving
FROM pizza
WHERE NOT omschrijving LIKE '%kip%';






### Opdracht: Alle pizza's zonder paprika en zonder ui

Luna wil een overzicht van alle pizza's waar <b>geen</b> paprika op zit, maar ook geen <b>ui</b>. 
Ze schrijft daarvoor de volgende query, maar er zitten een paar fouten in. Kan jij het aanpassen zodat de juiste overzicht gegeven wordt, zoals hieronder?

Juiste overzicht:
| naam        | omschrijving                                                       |
|-------------|---------------------------------------------------------------------|
| Margherita  | Tomaat, kaas en oregano                                            |
| Napoletana  | Tomaat, kaas, ansjovis, olijven, kappertjes en oregano            |
| Prosciutto  | Tomaat, kaas, ham en oregano                                       |
| Funghi      | Tomaat, kaas, champignons en oregano                               |
| Salame      | Tomaat, kaas, salami en oregano                                    |

Tip: Gebruik eventueel commentaar '--' om een deel van je code te verbergen zodat je kunt kijken welke delen wel en niet goed werken.


SELECT naam, omschrijving
FROM pizza
WHERE omschrijving NOT LIKE 'paprika' OR 'uien';




ANTWOORD:
SELECT naam, omschrijving
FROM pizza
WHERE omschrijving NOT LIKE '%paprika%' AND omschrijving NOT LIKE '%ui%';




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
WHERE basisprijs < 7.5 AND (naam LIKE 'M%' OR naam LIKE '%A');






### AFSLUITENDE OPDRACHTEN




### Afsluitende opdracht

Toon van alle pizza's de omschrijving en de naam (in die volgorde).
<!-- ANTWOORD
SELECT omschrijving, naam
FROM pizza;
-->




### Opdracht: Alle goedkope pizza's met een 'C'

Toon een overzicht van alle pizza's waarvan de naam met 'C' begint maar niet meer kost dan 8 euro.

| naam         |
|--------------|
| Cippola      |
| Calimero     |
| Capricciosa  |


ANTWOORD: 
SELECT naam
FROM pizza
WHERE naam LIKE 'C%' AND basisprijs <= 8.0;




### Afsluitende opdracht

Schrijf een SQL-query om alle pizza's te vinden met een basisprijs van minimaal €9,00 én die het woord 'salami' in de omschrijving bevatten.

| naam                   | basisprijs |
| ---------------------- | ---------- |
| Calzone (dichte pizza) | 9.0        |
| Fantasia               | 9.0        |
| Specialità di Danilo   | 9.5        |



Antwoord:
SELECT naam, basisprijs
FROM pizza
WHERE basisprijs >= 9
  AND omschrijving LIKE '%salami%';


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
<li>Gebruik toegang op basis van rollen (bijv. alleen de beheerder mag DELETE uitvoeren).
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

<p>Hier een overzicht van de tabellen in de database:</p><img src="https://raw.githubusercontent.com/rweeda/PythonIA/main/sql/DaniloIA_ERD.png" alt="overzicht tabellen" width="500"></p


TODO [ERDtoelichting.png]

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



## UITLEG  Gegevens uit meerdere tabellen combineren met JOIN

Tot nu toe heb je geleerd hoe je gegevens uit één tabel opvraagt. Maar soms wil je gegevens uit meerdere tabellen combineren. Daarvoor gebruik je `JOIN`.


Stel je voor: je hebt een lijst met bestellingen van pizza’s. Die staat in de tabel `besteldepizza`. Daarin zie je **welke pizza is besteld**, maar niet de naam — alleen een `pizzacode`.



### opdracht:
Schrijf in je eigen woorden wat er gebeurt bij een `JOIN`. Wat moet er kloppen tussen twee tabellen om een `JOIN` te kunnen maken?





### Opdracht: Waarom is een JOIN nodig in de volgende query?

```
SELECT besteldepizza.besteldepizzacode, pizza.naam
FROM besteldepizza
JOIN pizza ON besteldepizza.pizzacode = pizza.pizzacode;
```
a. Omdat tabel `besteldepizza` geen gegevens bevat over pizzacodes.
b. Omdat je een extra filter op de gegevens wilt toepassen.
c. Omdat de naam van de pizza niet in tabel `besteldepizza` staat.
d. Omdat je gegevens uit dezelfde tabel wilt combineren.


ANTWOORD:
c. Omdat de naam van de pizza niet in besteldepizza staat




### Opdracht: Naam van de pizza bij de bestelling

Toon per besteldepizza de naam van de pizza. Gebruik de tabellen `besteldepizza` en `pizza`.

ANTWOORD:
SELECT besteldepizza.besteldepizzacode, pizza.naam
FROM besteldepizza
JOIN pizza ON besteldepizza.pizzacode = pizza.pizzacode;




### Opdracht: Omschrijving van de bodem bij een bestelling

Laat zien welke bodembeschrijving hoort bij elke bestelde pizza. Gebruik besteldepizza en bodem.

ANTWOORD:

SELECT besteldepizza.besteldepizzacode, bodem.omschrijving
FROM besteldepizza
JOIN bodem ON besteldepizza.bodemcode = bodem.bodemcode;











### Opdracht: maak een overzicht van de bestelde pizza en het formaat



### Opdracht: maak een overzicht voor de besteldePizza en datum en bezorg tijd






### Oefenopdracht
Toon de laagste prijs van een pizzabodem in de tabel `bodem`.


**Uitwerking:**
```sql
SELECT MIN(prijs) AS goedkoopste_bodem
FROM bodem;
```

## 🔹 2. `MAX()` – Maximumwaarde



### Oefenopdracht
Wat is de hoogste toeslag voor een pizzabodem? Gebruik de tabel `bodem`.


**Uitwerking:**
```sql
SELECT MAX(prijs) AS hoogste_toeslag
FROM bodem;
```


## `SUM()` – Totaal optellen



### Oefenopdracht
Bereken de totale prijs van alle bestellingen in de tabel `bestelling`.


**Uitwerking:**
```sql
SELECT SUM(totaalprijs) AS totaal_bestellingen
FROM bestelling;
```



## 4. `AVG()` – Gemiddelde



### Oefenopdracht
Bereken de gemiddelde toeslag voor bodems in de tabel `bodem`.



**Uitwerking:**
```sql
SELECT AVG(prijs) AS gemiddelde_bodem_toeslag
FROM bodem;
```


##  `COUNT(*)` – Aantal rijen tellen



### Oefenopdracht
Hoeveel bestellingen staan er in de tabel `bestelling`?

**Uitwerking:**
```sql
SELECT COUNT(*) AS aantal_bestellingen
FROM bestelling;
```

---

## `DISTINCT` – Unieke waarden selecteren

Stel dat je alle woonplaatsen wilt zien van de tabel `klant`.


| plaats     |
|------------|
| Enschede   |
| Enschede   |
| Enschede   |
| Enschede   |
| Hengelo    |
| Enschede   |
| Enschede   |
| ...        |



Je ziet dat er dubbele waarden te zien zijn. Om te voorkomen dat er dubbele waarden worden getoond, kun je DISTINCT gebruiken. 
 

`DISTINCT kolom` toont alleen **verschillende (unieke)** waarden uit een kolom.  
Bijvoorbeeld: alle verschillende plaatsen waar klanten wonen.



### Oefenopdracht
Toon alle unieke bezorgdatums in de tabel `bestelling`.

**Uitwerking:**
```sql
SELECT DISTINCT datum
FROM bestelling;
```

---

## Rekenen met `+`, `-`, `*`, `/`



### Oefenopdracht
Toon per pizza de basisprijs, een bezorgtoeslag van €0,50, en het totaalbedrag (basisprijs + toeslag).

**Uitwerking:**
```sql
SELECT naam, basisprijs, basisprijs + 0.50 AS totaalprijs
FROM pizza;
```




### Opdracht: Aantal pizza's in totaal besteld
Toon het aantal pizza's dat er in totaal zijn besteld.

ANTWOORD:

SELECT COUNT(*) 
FROM besteldepizza;



### Opdracht: Toon van alle bestellingen: pizzanaam, formaat, bodem + basisprijs +plusprijs formaat, plusprijs bodem, Totaal pijs




## AFSLUITENDE OPDRACHTEN 




### AO: Opdracht

Toon unieke combinaties van bodemcode en omschrijving.

ANTWOORD:
SELECT DISTINCT bodemcode, omschrijving 
FROM besteldepizza;





### Opdracht: Toon alle kortingen die bij een bestelling horen

Toon alle kortingen die bij een bestelling horen. Hiervoor heb je de tabellen `besteldepizza` en `kortingsbonnen` nodig.

ANTWOORD:

```
SELECT 
  besteldepizza.bestelcode,
  kortingsbonnen.korting,
  kortingsbonnen.datum
FROM besteldepizza
JOIN kortingsbonnen ON besteldepizza.boncode = kortingsbonnen.boncode;
```

## Gegevens sorteren

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


###Opdracht volgorde van onderdelen

Zet de onderdelen van een SQL-query in de juiste volgorde:
FROM – ORDER BY – LIMIT - SELECT – WHERE


ANTWOORD: 
SELECT
FROM
WHERE
ORDER BY
LIMIT




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
Schrijf een query om een nieuwe bestelling toe te voegen met besteldepizzacode = 6, bodemcode 2, omschrijving 'American style'.


ANTWOORD:
INSERT INTO besteldepizza (besteldepizzacode, bodemcode, omschrijving)
VALUES (6, 2, 'American style');



### AFSLUITENDE OPDRACHT
Stel dat er een andere tabel is met `pizzabodemprijzen`. 


Voeg die tabel toe en schrijf een query die de totale prijs per bestelling toont.
CREATE TABLE bodem (
    bodemcode INTEGER PRIMARY KEY,
    prijs REAL
);












### Opdracht: JOIN met drie tabellen toepassen toepassen
<ol type="alpha">
<li>
Toon een overzicht van alle bestelde pizza’s, met daarbij:
- de bestelcode (uit tabel `besteldepizza')
- de pizzanaam (uit tabel `pizza')
- en de bodembeschrijving (uit tabel `bodem`)

Gebruik hiervoor `JOIN` om de tabellen aan elkaar te koppelen.

Gebruik de de tabellen `besteldepizza`, `pizza` en `bodem`. Koppel er steeds twee tegelijk.


**Hint:** je moet twee JOINs gebruiken.
</li>
<li>Waarom kun je dit niet doen zonder JOIN?
</li>
</ol>




### Opdracht: naam van de bezorger en bijbehorende de klantgegevens: naam adres, postcode, plaats,




### Opdracht: overzicht van alle bestellingen: pizzanaam, formaat, bodem

