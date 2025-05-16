
# 1.1: Inleiding databases

<p>Het is vrijdagavond. Je weet nog niet wat je wilt eten maar
hebt gehoord dat een nieuwe pizzeria – Pizzeria Danilo, net geopend om de
hoek – hele lekkere pizza’s maakt. Als je een pizza bestelt, moet je
natuurlijk wel eerst weten welke je wilt hebben. Als je de website van je
plaatselijke pizzeria erbij hebt gepakt word je overweldigd door de
hoeveelheid opties. Al deze opties staan in een <b>database</b>.</p>

<img
src="https://raw.githubusercontent.com/rweeda/PythonIA/main/sql/img/H1_1_pizzabezorger.png"
alt="afbeelding van een bezorger" width="300">


<p>Maar wat is een database? En hoe ziet zoiets eruit? Danilo moet veel
<b>gegevens</b> bijhouden. Zoals bijvoorbeeld, de naam van de pizza's, de
prijs en de ingrediënten. Maar ook de namen en adressen van klanten en
gegevens over bestellingen en bezorgers. </p>


<p>Die gegevens worden bewaard in tabellen. En tabellen bestaan weer uit
rijen en kolommen met gegevens die opgeslagen worden. Die gegevens noemen we
<b>data</b>. Gestructureerde data is informatie die op een vaste,
georganiseerde manier is opgeslagen, zodat computers die makkelijk kunnen
lezen, begrijpen en verwerken.</p>


### Verwerkingsopdracht 1.1.1 Kolommen kiezen bij het ontwerp van een tabel

Stel dat jij bij Danilo's Pizzeria wilt bestellen. Om de contactgegevens op
te slaan in een database moet je het webformulier hieronder invullen.

Bekijk het webformulier goed.



<p><img
src="https://raw.githubusercontent.com/rweeda/PythonIA/main/sql/img/H1_webform.png"
alt="webformulier" width="600"></p>


We maken een tabel waarin we de contactgegevens opslaan. Zo kunnen we
makkelijk de gegevens van klanten terugvinden als ze een bestelling plaatsen.
<ol style="list-style-type: lower-alpha">

<li>Welke gegevens worden verzameld? Noem alle velden.

<li>Wat betekent het sterretje, bijvoorbeeld achter 'Voornaam'?

<li>Wat gebeurt er als er twee verschillende mensen zijn met dezelfde
voornaam en achternaam waarvan je het adres wilt opzoeken? Wat voor oplossing
hebben we op school hiervoor?

<li>Bedenk een oplossing voor Danilo's pizzeria voor het eenduidig opslaan
van klantgegevens.

<li>Hieronder staat een tabel om de gegevens op te slaan. Geef de kolommen
namen (bij 'A' t/m 'H'). Geef de tabel ook een naam.

</ol>


 |   A   |   B   |   C   |   D   |   E   |   F   |   G   |   H   |
|-------|-------|-------|-------|-------|-------|-------|-------| 
|       |        |       |       |       |       |       |       |


<p>Bekijk <a
href="https://rweeda.github.io/PythonIA/docs/IA_sql_oplossingen.html#opgave111"
target="_blank">hier</a> de voorbeelduitwerking.</p>


<!--
ANTWOORDEN: <ol style="list-style-type: lower-alpha">

<li>Deze gegevens worden verzameld: voornaam, tussenvoegsel, achternaam,
adres, postcode, plaats en telefoon.

<li>Dat is een veld dat verplicht ingevuld moet worden.</li>

<li>Als twee klanten dezelfde naam hebben kun je ze niet uit elkaar halen, je
kunt dan niet hun juiste adres opzoeken. Als oplossing gebruiken we een
unieke waarde waarvan er maar één is, zoals een leerlingnummer op school, of
een BSN.

<li>Voor Danilo's pizzeria zou een uniek nummer een klantnummer kunnen zijn.

<li>Zie hieronder <li>tabelnaam: klanten

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
      <th>telefoon/th>
    </tr>
  </thead>
</table>

-->

## 1.2: Verschillende soorten data


In een database sla je data op een gestructureerde
manier op. Daarvoor moet je voor iedere kolom aangeven wat voor soort gegevens
je wilt opslaan, oftewel het <b>datatype</b>.

In SQLite, de database waar wij mee werken, zijn er drie datatypen: 

<ul>
<li><b>TEXT</b>: een stuk tekst. Bijvoorbeeld: 'Jaap' <li><b>INTEGER</b>: een
geheel getal. Bijvoorbeeld: 4 <li><b>REAL</b>: een kommagetal. Bijvoorbeeld:
2.50 </ul>

### Opdracht 1.2.1 Datatypes kiezen bij het ontwerp van een tabel

Ga verder met de tabel uit
de vorige opdracht. 

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
      <th>telefoon/th>
    </tr>
  </thead>
</table>


<br>Geef bij elke kolom  aan welk van de
volgende type gegevens het bevat: <ul> <li>TEXT: een tekst <li>INTEGER: een
geheel getal <li>REAL: een kommagetal </ul>



Omdat er maar drie datatypen zijn zul je sommige gegevens als een TEXT
opslaan. Bijvoorbeeld, een datum sla je in de vorm jjjj-mm-dd (j: jaar, m:
maand, d:dag) op als een tekst, bijvoorbeeld: "2025-04-20". Een
telefoonnummer zul je ook als een tekst opslaan, omdat anders de voorloop nul
wegvalt, bijvoorbeeld: "0688567389".


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
      <th>telefoon/th>
    </tr>
        <tr>
      <td>INTEGER</td>
      <td>TEXT</td>
      <td>TEXT</td>
      <td>TEXT</td>
      <td>TEXT</td>
      <td>TEXT</td>
      <td>TEXT</td>
      <td>TEXT/td>
    </tr>
  </thead>
</table>





-->



## 1.3: Primary key 


Elke tabel heeft een kolom hebben waarmee je gegevens
kan aanwijzen: een <b>primary key</b>. Deze kolom moet <b>unieke</b> gegevens
hebben, een kolom waar nooit twee keer hetzelfde waarde voor mag komen. 

Een
voorbeeld is <i>leerlingnummer</i>. Er kunnen geen twee leerlingen dezelfde
leerlingnummer hebben. Terwijl er misschien wel twee leerlingen met dezelfde
naam zijn, bijvoorbeeld Tom Janssen. Met een leerlingnummer weet je zeker
over wie je het hebt. Een andervoorbeeld is een gebruikersnaam in een spel,
daar mag er maar één van zijn.

(<i>Toelichting: een primary key kan uit meerdere kolommen samen bestaan,
maar dat behandelen we in deze cursus niet.</i>)

### Verwerkingsopdracht 1.3.1 Wat is een primary key?

Welke van de volgende uitspraken over primary keys is correct?


A. Een primary key mag leeg zijn
B. Een primary key mag dubbel voorkomen
C. Een primary key identificeert elke rij op unieke wijze
D. Een primary key is altijd tekst


<p>Bekijk <a
href="https://rweeda.github.io/PythonIA/docs/IA_sql_oplossingen.html#opgave131"
target="_blank">hier</a> de voorbeelduitwerking.</p>

<!--
ANTWOORD: Antwoord C is juist
-->

### Verwerkingsopdracht 1.3.2 Welk kolom is een primary key?

Bekijk weer het tabel `klanten`. Welk kolom is hier de primary key?

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
      <th>telefoon/th>
    </tr>
  </thead>
</table>


<p>Bekijk <a
href="https://rweeda.github.io/PythonIA/docs/IA_sql_oplossingen.html#opgave132"
target="_blank">hier</a> de voorbeelduitwerking.</p>

<!--
ANTWOORD: Kolom <i>klantnummer</i> is de primary key. Elk klant heeft een eigen unieke klantnummer. 
-->


## 1.4: Eisen stellen aan data 

Naast dat data van een bepaald type is, kun
je nog anderen eisen stellen aan waarden in een bepaald kolom, bijvoorbeeld:
<ul>
  <li>PRIMARY KEY: unieke waarde
  <li>NOT NULL: mag niet leeg zijn



### Verwerkingsopdracht 1.4 Eisen aan datat stellen bij het ontwerpen van een tabel 


Ga verder met de tabel
uit de vorige opdracht. <br>

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
      <th>telefoon/th>
    </tr>
        <tr>
      <td>INTEGER</td>
      <td>TEXT</td>
      <td>TEXT</td>
      <td>TEXT</td>
      <td>TEXT</td>
      <td>TEXT</td>
      <td>TEXT</td>
      <td>TEXT/td>
    </tr>
  </thead>
</table>





Geef bij elke kolom aan of er speciale eisen aan gesteld zijn:
  <ul>
  <li>PRIMARY KEY: een unieke waarde (in het Nederlands <i>primaire sleutel</i>)
  <li>NOT NULL: mag niet leeg zijn
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



# 1.5: Nut van databases


[![Watch the
video](https://www.youtube.com/watch?v=t8jgX1f8kc4/hqdefault.jpg)](https://www.youtube.com/watch?v=t8jgX1f8kc4)


<p>Je kunt je voorstellen dat Danilo graag een goed overzicht wil houden van
alle verzamelde gegevens. Daarom gebruikt hij een <b>database</b>. Een
database is een gestructureerde manier om gegevens op te slaan. Met een
database is het mogelijk om door middel van een speciale vraagtaal gegevens
op te vragen en te combineren tot nuttige informatie.</p>

<p>Data is overal, niet alleen in de pizzeria van Danilo. Zodra jij je op het
internet begeeft laat je een spoor van gegevens achter en die data moet
ergens heen. Terwijl jij, bijvoorbeeld, gebruik maakt van YouTube worden
verschillende gegevens verzameld die hergebruikt kunnen worden om een
gepersonaliseerde ervaring aan te kunnen bieden. Denk hierbij aan hoe lang je
naar een video kijkt, naar welke video’s je zoekt of op welke video’s die
aangeraden worden jij ook echt doorklikt. Ook moet er veel informatie over de
video’s zelf opgeslagen worden zoals de titel, de thema’s, de lengte, etc. Je
kunt je voorstellen dat via het internet zo een enorme hoeveelheid data
verzameld wordt.</p>


<p>Jouw school maakt ook gebruik van databases. Gebruikt je school Magister
of Somtoday? Deze programma's slaan informatie over jou als leerling op in
een database. Hiermee kan je docent huiswerk opgeven en toetscijfers inzien
en invoeren, kan de schoolleiding zien hoe het met verschillende klassen gaat
en kan jij zien hoe je er voor staat met al je vakken of opdrachten
inleveren.</p>

# 1.6: Databasemanagementsysteem (DBMS) 


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
databases worden beheerd door een databasebeheersysteem (*Database Management
System*, of DBMS). </p>


[TODO IMG]


<p>Zo’n systeem zorgt ervoor dat de data betrouwbaar en correct blijft, en
dat wij op een eenvoudige manier informatie kunnen opvragen wanneer we die
nodig hebben.</p>



### Verwerkignsopdracht 1.6.1  Waar vind je databases?

<p>Waarschijnlijk heb je al eerder gebruik gemaakt van een database,
misschien zonder dat je dat wist. Laten we eens op onderzoek uit gaan en
kijken of we nog meer databases kunnen vinden.</p>

<ol style="list-style-type: lower-alpha"> <li>Bedenk nog een voorbeeld van
een website die, naar jouw verwachting, gebruik maakt van een database. </li>
<li>Wat voor soort data zou opgeslagen worden in deze database?</li> </ol>

<p>Bekijk <a
href="https://rweeda.github.io/PythonIA/docs/IA_sql_oplossingen.html#opgave161"
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







### Verwerkingsopdracht 1.6.2 Gegevens, data en informatie


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


# 1.7: Samenvatting Databases

Bij het maken van de vorige opdrachten heb je veel geleerd over
gestructureerde data. We vatten dat nu samen.

<ul> 

<li><b>Database</b>: Een georganiseerde verzameling gegevens, opgeslagen
in tabellen met rijen en kolommen. In een pizzeria zoals Danilo’s worden gegevens opgeslagen over o.a. pizza’s, klanten, bestellingen en bezorgers.
<li>Een tabel heeft kolommen. Ieder kolom heeft een naam zoals <i>voornaam</i>, <i>adres</i>, <i>telefoonnummer</i>, enz. en een datatype (bijv. tekst of getal).
 <li><b>Datatypes</b> in SQLite:  INTEGER -
Gehele getallen (bijv. een klantnummer: 4054), TEXT - Tekstuele gegevens (bijv. een naam :'Jaap') en REAL -
Kommagetallen (bijv. een prijs: 2.50) <li><b>Primary Key</b>: Elk tabel heeft een kolom waarbij elke rij uniek is. Voorbeelden: klantnummer, leerlingnummer.
<li>Gegevens</b> zijn feiten die je kunt verzamelen, zoals een naam of temperatuur.
<li>Data</b> zijn opgeslagen gegevens (in tabellen of bestanden).
<li>Informatie</b> is eïnterpreteerde data die betekenis heeft, bijvoorbeeld een weerbericht.</ul>
