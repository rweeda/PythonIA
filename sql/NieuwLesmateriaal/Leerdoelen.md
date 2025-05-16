###Overzicht Onderwerp 1: Inleiding databases
 <div class="activity-item time-block">
    <div class="fa fa-clock-o fa-3x"><br></div>
    <br>XX uur
</div>


<p>We beginnen met het verkennen van databases. Wat zijn het, waar kom je ze 
tegen, hoe zijn ze opgebouwd en hoe kun je er nuttige informatie uit halen? 
In deze onderwerp werk je met een database van Pizzeria Danilo.</p>

<p>Elke keer als je Informatica-Actief opnieuw opstart, wordt de 
oorspronkelijke database hersteld. Je hoeft dus niet bang te zijn om iets 
fout te doen — experimenteren mag!

<img src="https://raw.githubusercontent.com/rweeda/PythonIA/main/sql/img/H1_overzicht.png" width="100">
</p>


<p>Leerdoelen</p>

In dit onderwerp:



###Overzicht ONDERWERP 1: DATABASES
 <div class="activity-item time-block">
    <div class="fa fa-clock-o fa-3x"><br></div>
    <br>XX uur
</div>


<p>Data is overal. In dit onderwerp leer je hoe data op een gestructureerde manier in tabellen van een database wordt opgeslagen. Je kunt eenvoudig en snel informatie opvragen wanneer dat nodig is. Zo’n verzoek noem je een <b>query</b> en daarvoor heb je een speciale vraagtaal
nodig: <b>SQL</b>. Dat staat voor <i>Structured Query Language</i>. Dat is de standaardtaal om met databases te werken.
In deze onderwerp gebruik je <b>SQLite</b> — een eenvoudige, lichtgewicht database — om SQL te leren.

Met een SQL query (oftewel, zoekvraag), kun je gegevens uit een database tonen. In deze cursus gebruiken we <i>SQLite</i>, dat is een eenvoudige, lichtgewicht database.</p>


In dit onderwerp:

<ul>
<li>leer je de begrippen database, SQL en SQLite;
<li>leer je dat een <i>database</i> een georganiseerde verzameling gegevens is, opgeslagen in tabellen met rijen en kolommen;
<li>leer je hoe data gestructureerd opgeslagen wordt in een tabel</li>
<li>leer je de drie datatypen van SQLite: TEXT (tekst), INTEGER (geheel getal) en REAL (kommagetal)</li>
<li>leer je dat elk tabel een <i>primary key</i> heeft, dat is een kolom waarbij elk rij een uniek gegeven heeft;
<li>leer je zelf een tabel ontwerpen;
<li>leer je wat een databasemanagementsysteem (DBMS) is;
<li>leer je het verschil tussen gegevens, data en informatie.
</ul>



### Overzicht ONDERWERP 2: SQL SELECT - FROM - WHERE
 <div class="activity-item time-block">
    <div class="fa fa-clock-o fa-3x"><br></div>
    <br>XX uur
</div>


<p>In deze onderwerp werk je met een database van Pizzeria Danilo. De database bestaat uit meerdere tabellen, bijvoorbeeld tabel <i>pizza</i> met informatie over de verschillende pizza's, en <i>klanten</i> met de contactgegevens van de klanten. 
Met <b>SQL</b> (Structured Query Language) kan je gegevens uit de database halen. Je leert verschillende commando's waarmee je de gegevens kan tonen.</p>


<p>Leerdoelen</p>

In dit onderwerp:
<ul> 
<li>leer je dat SQL (Structured Query Language) de standaardtaal om gegevens in een database op te slaan, te bewerken en op te halen;
<li>leer je het begip query voor een zoekvraag;</li>
<li>leer je een <code>SELECT - FROM</code> query te gebruiken om informatie uit een tabel te halen;</li>
<li>leer je welke SQL commando's er zijn en in welk volgorde ze staan;</li>
<li>leer je een <code>WHERE</code> te gebruiken om voorwaarden aan de opgehaalde informatie te stellen;</li>
<li>maak je kennis met meerdere tabellen uit de database van Danilo's pizzeria;</li>

<li>leer je gebruik te maken van commentaar;</li>
<li>leer je nette queries te schrijven;</li>
<li>leer je fouten op te sporen en op te lossen.</li>
</ul>


###Overzicht Onderwerp 3: SQL - : Operatoren, sorteren en LIMIT
 <div class="activity-item time-block">
    <div class="fa fa-clock-o fa-3x"><br></div>
    <br>XX uur
</div>


<p>In dit onderwerp leer je hoe je informatie kan opvragen dat aan specifieke voorwaarden moet voldoen. We breiden de WHERE uit met wiskundige operatoren, logische operatoren en leren met de LIKE te zoeken naar delen van teksten. </p>


<p>Leerdoelen</p>

In dit onderwerp:
<ul> 


<li>leer je een kolom te hernoemen met `AS`;</li>
<li>leer je het aantal rijen te beperken met `LIMIT`;</li>
<li>leer je gegevens in een kolom sorteren met `ORDER BY`;
<li>leer je wiskundige operatoren gebruiken: '<', '<=', '>', '>=' en '<>';</li>
<li>leer je zoeken met <code>LIKE</code> en joker '%';
<li>leer je logische operatoren AND, OR, NOT te gebruiken, en combinaties daarvan.


</ul>


# Overzicht Onderwerp 4: Create - Read - Update - Delete

 <div class="activity-item time-block">
    <div class="fa fa-clock-o fa-3x"><br></div>
    <br>XX uur
</div>


<p>Naast het opzoeken van informatie, kun je met SQL ook tabellen maken, vullen, aanpassen en verwijderen. Deze acties heten CRUD (Create, Read, Update, Delete). Om te zorgen dat informatie veilig blijft, hebben gebruikers vaak verschillende rechten. Niet iedereen mag zomaar tabellen verwijderen, en ook niet iedereen mag alle gegevens inzien. In deze onderwerp leer je alle acties uitvoeren: het van maken van tabellen, het aanpassen en toevoegen van gegevens en verwijderen van gegevens en tabellen.

<p>Elke keer als je webpagina ververst, wordt de 
oorspronkelijke database hersteld. Je hoeft dus niet bang te zijn om iets 
fout te doen — experimenteren mag!
</p>

<p>Leerdoelen</p>

In dit onderwerp:
<ul> 
<li>leer je dat er naast het ophalen (Read) van tabellen en gegevens ook andere acties mogelijk zijn, namelijk aanmaken (Create) aanpassen (Update), en verwijderen (Delete) van gegevens en van tabellen;
<li>leer je dat de vier acties samen een acronym 'CRUD' (Create-Read-Update-Delete) hebben;</li>
<li>leer je dat gebruikers verschillende CRUD rechten hebben op een database;
<li>leer je hoe je met de SQL statement <code>CREATE TABLE</code> een tabel maakt;
<li>leer je hoe je een kolom als primary key aanmaakt, en deze automatisch doornummert;
<li>leer je hoe je met de SQL statement <code>INSERT INTO... VALUES</code> gegevens in een tabel invoert, waaronder ook een NULL voor een waarde dat automatisch genummerd wordt

</ul>

###Overzicht Onderwerp 5: JOIN, FUNCTIES en GROUP BY


 <div class="activity-item time-block">
    <div class="fa fa-clock-o fa-3x"><br></div>
    <br>XX uur
</div>

<p>In dit onderwerp... </p>

<p>Leerdoelen</p>

In dit onderwerp:
<ul> 
<li>met `JOIN` gegevens uit meerdere tabellen combineren;
<li>leer je met SQL groepsfuncties gebruiken op kolommen: `MIN()`, `MAX()`, `SUM()`, `AVG()`,  `COUNT(*)`, `DISTINCT`;

<li>leer je met `GROUP BY` rijen met gegevens te groeperen zodat je daarna functies kan gebruiken
<li>leer je met `HAVING` ...

<li>OPTIONEEL??? leer je rekenen met: `+`, `-`, `*`, `/`
<li>


</ul>
