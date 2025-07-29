

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

In SQLite, de database waar wij mee werken, zijn er drie datatypen: 
<ul>
<li><b>TEXT</b>: een stuk tekst. Bijvoorbeeld: 'Jaap'
<li><b>INTEGER</b>: een geheel getal. Bijvoorbeeld: 4
<li><b>REAL</b>: een kommagetal. Bijvoorbeeld: 2.50
</ul>

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


###Databasemanagementsysteem (DBMS) 
<p>Een database kan al snel heel groot 
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
System*, of DBMS). </p>


[IMG]


<p>Zo’n systeem zorgt ervoor dat de data betrouwbaar en 
correct blijft, en dat wij op een eenvoudige manier informatie kunnen 
opvragen wanneer we die nodig hebben.</p> 





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


## Terugblik

Bij het maken van de vorige opdrachten heb je veel geleerd over gestructureerde data. We vatten dat nu samen.

<ul>
<li><b>Database</b>: Een georganiseerde verzameling gegevens, opgeslagen in tabellen met rijen en kolommen.
<li><b>Datatypes</b> in SQLite:  INTEGER - Gehele getallen (bijv. 4), TEXT - Tekstuele gegevens (bijv. 'Jaap') en REAL - Kommagetallen (bijv. 2.50)
<li><b>Primary Key</b>: Een kolom die elke rij uniek identificeert; moet uniek en niet leeg zijn.
</ul>




####################



# ONDERWERP 2: SQL SELECT

# SQL 

<p>SQL staat voor <i>Structured Query Language</i>. Het is de 
standaardtaal om data in een database op te slaan, te bewerken en op te 
halen. Zo’n verzoek aan de database noem je een <b>query</b>, wat letterlijk 
‘vraag’ betekent in het Engels. Als je een query schrijft, stel je dus eigenlijk een vraag aan de database. Bijvoorbeeld: “Welke klanten wonen in 
Amsterdam?”</p>

<p>In deze cursus leer je hoe je SQL gebruikt binnen 
<b>SQLite</b> — een eenvoudige, lichtgewicht databasesysteem. We beginnen met 
leren hoe je informatie kunt ophalen. Daarna leer je ook hoe je gegevens kunt 
opslaan, aanpassen en verwijderen. Tot slot ga je zelfs je eigen tabellen 
aanmaken.</p> 




<p>Bij de volgende opgaven maken we gebruik van de database van Danilo's pizzeria. Hieronder zie je hoe de tabel <i>pizza</i> er uitziet met de gegevens van een aantal pizza's erin.</p>

<!--De afbeelding hieronder toont de kolommen van tabel <i>pizza</i>:

<p><img src="https://raw.githubusercontent.com/rweeda/PythonIA/main/sql/img/ERD_pizza.png" alt="Tabel pizza" width="300"></p>


-->

<p><img src="https://raw.githubusercontent.com/rweeda/PythonIA/main/sql/img/H1_tabel_pizza.png" alt="Tabel pizza" width="800"></p>



<!--
| pizzacode | naam                  | omschrijving                                                             | basisprijs |
|-----------|-----------------------|---------------------------------------------------------------------------|------------|
| 1         | Margherita            | Tomaat,kaas en oregano                                                    | 6.0        |
| 2         | Napoletana            | Tomaat, kaas, ansjovis, olijven, kappertjes en oregano                   | 7.5        |
| 3         | Prosciutto            | Tomaat, kaas, ham en oregano                                              | 7.5        |
| 4         | Funghi                | Tomaat, kaas, champignons en oregano                                     | 7.5        |
| ...       | ...                   | ...                                                                       | ...        |
| 36        | Combinazione          | Eigen keuze pizza                                                        | 10.5       |

-->


<p>Met een query kun je gegevens uit een tabel ophalen. Met SELECT kun je data selecteren van een database en in een overzicht tonen. 
Met FROM geef je aan uit welke tabel de informatie gehaald moet worden. Hoe dat werkt leer je nu.</p>


---------------------------------------


## 2.1: Je eerste query

Om één kolom op te halen geef je na de SELECT de kolomnaam op, en na de FROM de tabelnaam:
 
 ```SQL
SELECT kolomnaam
FROM tabelnaam;
```

Run de code hieronder (dat kan met CRTR+ENTER of door bovenin op 'Run' te drukken):

SELECT naam 
FROM pizza;

Daarmee krijg je zo'n volgende overzicht:

| naam                    |
|-------------------------|
| Margherita              |
| Napoletana              |
| Prosciutto              |
| Funghi                  |
| Salame                  |
| ...                     |
| Combinazione            |



### Opdracht 2.1: Alle pizzacodes tonen
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



<p>Bekijk <a href="https://rweeda.github.io/PythonIA/docs/IA_sql_oplossingen.html#opgave21" target="_blank">hier</a> de voorbeelduitwerking.</p>

<!--
ANTWOORD

<ol style="list-style-type: lower-alpha">
<li>
<pre><code class="language-sql">
SELECT pizzacode 
FROM pizza;
</code></pre>
<li>Elke pizzacode komt maar één keer voor. Dat betekent dat elke pizza een unieke code heeft. Zo’n unieke code noemen we een primary key. Een primary key zorgt ervoor dat je elk record in een tabel kunt herkennen. In dit geval herken je elke pizza aan zijn pizzacode.
</ol>
-->

## 2.2 Meerdere kolommen uit een tabel halen
Je kunt ook een meerdere kolommen ophalen. Dat doe je als volgt:
 ```SQL
SELECT kolom1, kolom2, ...
FROM tabelnaam;
```

### Opdracht 2.2: Menu printen

Maak een menu door de pizzanamen (kolom <i>naam</i>), <i>omschrijving</i> en de prijs (kolom <i>basisprijs</i> uit het tabel <i>pizza</i> te halen.


| naam                   | omschrijving                                                             | basisprijs |
|------------------------|----------------------------------------------------------------------------|------------|
| Margherita             | Tomaat,kaas en oregano                                                    | 6.0        |
| Napoletana             | Tomaat, kaas, ansjovis, olijven, kappertjes en oregano                   | 7.5        |
| Prosciutto             | Tomaat, kaas, ham en oregano                                              | 7.5        |
| Funghi                 | Tomaat, kaas, champignons en oregano                                     | 7.5        |
| ...                    | ...                                                                      | ...        |
| Combinazione           | Eigen keuze pizza                                                        | 10.5       |


<p>Bekijk <a href="https://rweeda.github.io/PythonIA/docs/IA_sql_oplossingen.html#opgave22" target="_blank">hier</a> de voorbeelduitwerking.</p>
<!-- ANTWOORD:
<pre><code class="language-sql">
SELECT pizzanaam, omschrijving, basisprijs 
FROM pizza;
</code></pre>
-->

### 2.3 Alle gegevens van een tabel ophalen

<p>Om alle kolommen op te halen gebruik je na de SELECT een '*'</p>
 
```SQL
SELECT * 
FROM tabelnaam;
```

### Opdracht 2.3 Alle gegevens van tabel pizza ophalen

Toon alle kolommen met gegevens van tabel <i>pizza</i>, zoals in het voorbeeld hieronder: 

| pizzacode | naam                  | omschrijving                                                             | basisprijs |
|-----------|-----------------------|---------------------------------------------------------------------------|------------|
| 1         | Margherita            | Tomaat,kaas en oregano                                                    | 6.0        |
| 2         | Napoletana            | Tomaat, kaas, ansjovis, olijven, kappertjes en oregano                   | 7.5        |
| 3         | Prosciutto            | Tomaat, kaas, ham en oregano                                              | 7.5        |
| 4         | Funghi                | Tomaat, kaas, champignons en oregano                                     | 7.5        |
| ...       | ...                   | ...                                                                       | ...        |
| 36        | Combinazione          | Eigen keuze pizza                                                        | 10.5       |

<p>Bekijk <a href="https://rweeda.github.io/PythonIA/docs/IA_sql_oplossingen.html#opgave23" target="_blank">hier</a> de voorbeelduitwerking.</p>

<!-- ANTWOORD:
<pre><code class="language-sql">
SELECT *
FROM pizza
</code></pre>
-->


## 2.4: Commando's voor het ophalen van informatie

De taal voor het ophalen van informatie bestaat uit slechts 6 commando’s waarmee je 
leert werken. De commando’s zijn:


<p><img src="https://raw.githubusercontent.com/rweeda/PythonIA/main/sql/img/H1_commandos.png" alt="Commando's voor het ophalen van informatie" width="400"></p>


Je hoeft niet alle commando's te gebruiken, maar ze staan wel <b>altijd in deze volgorde</b>.




## 2.5 Voorwaarden met de WHERE

<p>Met WHERE kun je beperken welke rijen getoond moet worden. Met WHERE kun je een voorwaarde aangeven, bijvoorbeeld: ’waarbij de informatie voldoet aan ...’</p>

<p>Je geeft altijd eerst een SELECT op voor de gegevens die opgehaald moeten worden, dan met FROM de tabel waaruit de gegevens moeten komen, en met WHERE welke beperking er is.</p>


<p>Bijvoorbeeld, met de volgende query tonen we alle pizza's die precies 8 euro kosten:</p
```SQL
SELECT *
FROM pizza
WHERE basisprijs=8
```

| pizzacode | naam           | omschrijving                                                             | basisprijs |
|-----------|----------------|----------------------------------------------------------------------------|------------|
| 10        | Capricciosa    | Tomaat, kaas, ham, champignons, paprika, artisjokken en oregano          | 8.0        |
| 11        | Primavera      | Tomaat, kaas, ham, salami en oregano                                     | 8.0        |
| 12        | Venezia        | Tomaat, kaas, ham, champignons, ananas en oregano                        | 8.0        |
| ...       | ...            | ...                                                                      | 8.0        |
| 30        | Romana         | Tomaat, kaas, spek, uien, champignons, ei en oregano                     | 8.0        |




### Opdracht 2.4: Omschrijving van een Inferno pizza
Schrijf een query om de omschrijving van de pizza 'Inferno' te tonen, zoals in het voorbeeld hieronder.

| omschrijving |
|--------------|
| Tomaat, kaas, ham, spaanse peper, kappertjes, salami, olijven en oregano  |

<p>Bekijk <a href="https://rweeda.github.io/PythonIA/docs/IA_sql_oplossingen.html#opgave24" target="_blank">hier</a> de voorbeelduitwerking.</p>

<!-- ANTWOORD:
<pre><code class="language-sql">
ANTWOORD:
SELECT omschrijving
FROM pizza
WHERE naam='Inferno'
</code></pre>
-->




## 2.6 Kennis maken met de andere tabellen


<p>Danilo's pizzeria database bestaat uit meer tabellen dan alleen <i>pizza</i>. Er wordt ook bijvoorbeeld ook informatie opgeslagen over klanten, berzorgers en bestellingen. In de afbeelding hieronder zie je alle 7 tabellen.</p>


<p>
<a href="https://raw.githubusercontent.com/rweeda/PythonIA/main/sql/img/DaniloIA_ERD.png" target="_blank">
  <img src="https://raw.githubusercontent.com/rweeda/PythonIA/main/sql/img/DaniloIA_ERD.png" alt="Klik om in een nieuw venster te openen" width="1000"/>
</a></p>



### Opdracht 2.5: Alle gegevens uit tabel <i>klant</i>
<p>Toon alle gegevens uit tabel <i>klant</i>.


<p>Bekijk <a href="https://rweeda.github.io/PythonIA/docs/IA_sql_oplossingen.html#opgave25" target="_blank">hier</a> de voorbeelduitwerking.</p>

<!-- ANTWOORD:
<pre><code class="language-sql">
SELECT *
FROM klant;
</code></pre>
-->


### Opdracht 2.6: Alle klanten uit Enschede

<p>Toon het adres, de postcode en de plaats van alle klanten die in Enschede wonen, zoals hieronder. Tip: de gegevens komen uit tabel <i>klant</i>.</p>
| adres              | postcode | woonplaats    |
|--------------------|----------|-----------|
| Gladioolstraat 11  | 3742TC   | Enschede  |
| Banckertlaan 7     | 3742MG   | Enschede  |
| Talmalaan 11       | 3741TX   | Enschede  |
| Krugerlaan 9       | 3743CJ   | Enschede  |
| Zandvoortweg 199   | 3741BE   | Enschede  |





<p>Bekijk <a href="https://rweeda.github.io/PythonIA/docs/IA_sql_oplossingen.html#opgave26" target="_blank">hier</a> de voorbeelduitwerking.</p>

<!-- ANTWOORD:
<pre><code class="language-sql">
SELECT adres, postcode, woonplaats
FROM klant
WHERE plaats='Enschede';
</code></pre>
-->


### Opdracht 2.7: Wachtwoord uit tabel bezorger.
Toon het wachtwoord van de bezorger met de naam Ronald Marbus, zoals hieronder.<br>
| wachtwoord  |
|-------------|
| R0nalt      |




Tips:
<ul>
<li>de gegevens komen uit tabel <i>bezorger</i>,</li>
<li>toon eerst alle kolommen, en kies dan welk kolom je nodig hebt.</li>
</ul>




<p>Bekijk <a href="https://rweeda.github.io/PythonIA/docs/IA_sql_oplossingen.html#opgave27" target="_blank">hier</a> de voorbeelduitwerking.</p>

<!-- ANTWOORD:
<pre><code class="language-sql">
SELECT wachtwoord
FROM bezorger
WHERE naam = 'Ronald Marbus';
</code></pre>
-->

## 2.7: Commentaar

Net als bij programmeren, kun je in SQL ook commentaar opnemen in je code. Dit doe je 
door twee streepjes ‘--’ ervoor te zetten. Dat ziet er dan zo uit (zie regel 2):</p>
SELECT * 
FROM pizza; -- dit is de tabelnaam


<!--
<p>Je kunt ook <code>/*</code> ervoor en <code>*/</code> erna zetten. Dat ziet er dan zo uit (zie regel 2):</p>
SELECT * 
FROM pizza; /* dit is de tabelnaam */
-->

## 2.8: Nette code
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

### Opdracht 2.8 Query netjes opschrijven
<ol style="list-style-type: lower-alpha">
De query hieronder is niet zo netjes opgeschreven.
<li>Voer de onderstaande query uit, dan zul je zien dat de query het gewoon doet. Bekijk de uitkomst.
<li>Pas deze query aan zodat hij voldoet aan alle voorwaarden van nette code.
<li>Voeg bij elke regel commentaar toe om aan te geven voor welk voorwaarde je het hebt aangepast.
</ol> 


naam,basisprijs From pizza wHERe basisprijs<8


<p>Bekijk <a href="https://rweeda.github.io/PythonIA/docs/IA_sql_oplossingen.html#opgave31" target="_blank">hier</a> de voorbeelduitwerking.</p>

<!--ANTWOORD
-- (1) SQL commando in hoofdletters, (4) spatie na de komma
SELECT naam, basisprijs
-- (2) Elke SQL commando op een nieuwe regel (en in hoofdletters)
FROM pizza
-- (4) spaties in de voorwaarde zodat het beter leesbaar is
-- (6) en afsluiten met een ; (maar dat hoeft niet)
WHERE basisprijs < 8;
-->


## 2.9: Fouten opsporen

Het kan voorkomen dat er een fout in je code zit. Hier zijn wat tips om die op te sporen: 
<ul>
<li>Krijg je een foutmelding? Lees die goed. Vaak staat er welke regel of welk onderdeel fout is.
<li>Soms krijg je geen foutmelding, maar ook geen resultaten — dan heb je een denkfout in je code zitten en vraag je iets op wat er niet is.
<li>Als iets niet werkt, test dan een stukje tegelijk. Begin met alleen `SELECT * FROM ...`, pas als dat werkt voor je daarna stukje voor stukje de WHERE-voorwaarden toe.
<li>Controleer de tabel- en kolomnamen. Typefouten in kolomnamen komen vaak voor. Met `SELECT * FROM ...` kun je de kolomnamen bekijken. 
<li>Zet tijdelijk delen van je code in commentaar (mert `--`) om te testen wat het probleem veroorzaakt.
<li>SQLite is niet hoofdlettergevoelig voor sleutelwoorden, maar wel voor strings, bijvoorbeeld 'enschede' in plaats van 'Enschede'.
</ul>


### Opdracht 2.8: Fout in query (1)
Piet wil met de query hieronder een overzicht van alle pizza's die minder dan 7 euro kosten. Wat is de fout in deze query? Los die op.
``` sql
SELECT naam basisprijs < 7.0 FROM WHERE pizza;
```

<p>Bekijk <a href="https://rweeda.github.io/PythonIA/docs/IA_sql_oplossingen.html#opgave28" target="_blank">hier</a> de voorbeelduitwerking.</p>


<!-- ANTWOORD:
De fout zat in de volgorde van de regels code.
<pre><code class="language-sql">
SELECT naam 
FROM pizza
WHERE basispijs < 7.0;
</code></pre>
-->

### Opdracht 2.9: Fout in query (2)
Lukas wil alle klantgegevens van klanten in Nijmegen zien. Hij gebruikt daarvoor het onderstaande code, maar dat levert niets op! Waarom niet? Pas de code aan zodat het een juiste overzicht geeft zoals hieronder.
 

SELECT * 
FROM klant
WHERE woonplaats = 'nijmegen';

<ol type="alpha">
<li>De kolom woonplaats bestaat niet
<li>De woonplaats moet met een hoofdletter geschreven zijn
<li>Er staan geen klanten in de database
<li>Er mogen geen spaties om de '='-teken staan
</ol>

| klantnummer | wachtwoord   | klantnaam         | adres                   | postcode | woonplaats | telefoon     |
|-------------|--------------|-------------------|--------------------------|----------|------------|--------------|
| 425         | M8eoyfuVd5   | Nina Vos          | Graafseweg 115           | 6531ZG   | Nijmegen   | 06-63017195  |
| 426         | BV8aYhfTeH   | Noa de Boer       | Daalseweg 103            | 6521GS   | Nijmegen   | 06-87240602  |
| 427         | IcMD8WuNRk   | Bram Kuipers      | Heyendaalseweg 300       | 6525EC   | Nijmegen   | 06-13617853  |
| ...         | ...   | ...     | ...     | ...   | ...   | ...  |



<p>Bekijk <a href="https://rweeda.github.io/PythonIA/docs/IA_sql_oplossingen.html#opgave29" target="_blank">hier</a> de voorbeelduitwerking.</p>

<!-- ANTWOORD: b
De woonplaatsen zijn met een hoofdletter geschreven (bv. 'Nijmegen'). SQL vergelijkt tekst hoofdlettergevoelig. In dit geval zijn er klanten die in 'nijmegen' wonen, maar wel in 'Nijmegen'. 

De juiste query is:

<pre><code class="language-sql">
SELECT * 
FROM klant
WHERE woonplaats = 'Nijmegen';
-->


### Opdracht 2.10: Fout in query (2)
De code hieronder bevat een fout. Run de code, lees de foutmelding en herstel de fout.

``` sql
SELECT naam 
FROM pizzas
WHERE basispijs < 7.0;
</code></pre>
```

<p>Bekijk <a href="https://rweeda.github.io/PythonIA/docs/IA_sql_oplossingen.html#opgave210" target="_blank">hier</a> de voorbeelduitwerking.</p>


<!-- ANTWOORD:
De fout zat in de naam van de tabel.
<pre><code class="language-sql">
SELECT naam 
FROM pizza
WHERE basispijs < 7.0;
</code></pre>
-->



### Opdracht 2.11: Fout in query (3) 
De code hieronder bevat een fout. Run de code, lees de foutmelding en herstel de fout.

``` sql
SELECT pizzanaam 
FROM pizza
WHERE basispijs < 7.0;
```

<p>Bekijk <a href="https://rweeda.github.io/PythonIA/docs/IA_sql_oplossingen.html#opgave211" target="_blank">hier</a> de voorbeelduitwerking.</p>


<!-- ANTWOORD:
De fout zat in de kolomnaam.
<pre><code class="language-sql">
SELECT naam 
FROM pizza
WHERE basispijs < 7.0;
</code></pre>
-->

### Opdracht 2.11: Kolomnamen opzoeken
Je wil weten welke kolomnamen er in de tabel <i>bestelling</i> zitten. Welke query helpt je hierbij?


<p>Bekijk <a href="https://rweeda.github.io/PythonIA/docs/IA_sql_oplossingen.html#opgave211" target="_blank">hier</a> de voorbeelduitwerking.</p>


<!-- ANTWOORD:
Met de volgende query krijg je een overzicht van de hele tabel, inclusief de kolomnamen:
<pre><code class="language-sql">
SELECT * 
FROM bestelling;
</code></pre>
-->



### Overzicht ONDERWERP 3






## 3.3: Kolom hernoemen met <code>AS</code>

Met `AS` kan je een kolomnaam hernoemen.

Bijvoorbeeld, hieronder wordt de kolom `naam` getoond als `pizzanaam`


``` SQL
SELECT naam AS pizzanaam
FROM pizza;
```


| pizzanaam   |
|-------------|
| Margherita  |
| Napoletana  |
| Prosciutto  |
| Funghi      |
| Salame      |



### Opdracht 3.2 Kolom 'naam' hernoemen in 'bezorgernaam'
Toon een overzicht van alle namen van de bezorgers. Noem het kolom `bezorgernaam`.

<p>Bekijk <a href="https://rweeda.github.io/PythonIA/docs/IA_sql_oplossingen.html#opgave32" target="_blank">hier</a> de voorbeelduitwerking.</p>
<!-- ANTWOORD:
<pre><code class="language-sql">
SELECT naam AS bezorgernaam
FROM bezorger;
</code></pre>
-->



## 3.4: Aantal rijen beperken met <code>LIMIT</code>
<p>Met LIMIT kun je bepalen hoeveel rijen er getoond moeten worden.</p>

<p>Met de volgende code toon je alleen de eerste vijf rijen:</p>

SELECT *
FROM pizza
LIMIT 5;


### Opdracht 3.3 Alleen de eerste drie pizza's
Toon de naam (<i>pizzanaam</i>) en prijs (<i>basisprijs</i>) van de eerste drie pizza's.

<p>Bekijk <a href="https://rweeda.github.io/PythonIA/docs/IA_sql_oplossingen.html#opgave33" target="_blank">hier</a> de voorbeelduitwerking.</p>
<!-- ANTWOORD:
<pre><code class="language-sql">

SELECT pizzanaam, basisprijs
FROM pizza
LIMIT 3;

</code></pre>
-->





## 3.5: Wiskundige operatoren

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

VOEG VOORBEELD TOE




### Opdracht 3.4 Dure pizza's
Toon de namen en prijzen van de pizza's die 9,50 euro kosten of meer, zoals in het overzicht hieronder.


| naam                  | basisprijs |
|-----------------------|-------------|
| Specialità di Danilo | 9.5         |
| Combinazione          | 10.5        |


<p>Bekijk <a href="https://rweeda.github.io/PythonIA/docs/IA_sql_oplossingen.html#opgave34" target="_blank">hier</a> de voorbeelduitwerking.</p>
<!-- ANTWOORD:
<pre><code class="language-sql">

</code></pre>
-->



### Opdracht 3.5: Geen 8euro pizza's
Toon de namen en prijzen van de pizza's die <b>niet</b> 8 euro kosten.


<p>Bekijk <a href="https://rweeda.github.io/PythonIA/docs/IA_sql_oplossingen.html#opgave35" target="_blank">hier</a> de voorbeelduitwerking.</p>
<!-- ANTWOORD:
<pre><code class="language-sql">
SELECT naam, basisprijs
FROM pizza
WHERE basisprijs<>8;
</code></pre>
-->





## 3.5: WHERE met LIKE


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



### Opdracht 3.6 Alle pizza's waar de letter 'a' in voorkomt
Toon een overzicht van alle pizza's waar de letter 'a' in voorkomt:

<p>Bekijk <a href="https://rweeda.github.io/PythonIA/docs/IA_sql_oplossingen.html#opgave36" target="_blank">hier</a> de voorbeelduitwerking.</p>
<!-- ANTWOORD:
<pre><code class="language-sql">
SELECT naam
FROM pizza
WHERE naam LIKE '%a%';
</code></pre>
-->


### Opdracht 3.7 Alle klanten met een mobiele telefoonnummer.
Toon een overzicht van alle klanten die een 06-nummer hebben opgegeven.


<p>Bekijk <a href="https://rweeda.github.io/PythonIA/docs/IA_sql_oplossingen.html#opgave37" target="_blank">hier</a> de voorbeelduitwerking.</p>
<!-- ANTWOORD:
<pre><code class="language-sql">
SELECT *
FROM klant
WHERE telefoon LIKE '06%';
</code></pre>
-->




## 3.6: Logische operatoren AND, OR en NOT 
Je kunt de WHERE voorwaarde ook uitbreiden met de logische operatoren AND, OR, NOT of combinaties daarvan. 


### 3.6.1: AND (EN)
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



### OPDRACHT 3.8 Pizza's tussen de 8,50 en 10euro

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


<p>Bekijk <a href="https://rweeda.github.io/PythonIA/docs/IA_sql_oplossingen.html#opgave38" target="_blank">hier</a> de voorbeelduitwerking.</p>
<!-- ANTWOORD:
<pre><code class="language-sql">

SELECT naam, basisprijs
FROM pizza
WHERE basisprijs>=8.50 AND basisprijs<=10;
</code></pre>
-->




### 3.6.2: OR (OF)

Met *OR* moet aan één van de voorwaarden voldaan worden.

Bijvoorbeeld, de volgende query toont alle pizza's die met 'M' beginnen OF een basisprijs onder de 7euro hebben:
```SQL
SELECT naam, basisprijs
FROM pizza
WHERE naam LIKE 'M%' OR basisprijs < 7;
```


| naam       | basisprijs |
| ---------- | ---------- |
| Margherita | 6.0        |
| Cippola    | 6.5        |
| Marinara   | 8.5        |
| Mozzarella | 8.5        |





### OPDRACHT 3.9 Bestellingen met bestelcode
<p>Toon alle informatie over zowel bestellingen bestelcode 13 en die met bestelcode 30, zoals hieronder.</p>

| bestelcode | datum       | bestel_tijd | bezorg_tijd | bezorgernummer | klantnummer | korting |
| ---------- | ----------- | ----------- | ----------- | -------------- | ----------- | ------- |
| 13         | 2021-12-03  | 17:33:00    | 17:48:00    | 5              | 279         | 0.0     |
| 30         | 2021-12-05  | 17:55:00    | 18:11:00    | 8              | 376         | 0.0     |



<p>Bekijk <a href="https://rweeda.github.io/PythonIA/docs/IA_sql_oplossingen.html#opgave39" target="_blank">hier</a> de voorbeelduitwerking.</p>
<!-- ANTWOORD:
<pre><code class="language-sql">
SELECT *
FROM bestelling
WHERE bestelcode = 13 OR bestelcode = 30;
</code></pre>
-->




### OPDRACHT 3.10 Alle goedkope of gezonde pizza's
Maak een overzicht van alle pizza's goedkoper zijn dan €7,50 of fruit bevatten.

<p>Bekijk <a href="https://rweeda.github.io/PythonIA/docs/IA_sql_oplossingen.html#opgave310" target="_blank">hier</a> de voorbeelduitwerking.</p>
<!-- ANTWOORD:
<pre><code class="language-sql">
SELECT *
FROM pizza
WHERE basisprijs<7.50 OR omschrijving LIKE '%fruit%';
</code></pre>
-->





### 3.6.3: NOT (NIET)
Met `NOT` mag er aan géén van de voorwaarden voldaan worden.

Bijvoorbeeld, alle klanten die *niet* in Hengelo wonen:

SELECT *
FROM klanten
WHERE NOT plaats = 'Hengelo'


Bijvoorbeeld, alle pizza's waarbij de letter 'e' er <b>niet</b> in voorkomt:

SELECT naam
FROM pizza
WHERE naam NOT LIKE '%e%';




### OPDRACHT 3.11 Alle pizza's zonder kip

Toon een overzicht van alle pizza's waar <b>geen</b> kip op zit, dus ook geen kipfilet, zoals in het voorbeeld hieronder.

| pizzanaam   | omschrijving                                                       |
|-------------|---------------------------------------------------------------------|
| Margherita  | Tomaat, kaas en oregano                                            |
| Napoletana  | Tomaat, kaas, ansjovis, olijven, kappertjes en oregano            |
| Prosciutto  | Tomaat, kaas, ham en oregano                                       |
| Funghi      | Tomaat, kaas, champignons en oregano                               |
| Salame      | Tomaat, kaas, salami en oregano                                    |



<p>Bekijk <a href="https://rweeda.github.io/PythonIA/docs/IA_sql_oplossingen.html#opgave311" target="_blank">hier</a> de voorbeelduitwerking.</p>
<!-- ANTWOORD:
<pre><code class="language-sql"> 
SELECT naam AS pizzanaam, omschrijving
FROM pizza
WHERE omschrijving NOT LIKE '%kip%';
</code></pre>

ook goed:
<pre><code class="language-sql"> 
ANTWOORD: 
SELECT naam, omschrijving
FROM pizza
WHERE NOT omschrijving LIKE '%kip%';
</code></pre>
-->




### OPDRACHT 3.12 Alle pizza's zonder paprika en zonder ui

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




<p>Bekijk <a href="https://rweeda.github.io/PythonIA/docs/IA_sql_oplossingen.html#opgave312" target="_blank">hier</a> de voorbeelduitwerking.</p>
<!-- ANTWOORD:
<pre><code class="language-sql">
SELECT naam, omschrijving
FROM pizza
WHERE omschrijving NOT LIKE '%paprika%' AND omschrijving NOT LIKE '%ui%';
</code></pre>
-->



## 3.6.4: Meerdere operatoren combineren
Als je de AND, OR en NOT combineert moet je gebruik maken van haakjes voor de gewenste uitkomst.

Bijvoorbeeld, met de volgende query tonen we de pizza's die tussen de  €8,50 en €10,- kosten, of pizza's die geen salami bevatten:

SELECT naam, omschrijving, basisprijs
FROM pizza
WHERE (basisprijs>=8.50 AND basisprijs<=10) OR NOT omschrijving LIKE '%salami%';



### OPDRACHT 3.13 Toon pizza's gefiltererd op meerdere voorwaarden

Toon alle pizza's die minder dan €7,50 kosten, en met de letter M beginnen of letter A eindigen. 

<p>Bekijk <a href="https://rweeda.github.io/PythonIA/docs/IA_sql_oplossingen.html#opgave313" target="_blank">hier</a> de voorbeelduitwerking.</p>
<!-- ANTWOORD:
<pre><code class="language-sql">
SELECT *
FROM pizza
WHERE basisprijs < 7.5 AND (naam LIKE 'M%' OR naam LIKE '%A');
</code></pre>
-->



### AFSLUITENDE OPDRACHTEN


### Afsluitende opdracht

Toon van alle pizza's de omschrijving en de naam (in die volgorde).
<!-- ANTWOORD:
<pre><code class="language-sql">
SELECT omschrijving, naam
FROM pizza;
</code></pre>
-->


### Opdracht: Alle goedkope pizza's met een 'C'

Toon een overzicht van alle pizza's waarvan de naam met 'C' begint maar niet meer kost dan 8 euro.

| naam         |
|--------------|
| Cippola      |
| Calimero     |
| Capricciosa  |


<p>Bekijk <a href="https://rweeda.github.io/PythonIA/docs/IA_sql_oplossingen.html#opgave313" target="_blank">hier</a> de voorbeelduitwerking.</p>
<!-- ANTWOORD:
<pre><code class="language-sql">
SELECT naam
FROM pizza
WHERE naam LIKE 'C%' AND basisprijs <= 8.0;
</code></pre>
-->


### Afsluitende opdracht

Schrijf een SQL-query om alle pizza's te vinden met een basisprijs van minimaal €9,00 én die het woord 'salami' in de omschrijving bevatten.

| naam                   | basisprijs |
| ---------------------- | ---------- |
| Calzone (dichte pizza) | 9.0        |
| Fantasia               | 9.0        |
| Specialità di Danilo   | 9.5        |


<p>Bekijk <a href="https://rweeda.github.io/PythonIA/docs/IA_sql_oplossingen.html#opgave313" target="_blank">hier</a> de voorbeelduitwerking.</p>
<!-- ANTWOORD:
<pre><code class="language-sql">
SELECT naam, basisprijs
FROM pizza
WHERE basisprijs >= 9
  AND omschrijving LIKE '%salami%';
</code></pre>
-->



### ✅ Opdracht 1: Pizza’s binnen een prijsbereik
Toon de naam, omschrijving en prijs van alle pizza’s die **minstens €7,50** kosten en **maximaal €9,00**.

<!--
<pre><code class="language-sql">
SELECT naam, omschrijving, basisprijs
FROM pizza
WHERE basisprijs >= 7.50 AND basisprijs <= 9.00;
</code></pre>
-->

---

### ✅ Opdracht 2: Klantselectie op woonplaats én postcode
Toon het klantnummer en adres van alle klanten die in **‘Amsterdam’** wonen en waarvan de postcode begint met **‘10’**.

*Hint: gebruik de LIKE-operator.*

<!--
<pre><code class="language-sql">
SELECT klantnummer, adres
FROM klant
WHERE woonplaats = 'Amsterdam' AND postcode LIKE '10%';
</code></pre>
-->

### ✅ Opdracht 4: Kolommen en voorwaarden combineren
Toon het klantnummer en de woonplaats van alle klanten **niet uit Enschede of Nijmegen**, waarvan het telefoonnummer begint met ‘06’.

<!--
<pre><code class="language-sql">
SELECT klantnummer, woonplaats
FROM klant
WHERE woonplaats NOT 'Enschede' AND woonplaats NOT 'Nijmegen'
  AND telefoon LIKE '06%';
</code></pre>
-->



# ONDERWERP 4


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
<ol style="list-style-type: lower-alpha">
<li>Welke acties (Create, Read, Update, Delete) moet een klant kunnen uitvoeren op de tabel <code>besteldePizza</code>?
<li>Licht je antwoord toe: waarom is het logisch dat een klant sommige dingen wel en andere dingen niet mag? 
</ol>


<p>Bekijk <a href="https://rweeda.github.io/PythonIA/docs/IA_sql_oplossingen.html#opgave313" target="_blank">hier</a> de voorbeelduitwerking.</p>
<!--
ANTWOORDEN:
<ol style="list-style-type: lower-alpha">
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

-->

### Opdracht CRUD Rechten van de bezorger bepalen
Een bezorger krijgt een overzicht van de pizza’s die hij moet afleveren. Na bezorging vinkt hij in het systeem aan dat de bestelling is bezorgd, daarmee wordt de bezorgtijd vastgelegd.
<ol style="list-style-type: lower-alpha">
<li>Welke rechten heeft een bezorger nodig op de tabel besteldePizza?
<li>Welke informatie moet hij kunnen zien, en welke mag hij aanpassen?
<li>Waarom is het belangrijk dat een bezorger geen toegang heeft tot bepaalde gegevens?
</ol>

<p>Bekijk <a href="https://rweeda.github.io/PythonIA/docs/IA_sql_oplossingen.html#opgave313" target="_blank">hier</a> de voorbeelduitwerking.</p>
<!--
ANTWOORDEN:
<ol style="list-style-type: lower-alpha">
<li>Acties:
<ul>
<li>Read: Ja, om te kunnen zien welke bestellingen hij moet bezorgen, inclusief adresinformatie.
<li>Update: Ja, om de status van een bestelling te markeren als "bezorgd", waardoor de bezorgtijd wordt vastgelegd.
<li>Create/Delete: Nee, een bezorger mag geen bestellingen invoeren of verwijderen.
</ul>
<li>Toelichting: De bezorger heeft beperkte toegang. Hij mag alleen de status aanpassen, bijvoorbeeld een vinkje bij "bezorgd". Andere gegevens zijn niet zijn verantwoordelijkheid en moeten dus beschermd blijven.
</ol>
-->

### Opdracht CRUD Rechten van de databasebeheerder bepalen
De beheerder moet het hele systeem kunnen beheren, ook als er iets fout is gegaan.
<ol style="list-style-type: lower-alpha">
<li>Welke CRUD-rechten heeft een beheerder?
<li>Wat zijn de voor- en nadelen van het geven van volledige CRUD-rechten aan een beheerder?
<li>Zou je alle beheerders dezelfde rechten geven, of verschillende rollen aanmaken?
</ol>

<p>Bekijk <a href="https://rweeda.github.io/PythonIA/docs/IA_sql_oplossingen.html#opgave313" target="_blank">hier</a> de voorbeelduitwerking.</p>
<!--

ANTWOORDEN
<ol style="list-style-type: lower-alpha">
<li>Acties: Create, Read, Update, Delete: een beheerder heeft alle rechten.
<li>Voor- en nadelen:
<ul>
<li>Voordelen: De beheerder kan fouten corrigeren, testgegevens verwijderen, of het systeem onderhouden.
<li>Nadelen: Volledige rechten zijn gevoelig voor fouten of misbruik. Eén verkeerde DELETE-query kan veel gegevens verwijderen.
</ul>
<li>Overweging:
Je kunt overwegen om meerdere beheerdersrollen aan te maken, bijvoorbeeld een “technisch beheerder” (volledige toegang) en een “functioneel beheerder” (alleen lezen en bewerken, geen verwijderen).
</ol>
-->

### Opdracht Fouten voorkomen
Stel dat je per ongeluk een Delete-recht geeft aan klanten op de tabel besteldePizza.

<ol style="list-style-type: lower-alpha">
<li>Wat zou er kunnen gebeuren als een klant zijn eigen of andermans bestellingen kon verwijderen?
<li>Hoe kun je dit voorkomen?
</ol>

<p>Bekijk <a href="https://rweeda.github.io/PythonIA/docs/IA_sql_oplossingen.html#opgave313" target="_blank">hier</a> de voorbeelduitwerking.</p>
<!-- ANTWOORDEN
<ol style="list-style-type: lower-alpha">
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
-->


## Tabel 4.X: Nieuw tabel aanmaken

Met CREATE TABLE kun je een nieuwe tabel aanmaken. Je geeft dan de naam van de nieuwe tabel op met daarachter tussen haakjes ieder kolomnaam en de bijbehorende datatype.

Elk tabel heeft een primary key. In die kolom mag een waarde maar 1 keer voorkomen. De database kan automatisch voor je doornummeren zodra er nieuwe gegevens worden toegevoegd. Dat doe je met: <code>INTEGER PRIMARY KEY AUTOINCREMENT</code>



Hieronder een voorbeeld voor het maken van tabel <i>pizza</i> waarbij de <i>pizzacode</i> als primary key automatisch wordt genummerd:

CREATE TABLE pizza (
  pizzacode INTEGER PRIMARY KEY AUTOINCREMENT, 
  naam TEXT,
  omschrijving TEXT,
  basisprijs REAL)
  ;
  



### Opdracht Nieuwe tabel <i>kortingsbonnen</i> aanmaken

In deze opdrachten maken we een nieuw tabel toe voor *kortingsbonnen* waarin we informatie opslaan over de kortingsbonnen die in omloop zijn: <i>boncode</i>, hoeveel <i>korting</i> ze geven en tot welk <i>datum</i> de bon geldig is.


Schrijf een CREATE TABLE-statement voor de tabel <code>kortingsbon</code>. Bedenk welke kolommen je nodig hebt, en welke typen data je gebruikt. Denk aan:
<ul>
<li>Een primary key: <i>boncode</i>;
<li>automatisch doornummeren voor een unieke boncode (met AUTOINCREMENT);
<li>De juise datatype (TEXT, INTEGER, REAL) per kolom.
</ul>


<!-- ANTWOORD:
<pre><code class="language-sql">
CREATE TABLE kortingsbon (
    boncode INTEGER PRIMARY KEY AUTOINCREMENT,
    korting REAL,
    datum TEXT
);
</code></pre>
-->



 


## Gegevens in een tabel invoeren

Met <code>INSERT INTO... VALUES (...)</code> kun je gegevens in een tabel invoeren. Je geeft dan de naam van de tabel aan, en tussen haakjes de gegevens voor elk kolom in de tabel.

Let op:
<ul>
<li>Tekst moet tussen aanhalingstekens gezet worden. Bij getallen of kommagetallen hoeft dat niet.
<li>Bij een AUTOINCREMENT wordt automatisch genummerd (er wordt dus per gegeven een unieke primary key bepaald), daarom geef je daar de waarde <code>NULL</code> op.
</li>


Bijvoorbeeld, met de onderstaande code voegen we een pizza toe aan tabel <i>pizza</i>:
```SQL

INSERT INTO pizza VALUES (NULL, 'Pizza Hawaii', 'Ham en ananas', 8.50);
```
Toelichting:
<ul>
<li>Met <code>INSERT INTO</i> geven we aan dat we willen toevoegen aan tabel <i>pizza</i>;
<li>Met 'NULL' geven we aan dat er automatisch genummerd wordt;
<li>In de 2e kolom, namelijk <i>naam</i>, komt 'Pizza Hawaii' te staan;
<li>In de 3e kolom, namelijk <i>omschrijving</i> ...
<li> ...
</ul>

### Opdracht gegevens invullen aanmaken
Stel je hebt de tabel kortingsbon gemaakt met de volgende code.
```SQL
CREATE TABLE kortingsbon (
    boncode INTEGER PRIMARY KEY AUTOINCREMENT,
    korting REAL,
    datum TEXT
);
```

<ol type="alpha">
<li>Voeg een nieuwe kortingsbon toe met een korting van 0.50 euro en de datum 2025-12-20; 
<li>Haal met een SELECT de gegevens op van tabel <i>kortingsbon</i> en controleer dat het toevoegen van de kortingsbon goed is gegaan.
</ol>

Tips:
<ul>
<li>De kolom <i>boncode</i> heeft een AUTOINCREMENT en wordt dus automatisch doorgenummerd. Daarom geef je voor die gegegeven de waarde <code>NULL</code> op;
<li>Datum is een tekst en moet dus met aanhalingstekens opgegeven worden.
</ul>



<!-- ANTWOORD:
<ol type="alpha">
<li><pre><code class="language-sql">
INSERT INTO kortingsbon VALUES (NULL,0.50,"2025-12-20");
</code></pre>
<li><pre><code class="language-sql">
SELECT * 
FROM kortingsbon
</code></pre></li>
</ol>

-->




## Gegevens in een tabel aanpassen

Met UPDATE kun je gegevens in een tabel aanpassen. Je geeft dan de naam van de tabel aan. Daarna geeft je met SET aan wat de nieuwe waarde moet worden. Met WHERE geef je aan welke records aangepast moeten worden. Om één specifiek record aan te passen kun je hier het beste de 'primary key' gebruiken.

Bijvoorbeeld, met de volgende query wordt de pizzanaam van de pizza met code 1 aangepast naar "Hawaii"


UPDATE pizza
SET pizzanaam = "Hawaii"
WHERE pizzacode = 1;

Met `SELECT *` kan je controleren of het gelukt is:

SELECT *
FROM pizza



### Opdracht Pas de prijs van een pizza aan

Schrijf een query die voor de pizza met <i>pizzacode</i> gelijk aan 1, de <i>basisprijs</i> aanpast naar 9.50. Controleer daarna met `SELECT *` of het gelukt is.



<!-- ANTWOORD
<pre><code class="language-sql">
UPDATE pizza
SET basisprijs = 9.50
WHERE pizzacode = 1;
</code></pre>
-->



## Record uit een tabel verwijderen
Om een hele rij van gegevens uit een tabel te verwijderen, gebruik je `DELETE FROM`. Met `WHER`E geef je aan welk records verwijderd moeten worden. Om één specifiek record te verwijderen kun je hier het beste de 'primary key' gebruiken.

Bijvoorbeeld, met de volgende code worden alle gegevens over de pizza met <i>pizzacode</i> gelijk aan 1 verwijderd:

DELETE FROM Pizza
WHERE pizzacode = 1;


### Opdracht: Verwijder een pizza
Omdat deze nauwelijks besteld wordt, wil Danilo de "Pazza" pizza van het menu halen. Schrijf een query om de pizza uit de tabel te verwijderen. Controleer daarna met `SELECT *` of het gelukt is.

<!-- ANTWOORD
<pre><code class="language-sql">
-- verwijderen:
DELETE FROM pizza
WHERE naam = "Pazza";

-- check:
SELECT *
FROM pizza;
</code></pre>
-->



## Een tabel verwijderen
Met `DROP TABLE` kun je een hele tabel verwijderen, bijvoorbeeld tabel <i>klant</i>:

DROP TABLE klant


### Opdracht: Verwijder tabel <i>bodem</i>
Verwijder tabel <i>bodem</i>.
Probeer daarna met `SELECT *` de gegevens uit tabel <i>bodem</i> op te halen. Welk foutmelding krijg je.

<!-- ANTWOORD
<pre><code class="language-sql">
-- verwijderen:
DROP TABLE bodem;

-- check:
SELECT *
FROM bodem;

-- ophalen lukt niet omdat de tabel in de vorige stap verwijderd is.
</code></pre>
-->

## Overzicht van alle tabellen
In de schema hieronder zie je een overzicht van de tabellen.

<img src="https://raw.githubusercontent.com/rweeda/PythonIA/main/sql/DaniloIA_ERD.png" alt="overzicht tabellen" width="500"></p



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


Je kunt hier een filmpje bekijken waarin wordt uitgelegd wat primary en foreign keys zijn.
https://www.youtube.com/embed/obeOGxESGLI

<iframe width="560" height="315" src="https://www.youtube.com/embed/obeOGxESGLI?start=0&amp;end=150"></iframe>


### Opdracht Foreign keys bij Danilo's Pizzeria

Bekijk het overzicht van de tabellen en beantwoord de volgende vragen:
<img src="https://raw.githubusercontent.com/rweeda/PythonIA/main/sql/DaniloIA_ERD.png" alt="overzicht tabellen" width="500"></p



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

### ONDEWERP 5

## UITLEG  Gegevens uit meerdere tabellen combineren met JOIN

Tot nu toe heb je geleerd hoe je gegevens uit één tabel opvraagt. Maar soms wil je gegevens uit meerdere tabellen combineren. Daarvoor gebruik je `JOIN`.


Stel je voor: je hebt een lijst met bestellingen van pizza’s. Die staat in de tabel `besteldepizza`. Daarin zie je **welke pizza is besteld**, maar niet de naam — alleen een `pizzacode`.

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




### SAMENVATTING JOIN
JOIN is nodig om betekenisvolle combinaties van data uit verschillende tabellen te maken.



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

### Oefenopdracht
Toon de laagste prijs van een pizzabodem in de tabel `bodem`.


**Uitwerking:**
```sql
SELECT MIN(prijs) AS goedkoopste_bodem
FROM bodem;
```

## 🔹 2. `MAX()` – Maximumwaarde

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

### Oefenopdracht
Wat is de hoogste toeslag voor een pizzabodem? Gebruik de tabel `bodem`.


**Uitwerking:**
```sql
SELECT MAX(prijs) AS hoogste_toeslag
FROM bodem;
```


## `SUM()` – Totaal optellen

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

### Oefenopdracht
Bereken de totale prijs van alle bestellingen in de tabel `bestelling`.


**Uitwerking:**
```sql
SELECT SUM(totaalprijs) AS totaal_bestellingen
FROM bestelling;
```



## 4. `AVG()` – Gemiddelde

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

### Oefenopdracht
Bereken de gemiddelde toeslag voor bodems in de tabel `bodem`.



**Uitwerking:**
```sql
SELECT AVG(prijs) AS gemiddelde_bodem_toeslag
FROM bodem;
```


##  `COUNT(*)` – Aantal rijen tellen

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

###  Voorbeeldquery
```sql
SELECT DISTINCT plaats
FROM klant;
```

| plaats     |
|------------|
| Enschede   |
| Hengelo    |


### Oefenopdracht
Toon alle unieke bezorgdatums in de tabel `bestelling`.

**Uitwerking:**
```sql
SELECT DISTINCT datum
FROM bestelling;
```

---

## Rekenen met `+`, `-`, `*`, `/`

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



# UITLEG GROUP BY

GROUP BY groepeert rijen die dezelfde waarde hebben in één of meer kolommen. Daarna gebruik je functies zoals COUNT(), SUM(), AVG() of MAX() op elke groep. Tussen haakjes geef je aan op welk kolom de functie moet worden toegepast.

Bij GROUP BY staat vaak in de vraag het wordt 'per'. Bijvoorbeeld, hoeveel 'per' bestelling, of 'per klant'.


Bijvoorbeeld, de code hieronder geeft een overzicht van het aantal keer dat elk bodem besteld is. Het  groepeert alle `bodemcode`, en telt dan (COUNT) hoe vaak elke bodemcode is besteld:

SELECT bodemcode, COUNT(aantal) AS aantal_besteld
FROM besteldepizza
GROUP BY bodemcode;

| bodemcode | aantal_besteld |
|-----------|----------------|
| 1         | 2788           |
| 2         | 2905           |
| 3         | 140            |


De code hieronder geeft een overzicht van het totaal aantal bestelling per pizza. Deze groepeert `pizzacode`, en telt dan alle aantallen bij elkaar op (SUM).

SELECT pizzacode, SUM(aantal) AS totaal_besteld
FROM besteldePizza
GROUP BY pizzacode;


| pizzacode | totaal\_besteld |
| --------- | --------------- |
| 1         | 315              |
| 2         | 284             |
| 3         | 224              |
| …         | …               |





## Volgorde van keywords

De volgorde van de keywords is altijd:

SELECT ...
FROM ...
WHERE ...
GROUP BY ...
HAVING ...
ORDER BY ... DESC/ASC
LIMIT ... ;



### Opdracht
Toon van elk soort pizza hoeveel er gelijktijdig besteld worden, zoals in het overzicht hieronder.
De gegevens komen uit tabel `besteldepizza`.




| pizzacode | gemiddeld_aantal         |
|-----------|--------------------|
| 1         | 1.7119565217391304 |
| 2         | 1.7423312883435582 |
| 3         | 1.6115107913669064 |
| 4         | 1.7692307692307692 |
| 5         | 1.5813953488372092 |
| ...       | ...                |



ANTWOORD: 

SELECT pizzacode, AVG(aantal) AS gemiddeld_aantal
FROM besteldepizza
GROUP BY pizzacode;

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




### Opdracht
Toon per pizzacode het maximale aantal dat in één bestelling is besteld, zoals in de tabel hieronder.
De gegevens komen uit tabel `besteldePizza`.

| pizzacode | max\_per\_bestelling |
| --------- | -------------------- |
| 1         | 5                    |
| 2         | 6                    |
| 3         | 4                    |
| …         | …                    |



ANTWOORD:
SELECT pizzacode, MAX(aantal) AS max_per_bestelling
FROM besteldePizza
GROUP BY pizzacode;


### AFSLUITENDE OPDRACHTEN

Opdracht: Toon per klant (klantnummer) het hoogste aantal pizza’s dat hij/zij in één bestelling heeft besteld (gebruik MAX() en GROUP BY) zoals in het overzicht hieronder:

| klantnummer | max\_pizza\_per\_bestelling |
| ----------- | --------------------------- |
| 123         | 4                           |
| 135         | 6                           |
| 278         | 3                           |
| 312         | 5                           |
| 401         | 2                           |


Hint: Gebruik bestelling.bestelcode, klantnummer en besteldePizza.aantal via een JOIN.



ANTWOORD:
SELECT b.klantnummer, MAX(besteldePizza.aantal) AS max_pizza_per_bestelling
FROM bestelling JOIN besteldePizza  
	ON bestelling.bestelcode = besteldePizza.bestelcode
GROUP BY bestelling.klantnummer;


### Opdracht:
Welk bodem komt het vaakst voor bij pizza’s met de omschrijving 'American style'? Toon de bodemcode, omschrijving en het aantal keer dat die besteld is.



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

### Opdracht: naam van de bezorger en bijbehorende de klantgegevens: naam adres, postcode, plaats,


### Opdracht: overzicht van alle bestellingen: pizzanaam, formaat, bodem

