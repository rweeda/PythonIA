###Overzicht Onderwerp 1: Inleiding databases
 <div class="activity-item time-block">
    <div class="fa fa-clock-o fa-3x"><br></div>
    <br>XX uur
</div>


<p>We beginnen met het verkennen van databases. Wat zijn het, waar kom je ze 
tegen, hoe zijn ze opgebouwd en hoe kun je er nuttige informatie uit halen? 
In deze onderwerp werk je met een database van Pizzeria Danilo.</p>

<img src="https://raw.githubusercontent.com/rweeda/PythonIA/main/sql/img/H1_overzicht.png" width="100">
</p>


<p>Leerdoelen</p>

In dit onderwerp:



###Overzicht ONDERWERP 1: DATABASES

<h5><img src="https://raw.githubusercontent.com/rweeda/PythonIA/main/sql/img/H1_overzicht.png" alt="logo onderwerp 1" style="float: right; margin: 4px;" width="150" height="151">
1: Kennismaking met databases<br></h5>


<p>Data is overal. In dit onderwerp leer je hoe gegevens op een gestructureerde manier in tabellen van een database worden opgeslagen. Zo kun je snel en eenvoudig informatie opvragen wanneer je die nodig hebt. Zo’n verzoek noem je een <strong>query</strong>, en daarvoor gebruik je een speciale vraagtaal: <strong>SQL</strong>, wat staat voor <em>Structured Query Language</em>. Dit is de standaardtaal om met databases te werken.</p>

<p>In dit onderwerp gebruik je <strong>SQLite</strong> — een eenvoudige, lichtgewicht database — om SQL te leren.</p>

<p>We beginnen met het verkennen van databases. Wat zijn het? Waar kom je ze tegen? Hoe zijn ze opgebouwd? En hoe kun je er nuttige informatie uit halen? In deze cursus werk je met de database van Pizzeria Danilo als voorbeeld.</p>



<p>Naast het opzoeken van informatie, kun je met SQL ook tabellen maken, 
vullen, aanpassen en verwijderen. Deze acties heten CRUD (Create, Read, 
Update, Delete). Om te zorgen dat informatie veilig blijft, hebben gebruikers 
vaak verschillende rechten. Niet iedereen mag zomaar tabellen verwijderen, en 
ook niet iedereen mag alle gegevens inzien. In deze onderwerp leer je 
nadenken over wie welk acties mag uitvoeren op een database, bijvoorbeeld het 
aanpassen en toevoegen van gegevens en verwijderen van gegevens.</p> 

<p>Leerdoelen</p>

In dit onderwerp: <ul> 


</ul>

<p>In dit onderwerp:</p>
<ul>
  <li>leer je de begrippen <em>database</em>, <em>SQL</em> en <em>SQLite</em> kennen;</li>
  <li>ontdek je dat een <strong>database</strong> een georganiseerde verzameling gegevens is, opgeslagen in tabellen met rijen en kolommen;</li>
  <li>leer je hoe data gestructureerd wordt opgeslagen in tabellen;</li>
  <li>maak je kennis met de drie datatypen in SQLite: <strong>TEXT</strong> (tekst), <strong>INTEGER</strong> (geheel getal) en <strong>REAL</strong> (kommagetal);</li>
  <li>leer je dat elke tabel een <em>primary key</em> heeft: een kolom waarvan elk rij een unieke waarde bevat;</li>
  <li>ontwerp je zelf een eenvoudige tabel;</li>
  <li>leer je wat een <em>databasemanagementsysteem</em> (DBMS) is;</li>
  <li>leer je het verschil tussen gegevens, data en informatie;
  
  
<li>TODO leer je dat je gegevens uit een database kan ophalen (Read), kan 
maken (Create), aanpassen (Update), en verwijderen (Delete); 


<li>TODO OND1 leer je dat de vier acties samen een acronym 'CRUD' 
(Create-Read-Update-Delete) hebben;

</li> <li>TODO OND1 leer je dat gebruikers verschillende CRUD rechten hebben 
op een database; <li> TODO UITLEGGEN DAT HET UITVOEREN IN DE VERDIEPING STAAT 

</ul>
</p>
<p>
 <div class="activity-item time-block">
    <div class="fa fa-clock-o fa-3x"><br></div>
    <br>1 uur
</div>
</p>


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


###Overzicht Onderwerp 3: SQL - : Operatoren, ORDER BY en LIMIT
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
<li>leer je logische operatoren AND, OR, NOT te gebruiken, en combinaties daarvan;
<li>leer je met SQL groepsfuncties gebruiken op kolommen: `MIN()`, `MAX()`, `SUM()`, `AVG()`,  `COUNT(*)`;
<li>TODO `DISTINCT`;
</ul>

###Overzicht Onderwerp 4: JOIN


 <div class="activity-item time-block">
    <div class="fa fa-clock-o fa-3x"><br></div>
    <br>XX uur
</div>

<p>In dit onderwerp... </p>

<p>Leerdoelen</p>

In dit onderwerp:
<ul> 
<li>met `JOIN` gegevens uit meerdere tabellen combineren;
<li>TODO koppelen (Foreign key)
</ul>


###Overzicht Onderwerp VERDIEPING: GROUP BY, HAVING


 <div class="activity-item time-block">
    <div class="fa fa-clock-o fa-3x"><br></div>
    <br>XX uur
</div>

<p>In dit onderwerp... </p>

<p>Leerdoelen</p>

In dit onderwerp:
<ul> 


<li>leer je met `GROUP BY` rijen met gegevens te groeperen zodat je daarna functies kan gebruiken
<li>leer je met `HAVING` ...

<li>OPTIONEEL??? leer je rekenen met: `+`, `-`, `*`, `/`
</ul>


# Overzicht Onderwerp VERDIEPING: Create - Read - Update - Delete uitvoeren

 <div class="activity-item time-block">
    <div class="fa fa-clock-o fa-3x"><br></div>
    <br>XX uur
</div>


<p>Naast het opzoeken van informatie, kun je met SQL ook tabellen maken, 
vullen, aanpassen en verwijderen. Deze acties heten CRUD (Create, Read, 
Update, Delete). In deze onderwerp leer je alle acties uitvoeren: het van 
maken van tabellen, het aanpassen en toevoegen van gegevens en verwijderen 
van gegevens en tabellen. 

<p>Elke keer als je webpagina ververst, wordt de 
oorspronkelijke database hersteld. Je hoeft dus niet bang te zijn om iets 
fout te doen — experimenteren mag!
</p>


<p>Leerdoelen</p>

In dit onderwerp: <ul> VERDEIPING OBJECT: insert into update delete 


Op record niveau vs op tabelniveau


TABEL: 

<li>TODO OND1 leer je dat er naast het ophalen (Read) van tabellen en 
gegevens ook andere acties mogelijk zijn, namelijk aanmaken (Create) 
aanpassen (Update), en verwijderen (Delete) van gegevens en van tabellen; 

<li>VERDIPEING leer je hoe je met de SQL statement <code>CREATE TABLE</code> 
een tabel maakt; <li>VERDIEPING leer je hoe je een kolom als primary key 
aanmaakt, en deze automatisch doornummert; <li>VERDIEPING leer je hoe je met 
de SQL statement <code>INSERT INTO... VALUES</code> gegevens in een tabel 
invoert, waaronder ook een NULL voor een waarde dat automatisch genummerd 
wordt. <li>VERDIEPING TODO UPDATE <li>VERDIEPING TODO DELETE <li>ALTER 


</ul>

