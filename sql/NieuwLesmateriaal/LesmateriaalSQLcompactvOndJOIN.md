## ONDERWERP 5

## 5.1 Gegevens uit meerdere tabellen combineren


<p>Tot nu toe heb je geleerd hoe je gegevens uit één tabel opvraagt. Maar soms wil je gegevens uit meerdere tabellen combineren. Daarvoor gebruik je <em>JOIN .. ON ..</em>.</p>

<p>Stel je voor: je wilt van elk <b>besteldepizzacode</b> weten hoe de pizza heet. <br>
In de tabel <em>besteldepizza</em> zie je <strong>welke pizza is besteld</strong>, maar niet de naam — alleen een <em>pizzacode</em>. De namen van de pizza’s staan in een andere tabel: <em>pizza</em>. Als je wilt weten <strong>welke pizza’s</strong> er precies besteld zijn, moet je gegevens <strong>uit beide tabellen combineren</strong>.</p>

<p>Zoals je ziet:</p>
<ul>
  <li><em>besteldepizza</em> weet wél dat pizzacode 101 besteld is,</li>
  <li>maar <strong>alleen</strong> tabel <em>pizza</em> weet dat dit de <em>Margherita</em> is.</li>
</ul>

<table>
<tr><td>
<h3>Tabel: <em>besteldepizza</em></h3>


<table border="1" cellpadding="4" cellspacing="0">
  <thead>
    <tr>
      <th>besteldepizzacode</th>
      <th>pizzacode</th>
    </tr>
  </thead>
  <tbody>
    <tr><td>1</td><td>101</td></tr>
    <tr><td>2</td><td>102</td></tr>
    <tr><td>3</td><td>103</td></tr>
  </tbody>
</table>
</td><td>


<h3>Tabel: <em>pizza</em></h3>

<table border="1" cellpadding="4" cellspacing="0">
  <thead>
    <tr>
      <th>pizzacode</th>
      <th>naam</th>
    </tr>
  </thead>
  <tbody>
    <tr><td>101</td><td>Margherita</td></tr>
    <tr><td>102</td><td>Quattro Formaggi</td></tr>
    <tr><td>103</td><td>Salami</td></tr>
  </tbody>
</table>
</td></tr></table>



<p>In het <b>ERD-schema</b> (Entity-Relationship Diagram) hieronder zie je een overzicht van de tabellen en hoe ze met elkaar verbonden zijn. De pijlen geven de koppelingen tussen tabellen aan. Een bestelde pizza (in tabel <i>besteldePizza</i>) heeft een <b>pizzacode</b>. Aan het pijltje zie je dat de gegevens over de pizza te vinden zijn in de tabel <i>pizza</i>.</p>

<img src="https://raw.githubusercontent.com/rweeda/PythonIA/main/sql/DaniloIA_ERD.png" alt="overzicht tabellen" width="500">


### Verwerkingsopdracht 5.1.1 Koppelingen tussen tabellen

Welke twee tabellen zijn in de ERD direct aan elkaar gekoppeld via de kolom pizzacode?

<ul style="list-style-type: upper-alpha;">
  <li><em>klant</em> en <em>bestelling</em></li>
  <li><em>klant</em> en <em>pizza</em></li>
  <li><em>bestelling</em> en <em>bezorger</em></li>
  <li><em>bodem</em> en <em>klant</em></li>
</ul>

<p>Bekijk <a href="https://rweeda.github.io/PythonIA/docs/IA_sql_oplossingen.html#opgave511" target="_blank">hier</a> de voorbeelduitwerking.</p>
<!--
A (<em>klant</em> en <em>bestelling</em>).<p> Toelichting: De tabel <em>bestelling</em> bevat de kolom <b>klantnummer</b> die verwijst naar een rij in de tabel <em>klant</em>.</p>
-->


## 5.2 JOIN ...  ON ... - Gegevens uit meerdere tabellen combineren 


<p>Met een JOIN ... ON ... <strong>koppel je de gelijke rijen van twee tabellen aan elkaar</strong>. In het bovenstaande voorbeeld zien we dat <em>pizzacode</em> in zowel tabel <em>besteldepizza</em> voorkomt als in <em>pizza</em>. Achter <em>JOIN</em> geef je aan welke tabellen je combineert, en achter <em>ON</em> geef je aan welke kolommen gelijk moeten zijn.</p>

<p>De <em>.</em>-notatie (bijvoorbeeld <em>tabel.kolom</em>) gebruik je om aan te geven uit welke tabel een kolom komt.</p>

<p>Omdat de kolom <em>pizzacode</em> in beide tabellen voorkomt, geven we met de puntnotatie <em>besteldepizza.pizzacode</em> aan dat het uit tabel <em>besteldepizza</em> komt, en met <em>pizza.pizzacode</em> dat het uit tabel <em>pizza</em> komt.</p>

<table width="100%"><tr><td style="text-align:left; vertical-align:top; font-size:1.25rem;" width="35%">

<p>De query ziet er dus zo uit:</p>

<pre><code class="language-sql">
SELECT besteldepizza.besteldepizzacode, pizza.naam
FROM besteldepizza
JOIN pizza ON besteldepizza.pizzacode = pizza.pizzacode;
</code></pre>
</td><td width="65%">

De uitvoer van deze query is:

<table border="1" cellpadding="4" cellspacing="0">
  <thead>
    <tr>
      <th>besteldepizzacode</th>
      <th>naam</th>
    </tr>
  </thead>
  <tbody>
    <tr><td>1</td><td>Margherita</td></tr>
    <tr><td>2</td><td>Quattro Formaggi</td></tr>
    <tr><td>3</td><td>Salami</td></tr>
  </tbody>
</table>

</td></tr></table>



### Verwerkingsopdracht 5.2.1 Nut van een JOIN
Stel we willen een overzicht van de pizzanaam met de besteldepizzacode.
Waarom is een JOIN nodig in de query hieronder?
<ol type="A">
<li>Omdat tabel `besteldepizza` geen gegevens bevat over pizzacodes.
<li>Omdat je een extra filter op de gegevens wilt toepassen.
<li>>Omdat de naam van de pizza niet in tabel `besteldepizza` staat.
<li>Omdat je gegevens uit dezelfde tabel wilt combineren.
</ol>


<pre><code class="language-sql">
SELECT besteldepizza.besteldepizzacode, pizza.naam
FROM besteldepizza
JOIN pizza ON besteldepizza.pizzacode = pizza.pizzacode;
</code></pre>

<p>Bekijk <a href="https://rweeda.github.io/PythonIA/docs/IA_sql_oplossingen.html#opgave521" target="_blank">hier</a> de voorbeelduitwerking.</p>
<!-- ANTWOORD:
C. Omdat de naam van de pizza niet in `besteldepizza` staat
-->



### Verwerkingsopdracht 5.2.2 BesteldePizza, datum en bezorg tijd

<table width="100%"><tr><td style="text-align:left; vertical-align:top; font-size:1.25rem;" width="35%">

Maak een overzicht van de <b>besteldepizzacode</b>, en <b>besteldatum</b> en <b>bezorgtijd</b>. De gegevens komen uit tabellen <i>besteldePizza</i> en <i>>bestelling</i>. Toon het overzicht zoals hiernaast.


</td><td width="65%">

<table border="1" cellpadding="4" cellspacing="0">
  <thead>
    <tr>
      <th>besteldepizzacode</th>
      <th>bestel_datum</th>
      <th>bezorg_tijd</th>
    </tr>
  </thead>
  <tbody>
    <tr><td>1</td><td>2021-12-01</td><td>18:37:00</td></tr>
    <tr><td>2</td><td>2021-12-01</td><td>18:37:00</td></tr>
    <tr><td>3</td><td>2021-12-01</td><td>18:37:00</td></tr>
    <tr><td>4</td><td>2021-12-01</td><td>18:41:00</td></tr>
    <tr><td>…</td><td>…</td><td>…</td></tr>
    <tr><td>5833</td><td>2022-03-03</td><td>19:50:00</td></tr>
  </tbody>
</table>

</td></tr></table>



<p>Bekijk <a href="https://rweeda.github.io/PythonIA/docs/IA_sql_oplossingen.html#opgave522" target="_blank">hier</a> de voorbeelduitwerking.</p>
<!-- ANTWOORD:
<pre><code class="language-sql">
SELECT besteldePizza.besteldepizzacode, bestelling.bestel_datum, bestelling.bezorg_tijd
FROM besteldePizza
JOIN bestelling ON besteldePizza.bestelcode = bestelling.bestelcode;
</code></pre>
-->


### Verwerkingsopdracht 5.2.3 JOIN uitleggen
Schrijf in je eigen woorden wat er gebeurt bij een JOIN. Wat moet er kloppen tussen twee tabellen om een JOIN te kunnen maken?



<p>Bekijk <a href="https://rweeda.github.io/PythonIA/docs/IA_sql_oplossingen.html#opgave713" target="_blank">hier</a> de voorbeelduitwerking.</p>
<!-- ANTWOORD:
Een JOIN koppelt rijen van twee tabellen aan elkaar via een gemeenschappelijke kolom met gelijke waarden. Die kolommen moeten logisch bij elkaar horen en dezelfde soort informatie bevatten.
-->











# 5.3: Meer dan 2 tabellen koppelen

Je kunt ook meer dan 3 tabellen koppelen met een JOIN. Je koppelt eerst twee tabellen via de kolom met gelijke waarden.
Daarna voeg je een derde tabel toe met een extra JOIN.

```SQL
SELECT ...
FROM tabel1
JOIN tabel2 ON tabel1.kolom = tabel2.kolom
JOIN tabel3 ON tabel2.kolom = tabel3.kolom;
```


<table width="100%"><tr><td style="text-align:left; vertical-align:top; font-size:1.25rem;" width="35%">
<b>Voorbeeld. Deze query geeft een overzicht met <b>besteldepizzacode</b> (uit tabel <i>besteldePizza</i>), <b>naam</b> (uit tabel <i>pizza</i>) en <b>omschrijving</b> (uit tabel <i>formaat</i>) door de drie tabellen te koppelen via kolommen met gelijke waarden.</p>

<pre><code class="language-sql">
SELECT besteldePizza.besteldepizzacode, pizza.naam, formaat.omschrijving
FROM besteldePizza
JOIN pizza ON besteldePizza.pizzacode = pizza.pizzacode 
JOIN formaat ON besteldePizza.formaatcode = formaat.formaatcode; 
</code></pre>

</td><td width="65%">

<table border="1" cellpadding="4" cellspacing="0">

  <thead>
    <tr>
      <th>besteldepizzacode</th>
      <th>naam</th>
      <th>omschrijving</th>
    </tr>
  </thead>
  <tbody>
    <tr><td>1</td><td>Marinara</td><td>extra groot (40 cm)</td></tr>
    <tr><td>2</td><td>Hawai</td><td>groot (35 cm)</td></tr>
    <tr><td>3</td><td>Fantasia</td><td>klein (25 cm)</td></tr>
    <tr><td>4</td><td>Salmone</td><td>klein (25 cm)</td></tr>
    <tr><td>…</td><td>…</td><td>…</td></tr>
    <tr><td>5833</td><td>Prosciutto</td><td>medium (30 cm)</td></tr>
  </tbody>
</table>
</td></tr></table>

### Opdracht 5.3.1: Overzicht van naam en bodem van alle bestelde pizza's


<table width="100%"><tr><td style="text-align:left; vertical-align:top; font-size:1.25rem;" width="35%">

Maak een overzicht van alle bestelde pizza’s met daarbij de <b>naam</b> (uit tabel <i>pizza</i> van de pizza en de soort <b>omschrijving</b> van de bodem (uit tabel <i>bodem</i>).
Tip: Je hebt een derde tabel nodig, namelijk <i>besteldepizza</i> om de gegevens aan elkaar te koppelen.


</td><td width="65%">

<table border="1" cellpadding="4" cellspacing="0">
  <thead>
    <tr>
      <th>besteldepizzacode</th>
      <th>pizzanaam</th>
      <th>bodem</th>
    </tr>
  </thead>
  <tbody>
    <tr><td>1</td><td>Marinara</td><td>krokante dunne bodem</td></tr>
    <tr><td>2</td><td>Hawai</td><td>glutenvrije bodem</td></tr>
    <tr><td>3</td><td>Fantasia</td><td>panbodem</td></tr>
    <tr><td>4</td><td>Salmone</td><td>krokante dunne bodem</td></tr>
    <tr><td>…</td><td>…</td><td>…</td></tr>
    <tr><td>5833</td><td>Prosciutto</td><td>krokante dunne bodem</td></tr>
  </tbody>
</table>


</td></tr></table>



<p>Bekijk <a href="https://rweeda.github.io/PythonIA/docs/IA_sql_oplossingen.html#opgave531" target="_blank">hier</a> de voorbeelduitwerking.</p>
<!-- ANTWOORD:
<ol type="alpha">
<li>
<pre><code class="language-sql">
SELECT besteldepizza.bestelcode, pizza.naam AS pizzanaam, bodem.omschrijving AS bodembeschrijving
FROM besteldepizza
JOIN pizza ON besteldepizza.pizzacode = pizza.pizzacode
JOIN bodem ON besteldepizza.bodemcode = bodem.bodemcode;
</code></pre>
</li>
<li>
Je kunt dit niet doen zonder JOIN, omdat de informatie die je nodig hebt verspreid is over meerdere tabellen.<br>
In de tabel <code>besteldepizza</code> staat de <code>pizzacode</code> en de <code>bodemcode</code>,
maar de naam van de pizza staat in de tabel <code>pizza</code>,
en de omschrijving van de bodem staat in de tabel <code>bodem</code>.
</li>
</ol>
-->

### 5.4: Samenvatting
<ul>
  <li>Relaties tussen tabellen zijn zichtbaar in een ERD-schema (Entity-Relationship Diagram).</li>
  <li>Met een <code>JOIN</code> is het mogelijk om betekenisvolle combinaties van data uit verschillende tabellen te maken, zoals klantgegevens met bezorger, of pizza met formaat en bodem.</li>
  <li>De kolommen waarop je koppelt, moeten in beide tabellen voorkomen en dezelfde soort waarden bevatten.</li>
  <li>Met <code>tabel.kolom</code> geef je aan uit welke tabel een kolom komt.</li>
  <li>Je kunt meerdere <strong>JOINs</strong> gebruiken om drie of meer tabellen aan elkaar te koppelen.</li>
</ul>






### 5.5: Afsluitende Opdrachten



### Afsluitende Opdracht 5.5.1 Omschrijving van de bodem bij een bestelling

<table width="100%"><tr><td style="text-align:left; vertical-align:top; font-size:1.25rem;" width="35%">
Laat zien welke bodembeschrijving hoort bij elke bestelde pizza, zoals in het ovezicht hiernaast. De informatie komt uit tabellen <i>besteldepizza</i> en <i>bodem</i>.


</td><td width="65%">
<table border="1" cellpadding="4" cellspacing="0">
  <thead>
    <tr>
      <th>besteldepizzacode</th>
      <th>omschrijving</th>
    </tr>
  </thead>
  <tbody>
    <tr><td>1</td><td>American style</td></tr>
    <tr><td>2</td><td>American style</td></tr>
    <tr><td>3</td><td>American style</td></tr>
    <tr><td>4</td><td>American style</td></tr>
    <tr><td>…</td><td>…</td></tr>
    <tr><td>5832</td><td>Italian style</td></tr>
    <tr><td>5833</td><td>American style</td></tr>
  </tbody>
</table>



</td></tr></table>


<p>Bekijk <a href="https://rweeda.github.io/PythonIA/docs/IA_sql_oplossingen.html#opgave551" target="_blank">hier</a> de voorbeelduitwerking.</p>

<!-- ANTWOORD:
<pre><code class="language-sql">
SELECT besteldepizza.besteldepizzacode, bodem.omschrijving
FROM besteldepizza
JOIN bodem ON besteldepizza.bodemcode = bodem.bodemcode;
</code></pre>
-->

### Afsluitende Opdracht 5.5.2 Een overzicht van de bestelde pizza en het formaat

<table width="100%"><tr><td style="text-align:left; vertical-align:top; font-size:1.25rem;" width="35%">

Toon een overzicht van de bestelde pizza en het formaat zoals hiernaast.

</td><td width="65%">



</td></tr></table>



<p>Bekijk <a href="https://rweeda.github.io/PythonIA/docs/IA_sql_oplossingen.html#opgave552" target="_blank">hier</a> de voorbeelduitwerking.</p>
<!-- ANTWOORD:
<pre><code class="language-sql">
SELECT 
  besteldePizza.besteldepizzacode,
  pizza.naam AS pizzanaam,
  formaat.omschrijving AS formaat
FROM besteldePizza
JOIN pizza ON besteldePizza.pizzacode = pizza.pizzacode
JOIN formaat ON besteldePizza.formaatcode = formaat.formaatcode;
</code></pre>
-->




### Afsluitende Opdracht 5.5.3 Klanten en hun bezorgers

<table width="100%"><tr><td style="text-align:left; vertical-align:top; font-size:1.25rem;" width="35%">

<p>Maak een overzicht van bestellingen met de <b>naam van de klant</b>, het <b>adres</b> van de klant, en de <b>naam van de bezorger</b>. Toon het overzicht zoals hiernaast, let daarbij op de kolomnamen.</p>

<p>Tip: Hiervoor moet je de tabellen <i>bestelling</i>, <i>klant</i> en <i>bezorger</i>koppelen.

</td><td width="65%">
<table border="1" cellpadding="4" cellspacing="0">
  <thead>
    <tr>
      <th>klantnaam</th>
      <th>klantadres</th>
      <th>bezorgernaam</th>
    </tr>
  </thead>
  <tbody>
    <tr><td>Sanne Jansen</td><td>Lindenstraat 12</td><td>Mohammed</td></tr>
    <tr><td>Lars Willems</td><td>Beukenlaan 34</td><td>Julia</td></tr>
    <tr><td>Fatima El Amrani</td><td>Schoolstraat 5</td><td>Mohammed</td></tr>
    <tr><td>…</td><td>…</td><td>…</td></tr>
  </tbody>
</table>



</td></tr></table>


<p>Bekijk <a href="https://rweeda.github.io/PythonIA/docs/IA_sql_oplossingen.html#opgave553" target="_blank">hier</a> de voorbeelduitwerking.</p>
<!-- ANTWOORD:
SELECT 
  klant.naam AS klantnaam,
  klant.adres AS klantadres,
  bezorger.naam AS bezorgernaam
FROM bestelling
JOIN klant ON bestelling.klantnummer = klant.klantnummer
JOIN bezorger ON bestelling.bezorgercode = bezorger.bezorgercode;
</code></pre>
-->





### Afsluitende Opdracht 5.5.4 Bestellingen van klanten uit Enschede of Hengelo
<table width="100%"><tr><td style="text-align:left; vertical-align:top; font-size:1.25rem;" width="35%">

Toon de <b>bestelcode</b> en <b>klantnummer</b> van de eerste 3 bestellingen waarvan de klant uit <b>Enschede of Hengelo</b> komt, zoals in het overzicht hiernaast. De gegevens komen uit tabellen <i>klant</i> en <i>bestelling</i>.

</td><td width="65%">
<table border="1" cellpadding="4" cellspacing="0">
  <thead>
    <tr>
      <th>bestelcode</th>
      <th>klantnummer</th>
    </tr>
  </thead>
  <tbody>
    <tr><td>1</td><td>224</td></tr>
    <tr><td>4</td><td>323</td></tr>
    <tr><td>5</td><td>279</td></tr>
  </tbody>
</table>


</td></tr></table>

<p>Bekijk <a href="https://rweeda.github.io/PythonIA/docs/IA_sql_oplossingen.html#opgave554" target="_blank">hier</a> de voorbeelduitwerking.</p>
<!-- ANTWOORD:
<pre><code class="language-sql">
SELECT bestelcode, bestelling.klantnummer
FROM bestelling
JOIN klant  ON bestelling.klantnummer = klant.klantnummer
WHERE woonplaats = 'Enschede' OR woonplaats = 'Hengelo'
LIMIT 3;
</code></pre>
-->




### Afsluitende Opdracht 5.5.5 Bezorgerinformatie



<table width="100%"><tr><td style="text-align:left; vertical-align:top; font-size:1.25rem;" width="35%">
Toon uit tabel `bestelling` voor de eerste vijf gegevens, de naam van de bezorger en bijbehorende de klantgegevens (klantnaam, adres, postcode, en woonplaats). Toon het overzicht zoals hiernaast.
</td><td width="65%">
<table border="1" cellpadding="4" cellspacing="0">
  <thead>
    <tr>
      <th>bezorgernaam</th>
      <th>klantnaam</th>
      <th>adres</th>
      <th>postcode</th>
      <th>woonplaats</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Han Fröling</td>
      <td>Katja Pas</td>
      <td>Koperwiek 73</td>
      <td>3766AM</td>
      <td>Hengelo</td>
    </tr>
    <tr>
      <td>Afhalen</td>
      <td>Bram Kuipers</td>
      <td>Heyendaalseweg 300</td>
      <td>6525EC</td>
      <td>Nijmegen</td>
    </tr>
    <tr>
      <td>Ageeth Mooy</td>
      <td>Frank Goudsmit</td>
      <td>Pelikaanweg 17</td>
      <td>3762VA</td>
      <td>Hengelo</td>
    </tr>
    <tr>
      <td>Hans Boonstra</td>
      <td>Maarten Doornbos</td>
      <td>Mozartlaan 35</td>
      <td>3741HT</td>
      <td>Enschede</td>
    </tr>
    <tr>
      <td>Marleen Hoekstra</td>
      <td>Margaretha Verwoert - Gro</td>
      <td>Goudenregenlaan 30</td>
      <td>3741CB</td>
      <td>Enschede</td>
    </tr>
  </tbody>
</table>


</td></tr></table>

<p>Bekijk <a href="https://rweeda.github.io/PythonIA/docs/IA_sql_oplossingen.html#opgave555" target="_blank">hier</a> de voorbeelduitwerking.</p>

<!-- ANTWOORD
<pre><code class="language-sql">
SELECT 
    bezorger.naam AS bezorgernaam,
    klant.naam AS klantnaam,
    klant.adres,
    klant.postcode,
    klant.woonplaats
FROM bestelling
JOIN bezorger ON bestelling.bezorgernummer = bezorger.bezorgernummer
JOIN klant ON bestelling.klantnummer = klant.klantnummer
LIMIT 5;
</code></pre>
-->





### Afsluitende Opdracht 5.5.6 Voor de kok

<table width="100%"><tr><td style="text-align:left; vertical-align:top; font-size:1.25rem;" width="35%">
Maak voor de kok een overzicht van welke pizza's besteld zijn zoals hieronder, met daarin pizzanaam, formaat, bodem. Laat alleen de eerste 10 zien.

</td><td width="65%">

<table border="1" cellpadding="4" cellspacing="0">
  <thead>
    <tr>
      <th>pizzanaam</th>
      <th>formaat</th>
      <th>bodem</th>
    </tr>
  </thead>
  <tbody>
    <tr><td>Marinara</td><td>extra groot (40 cm)</td><td>American style</td></tr>
    <tr><td>Hawai</td><td>groot (35 cm)</td><td>American style</td></tr>
    <tr><td>Fantasia</td><td>klein (25 cm)</td><td>American style</td></tr>
    <tr><td>Salmone</td><td>klein (25 cm)</td><td>American style</td></tr>
    <tr><td>Fantasia</td><td>medium (30 cm)</td><td>American style</td></tr>
    <tr><td>Inferno</td><td>groot (35 cm)</td><td>American style</td></tr>
    <tr><td>Vegetariana</td><td>extra groot (40 cm)</td><td>Italian style</td></tr>
    <tr><td>Salame</td><td>klein (25 cm)</td><td>American style</td></tr>
    <tr><td>Borromea</td><td>klein (25 cm)</td><td>American style</td></tr>
    <tr><td>Calimero</td><td>groot (35 cm)</td><td>American style</td></tr>
  </tbody>
</table>

</td></tr></table>

<p>Bekijk <a href="https://rweeda.github.io/PythonIA/docs/IA_sql_oplossingen.html#opgave556" target="_blank">hier</a> de voorbeelduitwerking.</p>
<!-- ANTWOORD:
<pre><code class="language-sql">
SELECT 
    pizza.naam AS pizzanaam,
    formaat.omschrijving AS formaat,
    bodem.omschrijving AS bodem
FROM besteldePizza
JOIN pizza ON besteldePizza.pizzacode = pizza.pizzacode
JOIN formaat ON besteldePizza.formaatcode = formaat.formaatcode
JOIN bodem ON besteldePizza.bodemcode = bodem.bodemcode
LIMIT 10;
</code></pre>
-->






