https://basthon.informatica-actief.nl/?from= https://raw.githubusercontent.com/rweeda/PythonIA/main/sql/SQL_IA_7.1.ipynb&kernel=sql&from=&module=https://raw.githubusercontent.com/rweeda/PythonIA/main/sql/daniloIA.db
https://basthon.informatica-actief.nl/?from= https://raw.githubusercontent.com/rweeda/PythonIA/main/sql/SQL_IA_7.2.ipynb&kernel=sql&from=&module=https://raw.githubusercontent.com/rweeda/PythonIA/main/sql/daniloIA.db
https://basthon.informatica-actief.nl/?from= https://raw.githubusercontent.com/rweeda/PythonIA/main/sql/SQL_IA_7.3.ipynb&kernel=sql&from=&module=https://raw.githubusercontent.com/rweeda/PythonIA/main/sql/daniloIA.db
https://basthon.informatica-actief.nl/?from= https://raw.githubusercontent.com/rweeda/PythonIA/main/sql/SQL_IA_7.4.ipynb&kernel=sql&from=&module=https://raw.githubusercontent.com/rweeda/PythonIA/main/sql/daniloIA.db
https://basthon.informatica-actief.nl/?from= https://raw.githubusercontent.com/rweeda/PythonIA/main/sql/SQL_IA_7.5.ipynb&kernel=sql&from=&module=https://raw.githubusercontent.com/rweeda/PythonIA/main/sql/daniloIA.db
https://basthon.informatica-actief.nl/?from= https://raw.githubusercontent.com/rweeda/PythonIA/main/sql/SQL_IA_7.6.ipynb&kernel=sql&from=&module=https://raw.githubusercontent.com/rweeda/PythonIA/main/sql/daniloIA.db
https://basthon.informatica-actief.nl/?from= https://raw.githubusercontent.com/rweeda/PythonIA/main/sql/SQL_IA_7.7.ipynb&kernel=sql&from=&module=https://raw.githubusercontent.com/rweeda/PythonIA/main/sql/daniloIA.db
https://basthon.informatica-actief.nl/?from= https://raw.githubusercontent.com/rweeda/PythonIA/main/sql/SQL_IA_7.8.ipynb&kernel=sql&from=&module=https://raw.githubusercontent.com/rweeda/PythonIA/main/sql/daniloIA.db
https://basthon.informatica-actief.nl/?from= https://raw.githubusercontent.com/rweeda/PythonIA/main/sql/SQL_IA_7.9.ipynb&kernel=sql&from=&module=https://raw.githubusercontent.com/rweeda/PythonIA/main/sql/daniloIA.db
https://basthon.informatica-actief.nl/?from= https://raw.githubusercontent.com/rweeda/PythonIA/main/sql/SQL_IA_7.10.ipynb&kernel=sql&from=&module=https://raw.githubusercontent.com/rweeda/PythonIA/main/sql/daniloIA.db
https://basthon.informatica-actief.nl/?from= https://raw.githubusercontent.com/rweeda/PythonIA/main/sql/SQL_IA_7.11.ipynb&kernel=sql&from=&module=https://raw.githubusercontent.com/rweeda/PythonIA/main/sql/daniloIA.db
https://basthon.informatica-actief.nl/?from= https://raw.githubusercontent.com/rweeda/PythonIA/main/sql/SQL_IA_7.12.ipynb&kernel=sql&from=&module=https://raw.githubusercontent.com/rweeda/PythonIA/main/sql/daniloIA.db


https://basthon.informatica-actief.nl/?from= https://raw.githubusercontent.com/rweeda/PythonIA/main/sql/SQL_IA_5.2.ipynb&kernel=sql&from=&module=https://raw.githubusercontent.com/rweeda/PythonIA/main/sql/daniloIA.db

### ALGEMEEN INLEIDING
<h4>Gestructureerd data</h4>

<p>In deze cursus leer je werken met gestructureerde gegevens: <strong>databases</strong>.</p>


<p>Databases zijn overal. Wist je dat bijna alle grote bedrijven intensief gebruikmaken van databases om informatie op te slaan? Spotify stelt bijvoorbeeld elke dag nieuwe <em>Daily Mixes</em> samen op basis van jouw favoriete muziek. Google houdt in databases bij waar jij vaak naar zoekt, zodat het zoeken sneller en relevanter wordt. Ook reclames en advertenties worden gepersonaliseerd op basis van gegevens die worden opgeslagen terwijl jij je computer of telefoon gebruikt.</p>


<p>Al deze bedrijven, programma’s en apps maken gebruik van zogeheten databases — en daar ga jij in deze cursus meer over leren. Een veelgebruikte vorm is de <strong>relationele database</strong>: een database die bestaat uit meerdere tabellen die met elkaar in verband staan. Dat betekent dat gegevens uit de ene tabel gekoppeld zijn aan gegevens in een andere tabel. Zo’n database wordt beheerd door een <em>Database Management System</em> (DBMS), een systeem dat zorgt dat de gegevens betrouwbaar en correct blijven en dat je ze makkelijk kunt opvragen wanneer je ze nodig hebt.</p>

<p>Zo’n verzoek noem je een <strong>query</strong>, en daarvoor gebruik je een speciale vraagtaal: <strong>SQL</strong>, wat staat voor <em>Structured Query Language</em>. Dit is de standaardtaal om met relationele databases te werken. In deze module leer je werken met <strong>SQLite</strong> — een eenvoudige, lichtgewicht database — om SQL in de praktijk te gebruiken. Je leert hoe je gegevens kunt opvragen, invoeren en zelfs hoe je zelf tabellen aanmaakt.</p>

<p>De inhoud van dit lesmateriaal is, met toestemming, deels overgenomen uit het lesmateriaal van <a href="https://co-teach.nl/">Co-Teach</a>.</p>




<p>In deze cursus:</p>

<ul>
  <li>leer je dat een database wordt gebruikt om data op een gestructureerde manier (in tabellen) op te slaan;</li>
  <li>leer je dat gebruikers van een database verschillende rechten kunnen hebben, bijvoorbeeld om data in te voeren (CREATE), te lezen (READ), aan te passen (UPDATE) of te verwijderen (DELETE) — de zogeheten CRUD-rechten;</li>
  <li>leer je dat gegevens in een tabel uniek identificeerbaar moeten zijn via een <em>primary key</em>;</li>
  <li>leer je hoe je met SQL een query maakt om gegevens uit de database op te halen en weer te geven;</li>
  <li>leer je hoe je voorwaarden toevoegt aan de gegevens die getoond moeten worden (met <code>WHERE</code>);</li>
  <li>leer je hoe je de volgorde en hoeveelheid van de resultaten kunt aanpassen (met <code>ORDER BY</code> en <code>LIMIT</code>);</li>
  <li>leer je hoe tabellen aan elkaar gekoppeld zijn en hoe je gegevens uit meerdere tabellen combineert (met <code>JOIN</code>).</li>
</ul>

<p>In de verdieping:</p>

<ul>
  <li>leer je hoe je complexere zoekopdrachten uitvoert (met <code>GROUP BY</code> en <code>HAVING</code>);</li>
  <li>leer je hoe je gegevens toevoegt (met <code>INSERT INTO</code>), wijzigt (met <code>UPDATE</code>) of verwijdert (met <code>DELETE FROM</code>);</li>
  <li>leer je hoe je tabellen aanmaakt (<code>CREATE TABLE</code>), aanpast (<code>ALTER TABLE</code>) of verwijdert (<code>DROP TABLE</code>);</li>
  <li>leer je hoe je relaties tussen tabellen afleest uit een ERD-schema (Entity-Relationship Diagram);</li>
  <li>leer je wat een <em>foreign key</em> is en hoe je die aanmaakt.</li>
</ul>

<p>
Je kunt je werk op je computer opslaan via 'Bestand' en vervolgens 'Bewaar notebook als...'. Je kunt je werk in de leeromgeving ook tussentijds opslaan of inleveren. Zie hiervoor 'Opslaan of inleveren' aan het einde van elk onderwerp.
</p>

<!--

### Overzicht Onderwerp 1: Inleiding databases



<p>In dit onderwerp:</p>


<ul>
<li>leer je dat een database gebruikt wordt om data op een gestructureerde manier (in tabellen) op te slaan;
<li>leer je dat gebruikers van een database verschillende rechten hebben, bijvoorbeeld om data in te voeren (CREATE), lezen (READ), aan te passen (UPDATE), of te verwijderen (DELETE) - de zogeheten CRUD rechten;
<li>leer je dat gegevens in een tabel uniek aanwijsbaar moeten zijn, met een primary key;
<li>leer je met SQL een query te maken om gegevens uit de database te halen en te tonen;
<li>leer je met voorwaarden aan de gegevens te stellen die getoond moeten worden;
<li>leer je hoe tabellen aan elkaar gekoppeld zijn en hoe je gegevens uit verschillende tabellen kunt combineren.
</ul>


<p>
Je kunt je werk op je computer opslaan via 'Bestand' en vervolgens 'Bewaar notebook als...'. Je kunt je werk in de leeromgeving ook tussentijds opslaan of inleveren. Zie hiervoor 'Opslaan of inleveren' aan het einde van elk onderwerp.
</p>

 <div class="activity-item time-block">
    <div class="fa fa-clock-o fa-3x"><br></div>
    <br>1 uur
</div>
-->

### Overzicht ONDERWERP 1: Kennismaken met databases
<!-->
<h5><img src="https://raw.githubusercontent.com/rweeda/PythonIA/main/sql/img/H1_overzicht.png" alt="logo onderwerp 1" style="float: right; margin: 4px;" width="150" height="151">
1: Kennismaking met databases<br></h5>-->

<h4><<img src="https://raw.githubusercontent.com/rweeda/PythonIA/main/sql/img/H1_1_pizzabezorger.png" alt="afbeelding van een pizza bezorger"   role="presentation" class="img-responsive atto_image_button_right" style="float: right; margin: 4px;" width="150">Onderwerp 1: Kennismaken met databases</h4>


<p>Data is overal. In dit onderwerp leer je hoe gegevens op een gestructureerde manier in tabellen van een database worden opgeslagen. Zo kun je snel en eenvoudig informatie opvragen wanneer je die nodig hebt. Zo’n verzoek noem je een <strong>query</strong>, en daarvoor gebruik je een speciale vraagtaal: <strong>SQL</strong>, wat staat voor <em>Structured Query Language</em>. Dit is de standaardtaal om met databases te werken.</p>

<p>In dit onderwerp gebruik je <strong>SQLite</strong> — een eenvoudige, lichtgewicht database — om SQL te leren.</p>

<p>We beginnen met het verkennen van databases. Wat zijn het? Waar kom je ze tegen? Hoe zijn ze opgebouwd? En hoe kun je er nuttige informatie uit halen? In deze cursus werk je met de database van Pizzeria Danilo als voorbeeld.</p>

<p>Met SQL kun je gegevens in een database invoeren (Create), opzoeken (Read), aanpassen (Update) en verwijderen (Delete). Afgekort heten deze acties <strong>CRUD</strong>. Om te zorgen dat informatie veilig blijft, hebben gebruikers vaak verschillende rechten. Niet iedereen mag zomaar tabellen verwijderen of alle gegevens inzien. In dit onderwerp leer je nadenken over wie welke acties mag uitvoeren op een database, zoals het aanpassen, toevoegen of verwijderen van gegevens.</p>

<p>In dit onderwerp:</p>
<ul>
  <li>leer je dat een <strong>database</strong> wordt gebruikt om data op een gestructureerde manier (in tabellen) op te slaan;</li>
  <li>leer je zelf een eenvoudige tabel ontwerpen;</li>
  <li>maak je kennis met de drie datatypen in <em>SQLite</em>: <strong>TEXT</strong> (tekst), <strong>INTEGER</strong> (geheel getal) en <strong>REAL</strong> (kommagetal);</li>
  <li>leer je dat elke tabel een <em>primary key</em> heeft: een kolom waarin elke rij een unieke waarde bevat;</li>
  <li>leer je wat een <em>databasemanagementsysteem</em> (DBMS) is;</li>
  <li>leer je dat gebruikers van een database verschillende rechten kunnen hebben, bijvoorbeeld om data in te voeren (CREATE), te lezen (READ), aan te passen (UPDATE) of te verwijderen (DELETE) — de zogeheten <strong>CRUD-rechten</strong>;</li>
  <li>leer je het verschil tussen gegevens, data en informatie.</li>
</ul>


</p>
<p>
 <div class="activity-item time-block">
    <div class="fa fa-clock-o fa-3x"><br></div>
    <br>1 uur
</div>
</p>


### Overzicht ONDERWERP 2: SELECT - FROM


<h4><!--<img src="https://raw.githubusercontent.com/rweeda/PythonIA/main/sql/img/Dbase_CRUD.png" alt="Database aanpassen"   role="presentation" class="img-responsive atto_image_button_right">-->Onderwerp 3: SELECT FROM</h4>




<p>In deze onderwerp werk je met een database van Pizzeria Danilo. De database bestaat uit meerdere tabellen, bijvoorbeeld tabel <i>pizza</i> met informatie over de verschillende pizza's, en <i>klanten</i> met de contactgegevens van de klanten. 
Met <b>SQL</b> (Structured Query Language) kan je gegevens uit de database halen. Je leert verschillende commando's waarmee je de gegevens kan tonen.</p>


<p>Leerdoelen</p>

In dit onderwerp:
<ul> 
<li>leer je dat SQL (Structured Query Language) de standaardtaal om gegevens in een database op te slaan, te bewerken en op te halen;
<li>leer je het begip query voor een zoekvraag;</li>
<li>leer je een <code>SELECT ... FROM ... </code> query te gebruiken om informatie uit een tabel te halen;</li>
<li>leer je een kolom te hernoemen met <code>AS</code>;</li>

<li>maak je kennis met meerdere tabellen uit de database van Danilo's pizzeria;</li>

</ul>


 <div class="activity-item time-block">
    <div class="fa fa-clock-o fa-3x"><br></div>
    <br>1 uur
</div>


### Overzicht 3: WHERE

<h4><!--<img src="https://raw.githubusercontent.com/rweeda/PythonIA/main/sql/img/Dbase_CRUD.png" alt="Database aanpassen"   role="presentation" class="img-responsive atto_image_button_right">-->Onderwerp 3: WHERE</h4>




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

 <div class="activity-item time-block">
    <div class="fa fa-clock-o fa-3x"><br></div>
    <br>2 uur
</div>

### Overzicht Onderwerp 4: 

<h4><!--<img src="https://raw.githubusercontent.com/rweeda/PythonIA/main/sql/img/Dbase_CRUD.png" alt="Database aanpassen"   role="presentation" class="img-responsive atto_image_button_right">-->Onderwerp 4: LIMIT, ORDER BY en groepsfuncties</h4>





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

 <div class="activity-item time-block">
    <div class="fa fa-clock-o fa-3x"><br></div>
    <br>1 uur
</div>


### Overzicht Onderwerp 5: JOIN


<h4><img src="https://raw.githubusercontent.com/rweeda/PythonIA/main/sql/img/tabel_kortingsbonnen_gekoppeld_bestelling.png" alt="Database aanpassen"   role="presentation" class="img-responsive atto_image_button_right" width="200">Onderwerp 5: JOIN</h4>



<p>De kracht van een database is dat die in staat is om gegevens uit verschillende tabellen te combineren. In dit onderwerp leer je hoe tabellen aan elkaar gekoppeld zijn, en hoe je met <code>JOIN</code> gegevens uit meerdere tabellen samenvoegt in één overzicht.</p>

<p>In dit onderwerp:</p>
<ul>

<li>leer je de koppelingen tussen tabellen af te lezen uit een ERD-schema;
  <li>leer je hoe je een ERD-schema kunt gebruiken om te zien hoe tabellen aan elkaar gekoppeld zijn;</li>
  <li>leer je hoe je met <code>tabel.kolom</code> aangeeft uit welke tabel een kolom komt — handig als kolomnamen gelijk zijn;</li>
  <li>leer je hoe je met <code>JOIN ... ON ...</code> gegevens uit meerdere tabellen kunt combineren;</li>
  <li>leer je dat de kolommen waarop je koppelt, in beide tabellen moeten voorkomen en dezelfde soort waarden moeten bevatten;</li>
  <li>leer je dat je meerdere <strong>JOINs</strong> kunt gebruiken om drie of meer tabellen aan elkaar te koppelen.</li>
</ul>



 <div class="activity-item time-block">
    <div class="fa fa-clock-o fa-3x"><br></div>
    <br>1 uur
</div>


# Overzicht Onderwerp VERDIEPING: GROUP BY, HAVING

<h4><img src="https://raw.githubusercontent.com/rweeda/PythonIA/main/sql/img/Dbase_CRUD.png" alt="Database aanpassen"   role="presentation" class="img-responsive atto_image_button_right">Onderwerp 6</h4>


<p>In dit onderwerp... </p>

<p>Leerdoelen</p>

In dit onderwerp:
<ul> 


<li>leer je met `GROUP BY` rijen met gegevens te groeperen zodat je daarna functies kan gebruiken
<li>leer je met `HAVING` ...

<li>OPTIONEEL??? leer je rekenen met: `+`, `-`, `*`, `/`
</ul>


 <div class="activity-item time-block">
    <div class="fa fa-clock-o fa-3x"><br></div>
    <br>XX uur
</div>


###
<!--
<h4><img src="https://raw.githubusercontent.com/rweeda/PythonIA/main/sql/img/Dbase_CRUD.png" alt="Database aanpassen" style="float: right; margin: 4px;" width="150" height="151">
7: Create - Read - Update - Delete uitvoeren</h4>
-->


<h4><img src="https://raw.githubusercontent.com/rweeda/PythonIA/main/sql/img/Dbase_CRUD.png" alt="Database aanpassen"   role="presentation" class="img-responsive atto_image_button_right">Onderwerp 7: Create - Read - Update - Delete uitvoeren</h4>


<p>Naast het opzoeken van informatie, kun je met SQL ook tabellen maken, 
vullen, aanpassen en verwijderen. Deze acties heten CRUD (Create, Read, 
Update, Delete). In deze onderwerp leer je met SQL alle acties uit te voeren: eerste het invoeren, aanpassen en verwijderen van gegevens uit tabellen. Daarna leer je ook hoe je tabellen zelf kunt aanmaken, aanpassen en verwijderen.
</p>

<p>Elke keer dat je de webpagina ververst, wordt de oorspronkelijke database hersteld. Je hoeft dus niet bang te zijn om iets fout te doen — experimenteren mag!</p>

<p>Wil je je code bewaren? Sla deze dan op via 'Bestand' en vervolgens 'Bewaar notebook als...'. Je kunt je werk ook tussentijds opslaan of inleveren.</p>





<p>In dit onderwerp:</p>

<ul>
<li>leer je gegevens invoeren in een tabel met <code>INSERT INTO ... VALUES</code>, waaronder ook NULL voor een waarde dat automatisch genummerd 
wordt;
<li>leer je gegevens verwijderen uit een tabel met <code>DELETE FROM ... WHERE ... </code>;
<li>leer je gegevens aanpassen in een tabel met <code>UPDATE ... SET ... WHERE ... </code>;

<li>leer je een nieuw tabel aanmaken met <code>CREATE TABLE</code>, waaronder ook hoe je een kolom als primary key 
aanmaakt, en deze automatisch doornummert;
<li>leer je een tabel verwijderen met <code>DROP TABLE</code>;

<li>leer je de structuur van een tabel aan te passsen met <code>ALTER TABLE</code>:
<ul>
<li>kolom toevoegen met <code>ADD</code>;
<li>kolom hernoemen met <code>RENAME COLUMN</code>;
<li>tabel hernoemen met <code>RENAME TO</code>;
</ul>
</li>
<li>leer je de relaties tussen tabellen af te lezen uit een ERD-schema;
<li>leer je waarom je tabellen aan elkaar koppelt met een <b>foreign key</b>;
<li>leer je hoe je in SQL een foreign key toevoegt aan een tabel.

</ul>

 <div class="activity-item time-block">
    <div class="fa fa-clock-o fa-3x"><br></div>
    <br>1 uur
</div>
