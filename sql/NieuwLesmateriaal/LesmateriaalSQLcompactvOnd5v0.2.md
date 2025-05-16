
# ONDERWERP 5


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

Ter herinnering, hieronder zie je alle tabellen die in Danilo's database staan.
<p> <a
href="https://raw.githubusercontent.com/rweeda/PythonIA/main/sql/img/DaniloIA_ERD.png"
target="_blank">
  <img src="https://raw.githubusercontent.com/rweeda/PythonIA/main/sql/img/DaniloIA_ERD.png" alt="Klik om in een nieuw venster te openen" width="1000"/>
</a></p>


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
