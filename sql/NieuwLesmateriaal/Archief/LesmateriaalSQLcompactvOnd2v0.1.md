
# ONDERWERP 2: SQL SELECT

# SQL

<p>SQL staat voor <i>Structured Query Language</i>. Het is de standaardtaal
om data in een database op te slaan, te bewerken en op te halen. Zo’n verzoek
aan de database noem je een <b>query</b>, wat letterlijk ‘vraag’ betekent in
het Engels. Als je een query schrijft, stel je dus eigenlijk een vraag aan de
database. Bijvoorbeeld: “Welke klanten wonen in Amsterdam?”</p>

<p>In deze cursus leer je hoe je SQL gebruikt binnen <b>SQLite</b> — een
eenvoudige, lichtgewicht databasesysteem. We beginnen met leren hoe je
informatie kunt ophalen. Daarna leer je ook hoe je gegevens kunt opslaan,
aanpassen en verwijderen. Tot slot ga je zelfs je eigen tabellen
aanmaken.</p>




<p>Bij de volgende opgaven maken we gebruik van de database van Danilo's
pizzeria. Hieronder zie je hoe de tabel <i>pizza</i> er uitziet met de
gegevens van een aantal pizza's erin.</p>

<!--De afbeelding hieronder toont de kolommen van tabel <i>pizza</i>:

<p><img
src="https://raw.githubusercontent.com/rweeda/PythonIA/main/sql/img/ERD_pizza.png"
alt="Tabel pizza" width="300"></p>


-->

<p><img
src="https://raw.githubusercontent.com/rweeda/PythonIA/main/sql/img/H1_tabel_pizza.png"
alt="Tabel pizza" width="800"></p>



<!-- | pizzacode | naam                  | omschrijving
| basisprijs |
|-----------|-----------------------|---------------------------------------------------------------------------|------------|
| 1         | Margherita            | Tomaat,kaas en oregano
| 6.0        | | 2         | Napoletana            | Tomaat, kaas, ansjovis,
olijven, kappertjes en oregano                   | 7.5        | | 3         |
Prosciutto            | Tomaat, kaas, ham en oregano
| 7.5        | | 4         | Funghi                | Tomaat, kaas,
champignons en oregano                                     | 7.5        | |
...       | ...                   | ...
| ...        | | 36        | Combinazione          | Eigen keuze pizza
| 10.5       |

-->


<p>Met een query kun je gegevens uit een tabel ophalen. Met SELECT kun je
data selecteren van een database en in een overzicht tonen. Met FROM geef je
aan uit welke tabel de informatie gehaald moet worden. Hoe dat werkt leer je
nu.</p>


---------------------------------------


## 2.1: Je eerste query

Om één kolom op te halen geef je na de SELECT de kolomnaam op, en na de FROM
de tabelnaam:

 ```SQL
SELECT kolomnaam FROM tabelnaam; ```

Run de code hieronder (dat kan met CRTR+ENTER of door bovenin op 'Run' te
drukken):

SELECT naam FROM pizza;

Daarmee krijg je zo'n volgende overzicht:

| naam                    | |-------------------------| | Margherita
| | Napoletana              | | Prosciutto              | | Funghi
| | Salame                  | | ...                     | | Combinazione
|



### Opdracht 2.1: Alle pizzacodes tonen <ol style="list-style-type:
lower-alpha"> <li>Toon alle pizzacodes (kolom <i>pizzacode</i>) in tabel
<i>pizza</i>. <li>Wat zie je als je naar de pizzacodes kijkt? Leg uit wat dat
te maken heeft met de 'primary key'. </ol>

| pizzacode | |-----------| | 1         | | 2         | | 3         | | 4
| | ...       | | 36        |



<p>Bekijk <a
href="https://rweeda.github.io/PythonIA/docs/IA_sql_oplossingen.html#opgave21"
target="_blank">hier</a> de voorbeelduitwerking.</p>

<!-- ANTWOORD

<ol style="list-style-type: lower-alpha"> <li> <pre><code
class="language-sql"> SELECT pizzacode FROM pizza; </code></pre> <li>Elke
pizzacode komt maar één keer voor. Dat betekent dat elke pizza een unieke
code heeft. Zo’n unieke code noemen we een primary key. Een primary key zorgt
ervoor dat je elk record in een tabel kunt herkennen. In dit geval herken je
elke pizza aan zijn pizzacode. </ol> -->

## 2.2 Meerdere kolommen uit een tabel halen Je kunt ook een meerdere
kolommen ophalen. Dat doe je als volgt:
 ```SQL
SELECT kolom1, kolom2, ... FROM tabelnaam; ```

### Opdracht 2.2: Menu printen

Maak een menu door de pizzanamen (kolom <i>naam</i>), <i>omschrijving</i> en
de prijs (kolom <i>basisprijs</i> uit het tabel <i>pizza</i> te halen.


| naam                   | omschrijving
| basisprijs |
|------------------------|----------------------------------------------------------------------------|------------|
| Margherita             | Tomaat,kaas en oregano
| 6.0        | | Napoletana             | Tomaat, kaas, ansjovis, olijven,
kappertjes en oregano                   | 7.5        | | Prosciutto
| Tomaat, kaas, ham en oregano                                              |
7.5        | | Funghi                 | Tomaat, kaas, champignons en oregano
| 7.5        | | ...                    | ...
| ...        | | Combinazione           | Eigen keuze pizza
| 10.5       |


<p>Bekijk <a
href="https://rweeda.github.io/PythonIA/docs/IA_sql_oplossingen.html#opgave22"
target="_blank">hier</a> de voorbeelduitwerking.</p> <!-- ANTWOORD:
<pre><code class="language-sql"> SELECT pizzanaam, omschrijving, basisprijs
FROM pizza; </code></pre> -->

### 2.3 Alle gegevens van een tabel ophalen

<p>Om alle kolommen op te halen gebruik je na de SELECT een '*'</p>

```SQL SELECT * FROM tabelnaam; ```

### Opdracht 2.3 Alle gegevens van tabel pizza ophalen

Toon alle kolommen met gegevens van tabel <i>pizza</i>, zoals in het
voorbeeld hieronder:

| pizzacode | naam                  | omschrijving
| basisprijs |
|-----------|-----------------------|---------------------------------------------------------------------------|------------|
| 1         | Margherita            | Tomaat,kaas en oregano
| 6.0        | | 2         | Napoletana            | Tomaat, kaas, ansjovis,
olijven, kappertjes en oregano                   | 7.5        | | 3         |
Prosciutto            | Tomaat, kaas, ham en oregano
| 7.5        | | 4         | Funghi                | Tomaat, kaas,
champignons en oregano                                     | 7.5        | |
...       | ...                   | ...
| ...        | | 36        | Combinazione          | Eigen keuze pizza
| 10.5       |

<p>Bekijk <a
href="https://rweeda.github.io/PythonIA/docs/IA_sql_oplossingen.html#opgave23"
target="_blank">hier</a> de voorbeelduitwerking.</p>

<!-- ANTWOORD: <pre><code class="language-sql"> SELECT * FROM pizza
</code></pre> -->


## 2.4: Commando's voor het ophalen van informatie

De taal voor het ophalen van informatie bestaat uit slechts 6 commando’s
waarmee je leert werken. De commando’s zijn:


<p><img
src="https://raw.githubusercontent.com/rweeda/PythonIA/main/sql/img/H1_commandos.png"
alt="Commando's voor het ophalen van informatie" width="400"></p>


Je hoeft niet alle commando's te gebruiken, maar ze staan wel <b>altijd in
deze volgorde</b>.




## 2.5 Voorwaarden met de WHERE

<p>Met WHERE kun je beperken welke rijen getoond moet worden. Met WHERE kun
je een voorwaarde aangeven, bijvoorbeeld: ’waarbij de informatie voldoet aan
...’</p>

<p>Je geeft altijd eerst een SELECT op voor de gegevens die opgehaald moeten
worden, dan met FROM de tabel waaruit de gegevens moeten komen, en met WHERE
welke beperking er is.</p>


<p>Bijvoorbeeld, met de volgende query tonen we alle pizza's die precies 8
euro kosten:</p ```SQL SELECT * FROM pizza WHERE basisprijs=8 ```

| pizzacode | naam           | omschrijving
| basisprijs |
|-----------|----------------|----------------------------------------------------------------------------|------------|
| 10        | Capricciosa    | Tomaat, kaas, ham, champignons, paprika,
artisjokken en oregano          | 8.0        | | 11        | Primavera      |
Tomaat, kaas, ham, salami en oregano                                     |
8.0        | | 12        | Venezia        | Tomaat, kaas, ham, champignons,
ananas en oregano                        | 8.0        | | ...       | ...
| ...                                                                      |
8.0        | | 30        | Romana         | Tomaat, kaas, spek, uien,
champignons, ei en oregano                     | 8.0        |




### Opdracht 2.4: Omschrijving van een Inferno pizza Schrijf een query om de
omschrijving van de pizza 'Inferno' te tonen, zoals in het voorbeeld
hieronder.

| omschrijving | |--------------| | Tomaat, kaas, ham, spaanse peper,
kappertjes, salami, olijven en oregano  |

<p>Bekijk <a
href="https://rweeda.github.io/PythonIA/docs/IA_sql_oplossingen.html#opgave24"
target="_blank">hier</a> de voorbeelduitwerking.</p>

<!-- ANTWOORD: <pre><code class="language-sql"> ANTWOORD: SELECT omschrijving
FROM pizza WHERE naam='Inferno' </code></pre> -->




## 2.6 Kennis maken met de andere tabellen


<p>Danilo's pizzeria database bestaat uit meer tabellen dan alleen
<i>pizza</i>. Er wordt ook bijvoorbeeld ook informatie opgeslagen over
klanten, berzorgers en bestellingen. In de afbeelding hieronder zie je alle 7
tabellen.</p>


<p> <a
href="https://raw.githubusercontent.com/rweeda/PythonIA/main/sql/img/DaniloIA_ERD.png"
target="_blank">
  <img src="https://raw.githubusercontent.com/rweeda/PythonIA/main/sql/img/DaniloIA_ERD.png" alt="Klik om in een nieuw venster te openen" width="1000"/>
</a></p>



### Opdracht 2.5: Alle gegevens uit tabel <i>klant</i> <p>Toon alle gegevens
uit tabel <i>klant</i>.


<p>Bekijk <a
href="https://rweeda.github.io/PythonIA/docs/IA_sql_oplossingen.html#opgave25"
target="_blank">hier</a> de voorbeelduitwerking.</p>

<!-- ANTWOORD: <pre><code class="language-sql"> SELECT * FROM klant;
</code></pre> -->


### Opdracht 2.6: Alle klanten uit Enschede

<p>Toon het adres, de postcode en de plaats van alle klanten die in Enschede
wonen, zoals hieronder. Tip: de gegevens komen uit tabel <i>klant</i>.</p> |
adres              | postcode | woonplaats    |
|--------------------|----------|-----------| | Gladioolstraat 11  | 3742TC
| Enschede  | | Banckertlaan 7     | 3742MG   | Enschede  | | Talmalaan 11
| 3741TX   | Enschede  | | Krugerlaan 9       | 3743CJ   | Enschede  | |
Zandvoortweg 199   | 3741BE   | Enschede  |





<p>Bekijk <a
href="https://rweeda.github.io/PythonIA/docs/IA_sql_oplossingen.html#opgave26"
target="_blank">hier</a> de voorbeelduitwerking.</p>

<!-- ANTWOORD: <pre><code class="language-sql"> SELECT adres, postcode,
woonplaats FROM klant WHERE plaats='Enschede'; </code></pre> -->


### Opdracht 2.7: Wachtwoord uit tabel bezorger. Toon het wachtwoord van de
bezorger met de naam Ronald Marbus, zoals hieronder.<br> | wachtwoord  |
|-------------| | R0nalt      |




Tips: <ul> <li>de gegevens komen uit tabel <i>bezorger</i>,</li> <li>toon
eerst alle kolommen, en kies dan welk kolom je nodig hebt.</li> </ul>




<p>Bekijk <a
href="https://rweeda.github.io/PythonIA/docs/IA_sql_oplossingen.html#opgave27"
target="_blank">hier</a> de voorbeelduitwerking.</p>

<!-- ANTWOORD: <pre><code class="language-sql"> SELECT wachtwoord FROM
bezorger WHERE naam = 'Ronald Marbus'; </code></pre> -->

## 2.7: Commentaar

Net als bij programmeren, kun je in SQL ook commentaar opnemen in je code.
Dit doe je door twee streepjes ‘--’ ervoor te zetten. Dat ziet er dan zo uit
(zie regel 2):</p> SELECT * FROM pizza; -- dit is de tabelnaam


<!-- <p>Je kunt ook <code>/*</code> ervoor en <code>*/</code> erna zetten.
Dat ziet er dan zo uit (zie regel 2):</p> SELECT * FROM pizza; /* dit is de
tabelnaam */ -->

## 2.8: Nette code <p>Net als andere programmeertalen, zijn er afspraken om
nette en leesbare queries te schrijven.</p>



<ol> <li>Schrijf de SQL opdrachten altijd met HOOFDLETTERS. <li>Schrijf elke
opdracht op een nieuwe regel. <li>Als je meerdere items achter een SELECT of
FROM opdracht hebt staan dan moet je deze scheiden met een komma. <li>Gebruik
spaties om de leesbaarheid tussen items te vergroten. <li>Schrijf commentaar
in je query om uit te leggen wat je doet (vooral bij WHERE en GROUP BY).
<li>Je mag een query afsluiten met een puntkomma (;), maar dat hoeft bij
eenvoudige queries niet. </ol>

Hieronder een voorbeeld van nette code: <code> SELECT naam, basisprijs FROM
pizza -- Alleen pizza's bekijken die goedkoper zijn dan 10 euro -- EN duurder
dan 8 euro 50 WHERE basisprijs <= 10 AND basisprijs >= 8.50; </code>

### Opdracht 2.8 Query netjes opschrijven <ol style="list-style-type:
lower-alpha"> De query hieronder is niet zo netjes opgeschreven. <li>Voer de
onderstaande query uit, dan zul je zien dat de query het gewoon doet. Bekijk
de uitkomst. <li>Pas deze query aan zodat hij voldoet aan alle voorwaarden
van nette code. <li>Voeg bij elke regel commentaar toe om aan te geven voor
welk voorwaarde je het hebt aangepast. </ol>


naam,basisprijs From pizza wHERe basisprijs<8


<p>Bekijk <a
href="https://rweeda.github.io/PythonIA/docs/IA_sql_oplossingen.html#opgave31"
target="_blank">hier</a> de voorbeelduitwerking.</p>

<!--ANTWOORD -- (1) SQL commando in hoofdletters, (4) spatie na de komma
SELECT naam, basisprijs -- (2) Elke SQL commando op een nieuwe regel (en in
hoofdletters) FROM pizza -- (4) spaties in de voorwaarde zodat het beter
leesbaar is -- (6) en afsluiten met een ; (maar dat hoeft niet) WHERE
basisprijs < 8; -->


## 2.9: Fouten opsporen

Het kan voorkomen dat er een fout in je code zit. Hier zijn wat tips om die
op te sporen: <ul> <li>Krijg je een foutmelding? Lees die goed. Vaak staat er
welke regel of welk onderdeel fout is. <li>Soms krijg je geen foutmelding,
maar ook geen resultaten — dan heb je een denkfout in je code zitten en vraag
je iets op wat er niet is. <li>Als iets niet werkt, test dan een stukje
tegelijk. Begin met alleen `SELECT * FROM ...`, pas als dat werkt voor je
daarna stukje voor stukje de WHERE-voorwaarden toe. <li>Controleer de tabel-
en kolomnamen. Typefouten in kolomnamen komen vaak voor. Met `SELECT * FROM
...` kun je de kolomnamen bekijken. <li>Zet tijdelijk delen van je code in
commentaar (mert `--`) om te testen wat het probleem veroorzaakt. <li>SQLite
is niet hoofdlettergevoelig voor sleutelwoorden, maar wel voor strings,
bijvoorbeeld 'enschede' in plaats van 'Enschede'. </ul>


### Opdracht 2.8: Fout in query (1) Piet wil met de query hieronder een
overzicht van alle pizza's die minder dan 7 euro kosten. Wat is de fout in
deze query? Los die op. ``` sql SELECT naam basisprijs < 7.0 FROM WHERE
pizza; ```

<p>Bekijk <a
href="https://rweeda.github.io/PythonIA/docs/IA_sql_oplossingen.html#opgave28"
target="_blank">hier</a> de voorbeelduitwerking.</p>


<!-- ANTWOORD: De fout zat in de volgorde van de regels code. <pre><code
class="language-sql"> SELECT naam FROM pizza WHERE basispijs < 7.0;
</code></pre> -->

### Opdracht 2.9: Fout in query (2) Lukas wil alle klantgegevens van klanten
in Nijmegen zien. Hij gebruikt daarvoor het onderstaande code, maar dat
levert niets op! Waarom niet? Pas de code aan zodat het een juiste overzicht
geeft zoals hieronder.


SELECT * FROM klant WHERE woonplaats = 'nijmegen';

<ol type="alpha"> <li>De kolom woonplaats bestaat niet <li>De woonplaats moet
met een hoofdletter geschreven zijn <li>Er staan geen klanten in de database
<li>Er mogen geen spaties om de '='-teken staan </ol>

| klantnummer | wachtwoord   | klantnaam         | adres                   |
postcode | woonplaats | telefoon     |
|-------------|--------------|-------------------|--------------------------|----------|------------|--------------|
| 425         | M8eoyfuVd5   | Nina Vos          | Graafseweg 115           |
6531ZG   | Nijmegen   | 06-63017195  | | 426         | BV8aYhfTeH   | Noa de
Boer       | Daalseweg 103            | 6521GS   | Nijmegen   | 06-87240602
| | 427         | IcMD8WuNRk   | Bram Kuipers      | Heyendaalseweg 300
| 6525EC   | Nijmegen   | 06-13617853  | | ...         | ...   | ...     |
...     | ...   | ...   | ...  |



<p>Bekijk <a
href="https://rweeda.github.io/PythonIA/docs/IA_sql_oplossingen.html#opgave29"
target="_blank">hier</a> de voorbeelduitwerking.</p>

<!-- ANTWOORD: b De woonplaatsen zijn met een hoofdletter geschreven (bv.
'Nijmegen'). SQL vergelijkt tekst hoofdlettergevoelig. In dit geval zijn er
klanten die in 'nijmegen' wonen, maar wel in 'Nijmegen'.

De juiste query is:

<pre><code class="language-sql"> SELECT * FROM klant WHERE woonplaats =
'Nijmegen'; -->


### Opdracht 2.10: Fout in query (2) De code hieronder bevat een fout. Run de
code, lees de foutmelding en herstel de fout.

``` sql SELECT naam FROM pizzas WHERE basispijs < 7.0; </code></pre> ```

<p>Bekijk <a
href="https://rweeda.github.io/PythonIA/docs/IA_sql_oplossingen.html#opgave210"
target="_blank">hier</a> de voorbeelduitwerking.</p>


<!-- ANTWOORD: De fout zat in de naam van de tabel. <pre><code
class="language-sql"> SELECT naam FROM pizza WHERE basispijs < 7.0;
</code></pre> -->



### Opdracht 2.11: Fout in query (3) De code hieronder bevat een fout. Run de
code, lees de foutmelding en herstel de fout.

``` sql SELECT pizzanaam FROM pizza WHERE basispijs < 7.0; ```

<p>Bekijk <a
href="https://rweeda.github.io/PythonIA/docs/IA_sql_oplossingen.html#opgave211"
target="_blank">hier</a> de voorbeelduitwerking.</p>


<!-- ANTWOORD: De fout zat in de kolomnaam. <pre><code class="language-sql">
SELECT naam FROM pizza WHERE basispijs < 7.0; </code></pre> -->

### Opdracht 2.11: Kolomnamen opzoeken Je wil weten welke kolomnamen er in de
tabel <i>bestelling</i> zitten. Welke query helpt je hierbij?


<p>Bekijk <a
href="https://rweeda.github.io/PythonIA/docs/IA_sql_oplossingen.html#opgave211"
target="_blank">hier</a> de voorbeelduitwerking.</p>


<!-- ANTWOORD: Met de volgende query krijg je een overzicht van de hele
tabel, inclusief de kolomnamen: <pre><code class="language-sql"> SELECT *
FROM bestelling; </code></pre> -->
