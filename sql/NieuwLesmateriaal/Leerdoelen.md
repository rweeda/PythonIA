https://basthon.informatica-actief.nl/?from= https://raw.githubusercontent.com/rweeda/PythonIA/main/sql/SQL_IA_4.1.ipynb&kernel=sql&from=&module=https://raw.githubusercontent.com/rweeda/PythonIA/main/sql/daniloIA.db
https://basthon.informatica-actief.nl/?from= https://raw.githubusercontent.com/rweeda/PythonIA/main/sql/SQL_IA_4.2.ipynb&kernel=sql&from=&module=https://raw.githubusercontent.com/rweeda/PythonIA/main/sql/daniloIA.db
https://basthon.informatica-actief.nl/?from= https://raw.githubusercontent.com/rweeda/PythonIA/main/sql/SQL_IA_4.3.ipynb&kernel=sql&from=&module=https://raw.githubusercontent.com/rweeda/PythonIA/main/sql/daniloIA.db
https://basthon.informatica-actief.nl/?from= https://raw.githubusercontent.com/rweeda/PythonIA/main/sql/SQL_IA_4.4.ipynb&kernel=sql&from=&module=https://raw.githubusercontent.com/rweeda/PythonIA/main/sql/daniloIA.db
https://basthon.informatica-actief.nl/?from= https://raw.githubusercontent.com/rweeda/PythonIA/main/sql/SQL_IA_4.5.ipynb&kernel=sql&from=&module=https://raw.githubusercontent.com/rweeda/PythonIA/main/sql/daniloIA.db
https://basthon.informatica-actief.nl/?from= https://raw.githubusercontent.com/rweeda/PythonIA/main/sql/SQL_IA_4.6.ipynb&kernel=sql&from=&module=https://raw.githubusercontent.com/rweeda/PythonIA/main/sql/daniloIA.db
https://basthon.informatica-actief.nl/?from= https://raw.githubusercontent.com/rweeda/PythonIA/main/sql/SQL_IA_4.7.ipynb&kernel=sql&from=&module=https://raw.githubusercontent.com/rweeda/PythonIA/main/sql/daniloIA.db
https://basthon.informatica-actief.nl/?from= https://raw.githubusercontent.com/rweeda/PythonIA/main/sql/SQL_IA_4.8.ipynb&kernel=sql&from=&module=https://raw.githubusercontent.com/rweeda/PythonIA/main/sql/daniloIA.db
https://basthon.informatica-actief.nl/?from= https://raw.githubusercontent.com/rweeda/PythonIA/main/sql/SQL_IA_4.9.ipynb&kernel=sql&from=&module=https://raw.githubusercontent.com/rweeda/PythonIA/main/sql/daniloIA.db
https://basthon.informatica-actief.nl/?from= https://raw.githubusercontent.com/rweeda/PythonIA/main/sql/SQL_IA_4.10.ipynb&kernel=sql&from=&module=https://raw.githubusercontent.com/rweeda/PythonIA/main/sql/daniloIA.db
https://basthon.informatica-actief.nl/?from= https://raw.githubusercontent.com/rweeda/PythonIA/main/sql/SQL_IA_4.11.ipynb&kernel=sql&from=&module=https://raw.githubusercontent.com/rweeda/PythonIA/main/sql/daniloIA.db
https://basthon.informatica-actief.nl/?from= https://raw.githubusercontent.com/rweeda/PythonIA/main/sql/SQL_IA_4.12.ipynb&kernel=sql&from=&module=https://raw.githubusercontent.com/rweeda/PythonIA/main/sql/daniloIA.db

### Overzicht Onderwerp 1: Inleiding databases
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
<ul>
<li>leer je dat een database gebruikt wordt om data op een gestructureerde manier (in tabellen) op te slaan;
<li>leer je dat gebruikers van een database verschillende rechten hebben, bijvoorbeeld om data in te voeren (CREATE), lezen (READ), aan te passen (UPDATE), of te verwijderen (DELETE) - de zogeheten CRUD rechten;
<li>leer je dat gegevens in een tabel uniek aanwijsbaar moeten zijn, met een primary key;
<li>leer je met SQL een query te maken om gegevens uit de database te halen en te tonen;
<li>leer je met voorwaarden aan de gegevens te stellen die getoond moeten worden;
<li>leer je hoe tabellen aan elkaar gekoppeld zijn en hoe je gegevens uit verschillende tabellen kunt combineren.
</ul>





### Overzicht ONDERWERP 1: DATABASES

<h5><img src="https://raw.githubusercontent.com/rweeda/PythonIA/main/sql/img/H1_overzicht.png" alt="logo onderwerp 1" style="float: right; margin: 4px;" width="150" height="151">
1: Kennismaking met databases<br></h5>


<p>Data is overal. In dit onderwerp leer je hoe gegevens op een gestructureerde manier in tabellen van een database worden opgeslagen. Zo kun je snel en eenvoudig informatie opvragen wanneer je die nodig hebt. Zo’n verzoek noem je een <strong>query</strong>, en daarvoor gebruik je een speciale vraagtaal: <strong>SQL</strong>, wat staat voor <em>Structured Query Language</em>. Dit is de standaardtaal om met databases te werken.</p>

<p>In dit onderwerp gebruik je <strong>SQLite</strong> — een eenvoudige, lichtgewicht database — om SQL te leren.</p>

<p>We beginnen met het verkennen van databases. Wat zijn het? Waar kom je ze tegen? Hoe zijn ze opgebouwd? En hoe kun je er nuttige informatie uit halen? In deze cursus werk je met de database van Pizzeria Danilo als voorbeeld.</p>


<p>Met SQL kun je gegevens in een database invoeren (Create), opzoeken (Read), aanpassen (Update) en verwijderen (Delete). Afgekort heten deze acties CRUD. Om te zorgen dat informatie veilig blijft, hebben gebruikers 
vaak verschillende rechten. Niet iedereen mag zomaar tabellen verwijderen, en 
ook niet iedereen mag alle gegevens inzien. In deze onderwerp leer je 
nadenken over wie welk acties mag uitvoeren op een database, bijvoorbeeld het 
aanpassen en toevoegen van gegevens en verwijderen van gegevens.</p> 

<p>Leerdoelen</p>


<p>In dit onderwerp:</p>
<ul>
  <li>leer je de begrippen <em>database</em>, <em>SQL</em> en <em>SQLite</em> kennen;</li>
  <li>ontdek je dat een <strong>database</strong> een georganiseerde verzameling gegevens is, opgeslagen in tabellen met rijen en kolommen;</li>
  <li>leer je hoe data gestructureerd wordt opgeslagen in tabellen;</li>
  <li>maak je kennis met de drie datatypen in SQLite: <strong>TEXT</strong> (tekst), <strong>INTEGER</strong> (geheel getal) en <strong>REAL</strong> (kommagetal);</li>
  <li>leer je dat elke tabel een <em>primary key</em> heeft: een kolom waarvan elk rij een unieke waarde bevat;</li>
  <li>ontwerp je zelf een eenvoudige tabel;</li>
  <li>leer je wat een <em>databasemanagementsysteem</em> (DBMS) is;</li>
  <li>TODO leer je dat je gegevens uit een database kan ophalen (Read), 
maken (Create), aanpassen (Update), en verwijderen (Delete) - afgekort tot <b>CRUD</b>; 
  <li>leer je het verschil tussen gegevens, data en informatie;
  
  




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


### Overzicht ONDERWERP 2: SELECT - FROM
 <div class="activity-item time-block">
    <div class="fa fa-clock-o fa-3x"><br></div>
    <br>1 uur
</div>


<p>In deze onderwerp werk je met een database van Pizzeria Danilo. De database bestaat uit meerdere tabellen, bijvoorbeeld tabel <i>pizza</i> met informatie over de verschillende pizza's, en <i>klanten</i> met de contactgegevens van de klanten. 
Met <b>SQL</b> (Structured Query Language) kan je gegevens uit de database halen. Je leert verschillende commando's waarmee je de gegevens kan tonen.</p>


<p>Leerdoelen</p>

In dit onderwerp:
<ul> 
<li>leer je dat SQL (Structured Query Language) de standaardtaal om gegevens in een database op te slaan, te bewerken en op te halen;
<li>leer je het begip query voor een zoekvraag;</li>
<li>leer je een <code>SELECT - FROM</code> query te gebruiken om informatie uit een tabel te halen;</li>
<li>leer je een kolom te hernoemen met <code>AS</code>;</li>

<li>maak je kennis met meerdere tabellen uit de database van Danilo's pizzeria;</li>

</ul>

### Overzicht 3: WHERE
<h4>3: WHERE</h4>
 <div class="activity-item time-block">
    <div class="fa fa-clock-o fa-3x"><br></div>
    <br>2 uur
</div>
<p>In dit onderwerp leer je hoe je met WHERE informatie kunt opvragen die aan specifieke voorwaarden moet voldoen. We breiden WHERE uit met wiskundige operatoren, logische operatoren en leren met de LIKE te zoeken naar delen van teksten. Daarnaast leer je hoe je omgaat met fouten door foutmeldingen lezen en fouten op te sporen. Ook leer je commentaar te gebruiken, en het schrijven van nette queries om fouten te voorkomen.</p>

<p>Leerdoelen</p>

In dit onderwerp:
<ul> 

<li>leer je <code>WHERE</code> te gebruiken om voorwaarden aan de opgehaalde informatie te stellen;</li>
<li>leer je wiskundige operatoren gebruiken: '<', '<=', '>', '>=' en '<>';</li>
<li>leer je zoeken met <code>LIKE</code> en joker '%';
<li>leer je logische operatoren <code>AND</code>, <code>OR</code>, <code>NOT</code> te gebruiken, en combinaties daarvan;

<li>leer je gebruik te maken van commentaar;</li>
<li>leer je nette queries te schrijven;</li>
<li>leer je fouten op te sporen en op te lossen.</li>
</ul>

### Overzicht Onderwerp 4: 
<h4>5: LIMIT, ORDER BY en groepsfuncties</h4>
 <div class="activity-item time-block">
    <div class="fa fa-clock-o fa-3x"><br></div>
    <br>1 uur
</div>


<p>In dit onderwerp leer je welke andere SQL commando's er zijn. Bijvoorbeeld om het aantal rijen in een overzicht te beperken, of om een kolom te sorteren. Daarnaast leren we groepsfuncties gebruiken om rekensommen te maken op kolommen, en met DISTINCT alleen unieke waarden op te halen.</p>


<p>Leerdoelen</p>

In dit onderwerp:
<ul> 

<li>leer je welke SQL commando's er zijn en in welk volgorde ze staan;</li>
<li>leer je het aantal rijen te beperken met <code>LIMIT</code>;</li>
<li>leer je gegevens in een kolom sorteren met <code>ORDER BY</code>;

<li>leer je SQL functies gebruiken op kolommen: <code>COUNT()</code>, <code>MIN()</code>, <code>MAX()</code>, <code>SUM()</code>, <code>AVG()</code>;
<li>leer je met <code>DISTINCT</code> alleen unieke waarden terug te krijgen door dubbele rijen uit het resultaat te verwijderen;
<li>leer je met <code>COUNT(DISTINCT ..)</code> het aantal unieke waarden in een kolom te tellen.

</ul>


### Overzicht Onderwerp 5: JOIN
<h4>6: JOIN</h4>

 <div class="activity-item time-block">
    <div class="fa fa-clock-o fa-3x"><br></div>
    <br>1 uur
</div>

<p>De kracht van een database is dat het in staat stelt om gegevens uit verschillende tabellen te combineren. In dit onderwerp leer je hoe tabellen aan elkaar gekoppeld zijn, en hoe je met JOIN gegevens uit verschillende tabellen samenvoegen in een overzicht.</p>

<p>Leerdoelen</p>

In dit onderwerp:
<ul> 
<li>leer je hoe je een strokendiagram kunt gebruiken om te zien hoe tabellen aan elkaar gekoppeld zijn;
<li>leer je dat gegevens in een tabel aan een ander gekoppeld kunnen worden met een <b>foreign key</b>;
<li>leer je met <code>JOIN</code> gegevens uit meerdere tabellen combineren;
</ul>


# Overzicht Onderwerp VERDIEPING: GROUP BY, HAVING


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
Update, Delete). In deze onderwerp leer je alle acties uitvoeren: eerste het invoeren, aanpassen en verwijderen van gegevens uit tabellen. Daarna leer je ook hoe je tabellen kunt aanmaken, aanpassen en verwijderen.
</p>
<p>Elke keer als je webpagina ververst, wordt de 
oorspronkelijke database hersteld. Je hoeft dus niet bang te zijn om iets 
fout te doen — experimenteren mag!
</p>


<p>Leerdoelen</p>

In dit onderwerp:

<ul>
<li>leer je gegevens invoeren in een tabel met <code>INSERT INTO</code>;
<li>leer je gegevens aanpassen in een tabel met <code>INSERT INTO</code>;


 VERDEIPING OBJECT: insert into update delete 


Op record niveau vs op tabelniveau


TABEL: 

<li>TODO OND1 leer je dat er naast het ophalen (Read) van tabellen en 
gegevens ook andere acties mogelijk zijn, namelijk aanmaken (Create) 
aanpassen (Update), en verwijderen (Delete) van gegevens en van tabellen; 
<li>VERDIPEING leer je hoe je met de SQL statement <code>CREATE TABLE</code> 
een tabel maakt; 
<li>VERDIEPING leer je hoe je een kolom als primary key 
aanmaakt, en deze automatisch doornummert; 
<li>VERDIEPING leer je hoe je met 
de SQL statement <code>INSERT INTO... VALUES</code> gegevens in een tabel 
invoert, waaronder ook een NULL voor een waarde dat automatisch genummerd 
wordt. 
<li>VERDIEPING TODO UPDATE 
<li>VERDIEPING TODO DELETE 
<li>ALTER 


</ul>

