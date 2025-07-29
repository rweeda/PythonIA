
# ONDERWERP 7: Gegevens invoeren, aanpassen en verwijderen

<p>Elke keer dat je de webpagina ververst, wordt de oorspronkelijke database hersteld. Je hoeft dus niet bang te zijn om iets fout te doen — experimenteren mag!</p>

<p>Wil je je code bewaren? Sla deze dan op via 'Bestand' en vervolgens 'Bewaar notebook als...'. Je kunt je werk ook tussentijds opslaan of inleveren.</p>

## 7.1: Gegevens in een tabel invoeren

<p>Met INSERT INTO ... VALUES (...) voeg je nieuwe gegevens toe aan een tabel.</p>

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

### Verwerkingsopdracht 7.1.1 Pizza toevoegen en controleren

<ol type="a">
  <li>Voer de code hierboven uit om een <i>Pizza Hawaii</i> toe te voegen aan de tabel <i>pizza</i>.</li>
  <li>Controleer daarna of het is gelukt. Dit doe je met:</li>


<pre><code class="language-sql">
SELECT *
FROM pizza;
</code></pre>
</ol>
<p>Bekijk <a
href="https://rweeda.github.io/PythonIA/docs/IA_sql_oplossingen.html#opgave711"
target="_blank">hier</a> de voorbeelduitwerking.</p>

<!--
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



### Verwerkingsopdracht 7.1.2 Een nieuwe glutenvrije bodem

<p>We gebruiken de tabel <i>bodem</i>. Deze bevat de kolommen:</p>
<ul>
  <li><b>bodemcode</b> (AUTOINCREMENT, hoef je niet zelf in te vullen)</li>
  <li><b>omschrijving</b> (bijvoorbeeld "Dunne bodem")</li>
  <li><b>plusprijs</b> (bijvoorbeeld 1.00)</li>
</ul>

<p>Welke van de volgende <code>INSERT INTO</code>-statements voegt correct een nieuwe bodem toe met omschrijving <b>Glutenvrij</b> en een toeslag van €1,50?</p>

<ul type="A">
  <li>
<pre><code class="language-sql">
INSERT INTO bodem (bodemcode, omschrijving, plusprijs)
VALUES (5, "Glutenvrij", 1.50);
</code></pre>
  </li>
  <li>
<pre><code class="language-sql">
INSERT INTO bodem (omschrijving, plusprijs)
VALUES ("Glutenvrij", 1.50);
</code></pre>
  </li>
  <li>
<pre><code class="language-sql">
INSERT INTO bodem
VALUES ("Glutenvrij", 1.50);
</code></pre>
  </li>
  <li>
<pre><code class="language-sql">
INSERT INTO bodem (omschrijving, plusprijs)
VALUES (Glutenvrij, €1,50);
</code></pre>
  </li>
</ul>

<p>Bekijk de <a href="https://rweeda.github.io/PythonIA/docs/IA_sql_oplossingen.html#opgave712" target="_blank">voorbeelduitwerking</a>.</p>

<!--
Antwoord: B
Toelichting: bodemcode is een AUTOINCREMENT-veld en moet je dus NULL invullen.
Bij antwoord D ontbreken aanhalingstekens en het euroteken is fout in SQL.
-->
### Verwerkingsopdracht 7.1.3 Pan-bodem toevoegen

<p>Gebruik de tabel <i>bodem</i>. Deze bevat de kolommen:</p>
<ul>
  <li><b>bodemcode</b> (AUTOINCREMENT)</li>
  <li><b>omschrijving</b></li>
  <li><b>plusprijs</b></li>
</ul>

<ol type="a">
  <li>Voeg een nieuwe dikke bodem toe met de omschrijving "Pan" en een toeslag van €2,00.</li>
  <li>Controleer daarna of het gelukt is. Dit doe je met:</li>
</ol>

<pre><code class="language-sql">
SELECT *
FROM bodem;
</code></pre>

<p>Bekijk de <a href="https://rweeda.github.io/PythonIA/docs/IA_sql_oplossingen.html#opgave713" target="_blank">voorbeelduitwerking</a>.</p>


<!--
<pre><code class="language-sql"> 
INSERT INTO bodem (bodemcode, omschrijving, plusprijs)
VALUES (NULL, "Pan", 2.00);


-- check:
SELECT *
FROM bodem;
</code></pre>
-->

## 7.2: Gegevens uit een tabel verwijderen

<p>Met DELETE FROM kun je een of meerdere rijen verwijderen uit een tabel:</p>

<pre><code class="language-sql">
DELETE FROM tabelnaam
WHERE voorwaarde;
</code></pre>

<ul>
  <li>Achter DELETE FROM geef je de naam van de tabel aan.</li>
  <li>Met WHERE geef je aan welke rij(en) je wilt verwijderen. Gebruik hier bij voorkeur de <i>primary key</i>.</li>
  <li>Let op: Als je geen WHERE gebruikt, worden <i>alle</i> rijen uit de tabel verwijderd!</li>
</ul>

<p>Voorbeeld: Deze query verwijdert de rij uit de tabel <i>pizza</i> waarbij de <b>pizzacode</b> gelijk is aan 1:</p>

<pre><code class="language-sql">
DELETE FROM pizza
WHERE pizzacode = 1;
</code></pre>

### Verwerkingsopdracht: Pizza verwijderen en controleren

<ol type="a">
  <li>Voer de code hierboven uit waarmee de pizza met <i>pizzacode</i> 1 wordt verwijderd uit de tabel <i>pizza</i>.</li>
  <li>Controleer daarna of het is gelukt met:</li>
</ol>

<pre><code class="language-sql">
SELECT *
FROM pizza;
</code></pre>



### Verwerkingsopdracht: Verwijder een pizza

<p>Omdat deze nauwelijks besteld wordt, wil Danilo de "Pazza"-pizza van het menu halen.</p>

<ol type="a">
  <li>Schrijf een query om deze pizza uit de tabel te verwijderen.</li>
  <li>Controleer daarna met <code>SELECT *</code> of het gelukt is.</li>
</ol>

<p>Bekijk de <a href="https://rweeda.github.io/PythonIA/docs/IA_sql_oplossingen.html#opgave471" target="_blank">voorbeelduitwerking</a>.</p>
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




## 7.3: Gegevens in een tabel aanpassen

<p>Met UPDATE kun je gegevens in een tabel aanpassen:</p>

<pre><code class="language-sql">
UPDATE tabelnaam
SET kolom1 = nieuwe_waarde1, kolom2 = nieuwe_waarde2
WHERE voorwaarde;
</code></pre>

<ul>
  <li>Achter <code>UPDATE</code> geef je de naam van de tabel aan.</li>
  <li>Met <code>SET</code> geef je aan welke kolom(kolommen) je wilt aanpassen en wat de nieuwe waarde wordt.</li>
  <li>Met <code>WHERE</code> geef je aan welke rij(en) je wilt aanpassen, bij voorkeur via de <i>primary key</i>.</li>
  <li><strong>Let op:</strong> Als je geen <code>WHERE</code> gebruikt, worden <i>alle</i> rijen aangepast!</li>
</ul>

<p>Voorbeeld: deze query past de naam van de pizza met <b>pizzacode</b> 1 aan naar "Hawaii". Alle andere kolommen blijven ongewijzigd:</p>

<pre><code class="language-sql">
UPDATE pizza
SET pizzanaam = "Hawaii"
WHERE pizzacode = 1;
</code></pre>

### Verwerkingsopdracht 7.3.1 Pas de prijs van een pizza aan

<ol type="a">
  <li>Schrijf een query die voor de pizza met <b>naam</b> gelijk aan <i>"Margherita"</i> de <b>basisprijs</b> verhoogt naar €8,00.</li>
  <li>Controleer daarna met <code>SELECT *</code> of het gelukt is.</li>
</ol>

<p>Bekijk de <a href="https://rweeda.github.io/PythonIA/docs/IA_sql_oplossingen.html#opgave471" target="_blank">voorbeelduitwerking</a>.</p>
<!--
<pre><code class="language-sql"> 
UPDATE pizza
SET basisprijs = 8.00
WHERE naam = "Margherita";
</code></pre>
-->


## 7.4: Nieuwe tabel aanmaken

<p>Met een <code>CREATE TABLE</code>-query maak je een nieuwe tabel aan in de database.</p>

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
  <li>Tussen haakjes zet je per kolom de kolomnaam en het datatype (zoals <code>TEXT</code>, <code>INTEGER</code> of <code>REAL</code>).</li>
</ul>

<p>Elke tabel moet een primary key hebben. De database kan automatisch doornummeren zodra er nieuwe gegevens worden toegevoegd. In die kolom mag elke waarde maar één keer voorkomen. Dit doe je met: <code>INTEGER PRIMARY KEY AUTOINCREMENT</code>.</p>

<p>Voorbeeld: Deze query maakt een tabel <i>pizza</i> waarbij de <i>pizzacode</i> als primary key automatisch wordt genummerd:</p>

<pre><code class="language-sql">
CREATE TABLE pizza (
  pizzacode INTEGER PRIMARY KEY AUTOINCREMENT, 
  naam TEXT,
  omschrijving TEXT,
  basisprijs REAL
);
</code></pre>

### Verwerkingsopdracht 7.4.1 Nieuwe tabel kortingsbonnen aanmaken

<p>Maak een nieuwe tabel <i>kortingsbon</i> aan waarin je informatie opslaat over kortingsbonnen die in omloop zijn: <b>boncode</b>, hoeveel <b>korting</b> ze geven en tot welke <b>datum</b> ze geldig zijn.</p>

<ol type="a">
  <li>Schrijf een <code>CREATE TABLE</code>-query voor de tabel <code>kortingsbon</code>. Bedenk welke kolommen je nodig hebt, en welke datatypes je gebruikt. Denk aan:
    <ul>
      <li>Een primary key: <i>boncode</i></li>
      <li>Automatisch doornummeren met <code>AUTOINCREMENT</code></li>
      <li>De juiste datatypes: <code>TEXT</code>, <code>INTEGER</code>, <code>REAL</code></li>
    </ul>
  </li>
  <li>Als je met <code>SELECT *</code> controleert of de tabel is aangemaakt, zie je geen gegevens. Waarom niet?</li>
</ol>

<p>Bekijk de <a href="https://rweeda.github.io/PythonIA/docs/IA_sql_oplossingen.html#opgave471" target="_blank">voorbeelduitwerking</a>.</p>
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



## 7.5: Een tabel verwijderen

<p>Met een <code>DROP TABLE</code>-query verwijder je een hele tabel uit de database. Alle gegevens in de tabel gaan dan verloren.</p>

<pre><code class="language-sql">
DROP TABLE tabelnaam;
</code></pre>

<ul>
  <li>Achter <code>DROP TABLE</code> geef je de naam van de tabel die je wilt verwijderen.</li>
  <li><strong>Let op:</strong> Deze actie kan niet ongedaan worden gemaakt!</li>
  <li>Wil je de oorspronkelijke database herstellen? Ververs dan de webpagina. Sla wel eerst je werk op via 'Bestand' en vervolgens 'Bewaar notebook als...'.</li>
</ul>

<p>Voorbeeld: deze query verwijdert de tabel <i>kortingsbon</i>:</p>

<pre><code class="language-sql">
DROP TABLE kortingsbon;
</code></pre>

### Verwerkingsopdracht: Verwijder tabel bodem

<ol type="a">
  <li>Verwijder de tabel <i>bodem</i>.</li>
  <li>Probeer daarna met <code>SELECT *</code> de gegevens uit de tabel op te halen. Welke foutmelding krijg je?</li>
</ol>

<p>Bekijk de <a href="https://rweeda.github.io/PythonIA/docs/IA_sql_oplossingen.html#opgave471" target="_blank">voorbeelduitwerking</a>.</p>

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


## 7.6: Tabel aanpassen – Kolom toevoegen

<p>Met een <code>ALTER TABLE</code>-query kun je de structuur van een bestaande tabel aanpassen, bijvoorbeeld door een kolom toe te voegen.</p>

<pre><code class="language-sql">
ALTER TABLE tabelnaam
ADD kolomnaam datatype;
</code></pre>

<ul>
  <li>Achter <code>ALTER TABLE</code> geef je de naam van de tabel op.</li>
  <li>Met <code>ADD</code> voeg je een kolom toe, gevolgd door de naam en het datatype.</li>
</ul>

<p>Voorbeeld: deze query voegt een kolom <b>email</b> toe aan de tabel <i>bezorger</i>:</p>

<pre><code class="language-sql">
ALTER TABLE bezorger
ADD email TEXT;
</code></pre>

### Verwerkingsopdracht: Kolom toevoegen

Voeg de kolom <b>geboortedatum</b> toe aan tabel <i>klant</i>.

<p>Bekijk de <a href="https://rweeda.github.io/PythonIA/docs/IA_sql_oplossingen.html#opgave471" target="_blank">voorbeelduitwerking</a>.</p>

<!--
<pre><code class="language-sql">
ALTER TABLE klant
ADD geboortedatum TEXT;
</code></pre>
-->



## 7.7: Tabel aanpassen – Kolom hernoemen

<p>Met <code>ALTER TABLE ... RENAME COLUMN</code> kun je een bestaande kolom een nieuwe naam geven.</p>

<pre><code class="language-sql">
ALTER TABLE tabelnaam
RENAME COLUMN oude_kolomnaam TO nieuwe_kolomnaam;
</code></pre>

<ul>
  <li>Geef eerst de naam van de tabel op.</li>
  <li>Gebruik daarna <code>RENAME COLUMN</code> om de kolom te hernoemen.</li>
</ul>

<p>Voorbeeld: hernoem de kolom <b>plusprijs</b> naar <b>toeslag</b> in de tabel <i>bodem</i>:</p>

<pre><code class="language-sql">
ALTER TABLE bodem
RENAME COLUMN plusprijs TO toeslag;
</code></pre>

### Verwerkingsopdracht 7.7.1 Kolom hernoemen

<p>Hernoem de kolom <b>naam</b> naar <b>klantnaam</b> in de tabel <i>klant</i>.</p>

<p>Bekijk de <a href="https://rweeda.github.io/PythonIA/docs/IA_sql_oplossingen.html#opgave771" target="_blank">voorbeelduitwerking</a>.</p>

<!--
<pre><code class="language-sql">
ALTER TABLE klant
RENAME COLUMN naam TO klantnaam;
</code></pre>
-->


## 7.8: Tabel aanpassen – Tabel hernoemen

<p>Met <code>ALTER TABLE ... RENAME TO</code> geef je een bestaande tabel een nieuwe naam.</p>

<pre><code class="language-sql">
ALTER TABLE oude_tabelnaam
RENAME TO nieuwe_tabelnaam;
</code></pre>

<ul>
  <li>Achter <code>ALTER TABLE</code> geef je de oude tabelnaam op.</li>
  <li>Met <code>RENAME TO</code> geef je de nieuwe naam.</li>
</ul>

<p>Voorbeeld: hernoem tabel <i>bezorger</i> naar <i>medewerker</i>:</p>

<pre><code class="language-sql">
ALTER TABLE bezorger
RENAME TO medewerker;
</code></pre>

### Verwerkingsopdracht 7.8.1 Tabel hernoemen

<p>Hernoem de tabel <i>formaat</i> naar <i>grootte</i>.</p>
<p>Bekijk de <a href="https://rweeda.github.io/PythonIA/docs/IA_sql_oplossingen.html#opgave481" target="_blank">voorbeelduitwerking</a>.</p>
<!--
<pre><code class="language-sql">
ALTER TABLE formaat
RENAME TO grootte;
</code></pre>
-->

## 7.9: Overzicht van alle tabellen

<p>In het <b>ERD-schema</b> (Entity-Relationship Diagram) hieronder zie je een overzicht van de tabellen en hoe ze met elkaar verbonden zijn.</p>

<img src="https://raw.githubusercontent.com/rweeda/PythonIA/main/sql/DaniloIA_ERD.png" alt="overzicht tabellen" width="500">

<p>De pijlen geven de koppelingen tussen tabellen aan. Een bestelling heeft een klantnummer. Aan het pijltje zie je dat de gegevens over de klant te vinden zijn in de tabel <i>klanten</i>.</p>

<p><strong>Extra:</strong> De tekens bij de pijlen geven het type relatie aan. De relatie tussen <i>klant</i> en <i>bestelling</i> is een één-op-veel-relatie: één klant kan meerdere bestellingen hebben, maar een bestelling hoort bij één klant.</p>


## 7.10: Tabellen koppelen met een foreign key

In een eerdere opdracht heb je een nieuwe tabel gemaakt om informatie over kortingsbonnen bij te houden: de waarde van de korting en de geldigheidsdatum. Hieronder zie je de bijborende query en tabel die daarbij gemaakt is.

<table>
<tr><td>
<pre><code class="language-sql">
CREATE TABLE kortingsbonnen (
    boncode INTEGER PRIMARY KEY AUTOINCREMENT,
    korting REAL,
    datum TEXT
);
</code></pre>
</td><td>
<p><img
src="https://raw.githubusercontent.com/rweeda/PythonIA/main/sql/img/tabel_kortingsbonnen.png"
alt="Tabel kortingsbonnen" width="200"></p>
</td></tr></table>


<p>Stel, je wilt bijhouden welke kortingsbon is gebruikt bij een bestelling. Dan moet je de tabel <i>besteldePizza</i> uitbreiden met een kolom die verwijst naar de tabel <i>kortingsbonnen</i>. In het schema hieronder zie je dat er met een verbinding een relatie is getekend tussen <b>boncode</b> uit tabel <i>bestellingen</i> en <b>boncode</b> uit tabel <i>kortingsbonnen</i>.</p>

<p><img
src="https://raw.githubusercontent.com/rweeda/PythonIA/main/sql/img/tabel_kortingsbonnen_gekoppeld_bestelling.png"
alt="Tabel kortingsbonnen" width="200"></p>



<p>De relatie tussen tabellen leg je vast met een <b>foreign key</b>. Een <i>foreign key</i> is een kolom in een tabel die verwijst naar de <i>primary key</i> van een andere tabel. In dit voorbeeld verwijst de foreign key <b>boncode</b> uit tabel <i>bestellingen</i> naar de primary key <b>boncode</b> uit tabel <i>kortingsbonnen</i>.</p>

<!--
<ul>
  <li>Je legt een verband tussen twee tabellen.</li>
  <li>Je voorkomt fouten, zoals het invullen van een boncode die niet bestaat.</li>
  <li>Je kunt makkelijker gegevens opvragen, zoals welke bestellingen met welke bon zijn gedaan.</li>
</ul>
-->


### Verwerkingsopdracht 7.10.1 Foreign keys bij Danilo's Pizzeria

Bekijk het overzicht van de tabellen en beantwoord de volgende vragen:
<img src="https://raw.githubusercontent.com/rweeda/PythonIA/main/sql/DaniloIA_ERD.png" alt="overzicht tabellen" width="500"></p>


<ol type="a">
  <li>Hoeveel foreign keys heeft de tabel <i>besteldePizza</i>? Noem per key de bijbehorende tabel en kolomnaam.</li>
  <li>Hoeveel foreign keys heeft de tabel <i>formaat</i>?</li></ol>

<p>Bekijk de <a href="https://rweeda.github.io/PythonIA/docs/IA_sql_oplossingen.html#opgave471" target="_blank">voorbeelduitwerking</a>.</p>



<!--

ANTWOORDEN:
<ol type="a">
<li>Tabel <i>besteldepizza</i> heeft vier foreign keys, namelijk:
	<ol><li><b>bestelcode</b> uit tabel <i>bestelling</i> 
	<ol><li><b>pizzacode</b> uit tabel <i>pizza</i> 
	<ol><li><b>bodemcode</b> uit tabel <i>bodem</i> 
	<ol><li><b>formaatcode</b> uit tabel <i>formaat</i> 
	</ol>
</ol>

-->


## 7.11: Een foreign key maken in SQL

Voor het maken van een foreign key voeg je een regel toe in je CREATE TABLE-query:

<pre><code class="language-sql">
CREATE TABLE tabelnaam(
  kolomnaam datatype
  FOREIGN KEY (kolomnaam) REFERENCES andereTabel(primary_key_kolom);
);
</code></pre>
<p>De verwijzing in de andere tabel moet altijd naar een primary key gaan.</p>


Voorbeeld. Deze query maakt een foreign <b>boncode</b> aan:

<pre><code class="language-sql">
CREATE TABLE besteldePizza (
    besteldePizzaID INTEGER PRIMARY KEY AUTOINCREMENT,
    pizzacode INTEGER,
    bestelcode INTEGER,
    boncode INTEGER,
    FOREIGN KEY (boncode) REFERENCES kortingsbonnen(boncode)
);
</code></pre>

<p>Toelichting:</p>
<ul> 
<li>De kolom <code>boncode</code> wordt toegevoegd aan de tabel <code>besteldePizza</code>.</li> 
<li>Met <code>FOREIGN KEY (boncode) REFERENCES kortingsbonnen(boncode)</code> leg je vast dat deze kolom verwijst naar de primary key <code>boncode</code> in de tabel <code>kortingsbonnen</code>.</li> 

</ul>

Je kunt hier een filmpje bekijken waarin wordt uitgelegd wat primary en foreign keys zijn.

[![Bekijk op Youtube](https://img.youtube.com/vi/obeOGxESGLI/hqdefault.jpg)](https://www.youtube.com/embed/obeOGxESGLI?start=0&amp;end=150)

<!--https://www.youtube.com/embed/obeOGxESGLI


<iframe width="560" height="315" src="https://www.youtube.com/embed/obeOGxESGLI?start=0&amp;end=150" frameborder="0" allowfullscreen></iframe>
-->

### Verwerkingsopdracht 7.10.1 Foreign keys bij Danilo's Pizzeria

Bekijk het overzicht van de tabellen en beantwoord de volgende vragen:
<img src="https://raw.githubusercontent.com/rweeda/PythonIA/main/sql/DaniloIA_ERD.png" alt="overzicht tabellen" width="500"></p>


<ol type="a">
  <li>Leg uit wat deze regel betekent: <code>FOREIGN KEY (formaatcode) REFERENCES formaat(formaatcode)</code>.</li>
  <li>Wat gaat er mis bij deze regel: <code>FOREIGN KEY (formaatcode) REFERENCES formaat(omschrijving)</code>?</li>
</ol>

<p>Bekijk de <a href="https://rweeda.github.io/PythonIA/docs/IA_sql_oplossingen.html#opgave471" target="_blank">voorbeelduitwerking</a>.</p>



<!--

ANTWOORDEN:
<ol type="a">

<li>Tabel <i>besteldePizza</i> heeft een kolom formaatcode. Daarvoor komen de gegevens uit tabel <i>formaat</i> en kolom <b>formaatcode</b>.
<li>De foreign key verwijst naar kolom <b>omschrijving</b> uit tabel <i>formaat</i>. Dit is niet goed, want het moet verwijzen naar de primary key van tabel <i>formaat</i>, en dus <b>formaatcode</b>.
</ol>

-->
