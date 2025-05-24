
# ONDERWERP 2: SQL SELECT

# 2.1: SQL

<p>SQL staat voor <i>Structured Query Language</i>. Het is de standaardtaal
om data in een database op te slaan, te bewerken en op te halen. Zo’n verzoek
aan de database noem je een <b>query</b>, wat letterlijk ‘vraag’ betekent in
het Engels. Als je een query schrijft, stel je dus eigenlijk een vraag aan de
database. Bijvoorbeeld: “Welke klanten wonen in Amsterdam?”. Met SQL haal je uit bestaande tabellen gegevens en maak je een overzicht hiervan.</p>


<img
src="https://raw.githubusercontent.com/rweeda/PythonIA/main/sql/img/H1_DbaseToTabel.png"
alt="Gegevens uit een database halen met SQL" width="300" align="right">

<p>In deze cursus leer je hoe je SQL gebruikt binnen <b>SQLite</b> — een
eenvoudige, lichtgewicht databasesysteem. We beginnen met leren hoe je
informatie kunt ophalen. Daarna leer je ook hoe je gegevens kunt opslaan,
aanpassen en verwijderen. Tot slot ga je zelfs je eigen tabellen
aanmaken.</p>




<p>Bij de volgende opgaven maken we gebruik van de database van Danilo's
pizzeria. Hieronder zie je hoe de tabel <i>pizza</i> eruitziet met de
gegevens van een aantal pizza’s erin.</p>

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


## 2.2: Je eerste SQL query

Om één kolom op te halen en deze te tonen, geef je na de SELECT de kolomnaam op, en na de FROM
de tabelnaam:




```sql
SELECT kolomnaam FROM tabelnaam;
```

Voer de code hieronder uit (dat kan met CTRL+ENTER of door bovenin op 'Run' te
drukken):



TODO BLOK
SELECT naam FROM pizza;



Daarmee krijg je zo'n volgende overzicht:

<table border="1">
  <thead>
    <tr>
      <th>naam</th>
    </tr>
  </thead>
  <tbody>
    <tr><td>Margherita</td></tr>
    <tr><td>Napoletana</td></tr>
    <tr><td>Prosciutto</td></tr>
    <tr><td>Funghi</td></tr>
    <tr><td>Salame</td></tr>
    <tr><td>...</td></tr>
    <tr><td>Combinazione</td></tr>
  </tbody>
</table>


### Opdracht 2.2.1: Alle pizzacodes tonen 

<table>
    <td valign="top" width="35%">
<ol style="list-style-type:lower-alpha"> 
<li>Geef een overzicht van alle pizzacodes (kolom <i>pizzacode</i>) in tabel
<code>pizza</code>, zoals in het voorbeeld hiernaast.
<li>Wat zie je als je naar de pizzacodes kijkt? Leg uit wat dat
te maken heeft met de 'primary key'.
</ol>
</td>    <td width="65%">
<table border="1">
  <thead>
    <tr>
      <th>pizzacode</th>
    </tr>
  </thead>
  <tbody>
    <tr><td>1</td></tr>
    <tr><td>2</td></tr>
    <tr><td>3</td></tr>
    <tr><td>...</td></tr>
  </tbody>
</table>

</tr>
</table>

<p>Bekijk <a
href="https://rweeda.github.io/PythonIA/docs/IA_sql_oplossingen.html#opgave221"
target="_blank">hier</a> de voorbeelduitwerking.</p>

<!-- ANTWOORD

<ol style="list-style-type: lower-alpha"> <li> <pre><code
class="language-sql"> SELECT pizzacode FROM pizza; </code></pre> <li>Elke
pizzacode komt maar één keer voor. Dat betekent dat elke pizza een unieke
code heeft. Zo’n unieke code noemen we een primary key. Een primary key zorgt
ervoor dat je elk record in een tabel kunt herkennen. In dit geval herken je
elke pizza aan zijn pizzacode. </ol> -->

## 2.3 Meerdere kolommen uit een tabel halen

Je kunt ook een meerdere kolommen ophalen. Dat doe je als volgt:

```sql
SELECT kolom1, kolom2, ... FROM tabelnaam;
```

### Opdracht 2.3.1 Menu printen
<table width="100%">
  <tr>
    <td valign="top" width="35%">
Maak een menu door de <i>naam</i> en <i>basisprijs</i> van elk pizza uit het tabel `pizza` te halen, zoals hiernaast.
    </td>
    <td width="65%">
      <table border="1">
        <thead>
          <tr>
            <th>naam</th>
            <th>basisprijs</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <td>Margherita</td>
            <td>6.0</td>
          </tr>
          <tr>
            <td>Napoletana</td>
            <td>7.5</td>
          </tr>
          <tr>
            <td>Prosciutto</td>
            <td>7.5</td>
          </tr>
          <tr>
            <td>Funghi</td>
            <td>7.5</td>
          </tr>
          <tr>
            <td>...</td>
            <td>...</td>
          </tr>
          <tr>
            <td>Combinazione</td>
            <td>10.5</td>
          </tr>
        </tbody>
      </table>
    </td>
  </tr>
</table>


<p>Bekijk <a
href="https://rweeda.github.io/PythonIA/docs/IA_sql_oplossingen.html#opgave231"
target="_blank">hier</a> de voorbeelduitwerking.</p> <!-- ANTWOORD:
<pre><code class="language-sql"> SELECT pizzanaam, omschrijving, basisprijs
FROM pizza; </code></pre> -->

### 2.4 Alle gegevens van een tabel ophalen

<p>Om alle kolommen op te halen gebruik je na de SELECT een '*'</p>

```SQL 
SELECT * 
FROM tabelnaam;
```

### Opdracht 2.4.1 Alle gegevens van tabel pizza ophalen
<table width="100%">
  <tr><td style="text-align:left; vertical-align:top; font-size:1rem;" width="35%">
Toon alle kolommen met gegevens van tabel <code>pizza</code>, zoals in het
voorbeeld hiernaast.
    </td>
    <td width="65%">
      <table border="1">
        <thead>
          <tr>
            <th>naam</th>
            <th>omschrijving</th>
            <th>basisprijs</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <td>Margherita</td>
            <td>Tomaat, kaas en oregano</td>
            <td>6.0</td>
          </tr>
          <tr>
            <td>Napoletana</td>
            <td>Tomaat, kaas, ansjovis, olijven, kappertjes en oregano</td>
            <td>7.5</td>
          </tr>
          <tr>
            <td>Prosciutto</td>
            <td>Tomaat, kaas, ham en oregano</td>
            <td>7.5</td>
          </tr>
          <tr>
            <td>Funghi</td>
            <td>Tomaat, kaas, champignons en oregano</td>
            <td>7.5</td>
          </tr>
          <tr>
            <td>...</td>
            <td>...</td>
            <td>...</td>
          </tr>
          <tr>
            <td>Combinazione</td>
            <td>Eigen keuze pizza</td>
            <td>10.5</td>
          </tr>
        </tbody>
      </table>
    </td>
  </tr>
</table>
<p>Bekijk <a
href="https://rweeda.github.io/PythonIA/docs/IA_sql_oplossingen.html#opgave241"
target="_blank">hier</a> de voorbeelduitwerking.</p>

<!-- ANTWOORD: <pre><code class="language-sql"> SELECT * FROM pizza
</code></pre> -->


## 2.5: Commando's voor het ophalen van informatie

De taal voor het ophalen van informatie bestaat uit slechts 6 commando’s
waarmee je leert werken. De commando’s zijn:


<p><img
src="https://raw.githubusercontent.com/rweeda/PythonIA/main/sql/img/H1_commandos.png"
alt="Commando's voor het ophalen van informatie" width="400"></p>


Je hoeft niet alle commando's te gebruiken, maar ze staan wel <b>altijd in
deze volgorde</b>.




## 2.6: Voorwaarden met de WHERE

<p>Met WHERE kun je beperken welke rijen getoond moet worden. Met WHERE kun
je een voorwaarde aangeven, bijvoorbeeld: 'waarbij de informatie voldoet aan
...'</p>

<p>Je geeft altijd eerst een SELECT op voor de gegevens die opgehaald moeten
worden, dan met FROM de tabel waaruit de gegevens moeten komen, en met WHERE
welke beperking geldt.</p>

<table width="100%">
  <tr><td style="text-align:left; vertical-align:top; font-size:1rem;" width="35%">
<p>Bijvoorbeeld, met de volgende query tonen we alle pizza's die precies 8
euro kosten:</p>

```SQL 
 SELECT * 
 FROM pizza
 WHERE basisprijs=8;
 ```
  </td>
  <td width="65%">
<table border="1">
  <thead>
    <tr>
      <th>pizzacode</th>
      <th>naam</th>
      <th>omschrijving</th>
      <th>basisprijs</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>10</td>
      <td>Capricciosa</td>
      <td>Tomaat, kaas, ham, champignons, paprika, artisjokken en oregano</td>
      <td>8.0</td>
    </tr>
    <tr>
      <td>11</td>
      <td>Primavera</td>
      <td>Tomaat, kaas, ham, salami en oregano</td>
      <td>8.0</td>
    </tr>
    <tr>
      <td>12</td>
      <td>Venezia</td>
      <td>Tomaat, kaas, ham, champignons, ananas en oregano</td>
      <td>8.0</td>
    </tr>
    <tr>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>8.0</td>
    </tr>
    <tr>
      <td>30</td>
      <td>Romana</td>
      <td>Tomaat, kaas, spek, uien, champignons, ei en oregano</td>
      <td>8.0</td>
    </tr>
  </tbody>
</table>
</td></tr></table>


### Opdracht 2.6.1 Omschrijving van een Inferno pizza tonen 
<table>
<tr><td valign="top" width=35%>
Schrijf een query om de
omschrijving van de pizza 'Inferno' te tonen, zoals in het voorbeeld
hiernaast.
</td><td>
<table border="1">
  <thead>
    <tr>
      <th>omschrijving</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Tomaat, kaas, ham, spaanse peper, kappertjes, salami, olijven en oregano</td>
    </tr>
  </tbody>
</table>
</tr>
</table>

<p>Bekijk <a
href="https://rweeda.github.io/PythonIA/docs/IA_sql_oplossingen.html#opgave24"
target="_blank">hier</a> de voorbeelduitwerking.</p>

<!-- ANTWOORD: 

<pre><code class="language-sql">SELECT omschrijving
FROM pizza WHERE naam='Inferno' </code></pre> 
-->




## 2.7: Kennis maken met de andere tabellen


<p>Danilo's pizzeria database bestaat uit meer tabellen dan alleen
<i>pizza</i>. Er wordt ook bijvoorbeeld informatie opgeslagen over
klanten, bezorgers en bestellingen. In de afbeelding hieronder zie je alle 7
tabellen.</p>


<p> <a
href="https://raw.githubusercontent.com/rweeda/PythonIA/main/sql/img/DaniloIA_ERD.png"
target="_blank">
  <img src="https://raw.githubusercontent.com/rweeda/PythonIA/main/sql/img/DaniloIA_ERD.png" alt="Klik om in een nieuw venster te openen" width="1000"/>
</a></p>



### Opdracht 2.7.1 Alle gegevens uit tabel <code>klant</code> tonen
<table>
<tr><td valign="top" width=35%>
<p>Toon alle gegevens
uit tabel <code>klant</code>, zoals in het voorbeeld hiernaast.
</td><td width="65%">
</td>
</tr>
</table>

<p>Bekijk <a
href="https://rweeda.github.io/PythonIA/docs/IA_sql_oplossingen.html#opgave271"
target="_blank">hier</a> de voorbeelduitwerking.</p>

<!-- ANTWOORD: <pre><code class="language-sql"> SELECT * FROM klant;
</code></pre> -->


### Opdracht 2.7.2: Alle klanten uit Enschede tonen

<table>
<tr><td valign="top" width=35%>Toon het adres, de postcode en de plaats van alle klanten die in Enschede
wonen, zoals hiernaast. Tip: De gegevens komen uit tabel <code>klant</code>.</p> 
</td><td width="65%">
<table border="1">
  <thead>
    <tr>
      <th>adres</th>
      <th>postcode</th>
      <th>woonplaats</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Gladioolstraat 11</td>
      <td>3742TC</td>
      <td>Enschede</td>
    </tr>
    <tr>
      <td>Banckertlaan 7</td>
      <td>3742MG</td>
      <td>Enschede</td>
    </tr>
    <tr>
      <td>Talmalaan 11</td>
      <td>3741TX</td>
      <td>Enschede</td>
    </tr>
    <tr>
      <td>Krugerlaan 9</td>
      <td>3743CJ</td>
      <td>Enschede</td>
    </tr>
    <tr>
      <td>Zandvoortweg 199</td>
      <td>3741BE</td>
      <td>Enschede</td>
    </tr>
  </tbody>
</table>
</tr></table>




<p>Bekijk <a
href="https://rweeda.github.io/PythonIA/docs/IA_sql_oplossingen.html#opgave272"
target="_blank">hier</a> de voorbeelduitwerking.</p>

<!-- ANTWOORD: <pre><code class="language-sql"> SELECT adres, postcode,
woonplaats FROM klant WHERE plaats='Enschede'; </code></pre> -->


### Opdracht 2.7.3 Wachtwoord van een bezorger
<table width="100%">
        <tr>
          <td valign="top" width="35%">
      Toon het wachtwoord van de
      bezorger met de naam Ronald Marbus, zoals hiernaast.
      Tips: <ul> <li>De gegevens komen uit tabel <code>bezorger</code>,</li> <li>toon
eerst alle kolommen, en kies dan welk kolom je nodig hebt.</li> </ul>
      </td>
          <td width="65%">
      <table border="1">
        <thead>
          <tr>
            <th>wachtwoord</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <td>R0nalt</td>
          </tr>
        </tbody>
      </table>
    </td>
  </tr>
</table>






<p>Bekijk <a
href="https://rweeda.github.io/PythonIA/docs/IA_sql_oplossingen.html#opgave273"
target="_blank">hier</a> de voorbeelduitwerking.</p>

<!-- ANTWOORD: <pre><code class="language-sql"> SELECT wachtwoord FROM
bezorger WHERE naam = 'Ronald Marbus'; </code></pre> -->

## 2.8: Commentaar
<p>In SQL kun je met <code>--</code> commentaar opnemen in je code.  
Alles na <code>--</code> op dezelfde regel wordt genegeerd door SQL, zie regel 2 hieronder.</p> 

SELECT * 
FROM pizza; -- dit is commentaar

Je kunt commentaar gebruiken om aantekeningen te maken. Maar je kan het ook gebruiken om code tijdelijk uit te schakelen, als je bijvoorbeeld een fout in je code wilt opsporen.

<!--
<p>Je kunt ook <code>/*</code> ervoor en <code>*/</code> erna zetten.
Dat ziet er dan zo uit (zie regel 2):</p>

SELECT * FROM pizza; /* dit is de
tabelnaam */ -->

## 2.9: Nette code 

<p>Net als andere programmeertalen, zijn er afspraken om
nette en leesbare queries te schrijven.</p>



<ol> 
<li>Schrijf de SQL-opdrachten altijd met HOOFDLETTERS. 
<li>Schrijf elke opdracht op een nieuwe regel;
<li>Als je meerdere items achter een SELECT of FROM opdracht hebt staan dan moet je deze scheiden met een komma;
<li>Gebruik spaties om de leesbaarheid tussen items te vergroten;
<li>Schrijf met <code>--</code> commentaar in je query om uit te leggen wat je doet (vooral bij WHERE en GROUP BY);
<li>Sluit een query af met een puntkomma <code>;</code>.
</ol>

Hieronder een voorbeeld van nette code: 

```SQL
SELECT naam, basisprijs FROM
pizza -- Alleen pizza's bekijken die goedkoper zijn dan 10 euro -- EN duurder
dan 8 euro 50 WHERE basisprijs <= 10 AND basisprijs >= 8.50;
```

### Opdracht 2.9.1 Query netjes opschrijven 

De query hieronder is niet zo netjes opgeschreven.
<ol style="list-style-type: lower-alpha"> 
<li>Voer de
onderstaande query uit, dan zul je zien dat de query het gewoon doet. Bekijk
de uitkomst. 
<li>Pas deze query aan zodat hij voldoet aan alle voorwaarden
van nette code. 
<li>Voeg bij elke regel commentaar toe om aan te geven voor
welk voorwaarde je het hebt aangepast. 
</ol>


naam,basisprijs From pizza wHERe basisprijs<8


<p>Bekijk <a
href="https://rweeda.github.io/PythonIA/docs/IA_sql_oplossingen.html#opgave31"
target="_blank">hier</a> de voorbeelduitwerking.</p>

<!--ANTWOORD -- (1) SQL commando in hoofdletters, (4) spatie na de komma
SELECT naam, basisprijs -- (2) Elke SQL commando op een nieuwe regel (en in
hoofdletters) FROM pizza -- (4) spaties in de voorwaarde zodat het beter
leesbaar is -- (6) en afsluiten met een ; (maar dat hoeft niet) WHERE
basisprijs < 8; -->


## 2.10: Fouten opsporen

Het kan voorkomen dat er een fout in je code zit. Hier zijn wat tips om die
op te sporen: 
<ul> 
<li>Krijg je een foutmelding? Lees die goed. Vaak staat er
welke regel of welk onderdeel fout is. 
<li>Soms krijg je geen foutmelding,
maar ook geen resultaten — dan heb je een denkfout in je code zitten en vraag
je iets op wat er niet is. 
<li>Als iets niet werkt, test dan een stukje
tegelijk. Begin met alleen `SELECT * FROM ...`, pas als dat werkt voor je
daarna stukje voor stukje de WHERE-voorwaarden toe.
 <li>Controleer de tabel-
en kolomnamen. Typefouten in kolomnamen komen vaak voor. Met `SELECT * FROM
...` kun je de kolomnamen bekijken. 
<li>Zet tijdelijk delen van je code in
commentaar (met `--`) om te testen wat het probleem veroorzaakt. 
<li>SQLite
is niet hoofdlettergevoelig voor sleutelwoorden, maar wel voor strings,
bijvoorbeeld 'enschede' in plaats van 'Enschede'. 
</ul>


### Opdracht 2.10.1 Fout in query (1) 

Piet wil met de query hieronder een
overzicht van alle pizza's die minder dan 7 euro kosten. Wat is de fout in
deze query? Los die op.

SELECT naam basisprijs < 7.0 FROM WHERE
pizza;

<p>Bekijk <a
href="https://rweeda.github.io/PythonIA/docs/IA_sql_oplossingen.html#opgave2101"
target="_blank">hier</a> de voorbeelduitwerking.</p>


<!-- ANTWOORD: De fout zat in de volgorde van de regels code. <pre><code
class="language-sql"> SELECT naam FROM pizza WHERE basispijs < 7.0;
</code></pre> -->

### Opdracht 2.10.2 Fout in query (2) 

<table width="100%">
  <tr>
    <td valign="top" width="35%">
Lukas wil alle klantgegevens van klanten
in Nijmegen zien, zoals het overzicht. Hij gebruikt daarvoor het onderstaande code, maar dat
levert niets op!

<ol style="list-style-type: lower-alpha"> 
<li>Waarom levert het niets op? Kies de juiste antwoord.
  <ol style="list-style-type: upper-alpha">
  <li> De kolom woonplaats bestaat niet <li>De woonplaats moet
  met een hoofdletter geschreven zijn <li>Er staan geen klanten in de database
  <li>Er mogen geen spaties om de '='-teken staan 
  </ol>
  <li>Pas de code aan zodat het de juiste overzicht
  geeft.
  </ol>
</ol>
    </td>
    <td width="65%">
      <table border="1">
        <thead>
          <tr>
            <th>klantnummer</th>
            <th>wachtwoord</th>
            <th>klantnaam</th>
            <th>adres</th>
            <th>postcode</th>
            <th>woonplaats</th>
            <th>telefoon</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <td>425</td>
            <td>M8eoyfuVd5</td>
            <td>Nina Vos</td>
            <td>Graafseweg 115</td>
            <td>6531ZG</td>
            <td>Nijmegen</td>
            <td>06-63017195</td>
          </tr>
          <tr>
            <td>426</td>
            <td>BV8aYhfTeH</td>
            <td>Noa de Boer</td>
            <td>Daalseweg 103</td>
            <td>6521GS</td>
            <td>Nijmegen</td>
            <td>06-87240602</td>
          </tr>
          <tr>
            <td>427</td>
            <td>IcMD8WuNRk</td>
            <td>Bram Kuipers</td>
            <td>Heyendaalseweg 300</td>
            <td>6525EC</td>
            <td>Nijmegen</td>
            <td>06-13617853</td>
          </tr>
          <tr>
            <td>...</td>
            <td>...</td>
            <td>...</td>
            <td>...</td>
            <td>...</td>
            <td>...</td>
            <td>...</td>
          </tr>
        </tbody>
      </table>
    </td>
  </tr>
</table>

TODO GEGEVEN:
SELECT *
FROM klant 
WHERE woonplaats = 'nijmegen';





<p>Bekijk <a
href="https://rweeda.github.io/PythonIA/docs/IA_sql_oplossingen.html#opgave2102"
target="_blank">hier</a> de voorbeelduitwerking.</p>

<!-- ANTWOORD: b De woonplaatsen zijn met een hoofdletter geschreven (bv.
'Nijmegen'). SQL vergelijkt tekst hoofdlettergevoelig. In dit geval zijn er
klanten die in 'nijmegen' wonen, maar wel in 'Nijmegen'.

De juiste query is:

<pre><code class="language-sql"> SELECT * FROM klant WHERE woonplaats =
'Nijmegen'; -->


### Opdracht 2.10.3: Fout in query (3) 

De code hieronder bevat een fout. Run de
code, lees de foutmelding en herstel de fout.

TODO
SELECT naam FROM pizzas WHERE basispijs < 7.0;


<p>Bekijk <a
href="https://rweeda.github.io/PythonIA/docs/IA_sql_oplossingen.html#opgave2103"
target="_blank">hier</a> de voorbeelduitwerking.</p>


<!-- ANTWOORD: De fout zat in de naam van de tabel. <pre><code
class="language-sql"> SELECT naam FROM pizza WHERE basispijs < 7.0;
</code></pre> -->



### Opdracht 2.10.4: Fout in query (4) 

De code hieronder bevat een fout. Run de
code, lees de foutmelding en herstel de fout.

``` sql SELECT pizzanaam FROM pizza WHERE basispijs < 7.0;```

<p>Bekijk <a
href="https://rweeda.github.io/PythonIA/docs/IA_sql_oplossingen.html#opgave2104"
target="_blank">hier</a> de voorbeelduitwerking.</p>


<!-- ANTWOORD: De fout zat in de kolomnaam. <pre><code class="language-sql">
SELECT naam FROM pizza WHERE basispijs < 7.0; </code></pre> -->




# Samenvatting Onderwerp 2

<ul>
<li><b>SQL</b> staat voor Structured Query Language. Het is de standaardtaal om gegevens in een database op te slaan, te bewerken en op te vragen;
<li>Een <b>query</b> is een vraag aan de database, bijvoorbeeld: "Welke pizza’s kosten minder dan 8 euro?";
<li>Een query levert een overzicht op met een deel van de data uit de database;
<li>Met `SELECT` kan je kolommen uit een tabel opvragen en weergeven;
<li>Met `WHERE` kan je voorwaarden stellen aan welke gegevens er opgehaald worden;
<li>Nette code schrijf je met HOOFDLETTERS voor SQL-commando’s, elk commando op een nieuwe regel, afgesloten door een <code>;</code>;
<li>Commentaar voeg je toe met <code>--</code>. Commentaar kun je gebruiken om delen van code tijdelijk weg te laten, bijvoorbeeld voor het opsporen van een fout (debuggen).
<li>De zes basis-onderdelen van een SQL-query staan altijd op de volgorde zoals aangegeven in het tabel hieronder.
</ul>

| Commando | Doel                                    |
|----------|-----------------------------------------|
| SELECT   | Kies welke kolommen je wilt tonen       |
| FROM     | Bepaal uit welke tabel je data haalt    |
| WHERE    | (Optioneel) Stel voorwaarden aan de data|
| GROUP BY | (Optioneel) Groeperen |
| HAVING | (Optioneel)Voorwaarde op groep |
| ORDER BY | (Optioneel) Sorteren |

# Afsluitende Opdrachten 2: SQL SELECT FROM

### Afsluitende Opdracht 2.11.1 Kolomnamen opzoeken 

Je wil weten welke kolomnamen er in de
tabel <i>bestelling</i> zitten. Welke query helpt je hierbij?


<p>Bekijk <a
href="https://rweeda.github.io/PythonIA/docs/IA_sql_oplossingen.html#opgave2111"
target="_blank">hier</a> de voorbeelduitwerking.</p>


<!-- ANTWOORD: Met de volgende query krijg je een overzicht van de hele
tabel, inclusief de kolomnamen: <pre><code class="language-sql"> SELECT *
FROM bestelling; </code></pre> -->


### Afsluitende Opdracht 2.11.2: Toon gegevens van een specifieke pizza

Toon de omschrijving en de basisprijs van de pizza met de naam **"Quattro Formaggi"**.

<p>Bekijk <a
href="https://rweeda.github.io/PythonIA/docs/IA_sql_oplossingen.html#opgave2112"
target="_blank">hier</a> de voorbeelduitwerking.</p>


<!--
<pre><code class="language-sql">
SELECT omschrijving, basisprijs
FROM pizza
WHERE naam = 'Quattro Formaggi';
</code></pre>
-->



### Afsluitende Opdracht 2.11.3: Klanten in een specifieke plaats
Toon het **klantnummer**, **naam** en **plaats** van alle klanten die wonen in **"Utrecht"**. 

<!--
<pre><code class="language-sql">
SELECT klantnummer, naam, plaats
FROM klant
WHERE plaats = 'Utrecht';
</code></pre>
-->

<p>Bekijk <a
href="https://rweeda.github.io/PythonIA/docs/IA_sql_oplossingen.html#opgave2113"
target="_blank">hier</a> de voorbeelduitwerking.</p>

### Afsluitende Opdracht 2.11.4: Netjes schrijven  
Onderstaande query werkt wel, maar is rommelig:


TODO GIVEN
<!--
<pre><code class="language-sql">
select naam,basisprijs from pizza where basisprijs>9
</code></pre>
-->
<ol type="alpha">
<li>Herschrijf de query netjes volgens de afspraken.
<li>Voeg commentaar toe bij de `WHERE`.
</ol>

<p>Bekijk <a
href="https://rweeda.github.io/PythonIA/docs/IA_sql_oplossingen.html#opgave2114"
target="_blank">hier</a> de voorbeelduitwerking.</p>


<!--
<pre><code class="language-sql">
SELECT naam, basisprijs
FROM pizza
WHERE basisprijs > 9; -- pizza's duurder dan 9 euro
</code></pre>
-->


### Afsluitende Opdracht 2.11.5 Debuggen van een fout  
Onderstaande query geeft een foutmelding. Zoek de fout en verbeter de query.

<!--
<pre><code class="language-sql">
SELECT wachtwoord FROM bezorger WHERE naam = Ronald Marbus;
</code></pre>
-->
<p>Bekijk <a
href="https://rweeda.github.io/PythonIA/docs/IA_sql_oplossingen.html#opgave2115"
target="_blank">hier</a> de voorbeelduitwerking.</p>

<!--
<pre><code class="language-sql">
SELECT wachtwoord
FROM bezorger
WHERE naam = 'Ronald Marbus';
</code></pre>
-->


### Afsluitende Opdracht 2.11.6 Debuggen en herschrijven van slordige query
De volgende query werkt niet goed. Voer hem eerst uit en analyseer de foutmelding. Herschrijf daarna de query netjes én correct:

<!--
<pre><code class="language-sql">
SELECT naam basisprijs FROM pizza WHERE basisprijs<7
</code></pre>
-->

<ol type="alpha">
<li>Wat is er fout?
<li>Schrijf een correcte en goed opgemaakte versie met commentaar.
</ol>

<p>Bekijk <a
href="https://rweeda.github.io/PythonIA/docs/IA_sql_oplossingen.html#opgave2116"
target="_blank">hier</a> de voorbeelduitwerking.</p>

<!--
<pre><code class="language-sql">
-- Er ontbreekt een komma tussen de kolommen.
-- Er ontbreekt een puntkomma aan het eind.
SELECT naam, basisprijs
FROM pizza
WHERE basisprijs < 7;
</code></pre>
-->


### Afsluitende Opdracht 2.11.7 Alle bezorgers bekijken  
<ol type="alpha">
<li>Toon alle kolommen en gegevens uit de tabel `bezorger`.  
<li>Welke kolomnamen zie je terug? Geef er drie en leg kort uit wat ze betekenen.
</ol>
<p>Bekijk <a
href="https://rweeda.github.io/PythonIA/docs/IA_sql_oplossingen.html#opgave2117"
target="_blank">hier</a> de voorbeelduitwerking.</p>

<!--
<ol type="alpha">
<li><pre><code class="language-sql">
SELECT * FROM bezorger;
</code></pre>
<li>Mogelijke kolommen:
<ul>
<li>`bezorgernummer`: uniek nummer van elke bezorger  
<li>`naam`: de naam van de bezorger  
<li>`wachtwoord`: gebruikt voor inloggen in het systeem
</ul>
</o>
-->



