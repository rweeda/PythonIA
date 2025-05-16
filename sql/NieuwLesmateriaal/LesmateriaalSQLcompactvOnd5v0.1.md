## ONDEWERP 5

## UITLEG  Gegevens uit meerdere tabellen combineren met `JOIN.. ON ...`

Tot nu toe heb je geleerd hoe je gegevens uit één tabel opvraagt. Maar soms wil je gegevens uit meerdere tabellen combineren. Daarvoor gebruik je `JOIN .. ON ..`.


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


## Wat doet een JOIN?

Met een JOIN **koppel je de gelijke rijen van twee tabellen aan elkaar**. In het bovenstaande voorbeeld zien we dat `pizzacode` in zowel tabel `besteldepizza` voorkomt als in `pizza`. Achter `JOIN` geven we aan uit welke tabellen de informatie komt, en achter `ON` geven we aan welke kolommen gelijk zijn. 


De `.`-notatie (bijvoorbeeld tabel.kolom) gebruik je om aan te geven uit welke tabel een kolom komt. 

Omdat de kolom `pizzacode` in beide tabellen voorkomt, geven we met de '.'-notatie `besteldepizza.pizzacode` aan dat het uit tabel `besteldepizza` komt, en met `pizza.pizzacode` uit tabel `pizza`.

De query ziet er dus zo uit:

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






### Opdracht: Naam van de pizza bij de bestelling

Toon per besteldepizza de naam van de pizza. Gebruik de tabellen `besteldepizza` en `pizza`.

ANTWOORD:
SELECT besteldepizza.besteldepizzacode, pizza.naam
FROM besteldepizza
JOIN pizza ON besteldepizza.pizzacode = pizza.pizzacode;
</code></pre>
-->


### Opdracht:
Schrijf in je eigen woorden wat er gebeurt bij een `JOIN`. Wat moet er kloppen tussen twee tabellen om een `JOIN` te kunnen maken?



<p>Bekijk <a href="https://rweeda.github.io/PythonIA/docs/IA_sql_oplossingen.html#opgave313" target="_blank">hier</a> de voorbeelduitwerking.</p>
<!-- ANTWOORD:
<pre><code class="language-sql">
</code></pre>
-->


### Opdracht: 
Waarom is een `JOIN` nodig in de volgende query waarin we een overzicht willen van de pizzanaam met de besteldepizzacode.

```
SELECT besteldepizza.besteldepizzacode, pizza.naam
FROM besteldepizza
JOIN pizza ON besteldepizza.pizzacode = pizza.pizzacode;
```
a. Omdat tabel `besteldepizza` geen gegevens bevat over pizzacodes.
b. Omdat je een extra filter op de gegevens wilt toepassen.
c. Omdat de naam van de pizza niet in tabel `besteldepizza` staat.
d. Omdat je gegevens uit dezelfde tabel wilt combineren.


<p>Bekijk <a href="https://rweeda.github.io/PythonIA/docs/IA_sql_oplossingen.html#opgave313" target="_blank">hier</a> de voorbeelduitwerking.</p>
<!-- ANTWOORD:
c. Omdat de naam van de pizza niet in `besteldepizza` staat
-->



### Opdracht: Omschrijving van de bodem bij een bestelling

Laat zien welke bodembeschrijving hoort bij elke bestelde pizza. Gebruik besteldepizza en bodem.


<p>Bekijk <a href="https://rweeda.github.io/PythonIA/docs/IA_sql_oplossingen.html#opgave313" target="_blank">hier</a> de voorbeelduitwerking.</p>
<!-- ANTWOORD:
<pre><code class="language-sql">
SELECT besteldepizza.besteldepizzacode, bodem.omschrijving
FROM besteldepizza
JOIN bodem ON besteldepizza.bodemcode = bodem.bodemcode;
</code></pre>
-->








### Opdracht: maak een overzicht van de bestelde pizza en het formaat



<p>Bekijk <a href="https://rweeda.github.io/PythonIA/docs/IA_sql_oplossingen.html#opgave313" target="_blank">hier</a> de voorbeelduitwerking.</p>
<!-- ANTWOORD:
<pre><code class="language-sql">
</code></pre>
-->


### Opdracht: maak een overzicht voor de besteldePizza en datum en bezorg tijd



<p>Bekijk <a href="https://rweeda.github.io/PythonIA/docs/IA_sql_oplossingen.html#opgave313" target="_blank">hier</a> de voorbeelduitwerking.</p>
<!-- ANTWOORD:
<pre><code class="language-sql">
</code></pre>
-->


### SAMENVATTING JOIN
JOIN is nodig om betekenisvolle combinaties van data uit verschillende tabellen te maken.




### Opdracht: Toon alle kortingen die bij een bestelling horen

Toon alle kortingen die bij een bestelling horen. Hiervoor heb je de tabellen `besteldepizza` en `kortingsbonnen` nodig.


<p>Bekijk <a href="https://rweeda.github.io/PythonIA/docs/IA_sql_oplossingen.html#opgave313" target="_blank">hier</a> de voorbeelduitwerking.</p>
<!-- ANTWOORD:
<pre><code class="language-sql">
SELECT 
  besteldepizza.bestelcode,
  kortingsbonnen.korting,
  kortingsbonnen.datum
FROM besteldepizza
JOIN kortingsbonnen ON besteldepizza.boncode = kortingsbonnen.boncode;
</code></pre>
-->


# JOIN MET MEER DAN 2 TABELLEN

Je kunt ook meer dan 3 tabellen koppelen met een `JOIN`. Je koppelt steeds twee tabellen tegelijk, en gebruikt een tweede `JOIN` om dat te koppelen aan een derde tabel.


### Opdracht: JOIN met drie tabellen toepassen toepassen
Toon een overzicht van alle bestelde pizza’s, met daarbij:
<ul>
<li>de bestelcode (uit tabel `besteldepizza')
<li>de pizzanaam (uit tabel `pizza')
<li>en de bodembeschrijving (uit tabel `bodem`)
</ul>

Gebruik een`JOIN` om de tabellen aan elkaar te koppelen. Gebruik de de tabellen `besteldepizza`, `pizza` en `bodem`. Koppel er steeds twee tegelijk.

Tip: je moet twee JOINs gebruiken.


<!-- ANTWOORD:
<ol type="alpha">
<li>
<pre><code class="language-sql">
SELECT besteldepizza.bestelcode, pizza.naam AS pizzanaam, bodem.omschrijving AS bodembeschrijving
FROM besteldepizza
JOIN pizza ON besteldepizza.pizzacode = pizza.pizzacode
JOIN bodem ON besteldepizza.bodemcode = bodem.bodemcode;
</code></pre>
</li>
<li>
Je kunt dit niet doen zonder JOIN, omdat de informatie die je nodig hebt verspreid is over meerdere tabellen.<br>
In de tabel <code>besteldepizza</code> staat de <code>pizzacode</code> en de <code>bodemcode</code>,
maar de naam van de pizza staat in de tabel <code>pizza</code>,
en de omschrijving van de bodem staat in de tabel <code>bodem</code>.
</li>
</ol>
-->



### Opdracht: Bezorgerinformatie
Toon uit tabel `bestelling` voor de eerste vijf gegevens, de naam van de bezorger en bijbehorende de klantgegevens (klantnaam, adres, postcode, en woonplaats). Toon het overzicht zoals hieronder.


| bezorgernaam     | klantnaam                   | adres                | postcode | woonplaats |
|------------------|-----------------------------|----------------------|----------|------------|
| Han Fröling      | Katja Pas                   | Koperwiek 73         | 3766AM   | Hengelo    |
| Afhalen          | Bram Kuipers                | Heyendaalseweg 300   | 6525EC   | Nijmegen   |
| Ageeth Mooy      | Frank Goudsmit              | Pelikaanweg 17       | 3762VA   | Hengelo    |
| Hans Boonstra    | Maarten Doornbos            | Mozartlaan 35        | 3741HT   | Enschede   |
| Marleen Hoekstra | Margaretha Verwoert - Gro   | Goudenregenlaan 30   | 3741CB   | Enschede   |


<!-- ANTWOORD
<pre><code class="language-sql">
SELECT 
    bezorger.naam AS bezorgernaam,
    klant.naam AS klantnaam,
    klant.adres,
    klant.postcode,
    klant.woonplaats
FROM bestelling
JOIN bezorger ON bestelling.bezorgernummer = bezorger.bezorgernummer
JOIN klant ON bestelling.klantnummer = klant.klantnummer
LIMIT 5;
</code></pre>
-->

### Opdracht Voor de kok

Maak voor de kok een overzicht van welke pizza's besteld zijn zoals hieronder, met daarin pizzanaam, formaat, bodem. Laat alleen de eerste 10 zien.

| pizzanaam | formaat            | bodem           |
|-----------|--------------------|------------------|
| Marinara  | extra groot (40 cm)| American style   |
| Hawai     | groot (35 cm)      | American style   |
| Fantasia  | klein (25 cm)      | American style   |
| Salmone   | klein (25 cm)      | American style   |
| Fantasia  | medium (30 cm)     | American style   |


<!-- ANTWOORD:
<pre><code class="language-sql">
SELECT 
    pizza.naam AS pizzanaam,
    formaat.omschrijving AS formaat,
    bodem.omschrijving AS bodem
FROM besteldePizza
JOIN pizza ON besteldePizza.pizzacode = pizza.pizzacode
JOIN formaat ON besteldePizza.formaatcode = formaat.formaatcode
JOIN bodem ON besteldePizza.bodemcode = bodem.bodemcode
LIMIT 10;
</code></pre>
-->


### Afsluitende Opdracht Bestellingen van klanten uit Enschede of Hengelo

Toon de `bestelcode` en `klantnummer` van alle bestellingen waarvan de klant uit **Enschede of Hengelo** komt, zoals in het overzicht hieronder. De gegevens komen uit tabellen `klant` en `bestelling`.

| bestelcode | klantnummer |
|------------|-------------|
| 1          | 224         |
| 4          | 323         |
| 5          | 279         |
| 6          | 199         |
| 7          | 323         |
| ...      | ... |


<!-- ANTWOORD:
<pre><code class="language-sql">
SELECT bestelcode, bestelling.klantnummer
FROM bestelling
JOIN klant  ON bestelling.klantnummer = klant.klantnummer
WHERE woonplaats = 'Enschede' OR woonplaats = 'Hengelo';
</code></pre>
-->




# Groepsfuncties

In deze onderwerp leer je hoe je met SQL berekeningen en samenvattingen kunt maken uit je database.  
We behandelen de volgende functies:

- `MIN()`
- `MAX()`
- `SUM()`
- `AVG()`
- `COUNT(*)`
- `DISTINCT`


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

### Oefenopdracht

Toon unieke combinaties van bodemcode en omschrijving.

**Uitwerking:**
```sql
ANTWOORD:
SELECT DISTINCT bodemcode, omschrijving 
FROM besteldepizza;
```

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

Om maar bepaalde gegevens te tonen *nadat* je een GROUP BY gebruikt, kun je gebruik maken van HAVING. Deze werkt op waarden zoals `COUNT(*)`, `AVG()`, `SUM()`...

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




