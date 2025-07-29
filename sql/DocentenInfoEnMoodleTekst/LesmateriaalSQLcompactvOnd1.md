
# 1.1: Inleiding databases

<p>Het is vrijdagavond. Je weet nog niet wat je wilt eten maar
hebt gehoord dat een nieuwe pizzeria – Pizzeria Danilo, net geopend om de
hoek – hele lekkere pizza’s maakt. Als je een pizza bestelt, moet je
natuurlijk wel eerst weten welke je wilt hebben. Als je de website van je
plaatselijke pizzeria erbij hebt gepakt word je overweldigd door de
hoeveelheid opties. Al deze opties staan in een <strong>database</strong>.</p>

<img
src="https://raw.githubusercontent.com/rweeda/PythonIA/main/sql/img/H1_1_pizzabezorger.png"
alt="afbeelding van een bezorger" width="200" align="right">


<p>Maar wat is een database? En hoe ziet zoiets eruit? 

Danilo moet veel
<strong>gegevens</strong> bijhouden. Zoals bijvoorbeeld, de naam van de pizza's, de
prijs en de ingrediënten. Maar ook de namen en adressen van klanten en
gegevens over bestellingen en bezorgers. Die gegevens worden bewaard in tabellen. En tabellen bestaan weer uit kolommen met rijen van gegevens die opgeslagen worden. Die gegevens noemen we
<strong>data</strong>. Door informatie op een vaste,
georganiseerde manier is op te slaan kunnen computers die makkelijk lezen, begrijpen en verwerken. Dat noemen we <strong>gestructureerde data</strong>. Een <strong>database</strong> is een verzameling van tabellen waaruit je eenvoudig (overzichten met) gegevens kunt opvragen.</p>


### Verwerkingsopdracht 1.1.1 Kolommen kiezen bij het ontwerp van een tabel

Stel dat jij bij Danilo's Pizzeria wilt bestellen. Om de contactgegevens op
te slaan in een database moet je het webformulier hieronder invullen.





<p><img
src="https://raw.githubusercontent.com/rweeda/PythonIA/main/sql/img/H1_webform.png"
alt="webformulier" width="600"></p>


We maken een tabel waarin we de contactgegevens opslaan. Zo kunnen we
makkelijk de gegevens van klanten terugvinden als ze een bestelling plaatsen.
<ol style="list-style-type: lower-alpha">
<li>Bekijk het webformulier hiernaast goed. Welke gegevens worden verzameld? Noem alle velden.</li>

<li>Wat betekent het sterretje, bijvoorbeeld achter 'Voornaam'?</li>

<li>Wat gebeurt er als er twee verschillende mensen zijn met dezelfde
voornaam en achternaam waarvan je het adres wilt opzoeken? Wat voor oplossing
hebben we op school hiervoor? Tip: wat voor uniek getal heeft elk leerling op school?</li>

<li>Bedenk een oplossing voor Danilo's pizzeria voor het eenduidig opslaan
van klantgegevens. Dus, bedenk iets unieks voor elke klant.</li>

<li>We maken een tabel om de gegevens in op te slaan. Kolom 'B' hebben we voor je alvast ingevuld met <i>voornaam</i>.
<ul>
<li>De eerste kolom, 'A' gebruik je voor je unieke waarde. Geef die een naam. 
<li>Geef ook de andere kolommen
namen (bij 'C' t/m 'H'). 
<li>Geef de tabel ook een naam.</li>
</ul>
</ol>

TABEL:
 <table border=1>
    <tr>
      <th>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; A &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</th>
      <th> voornaam </th>
      <th>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; C &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</th>
      <th>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; D &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</th>
      <th>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; E &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</th>
      <th>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; F &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</th>
      <th>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; G &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</th>
      <th>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; H &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</th>
    </tr>
    <tr><td>&nbsp;</td>
      <td>&nbsp;</td>
      <td>&nbsp;</td>
      <td>&nbsp;</td>
      <td>&nbsp;</td>
      <td>&nbsp;</td>
      <td>&nbsp;</td>
      <td>&nbsp;</td>
    </tr>
</table>



<p>Bekijk <a
href="https://rweeda.github.io/PythonIA/docs/IA_sql_oplossingen.html#opgave111"
target="_blank">hier</a> de voorbeelduitwerking.</p>


<!--
ANTWOORDEN: <ol style="list-style-type: lower-alpha">

<li>Deze gegevens worden verzameld: voornaam, tussenvoegsel, achternaam,
adres, postcode, plaats en telefoon.</li>

<li>Dat is een veld dat verplicht ingevuld moet worden.</li>

<li>Als twee klanten dezelfde naam hebben kun je ze niet uit elkaar halen, je
kunt dan niet hun juiste adres opzoeken. Als oplossing gebruiken we een
unieke waarde waarvan er maar één is, zoals een leerlingnummer op school, of
een BSN.</li>

<li>Voor Danilo's pizzeria zou een uniek nummer een klantnummer kunnen zijn.</li>

<li>Zie tabel hieronder./li>

</ol>


TABEL: klanten <table>
  <thead>
    <tr>
      <th>klantnummer</th>
      <th>voornaam</th>
      <th>tussenvoegsel</th>
      <th>achternaam</th>
      <th>adres</th>
      <th>postcode</th>
      <th>plaats</th>
      <th>telefoon</th>
    </tr>
  </thead>
</table>

-->

## 1.2: Verschillende soorten data


In een database sla je data op een gestructureerde
manier op. Daarvoor moet je voor iedere kolom aangeven wat voor soort gegevens
je wilt opslaan, oftewel het <strong>datatype</strong>.

In SQLite, de database waar wij mee werken, zijn er drie datatypes: 

<ul>
<li><strong>TEXT</strong>: een stuk tekst. Bijvoorbeeld: 'Jaap'</li>

<li><strong>INTEGER</strong>: een
geheel getal. Bijvoorbeeld: 4 </li>

<li><strong>REAL</strong>: een kommagetal. Bijvoorbeeld:
2.50</li>
 </ul>


Omdat er in SQLite maar drie datatypes zijn, worden sommige gegevens als TEXT
opgeslagen. Bijvoorbeeld, een datum sla je in de vorm jjjj-mm-dd (j: jaar, m:
maand, d:dag) op als een tekst, bijvoorbeeld: "2025-04-20". Een
telefoonnummer zul je ook als een tekst opslaan, omdat anders de voorloop nul
wegvalt, bijvoorbeeld: "0688567389".


### Verwerkingsopdracht 1.2.1 Datatypes kiezen bij het ontwerp van een tabel

Ga verder met de tabel uit
de vorige opdracht. 
<br>Geef bij elke kolom  aan welk van de
volgende type gegevens het bevat: 
<ul> 
  <li>TEXT: een tekst </li>
  <li>INTEGER: een geheel getal</li> 
  <li>REAL: een kommagetal</li> 
</ul>

TABEL: klanten 
<table border=1>
    <tr>
      <th>klantnummer</th>
      <th>voornaam</th>
      <th>tussenvoegsel</th>
      <th>achternaam</th>
      <th>adres</th>
      <th>postcode</th>
      <th>plaats</th>
      <th>telefoon</th>
    </tr>
    <tr><td>&nbsp;</td>
      <td>&nbsp;</td>
      <td>&nbsp;</td>
      <td>&nbsp;</td>
      <td>&nbsp;</td>
      <td>&nbsp;</td>
      <td>&nbsp;</td>
      <td>&nbsp;</td>
    </tr>
</table>









<p>Bekijk <a
href="https://rweeda.github.io/PythonIA/docs/IA_sql_oplossingen.html#opgave121"
target="_blank">hier</a> de voorbeelduitwerking.</p>


<!-- ANTWOORD:

TABEL: klanten <table>
  <thead>
    <tr>
      <th>klantnummer</th>
      <th>voornaam</th>
      <th>tussenvoegsel</th>
      <th>achternaam</th>
      <th>adres</th>
      <th>postcode</th>
      <th>plaats</th>
      <th>telefoon</th>
    </tr>
        <tr>
      <td>INTEGER</td>
      <td>TEXT</td>
      <td>TEXT</td>
      <td>TEXT</td>
      <td>TEXT</td>
      <td>TEXT</td>
      <td>TEXT</td>
      <td>TEXT</td>
    </tr>
  </thead>
</table>





-->



## 1.3: Primary key 


Elke tabel heeft een kolom hebben waarmee je gegevens
kan aanwijzen: een <strong>primary key</strong>. Deze kolom moet <strong>unieke</strong> gegevens
hebben, een kolom waar nooit twee keer hetzelfde waarde voor mag komen. 

Een
voorbeeld is <i>leerlingnummer</i>. Er kunnen geen twee leerlingen dezelfde
leerlingnummer hebben. Terwijl er misschien wel twee leerlingen met dezelfde
naam zijn, bijvoorbeeld Tom Janssen. Met een leerlingnummer weet je zeker
over wie je het hebt. Een ander voorbeeld is een klantnaam bij Pizzeria Danilo of gebruikersnaam in een spel,
daar mag er maar één van zijn.

(<i>Toelichting: een primary key kan uit meerdere kolommen samen bestaan,
maar dat behandelen we in deze cursus niet.</i>)

### Verwerkingsopdracht 1.3.1 Wat is een primary key?

Welke van de volgende uitspraken over primary keys is correct?

<ol style="list-style-type: lower-alpha">
<li>Een primary key mag leeg zijn
<li>Een primary key mag dubbel voorkomen
<li>Een primary key identificeert elke rij op unieke wijze
<li>Een primary key is altijd tekst
</ol>

<p>Bekijk <a
href="https://rweeda.github.io/PythonIA/docs/IA_sql_oplossingen.html#opgave131"
target="_blank">hier</a> de voorbeelduitwerking.</p>

<!--
ANTWOORD: Antwoord c is juist. Een primary key identificeert elke rij op unieke wijze
-->

### Verwerkingsopdracht 1.3.2 Welke kolom is een primary key?

Bekijk weer de tabel <code>klanten</code>. Welke kolom is hier de primary key?

TABEL: klanten 
<table border=1>
    <tr>
      <th>klantnummer</th>
      <th>voornaam</th>
      <th>tussenvoegsel</th>
      <th>achternaam</th>
      <th>adres</th>
      <th>postcode</th>
      <th>plaats</th>
      <th>telefoon</th>
    </tr>
    <tr><td>&nbsp;</td>
      <td>&nbsp;</td>
      <td>&nbsp;</td>
      <td>&nbsp;</td>
      <td>&nbsp;</td>
      <td>&nbsp;</td>
      <td>&nbsp;</td>
      <td>&nbsp;</td>
    </tr>
</table>


<p>Bekijk <a
href="https://rweeda.github.io/PythonIA/docs/IA_sql_oplossingen.html#opgave132"
target="_blank">hier</a> de voorbeelduitwerking.</p>

<!--
ANTWOORD: Kolom <em>klantnummer</em> is de primary key. Elk klant heeft een eigen unieke klantnummer. 
-->


## 1.4: Eisen stellen aan data 

Naast dat data van een bepaald type is, kun
je nog anderen eisen stellen aan waarden in een bepaald kolom, bijvoorbeeld:
<ul>
  <li>PRIMARY KEY: een unieke waarde;</li>
  <li>NOT NULL: mag niet leeg zijn.</li>

</ul>

### Verwerkingsopdracht 1.4 Eisen aan data stellen bij het ontwerpen van een tabel 


Ga verder met de tabel
uit de vorige opdracht. <br>

TABEL: klanten 
<table border=1>
  <thead>
    <tr>
      <th>klantnummer</th>
      <th>voornaam</th>
      <th>tussenvoegsel</th>
      <th>achternaam</th>
      <th>adres</th>
      <th>postcode</th>
      <th>plaats</th>
      <th>telefoon</th>
    </tr>
    <tr>
      <td>INTEGER</td>
      <td>TEXT</td>
      <td>TEXT</td>
      <td>TEXT</td>
      <td>TEXT</td>
      <td>TEXT</td>
      <td>TEXT</td>
      <td>TEXT</td>
    </tr>
  </thead>
</table>





Geef bij elke kolom aan of er speciale eisen aan gesteld zijn:
  <ul>
  <li>PRIMARY KEY: een unieke waarde (in het Nederlands <em>primaire sleutel</em>)</li>
  <li>NOT NULL: mag niet leeg zijn</li>
  </ul>


<p>Bekijk <a
href="https://rweeda.github.io/PythonIA/docs/IA_sql_oplossingen.html#opgave141"
target="_blank">hier</a> de voorbeelduitwerking.</p>

<!--
ANTWOORD: TABEL: klanten <table>
  <thead>
    <tr>
      <th>klantnummer<br>INTEGER PRIMARY KEY NOT NULL</th>
      <th>voornaam<br>TEXT NOT NULL</th>
      <th>tussenvoegsel<br>TEXT</th>
      <th>achternaam<br>TEXT NOT NULL</th>
      <th>adres<br>TEXT NOT NULL</th>
      <th>postcode<br>TEXT NOT NULL</th>
      <th>plaats<br>TEXT NOT NULL</th>
      <th>telefoon<br>TEXT NOT NULL</th>
    </tr>
  </thead>
</table>


-->



## 1.5: Nut van databases


[![Bekijk op Youtube](https://www.youtube.com/watch?v=t8jgX1f8kc4/hqdefault.jpg)](https://www.youtube.com/watch?v=t8jgX1f8kc4)


<iframe width="560" height="315"
  src="https://www.youtube.com/embed/v=t8jgX1f8kc4"
  frameborder="0"
  allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture"
  allowfullscreen>
</iframe>

<p>Je kunt je voorstellen dat Danilo graag een goed overzicht wil houden van
alle verzamelde gegevens. Daarom gebruikt hij een <strong>database</strong>. Een
database is een gestructureerde manier om gegevens op te slaan.</p>

<p>Danilo's database bestaat uit meerdere tabellen. Er is bijvoorbeeld een <em>tabel</em> klant met klantgegevens, een tabel <em>pizza</em> met alle pizza's die besteld kunnen worden, en een tabel <em>bestelling</em> waarin bijgehouden wordt welke pizza's er besteld zijn.
Hieronder zie je alle tabellen die in Danilo's database staan.
<p> <a
href="https://raw.githubusercontent.com/rweeda/PythonIA/main/sql/img/DaniloIA_ERD.png"
target="_blank">
  <img src="https://raw.githubusercontent.com/rweeda/PythonIA/main/sql/img/DaniloIA_ERD.png" alt="Klik om in een nieuw venster te openen" width="1000"/>
</a></p>


<p>Met een zoekvraag, of <strong>query</strong> vraag je een deel van de gegevens uit een database op. Je kunt gegevens ook combineren tot nuttige informatie, bijvoorbeeld op welke dagen de meeste pizza's besteld worden.
</p>





<p>Data is overal, niet alleen in de pizzeria van Danilo. Zodra jij je op het
internet begeeft laat je een spoor van gegevens achter. Terwijl jij, bijvoorbeeld, gebruik maakt van YouTube worden
verschillende gegevens verzameld die hergebruikt kunnen worden om een
gepersonaliseerde ervaring aan te kunnen bieden. Denk hierbij aan hoe lang je
naar een video kijkt, naar welke video’s je zoekt of op welke video’s die
aangeraden worden jij ook echt doorklikt. Ook moet er veel informatie over de
video’s zelf opgeslagen worden zoals de titel, de thema’s, de lengte, enz. Je
kunt je voorstellen dat via het internet zo een enorme hoeveelheid data
verzameld worden.</p>


<p>Jouw school maakt ook gebruik van databases. Gebruikt je school Magister
of Somtoday? Deze programma's slaan informatie over jou als leerling op in
een database. Hiermee kan je docent huiswerk opgeven en toetscijfers inzien
en invoeren, kan de schoolleiding zien hoe het met verschillende klassen gaat
en kan jij zien hoe je er voor staat met al je vakken of opdrachten
inleveren.</p>




### Verwerkingsopdracht 1.5.1  Waar vind je databases?

<p>Waarschijnlijk heb je al eerder gebruik gemaakt van een database,
misschien zonder dat je dat wist. Laten we eens op onderzoek uit gaan en
kijken of we nog meer databases kunnen vinden.</p>

<ol style="list-style-type: lower-alpha"> <li>Bedenk nog een voorbeeld van
een website die, naar jouw verwachting, gebruik maakt van een database. </li>
<li>Wat voor data worden opgeslagen in deze database?</li> </ol>

<p>Bekijk <a
href="https://rweeda.github.io/PythonIA/docs/IA_sql_oplossingen.html#opgave151"
target="_blank">hier</a> de voorbeelduitwerking.</p>



<!-- Voorbeelden van antwoorden: <ol style="list-style-type: lower-alpha">
<li>
  <li>Webwinkel</li>
  <li>Social media platform</li>
  <li>Magister of SOMtoday</li>
</li> <li>
  <li>Bij webwinkel: productenlijst</li>
  <li>Bij social media platform: posts</li>
  <li>Bij school database: gegevens over leerlingen zoals adres, cijfers en rooster</li>
</li> </ul> -->



## 1.6: Database management system (DBMS) 


<p>Een database kan al snel heel groot
worden. Er wordt niet alleen data in opgeslagen, maar ook data gewijzigd of
verwijderd. Een andere belangrijke functie is het opvragen en combineren van
gegevens. Bovendien heeft niet iedereen dezelfde toegang: als leerling kun je
alleen je eigen gegevens zien, terwijl een docent bijvoorbeeld de cijfers van
alle leerlingen kan bekijken, aanpassen of toevoegen.</p> 


<p>Al deze
bedrijven, programma’s en apps maken gebruik van zogeheten databases. Een
veelgebruikte soort is de relationele database: een database die bestaat uit
meerdere tabellen die met elkaar in verband staan. Dat betekent dat gegevens
uit de ene tabel gekoppeld zijn aan gegevens in een andere tabel. Deze
databases worden beheerd door een <strong>database management system (DBMS)</strong>. </p>

  <img src="https://raw.githubusercontent.com/rweeda/PythonIA/main/sql/img/H1_1dbase.png" alt="DBMS" width="1000"/>


<p>Zo’n systeem zorgt ervoor dat de data betrouwbaar en correct blijft, en
dat wij op een eenvoudige en veilige manier informatie kunnen opvragen wanneer we die
nodig hebben.</p>




## 1.7: Gegevens beheren: CRUD

Het beheren van gegevens kan je opdelen in vier categorieen: Create, Read, Update, Delete, afgekort tot <strong>CRUD</strong>:

<ul> 
<li><b>Create</b>: Nieuwe tabellen aanmaken (met CREATE TABLE), of gegevens toevoegen (met INSERT INTO);
<li><b>Read</b>: Opgeslagen gegevens bekijken (met SELECT);
<li><b>Update</b>: Opgeslagen gegevens bewerken (met UPDATE);
<li><b>Delete</b>: Opgeslagen gegevens verwijderen (met DELETE). 
</ul> 


<p>Een DBMS zorgt ervoor dat een beheerder al deze acties kan doen. Als er meerdere gebruikers zijn, bepaal je per gebruiker wat die mag. Een klant mag bijvoorbeeld alleen zijn eigen 
wachtwoord bewerken (Update) en niet dat van andere klanten.</p> 

De app van Danilo's Pizzeria heeft verschillende gebruikers, bijvoorbeeld klanten (die pizza's bestellen), bezorgers (brengen pizza's rond), en beheerders (die de hele database beheren).

Voorbeelden van CRUD acties op Danilo's Pizzeria zijn:
<ul>
<li>Create: Als een nieuwe bezorger in dienst komt, dan worden zijn gegevens door een beheerder toegevoegd. 
<li>Read: Om te zien op welk adres een pizza bezorgd moet worden, kan de bezorger deze opvragen.
<li>Update: De bezorger mag zijn eigen <i>telefoon</i>nummer aanpassen. 
<li>Delete: Als een bezorger ontslag neemt, worden zijn gegevens door een beheerder verwijderd.
</ul>
<!--
<ul>
<li>Create: Als een nieuwe bezorger in dienst komt, dan worden zijn gegevens toegevoegd aan tabel <code>bezorger</code>. 
<li>Read: Om te zien op welk adres een pizza bezorgd moet worden, kan de bezorger deze uit tabel <code>klant</code> opvragen.
<li>Update: De bezorger mag zijn eigen <i>telefoon</i>nummer aanpassen. 
<li>Delete: Als een bezorger ontslag neemt, worden zijn gegevens uit tabel <code>bezorger</code> verwijderd.
</ul>
-->

<!--
Ter herinnering, hieronder zie je alle tabellen die in Danilo's database staan.
<p> <a
href="https://raw.githubusercontent.com/rweeda/PythonIA/main/sql/img/DaniloIA_ERD.png"
target="_blank">
  <img src="https://raw.githubusercontent.com/rweeda/PythonIA/main/sql/img/DaniloIA_ERD.png" alt="Klik om in een nieuw venster te openen" width="1000"/>
</a></p>
-->

### Verwerkingsopdracht 1.7.1 CRUD rechten van klanten bepalen

We bekijken de CRUD-rechten die een klant heeft op tabel <code>klant</code>.

[TODO IMG TABEL KLANT *]
<ol style="list-style-type: lower-alpha">
<li>Bepaal welke van de volgende rechten de klant heeft op de eigen gegevens in de tabel <code>klant</code>?
<li>Waarom is het logisch dat een klant sommige dingen wel en andere dingen niet mag? 
</ol>


<p>Bekijk <a href="https://rweeda.github.io/PythonIA/docs/IA_sql_oplossingen.html#opgave171" target="_blank">hier</a> de voorbeelduitwerking.</p>
<!--
ANTWOORDEN:
<ol style="list-style-type: lower-alpha">
<li>Acties:
	<ul>
<li>Create: Ja, bij het aanmaken van een nieuw account.
<li>Read: Ja, mag eigen gegevens bekijken.
<li>Update: Ja, mag eigen gegevens wijzigen (zoals wachtwoord of adres).
<li>Delete: Meestal niet zelf; alleen door een beheerder.
</ul>
<li>Klanten mogen alleen hun eigen gegevens zien en invoeren, maar niet wijzigen of verwijderen. Dit voorkomt fouten en misbruik, en beschermt de privacy van andere klanten.
</ol>
-->

### Verwerkingsopdracht 1.7.2 CRUD Rechten van de bezorger bepalen
Een bezorger krijgt een overzicht van de pizza’s die hij moet afleveren. Na bezorging vinkt hij in het systeem aan dat de bestelling is bezorgd, daarmee wordt de bezorgtijd vastgelegd.
<ol style="list-style-type: lower-alpha">
<li>Welke CRUD-rechten heeft een bezorger nodig als hij een bestelling gaat bezorgen?
<li>Waarom is het belangrijk dat een bezorger geen toegang heeft tot bepaalde gegevens?
</ol>

<p>Bekijk <a href="https://rweeda.github.io/PythonIA/docs/IA_sql_oplossingen.html#opgave172" target="_blank">hier</a> de voorbeelduitwerking.</p>
<!--
ANTWOORDEN:
<ol style="list-style-type: lower-alpha">
<li>Acties:
<ul>
<li>Read: Ja, om te kunnen zien welke bestellingen hij moet bezorge naar welk adres.
<li>Update: Ja, om de bezorgtijd vast te leggen.
<li>Create/Delete: Nee, een bezorger mag geen bestellingen invoeren of verwijderen.
</ul>
<li>Toelichting: De bezorger heeft beperkte toegang. Hij mag alleen de bezorg_tijd aangeven, en dus aanpassen. Andere gegevens zijn niet zijn verantwoordelijkheid en moeten dus beschermd blijven. Hij mag bijvoorbeeld wel het adres van de klant inzien, maar niet de wachtwoord van de klant.
</ol>
-->


### Verwerkingsopdracht 1.7.3 Fouten voorkomen
Stel dat je per ongeluk een Delete-recht geeft aan een klant op de tabel waarin alle geplaatste bestellingen staan.

<ol style="list-style-type: lower-alpha">
<li>Wat zou er kunnen gebeuren als een klant zijn eigen of andermans bestellingen kon verwijderen?
<li>Hoe kun je dit voorkomen?
</ol>

<p>Bekijk <a href="https://rweeda.github.io/PythonIA/docs/IA_sql_oplossingen.html#opgave173" target="_blank">hier</a> de voorbeelduitwerking.</p>
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


### Verwerkingsopdracht 1.7.4 CRUD Rechten van de databasebeheerder bepalen
De beheerder moet het hele systeem kunnen beheren, ook als er iets fout is gegaan.
<ol style="list-style-type: lower-alpha">
<li>Welke CRUD-rechten heeft een beheerder?
<li>Wat zijn de voor- en nadelen van het geven van volledige CRUD-rechten aan een beheerder?
</ol>

<p>Bekijk <a href="https://rweeda.github.io/PythonIA/docs/IA_sql_oplossingen.html#opgave174" target="_blank">hier</a> de voorbeelduitwerking.</p>
<!--
ANTWOORDEN
<ol style="list-style-type: lower-alpha">
<li>Acties: Create, Read, Update, Delete: een beheerder heeft alle rechten.
<li>Voor- en nadelen:
<ul>
<li>Voordelen: De beheerder kan fouten corrigeren, testgegevens verwijderen, of het systeem onderhouden.
<li>Nadelen: Volledige rechten zijn gevoelig voor fouten of misbruik. Eén verkeerde DELETE-query kan veel gegevens verwijderen.
</ul>
</ol>
-->

## 1.8: Gegevens, data en informatie

In de praktijk worden de woorden data en gegevens veel door elkaar gebruikt.

<ul>
 <li><strong>Gegevens</strong> zijn feiten die je kunt verzamelen, zoals een naam of temperatuur.</li> 
 <li><strong>Data</strong> zijn opgeslagen gegevens (in tabellen of bestanden).</li> 
 <li><strong>Informatie</strong> is geïnterpreteerde data die betekenis heeft, bijvoorbeeld een weerbericht.</li>
</ul>

### Verwerkingsopdracht 1.8.1 Gegevens, data en informatie


<p>Woorden als <i>gegevens</i>, <i>data</i>, en <i>informatie</i> worden vaak
door elkaar gehaald. Is dat terecht of niet? Betekenen ze allemaal hetzelfde
of is er toch een verschil? Dat ga jij in deze opdracht uitzoeken.</p>


<ol style="list-style-type: lower-alpha">


<li>Zoek op internet naar de definitie van gegevens. Wat zijn gegevens?</li>
<li>Zoek op internet naar de definitie van data. Wat is data?</li> <li>Zoek
op internet naar de definitie van informatie. Wat is informatie?</li>
<li>Bepaal welk van de volgende woorden <i>gegevens</i>, <i>data</i> en
<i>informatie</i> bij ieder van de onderstaand thuishoren:
  <ul>
  <li>Het weerbericht
  <li>Windsnelheid gemeten met een windmolentje
  <li>Temperatuur gedurende de dag op elk uur gemeten.
  </ul>


</ol>


<p>Bekijk <a
href="https://rweeda.github.io/PythonIA/docs/IA_sql_oplossingen.html#opgave162"
target="_blank">hier</a> de voorbeelduitwerking.</p>


<!-- Mogelijke antwoorden: <ol style="list-style-type: lower-alpha">
<li>chatGPT: "Gegevens zijn feiten, cijfers en andere waarnemingen die
verzameld en opgeslagen kunnen worden om te worden geanalyseerd,
geïnterpreteerd of gebruikt voor besluitvorming." Met andere woorden,
allerlei eigenschappen van mensen en objecten die je kunt verzamelen en
opslaan om later te gebruiken en/of te combineren tot nuttige
informatie.</li>

<li>chatGPT: "Data bestaat uit feiten, cijfers en waarnemingen die worden
verzameld uit verschillende bronnen en die nog moeten worden geanalyseerd of
geïnterpreteerd om betekenis of waarde te krijgen." Met andere woorden,
opgeslagen eigenschappen van mensen en objecten die je kunt verzamelen en
opslaan om later te gebruiken en/of te combineren tot nuttige
informatie.</li>

<li>chatGPT: "Informatie is de kennis, inzichten, of betekenis die wordt
verkregen door het verzamelen, verwerken, analyseren en interpreteren van
ruwe feiten en cijfers. Het is georganiseerd en gestructureerd zodanig dat
het begrijpelijk en nuttig is voor de ontvanger, en het wordt gebruikt om
beslissingen te nemen, problemen op te lossen of communicatie te verbeteren"
Met andere woorden, informatie bestaat uit het (slim) combineren van data
(gegevens) om zo tot nuttige kennis te komen. Bijvoorbeeld het opstellen van
een profiel van iemand om een persoonlijke advertentie, advies of muziekkeuze
te kunnen geven.</li>

<li>

  <ul>
    <li>Het weerbericht bestaat uit een combinatie van gegevens en data  en dus is het informatie.
    <li>Windsnelheid die wordt gemeten en afgelezen is een gegeven is dat nog niet is opgeslagen. Dus zijn
    het gegevens.
    <li>"Temperatuur gedurende de dag" zijn metingen die elk uur zijn gedaan en zijn opgeslagen. Dus is
    het data.
  </ul>
In de praktijk worden de woorden data en gegevens veel door elkaar gebruikt.
</ol>

-->


# 1.9: Samenvatting 1. Databases
In deze opdracht heb je veel geleerd over gestructureerde data. We vatten dat nu samen.

<ul>
 <li><strong>Database</strong>: een georganiseerde verzameling gegevens, opgeslagen in tabellen met rijen en kolommen. In een pizzeria zoals Danilo’s worden gegevens opgeslagen over o.a. pizza’s, klanten, bestellingen en bezorgers.</li> 
 <li>Een tabel bestaat uit kolommen, elk met een naam zoals <i>voornaam</i>, <i>adres</i>, <i>telefoonnummer</i>, enz., en een datatype (bijv. tekst of getal).</li> <li><strong>Datatypes</strong> in SQLite: 
 <ul> 
 <li><strong>INTEGER</strong>: gehele getallen (bijv. een klantnummer: 4054)</li> <li><strong>TEXT</strong>: tekstuele gegevens (bijv. een naam: 'Jaap')</li> <li><strong>REAL</strong>: kommagetallen (bijv. een prijs: 2,50)</li> 
 </ul> 
 </li> 
 <li><strong>Primary key</strong>: elke tabel heeft een kolom waarin elke waarde uniek is. Voorbeelden: klantnummer, leerlingnummer.</li> 
 <li>Een database wordt beheerd door een <strong>Database Management System (DBMS)</strong>.</li> 
 <li>Om de gegevens in je database te beschermen, wordt er per gebruiker bepaald welke <strong>CRUD</strong>-rechten (Create, Read, Update, Delete) diegene op welke data heeft.</li> 
 <li><strong>Gegevens</strong> zijn feiten die je kunt verzamelen, zoals een naam of temperatuur.</li> 
 <li><strong>Data</strong> zijn opgeslagen gegevens (in tabellen of bestanden).</li> <li><strong>Informatie</strong> is geïnterpreteerde data die betekenis heeft, bijvoorbeeld een weerbericht.</li>
  </ul>
