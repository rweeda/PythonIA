
# ONDERWERP 5: Gegevens invoeren, aanpassen en verwijderen

<p>Elke keer dat je de webpagina ververst, wordt de oorspronkelijke database hersteld. Je hoeft dus niet bang te zijn om iets fout te doen — experimenteren mag!</p>

<p>Wil je je code bewaren? Sla deze dan op via 'Bestand' en vervolgens 'Bewaar notebook als...'. Je kunt je werk ook tussentijds opslaan of inleveren.</p>

## Gegevens in een tabel invoeren

<p>Met een <code>INSERT INTO... VALUES (...)</code>-query voeg je nieuwe gegevens toe aan een tabel.</p>

<pre><code class="language-sql">
INSERT INTO tabelnaam 
VALUES (waarde1, waarde2, waarde3, ... );
</code></pre>

<ul>
  <li>Achter <code>INSERT INTO</code> geef je de naam van de tabel aan.</li>
  <li>Achter <code>VALUES</code> geef je tussen haakjes voor elke kolom afzonderlijk de gegevens die ingevuld moeten worden.</li>
</ul>

<p>Bij sommige tabellen wordt voor de primary key gebruik gemaakt van <code>AUTOINCREMENT</code>. Een kolom met <code>AUTOINCREMENT</code> betekent dat de database zelf een oplopend nummer verzint. Bijvoorbeeld: de eerste rij krijgt automatisch nummer 1, de volgende 2, enzovoort. Voor zo'n kolom hoef je dat nummer niet zelf in te vullen — in plaats daarvan geef je <code>NULL</code> op.</p>

<p><strong>Let op:</strong></p>
<ul>
  <li>De volgorde van kolommen en waarden moet overeenkomen.</li>
  <li>Tekst moet tussen aanhalingstekens staan. Bij getallen is dat niet nodig.</li>
  <li>Bij een <code>AUTOINCREMENT</code> geef je <code>NULL</code> op, zodat automatisch wordt genummerd.</li>
</ul>

<p>Voorbeeld: Deze query voegt een nieuwe pizza toe aan de tabel <i>pizza</i>:</p>

<pre><code class="language-sql">
INSERT INTO pizza 
VALUES (NULL, 'Pizza Hawaii', 'Ham en ananas', 8.50);
</code></pre>

<p>Toelichting:</p>
<ul>
  <li>Met <code>INSERT INTO</code> geven we aan dat we iets willen toevoegen aan de tabel <i>pizza</i>.</li>
  <li>Met <code>VALUES</code> geven we aan welke gegevens in de tabel moeten worden opgeslagen.</li>
  <li>Met <code>NULL</code> geven we aan dat het id-nummer automatisch gegenereerd wordt.</li>
  <li>In de tweede kolom, <i>naam</i>, komt 'Pizza Hawaii' te staan.</li>
  <li>In de derde kolom, <i>omschrijving</i>, komt 'Ham en ananas'.</li>
  <li>In de vierde kolom, <i>basisprijs</i>, komt 8.50.</li>
</ul>


### Verwerkingsopdracht Pizza toevoegen en controleren
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

<ul type="a">
<li>Voeg een nieuwe dikke bodem toe met de omschrijving "Pan" en een toeslag van €2,00.</p>
<li>Controleer daarna of het gelukt is, dat kan met:

```SQL
SELECT *
FROM bodem
```
</ul>


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


## Gegevens uit een tabel verwijderen
<p>Met DELETE FROM kun je een hele rij van gegevens verwijderen uit een tabel:</p>

```SQL
DELETE FROM tabelnaam
WHERE voorwaarde;
```
<ul>
<li>Achter DELETE FROM geef je de naam van de tabel aan;</li>
<li>Met WHERE geef je aan welke gegevens aangepast moeten worden, hier het beste de <i>primary key</i> gebruiken;</li>
<li>Let op: De WHERE is belangrijk omdat anders <i>alle</i> rijen worden verwijderd! Controleer daarom na een aanpassing met <code>SELECT * FROM ... </code> of de aanpassing is gelukt.</li>
</ul>


Voorbeeld: Deze query verwijdert alle rijen uit de tabel <i>pizza</i> met <b>pizzacode</b> gelijk is aan 1.

```SQL
DELETE FROM pizza
WHERE pizzacode = 1;
```


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

<p>Bekijk <a
href="https://rweeda.github.io/PythonIA/docs/IA_sql_oplossingen.html#opgave471"
target="_blank">hier</a> de voorbeelduitwerking.</p>


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




## Gegevens in een tabel aanpassen
<p>Met UPDATE kun je gegevens in een tabel aanpassen:</p>
<!--
Je geeft dan de naam van de tabel aan, en tussen haakjes de gegevens voor elk kolom in de tabel. </p>
-->

```SQL
UPDATE tabelnaam
SET kolom1 = nieuwe_waarde1, kolom2 = nieuwe_waarde2
WHERE voorwaarde;
```

<ul>
<li>Achter UPDATE geef je de naam van de tabel aan;</li>
<lI>Met SET geef je aan wat de nieuwe waarde wordt;</li>
<li>Met WHERE geef je aan welke gegevens aangepast moeten worden, hier het beste de <i>primary key</i> gebruiken;
<li>>Let op: De WHERE is belangrijk omdat anders <i>alle</i> rijen worden aangepast! Controleer daarom na een aanpassing met <code>SELECT * FROM ... </code> of de aanpassing is gelukt.</li>
</ul>


Voorbeeld: deze query past de naam van de pizza met <b>pizzacode</b> 1 aan naar "Hawaii".
Alle andere kolommen blijven hetzelfde. 

```SQL
UPDATE pizza
SET pizzanaam = "Hawaii"
WHERE pizzacode = 1;
```



### Verwerkingsopdracht Pas de prijs van een pizza aan

<ol type="a">
<li>Schrijf een query die voor de pizza met <b>naam</b> gelijk aan "<i>Margherita</i>", de <b>basisprijs</b> verhogen naar €8,00. 
<li>Controleer daarna met <code>SELECT *</code> of het gelukt is.
</ol>
<p>Bekijk <a
href="https://rweeda.github.io/PythonIA/docs/IA_sql_oplossingen.html#opgave471"
target="_blank">hier</a> de voorbeelduitwerking.</p>

<!--
<pre><code class="language-sql"> 
UPDATE pizza
SET basisprijs = 8.00
WHERE naam = "Margherita";
</code></pre>
-->



# ONDERWERP X: Tabellen aanmaken, aanpassen en verwijderen

##  Nieuw tabel aanmaken

<p>
Met een <code>CREATE TABLE</code>-query maak je een nieuwe tabel aan in de database.
</p>

<pre><code class="language-sql">
CREATE TABLE tabelnaam (
  kolom1 datatype,
  kolom2 datatype,
  kolom3 datatype,
  ...
);
</code></pre>

<ul>
  <li>Achter <code>CREATE TABLE</code> geef je de naam van de nieuwe tabel aan.</li>
  <li>Tussen haakjes zet je per kolom de naam en het datatype (zoals <code>TEXT</code>, <code>INTEGER</code> of <code>REAL</code>).</li>
</ul>


<p>
Elke tabel moet een primary key hebben. De database kan automatisch doornummeren zodra er nieuwe gegevens worden toegevoegd. In die kolom mag elke waarde maar één keer voorkomen. Dat doe je met: <code>INTEGER PRIMARY KEY AUTOINCREMENT</code>.
</p>

Hieronder een voorbeeld voor het maken van tabel <i>pizza</i> waarbij de <i>pizzacode</i> als primary key automatisch wordt genummerd:

```SQL
CREATE TABLE pizza (
  pizzacode INTEGER PRIMARY KEY AUTOINCREMENT, 
  naam TEXT,
  omschrijving TEXT,
  basisprijs REAL)
  ;
```



### Verwerkingsopdracht Nieuwe tabel kortingsbonnen aanmaken

In deze opdracht maken we een nieuw tabel toe voor <i>kortingsbonnen</i> waarin we informatie opslaan over de kortingsbonnen die in omloop zijn: <b>boncode</b>, hoeveel <b>korting</b> ze geven en tot welk <b>datum</b> de bon geldig is.

<ol type="a">
<li>
Schrijf een CREATE TABLE-statement voor de tabel <code>kortingsbon</code>. Bedenk welke kolommen je nodig hebt, en welke typen data je gebruikt. Denk aan:
<ul>
<li>Een primary key: <i>boncode</i>;
<li>automatisch doornummeren voor een unieke boncode (met AUTOINCREMENT);
<li>De juise datatype (TEXT, INTEGER, REAL) per kolom.
</ul>
<li>Als je met <code>SELECT *</code> wil controleren of de tabel is aangemaakt, zie je geen gegevens in de tabel. Waarom niet?

</ol>

<p>Bekijk <a
href="https://rweeda.github.io/PythonIA/docs/IA_sql_oplossingen.html#opgave471"
target="_blank">hier</a> de voorbeelduitwerking.</p>


<!-- ANTWOORD:
<ol type="a">
<li>
<pre><code class="language-sql">
CREATE TABLE kortingsbon (
    boncode INTEGER PRIMARY KEY AUTOINCREMENT,
    korting REAL,
    datum TEXT
);
</code></pre>
</li>
<li>
Als de code geen foutmelding geeft, maar wel een lege tabel oplevert, dan is het aanmaken gelukt. Met <code>CREATE TABLE</code> heb je alleen de tabel aangemaakt. Met <code>INSERT INTO</code> kun je daarna gegevens invoeren.
</li>
</ol> 
-->



 



## Een tabel verwijderen
<p>
Met een <code>DROP TABLE</code>-query verwijder je een hele tabel uit de database. Alle gegevens in de tabel gaan dan ook verloren.
</p>

<pre><code class="language-sql">
DROP TABLE tabelnaam;
</code></pre>

<ul>
  <li>Achter <code>DROP TABLE</code> geef je de naam van de tabel die je wilt verwijderen.</li>
  <li>Let op: deze actie kan niet ongedaan worden gemaakt. Alle gegevens in de tabel worden definitief verwijderd.</li>
  <li>Wil je de oorsprinkelijk database hetstellen? In deze leeromgeving kan je de oorspronkelijke database terugkrijgen door de webpagina te verversen. Sla wel eerst je werk op via 'Bestand' en vervolgens 'Bewaar notebook als...'.
</ul>


Voorbeeld: Deze query verwijderd de tabel <i>kortingsbon</i>.
<pre><code class="language-sql">
DROP TABLE kortingsbon;
</code></pre>

### Verwerkingsopdracht: Verwijder tabel bodem
<ol type="a">
<li>Verwijder tabel <i>bodem</i>.
<li>Probeer daarna met <code>SELECT *</code> de gegevens uit tabel <i>bodem</i> op te halen. Welk foutmelding krijg je?
</ol>

<p>Bekijk <a
href="https://rweeda.github.io/PythonIA/docs/IA_sql_oplossingen.html#opgave471"
target="_blank">hier</a> de voorbeelduitwerking.</p>


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


## Tabel aanpassen - kolom toevoegen
<p>
Met een <code>ALTER TABLE</code>-query kun je de structuur van een bestaande tabel aanpassen, bijvoorbeeld door een kolom toe te voegen of te verwijderen.
</p>

<pre><code class="language-sql">
ALTER TABLE tabelnaam
ADD kolomnaam datatype;
</code></pre>

<ul>
  <li>Achter <code>ALTER TABLE</code> geef je de naam van de tabel aan die je wilt aanpassen.</li>
  <li>Met <code>ADD</code> voeg je een nieuwe kolom toe, gevolgd door de kolomnaam en het datatype (zoals <code>TEXT</code>, <code>INTEGER</code> of <code>REAL</code>).</li>
</ul>

Voorbeeld: Deze query voegt een nieuwe kolom email van het type TEXT toe aan de tabel bezorger. 
<pre><code class="language-sql">
ALTER TABLE bezorger
ADD email TEXT;
</code></pre>


### Verwerkingsopdracht: kolom toevoegen


<p>Bekijk <a
href="https://rweeda.github.io/PythonIA/docs/IA_sql_oplossingen.html#opgave471"
target="_blank">hier</a> de voorbeelduitwerking.</p>


<!--
<pre><code class="language-sql">
</code></pre>
-->



## Tabel aanpassen - Kolom hernoemen
<p>
Met <code>ALTER TABLE ... RENAME COLUMN</code> geef je een bestaande kolom een nieuwe naam.
</p>

<pre><code class="language-sql">
ALTER TABLE tabelnaam
RENAME COLUMN oude_kolomnaam TO nieuwe_kolomnaam;
</code></pre>

<ul>
  <li>Achter <code>ALTER TABLE</code> geef je de naam van de tabel waarin je de kolom wilt hernoemen.</li>
  <li>Met <code>RENAME COLUMN</code> verander je de naam van een bestaande kolom.</li>
</ul>


Voorbeeld: Deze query verandert de kolomnaam <b>plusprijs</b> in <b>toeslag</b> in de tabel <i>bodem</i>.

<pre><code class="language-sql">
ALTER TABLE bodem
RENAME COLUMN plusprijs TO toeslag;
</code></pre>


### Verwerkingsopdracht: kolom hernoemen
Verander de kolomnaam <b>naam</b> in <b>klantnaam</b> in de tabel <i>klant</i>.


<p>Bekijk <a
href="https://rweeda.github.io/PythonIA/docs/IA_sql_oplossingen.html#opgave471"
target="_blank">hier</a> de voorbeelduitwerking.</p>


<!--
<pre><code class="language-sql">
ALTER TABLE klant
RENAME COLUMN naam TO klantnaam;
</code></pre>
-->


## Tabel aanpassen - Tabel hernoemen
<p>
Met <code>ALTER TABLE ... RENAME TO</code> geef je een bestaande tabel een nieuwe naam.
</p>

<pre><code class="language-sql">
ALTER TABLE oude_tabelnaam
RENAME TO nieuwe_tabelnaam;
</code></pre>

<ul>
  <li>Achter <code>ALTER TABLE</code> geef je de huidige naam van de tabel op.</li>
  <li>Met <code>RENAME TO</code> verander je de naam van de hele tabel.</li>
</ul>

Voorbeeld: Deze query verandert de naam van de tabel <i>bezorger</i> in <i>medewerker</i>.

<pre><code class="language-sql">
ALTER TABLE bezorger
RENAME TO medewerker;
</code></pre>


<!--
<i>N.B.: In SQLite kun je geen kolom verwijderen, dat kan wel in andere databases. Dat kan dan met een ALTER TABEL ... DROP COLUMN ... </i>
-->

### Verwerkingsopdracht: tabel hernoemen

Verander de tabelnaam van <i>formaat</i> naar <i>grootte</i>.




<p>Bekijk <a
href="https://rweeda.github.io/PythonIA/docs/IA_sql_oplossingen.html#opgave471"
target="_blank">hier</a> de voorbeelduitwerking.</p>


<!--
<pre><code class="language-sql">
ALTER TABLE formaat
RENAME TO grootte;
</code></pre>
-->


## Overzicht van alle tabellen
In de <b>ERD</b>-schema (Entity-Relationship Diagram) hieronder zie je een overzicht van de tabellen en hoe ze met elkaar verbonden zijn.

<img src="https://raw.githubusercontent.com/rweeda/PythonIA/main/sql/DaniloIA_ERD.png" alt="overzicht tabellen" width="500"></p



De pijlen geven koppelingen tussen de tabellen aan. Een bestelling heeft een klantnummer. Aan het pijltje kun je zien dat de gegevens over de klant te vinden zijn in tabel <code>klanten</code>.

<p>
Extra:
De tekens bij de pijlen geven ook een relatie aan. De relatie tussen tabel <i>klant</i> en <i>bestelling</i> is een één-op-veel-relatie omdat 1 klant meerdere bestelling kan hebben, maar een bestelling altijd maar 1 klant heeft.
</p>



## Tabellen koppelen

In een vorige opdracht heb je een nieuwe tabel gemaakt om van kortingsbonnen de waarde en geldigheidsdatum bij te houden:

<table>
<tr><td>
```SQL
CREATE TABLE kortingsbonnen (
    boncode INTEGER PRIMARY KEY AUTOINCREMENT,
    korting REAL,
    datum TEXT
);
```
</td><td>
<p><img
src="https://raw.githubusercontent.com/rweeda/PythonIA/main/sql/img/tabel_kortingsbonnen.png"
alt="Tabel kortingsbonnen" width="200"></p>
</td></tr></table>

<p>Als je bij een bestelling wilt bijhouden welke kortingsbon gebruikt, dan moet je de tabel <i>besteldePizza</i> uitbreiden met een kolom die verwijst naar <i>kortingsbonnen</i>.</p>

<p>Dit doe je met een <b>foreign key</b>. Een foreign key is een kolom in een tabel die verwijst naar een primary key in een andere tabel. Zo leg je een relatie tussen twee tabellen.</p>

[picture ERD kortingsbonnen: DaniloIA_ERD_metKortingsbon.png]


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


### Verwerkingsopdracht Foreign keys bij Danilo's Pizzeria

Bekijk het overzicht van de tabellen en beantwoord de volgende vragen:
<img src="https://raw.githubusercontent.com/rweeda/PythonIA/main/sql/DaniloIA_ERD.png" alt="overzicht tabellen" width="500"></p



<ol type="a">
<li>Hoeveel foreign keys heeft tabel <i>besteldepizza</i>? Benoem voor elk de tabel waar naar verwezen wordt en de bijbehorende kolomnaam.
<li>Hoeveel foreign keys heeft tabel <i>formaat</i>?
<li>Leg in je eigen woorden wat de volgende code betekent: <code>FOREIGN KEY (formaatcode) REFERENCES formaat(formaatcode)</code>.
<li>Leg in je eigen woorden wat er mis is aan de volgende code: <code>FOREIGN KEY (formaatcode) REFERENCES formaat(omschrijving)</code>.
</ol>

<p>Bekijk <a
href="https://rweeda.github.io/PythonIA/docs/IA_sql_oplossingen.html#opgave471"
target="_blank">hier</a> de voorbeelduitwerking.</p>

<!--

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

-->


