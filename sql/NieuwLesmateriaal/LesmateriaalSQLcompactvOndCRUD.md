
# ONDERWERP 5: Gegegvens invoeren, aanpassen en verwijderen



## Gegevens in een tabel invoeren

<p>
Met een <code>INSERT INTO... VALUES (...)</code>-query voeg je nieuwe gegevens toe aan een tabel. Je geeft dan de naam van de tabel aan, en tussen haakjes de gegevens voor elk kolom in de tabel. </p>


<p>Bij sommige tabellen wordt voor de primary key gebruikt gemaakt van een AUTOINCREMENT. Een kolom met AUTOINCREMENT betekent dat de database zelf een nummer verzint dat steeds oploopt. 👉 Bijvoorbeeld, de eerste rij krijgt automatisch nummer 1, de volgende rij krijgt 2, en dan 3, enzovoort. Zo krijgt elke rij een eigen uniek nummer. Voor zo'n kolom hoef je dat nummer niet zelf te typen — in plaats daarvan geef je NULL aan.</p>



Let op:
<ul>
<li>De volgorde van kolommen en waarden moet kloppen.</li>
<li>Tekst moet tussen aanhalingstekens gezet worden. Bij getallen of kommagetallen hoeft dat niet.
<li>Bij een AUTOINCREMENT wordt automatisch genummerd, daarom geef je daar de waarde NULL op.
</ul>


Bijvoorbeeld, met de onderstaande code voegen we een pizza toe aan tabel <i>pizza</i>:

```SQL
INSERT INTO pizza 
VALUES (NULL, 'Pizza Hawaii', 'Ham en ananas', 8.50);
```
Toelichting:
<ul>
<li>Met INSERT INTO geven we aan dat we willen toevoegen aan tabel <i>pizza</i>;
<li>Met VALUES geven we aan welke gegevens in de tabel moeten komen te staan;l
<li>Met 'NULL' geven we aan dat er automatisch genummerd wordt;
<li>In de 2e kolom, namelijk <i>naam</i>, komt 'Pizza Hawaii' te staan;
<li>In de 3e kolom, namelijk <i>omschrijving</i> ...
<li> ...
</ul>

### Verwerkingsopdracht ... Toevoegen en controleren
<ol type="a">
<li>Run de code hierboven waarmee een <i>Pizza Hawaii</i> wordt toegevoegd aan tabel <i>pizza</i>.
<li>Controleer daarna of het is gelukt, dit kan met:


```SQL
SELECT *
FROM bodem
```
</ol>

<!--

<li>
<ol type="a">
<pre><code class="language-sql"> 
SELECT *
FROM bodem
</code></pre>
<li>
<pre><code class="language-sql"> 
-- check:
SELECT *
FROM pizza;
</code></pre>
</ol>
-->




### Verwerkingsopdracht ... Een nieuwe glutenbrij bodem

We gebruiken de tabel <i>bodem</i>. Deze bevat de kolommen:
<ul>
<li><b>bodemcode</b> (AUTOINCREMENT, hoef je niet zelf in te vullen)
<li><b>omschrijving</b> (bijvoorbeeld "Dunne bodem")
<li><b>plusprijs</b> (bijvoorbeeld 1.00)
</ul>

<p>Welke van de volgende `INSERT INTO`-statements voegt correct een nieuwe bodem toe met omschrijving <b>Glutenvrij</b> en een toeslag van €1,50?</p>
<ul type="A">
<li> 

```sql
INSERT INTO bodem (bodemcode, omschrijving, plusprijs)
VALUES (5, "Glutenvrij", 1.50);
```
</li>
<li>

```sql
INSERT INTO bodem (omschrijving, plusprijs)
VALUES (NULL, "Glutenvrij", 1.50);
```
</li>
<li>

```sql
INSERT INTO bodem
VALUES ("Glutenvrij", 1.50);
```

</li>
<li>

```sql
INSERT INTO bodem (omschrijving, plusprijs)
VALUES (Glutenvrij, €1,50);
```
</li>

<p>Bekijk <a
href="https://rweeda.github.io/PythonIA/docs/IA_sql_oplossingen.html#opgave471"
target="_blank">hier</a> de voorbeelduitwerking.</p>

<!--
Antwoord: B
Toelichting: bodemcode is een AUTOINCREMENT-veld en moet je dus NULL invullen.
Bij antwoord D ontbreken aanhalingstekens en het euroteken is fout in SQL.
-->

### Verwerkingsopdracht ... Pan bodem toevoegen
We gebruiken de tabel <i>bodem</i>. Deze bevat de kolommen:
<ul>
<li><b>bodemcode</b> (AUTOINCREMENT);
<li><b>omschrijving</b>;
<li><b>plusprijs</b>.
</ul>

<p>Voeg een nieuwe dikke bodem toe met de omschrijving "Pan" en een toeslag van €2,00.</p>
<p>Controleer daarna of het gelukt is, dat kan met:

```SQL
SELECT *
FROM bodem
```


<p>Bekijk <a
href="https://rweeda.github.io/PythonIA/docs/IA_sql_oplossingen.html#opgave471"
target="_blank">hier</a> de voorbeelduitwerking.</p>

<!--
<pre><code class="language-sql"> 
INSERT INTO bodem (bodemcode, omschrijving, plusprijs)
VALUES (NULL, "Pan", 2.00);


-- check:
SELECT *
FROM bodem;
</code></pre>
-->




## Gegevens in een tabel aanpassen
<p>Met UPDATE kun je gegevens in een tabel aanpassen:</p>

```SQL
UPDATE tabelnaam
SET kolom1 = nieuwe_waarde1, kolom2 = nieuwe_waarde2
WHERE voorwaarde;
```

<ul>
<li>Achter UPDATE geef je de naam van de tabel aan;</li>
<lI>Met SET geef je aan wat de nieuwe waarde wordt;</li>
<li>Met WHERE geef je aan welke gegevens aangepast moeten worden, hier het beste de <i>primary key</i> gebruiken.</li>
</ul>


Bijvoorbeeld, met de volgende query wordt de naam van de pizza met pizzacode 1 aangepast naar "Hawaii":

```SQL
UPDATE pizza
SET pizzanaam = "Hawaii"
WHERE pizzacode = 1;
```

<p>Let op: De WHERE is belangrijk omdat anders <i>alle</i> rijen worden aangepast! Controleer daarom na een aanpassing met <code>SELECT * FROM ... </code> of de aanpassing is gelukt.</p>


### Opdracht Pas de prijs van een pizza aan

Schrijf een query die voor de pizza met <b>naam</b> gelijk aan "<i>Margherita</i>", de <b>basisprijs</b> verhogen naar €8,00. Controleer daarna met `SELECT *` of het gelukt is.



<!-- ANTWOORD
<pre><code class="language-sql">
UPDATE pizza
SET basisprijs = 8.00
WHERE naam = "Margherita";
</code></pre>
-->



## Gegevens uit een tabel verwijderen
<p>Met DELETE FROM kun je een hele rij van gegevens verwijderen uit een tabel:</p>

```SQL
DELETE FROM tabelnaam
WHERE voorwaarde;
```
<ul>
<li>Achter DELETE FROM geef je de naam van de tabel aan;</li>
<li>Met WHERE geef je aan welke gegevens aangepast moeten worden, hier het beste de <i>primary key</i> gebruiken.</li>
</ul>


Bijvoorbeeld, met de volgende code worden alle gegevens over de pizza met <i>pizzacode</i> gelijk aan 1 verwijderd:

```SQL
DELETE FROM pizza
WHERE pizzacode = 1;
```

<p>Let op: De WHERE is belangrijk omdat anders <i>alle</i> rijen worden verwijderd! Controleer daarom na een aanpassing met <code>SELECT * FROM ... </code> of de aanpassing is gelukt.</p>

### Verwerkingsopdracht ... Verwijderen en controleren
<ol type="a">
<li>Run de code hierboven waarmee een <i>pizzacode</i> 1 wordt verwijderd uit tabel <i>pizza</i>.
<li>Controleer daarna of het is gelukt, dit kan met:

```SQL
SELECT *
FROM pizza
```
</ol>





### Verwerkingsopdracht: Verwijder een pizza
Omdat deze nauwelijks besteld wordt, wil Danilo de "Pazza" pizza van het menu halen. 
<ol type="a">
<li>Schrijf een query om de pizza uit de tabel te verwijderen. 
<li>Controleer daarna met `SELECT *` of het gelukt is.
</ol>

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



## Tabel 4.X: Nieuw tabel aanmaken

<p>Met CREATE TABLE kun je een nieuwe tabel aanmaken. Je geeft dan de naam van de nieuwe tabel op met daarachter tussen haakjes ieder kolomnaam en de bijbehorende datatype.</p>

<p>
Elk tabel moet een primary key hebben. De database kan automatisch voor je doornummeren zodra er nieuwe gegevens worden toegevoegd, zodat in die kolom mag een waarde maar 1 keer voorkomt. Dat doe je met: <code>INTEGER PRIMARY KEY AUTOINCREMENT</code>.



Hieronder een voorbeeld voor het maken van tabel <i>pizza</i> waarbij de <i>pizzacode</i> als primary key automatisch wordt genummerd:

CREATE TABLE pizza (
  pizzacode INTEGER PRIMARY KEY AUTOINCREMENT, 
  naam TEXT,
  omschrijving TEXT,
  basisprijs REAL)
  ;
  



### Opdracht Nieuwe tabel <i>kortingsbonnen</i> aanmaken

In deze opdrachten maken we een nieuw tabel toe voor <i>kortingsbonnen</i> waarin we informatie opslaan over de kortingsbonnen die in omloop zijn: <b>boncode</b>, hoeveel <b>korting</b> ze geven en tot welk <b>datum</b> de bon geldig is.


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



 



## Een tabel verwijderen
Met DROP TABLE kun je een hele tabel verwijderen, bijvoorbeeld tabel <i>klant</i>:

```SQL
DROP TABLE klant
```

### Opdracht: Verwijder tabel <i>bodem</i>
<ol type="a">
<li>Verwijder tabel <i>bodem</i>.
<li>Probeer daarna met `SELECT *` de gegevens uit tabel <i>bodem</i> op te halen. Welk foutmelding krijg je?
</ol>

<!-- ANTWOORD
<ol type="a">
<li>
<pre><code class="language-sql">
-- verwijderen:
DROP TABLE bodem;
</code></pre>
<li>
-- check:
<pre><code class="language-sql">
SELECT *
FROM bodem;-- ophalen lukt niet omdat de tabel in de vorige stap verwijderd is.
</code></pre>
</ol>
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

```SQL
CREATE TABLE kortingsbonnen (
    boncode INTEGER PRIMARY KEY AUTOINCREMENT,
    korting REAL,
    datum TEXT
);
```

[picture ERD kortingsbonnen: DaniloIA_ERD_metKortingsbon.png]

<p>Als je bij een bestelling wilt bijhouden welke kortingsbon gebruikt, dan moet je de tabel <i>besteldePizza</i> uitbreiden met een kolom die verwijst naar <i>kortingsbonnen</i>.</p>

<p>Dit doe je met een <b>foreign key</b>. Een foreign key is een kolom in een tabel die verwijst naar een primary key in een andere tabel. Zo leg je een relatie tussen twee tabellen.</p>


<p>Waarom doe je dit?
<ul>
<li>Je legt een relatie tussen twee tabellen: een bestelling kan een kortingsbon gebruiken.
<li>Je voorkomt fouten, zoals het invullen van een boncode die niet bestaat.
<li>Je kunt makkelijk gegevens opvragen, bijvoorbeeld welke bestellingen hebben welke bon gebruikt, en hoeveel korting er in totaal is gegeven is.
</ul>

<p>In het voorbeeld hieronder zie je hoe je tabel <i>besteldePizza</i> kunt uitbreiden met een foreign key die verwijst naar de primary key <b>boncode</b> van tabel <i>kortingsbonnen</i>.

```SQL
CREATE TABLE besteldePizza (
    besteldePizzaID INTEGER PRIMARY KEY AUTOINCREMENT,
    pizzacode INTEGER,
    bestelcode INTEGER,
    boncode INTEGER,
    FOREIGN KEY (boncode) REFERENCES kortingsbonnen(boncode)
);
```

Toelichting: 
<ul>
<li>Kolom <b>boncode</b> is aan tabel <i>besteldePizza</i> toegevoegd. Hier staat de gebruikte boncode uit tabel <i>kortingsbonnen</i> in.
<li>Met de onderste regel geven we aan dat de nieuwe kolom <b>boncode</b> uit tabel <i>besteldePizza</i> verwijst naar (REFERENCES) naar tabel de primary key <b>boncode</b> uit tabel <i>kortingsbonnen</i> met: <code>kortingsbonnen(boncode)</code>.
</ul>


Je kunt hier een filmpje bekijken waarin wordt uitgelegd wat primary en foreign keys zijn.
https://www.youtube.com/embed/obeOGxESGLI

<iframe width="560" height="315" src="https://www.youtube.com/embed/obeOGxESGLI?start=0&amp;end=150"></iframe>


### Opdracht Foreign keys bij Danilo's Pizzeria

Bekijk het overzicht van de tabellen en beantwoord de volgende vragen:
<img src="https://raw.githubusercontent.com/rweeda/PythonIA/main/sql/DaniloIA_ERD.png" alt="overzicht tabellen" width="500"></p



<ol type="a">
<li>Hoeveel foreign keys heeft tabel <i>besteldepizza</i>? Benoem voor elk de tabel waar naar verwezen wordt en de bijbehorende kolomnaam.
<li>Hoeveel foreign keys heeft tabel <i>formaat</i>?
<li>Leg in je eigen woorden wat de volgende code betekent: <code>FOREIGN KEY (formaatcode) REFERENCES formaat(formaatcode)</code>.
<li>Leg in je eigen woorden wat er mis is aan de volgende code: <code>FOREIGN KEY (formaatcode) REFERENCES formaat(omschrijving)</code>.
</ol>


ANTWOORDEN:
<ol type="a">
<li>Tabel <i>besteldepizza</i> heeft vier foreign keys, namelijk:
	<ol><li><b>bestelcode</b> uit tabel <i>bestelling</i> 
	<ol><li><b>pizzacode</b> uit tabel <i>pizza</i> 
	<ol><li><b>bodemcode</b> uit tabel <i>bodem</i> 
	<ol><li><b>formaatcode</b> uit tabel <i>formaat</i> 
	</ol>
<li>Tabel <i>formaat</i> heeft <b>geen</b> foreign key. Die heeft een primary key <b>formaatcode</b> die vanuit tabel <i>besteldePizza</i> als foreign key gebruikt wordt, maar die verwijst zelf niet naar een ander tabel en heeft dus geen foreign key.
<li>Tabel <i>besteldePizza</i> heeft een kolom formaatcode. Daarvoor komen de gegevens uit tabel <i>formaat</i> en kolom <b>formaatcode</b>.
<li>De foreign key verwijst naar kolom <b>omschrijving</b> uit tabel <i>formaat</i>. Dit is niet goed, want het moet verwijzen naar de primary key van tabel <i>formaat</i>, en dus <b>formaatcode</b>.
</ol>
