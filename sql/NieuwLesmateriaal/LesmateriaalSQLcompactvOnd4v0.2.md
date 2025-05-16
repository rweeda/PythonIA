## ONDERWERP 4

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






