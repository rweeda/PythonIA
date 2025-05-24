

### Overzicht ONDERWERP 3





## 3.1: Kolom hernoemen met <code>AS</code>

Met `AS` kan je een kolomnaam hernoemen. Dit doe je na de `SELECT`:

``` SQL
SELECT kolomnaam_in_tabel AS kolomnaam_in_overzicht
FROM tabel;
```


<table width="100%">
  <tr>
 <tr><td style="text-align:left; vertical-align:top; font-size:1.25rem;" width="35%">
Bijvoorbeeld, om de kolom <b>naam</b> te tonen als <b>pizzanaam</b>:
``` SQL
SELECT naam AS pizzanaam
FROM pizza;
```
    </td>
    <td width="65%">
<table border="1">
  <thead>
    <tr>
      <th>pizzanaam</th>
    </tr>
  </thead>
  <tbody>
    <tr><td>Margherita</td></tr>
    <tr><td>Napoletana</td></tr>
    <tr><td>Prosciutto</td></tr>
    <tr><td>Funghi</td></tr>
    <tr><td>Salame</td></tr>
  </tbody>
</table>

    </td>
  </tr>
</table>



### Verwerkingsopdracht 3.1.1 Kolom hernoemen
<table>
 <tr><td style="text-align:left; vertical-align:top; font-size:1.25rem;" width="35%">
Toon een overzicht van alle namen van de bezorgers zoals het overzicht hiernaast. Noem het kolom <b>bezorgernaam</b>. De gegevens komen uit tabel <i>bezorger</i>.
</td><td width=65%>
  <table border="1">
    <tr>
      <th>bezorgernaam</th>
    </tr>
    <tr><td>Afhalen</td></tr>
    <tr><td>Ageeth Mooy</td></tr>
    <tr><td>Eric Henze</td></tr>
    <tr><td>...</td></tr>
    <tr><td>Herman Prent</td></tr>
  </table>
</td>
</tr>
</table>


<p>Bekijk <a href="https://rweeda.github.io/PythonIA/docs/IA_sql_oplossingen.html#opgave311" target="_blank">hier</a> de voorbeelduitwerking.</p>
<!-- ANTWOORD:
<pre><code class="language-sql">
SELECT naam AS bezorgernaam
FROM bezorger;
</code></pre>
-->



## 3.2: Aantal rijen beperken met <code>LIMIT</code>
<p>Met LIMIT kun je bepalen hoeveel rijen er getoond moeten worden.</p>
``` SQL
SELECT kolomnaam
FROM tabel
LIMIT aantal_rijen;
```

<table width="100%">
 <tr><td style="text-align:left; vertical-align:top; font-size:1.25rem;" width="35%">
<p>Met de volgende code toon je alleen de eerste vijf rijen:</p>
``` SQL
SELECT *
FROM pizza
LIMIT 5;
```
    </td>
    <td width="65%">
<table border="1">
  <thead>
    <tr>
      <th>pizzacode</th>
      <th>naam</th>
      <th>omschrijving</th>
      <th>basisprijs</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>1</td>
      <td>Margherita</td>
      <td>Tomaat,kaas en oregano</td>
      <td>6</td>
    </tr>
    <tr>
      <td>2</td>
      <td>Napoletana</td>
      <td>Tomaat, kaas, ansjovis, olijven, kappertjes en oregano</td>
      <td>7.5</td>
    </tr>
    <tr>
      <td>3</td>
      <td>Prosciutto</td>
      <td>Tomaat, kaas, ham en oregano</td>
      <td>7.5</td>
    </tr>
    <tr>
      <td>4</td>
      <td>Funghi</td>
      <td>Tomaat, kaas, champignons en oregano</td>
      <td>7.5</td>
    </tr>
    <tr>
      <td>5</td>
      <td>Salame</td>
      <td>Tomaat, kaas, salami en oregano</td>
      <td>7.5</td>
    </tr>
  </tbody>
</table>
    </td>
  </tr>
</table>

### Verwerkingsopdracht 3.2.1 Alleen de eerste drie pizza's
<table width="100%">
 <tr><td style="text-align:left; vertical-align:top; font-size:1.25rem;" width="35%">
Toon de <b>naam</b> en <b>basisprijs</b> van de eerste drie pizza's, zoals in het overzicht hiernaast.
    </td>
    <td width="65%">
    </td>
    <table border="1">
  <thead>
    <tr>
      <th>naam</th>
      <th>basisprijs</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Margherita</td>
      <td>6</td>
    </tr>
    <tr>
      <td>Napoletana</td>
      <td>7.5</td>
    </tr>
    <tr>
      <td>Prosciutto</td>
      <td>7.5</td>
    </tr>
  </tbody>
</table>

  </tr>
</table>
<p>Bekijk <a href="https://rweeda.github.io/PythonIA/docs/IA_sql_oplossingen.html#opgave321" target="_blank">hier</a> de voorbeelduitwerking.</p>
<!-- ANTWOORD:
<pre><code class="language-sql">
SELECT naam, basisprijs
FROM pizza
LIMIT 3;
</code></pre>
-->




## 3.3: Gegevens sorteren met ORDER BY

Met ORDER BY kun je resultaten sorteren.
Hierbij moet je aangeven op welke kolom er gesorteerd moet worden en of het oplopend ('ASC') of juist 
aflopend ('DESC') moet zijn. Geef altijd eerst de SELECT en FROM aan, en daarna de ORDER BY.



Bijvoorbeeld, om de pizza's op oplopend op prijs te sorteren, dus met de goedkoopste pizza bovenaan:

SELECT naam, basisprijs
FROM pizza
ORDER BY basisprijs ASC;


Of om de bezorgers te aflopende sorteren op geboortedatum, dus met de jongste bezorger bovenaan:

SELECT naam, geboortedatum
FROM bezorger
ORDER BY gebdatum DESC;

Ter herinnering, hieronder de volgorde waarin alle commando's die gebruikt worden moeten staan:
<p><img
src="https://raw.githubusercontent.com/rweeda/PythonIA/main/sql/img/H1_commandos.png"
alt="Commando's voor het ophalen van informatie" width="400"></p>





### Verwerkingsopdracht 3.3.1 de drie duurste pizza's

<table width="100%"><tr><td style="text-align:left; vertical-align:top; font-size:1.25rem;" width="35%">
Geef een overzicht van de pizza's gesorteerd op prijs van laag naar hoog.
</td><td width="65%">
    <table border="1">
  <thead>
    <tr>
      <th>naam</th>
      <th>basisprijs</th>
    </tr>
  </thead>
  <tbody>
    <tr><td>Margherita</td><td>6</td></tr>
    <tr><td>Cippola</td><td>6.5</td></tr>
    <tr><td>Napoletana</td><td>7.5</td></tr>
    <tr><td>...</td><td>...</td></tr>
    <tr><td>Combinazione</td><td>10.5</td></tr>
  </tbody>
</table>

</td></tr></table>



<p>Bekijk <a href="https://rweeda.github.io/PythonIA/docs/IA_sql_oplossingen.html#opgave331" target="_blank">hier</a> de voorbeelduitwerking.</p>
<!-- ANTWOORD:
<pre><code class="language-sql">
SELECT naam, basisprijs
FROM pizza
ORDER BY basisprijs;
</code></pre>
Ook goed:
<pre><code class="language-sql">
SELECT naam, basisprijs
FROM pizza
ORDER BY basisprijs ASC;
</code></pre>
-->




### Verwerkingsopdracht 3.3.2 De vijf laatste bezorgingen
<table width="100%"><tr><td style="text-align:left; vertical-align:top; font-size:1.25rem;" width="35%">
Geef een overzicht van de pizza's gesorteerd op <b>bestel_datum</b>, zoals in het overzicht hiernaast. <br>
Tip: eerst aflopend sorteren, dan met LIMIT de bovenste acht bestellingen tonen.

</td><td width="65%">
<table border="1">
  <thead>
    <tr>
      <th>bestelcode</th>
      <th>bestel_datum</th>
    </tr>
  </thead>
  <tbody>
    <tr><td>1469</td><td>2022-03-03</td></tr>
    <tr><td>1470</td><td>2022-03-03</td></tr>
    <tr><td>1471</td><td>2022-03-03</td></tr>
    <tr><td>1473</td><td>2022-03-03</td></tr>
    <tr><td>1464</td><td>2022-03-02</td></tr>
    <tr><td>1465</td><td>2022-03-02</td></tr>
    <tr><td>1466</td><td>2022-03-02</td></tr>
    <tr><td>1467</td><td>2022-03-02</td></tr>
  </tbody>
</table>


    
</td></tr></table>



<p>Bekijk <a href="https://rweeda.github.io/PythonIA/docs/IA_sql_oplossingen.html#opgave332" target="_blank">hier</a> de voorbeelduitwerking.</p>
<!-- ANTWOORD:
<pre><code class="language-sql">
SELECT bestelcode, bestel_datum
FROM bestelling
ORDER BY bestel_datum DESC
LIMIT 8;
</code></pre>
-->


### Verwerkingsopdracht 3.3.3 Volgorde van onderdelen

Zet de onderdelen van een SQL-query in de juiste volgorde:
FROM – ORDER BY – LIMIT - SELECT – WHERE

<p>Bekijk <a href="https://rweeda.github.io/PythonIA/docs/IA_sql_oplossingen.html#opgave333" target="_blank">hier</a> de voorbeelduitwerking.</p>
<!-- ANTWOORD:
SELECT
FROM
WHERE
ORDER BY
LIMIT
-->







## 3.4: Wiskundige operatoren

<p>Naast de '='-teken kun ook andere operatoren in de WHERE gebruiken. Hier is een overzicht:</p>

|---------|-----------------------------|
| Operator| Betekenis                   |
|---------|-----------------------------|
| =       | gelijk aan                  |
| >       | groter dan                  |
| >=      | groter dan of gelijk aan    |
| <       | kleiner dan                 |
| <=      | kleiner dan of gelijk aan   |
| <>      | ongelijk aan                |
|---------|-----------------------------|


<b>Bijvoorbeeld, met de volgende query laten we de gegevens zien van klanten die <b>niet</b> in Enschede wonen:

SELECT *
FROM klant
WHERE plaats <> 'Enschede';


<b>En met de volgende query laten we de gegevens zien van pizza's die 8 euro of minder kosten:
SELECT *
FROM pizza
WHERE basisprijs <= 8;




### Verwerkingsopdracht 3.4.1 Dure pizza's

<table width="100%"><tr><td style="text-align:left; vertical-align:top; font-size:1.25rem;" width="35%">
Toon de <b>naam</b> en <b>basisprijs</b> van de pizza's die 9,50 euro kosten of meer, zoals in het overzicht hiernaast.
</td><td width="65%">
<table border="1">
  <thead>
    <tr>
      <th>naam</th>
      <th>basisprijs</th>
    </tr>
  </thead>
  <tbody>
    <tr><td>Specialità di Danilo</td><td>9.5</td></tr>
    <tr><td>Combinazione</td><td>10.5</td></tr>
  </tbody>
</table>


</td></tr></table>




<p>Bekijk <a href="https://rweeda.github.io/PythonIA/docs/IA_sql_oplossingen.html#opgave341" target="_blank">hier</a> de voorbeelduitwerking.</p>
<!-- ANTWOORD:
<pre><code class="language-sql">
SELECT naam, basisprijs
FROM pizza
WHERE basisprijs >=9.50;
</code></pre>
-->



### Verwerkingsopdracht 3.4.2: Geen 8 euro pizza's

<table width="100%"><tr><td style="text-align:left; vertical-align:top; font-size:1.25rem;" width="35%">
Toon de <b>naam</b> en <b>basisprijs</b> van de pizza's die <b>niet</b> 8 euro kosten.
</td><td width="65%">
    <table border="1">
  <thead>
    <tr>
      <th>naam</th>
      <th>basisprijs</th>
    </tr>
  </thead>
  <tbody>
    <tr><td>Margherita</td><td>6</td></tr>
    <tr><td>Napoletana</td><td>7.5</td></tr>
    <tr><td>...</td><td>...</td></tr>
    <tr><td>Della Casa</td><td>8.5</td></tr>
    <tr><td>Specialità di Danilo</td><td>9.5</td></tr>
    <tr><td>Combinazione</td><td>10.5</td></tr>
  </tbody>
</table>

</td></tr></table>




<p>Bekijk <a href="https://rweeda.github.io/PythonIA/docs/IA_sql_oplossingen.html#opgave342" target="_blank">hier</a> de voorbeelduitwerking.</p>
<!-- ANTWOORD:
<pre><code class="language-sql">
SELECT naam, basisprijs
FROM pizza
WHERE basisprijs<>8;
</code></pre>
-->





## 3.5: WHERE met LIKE


<p>Na de `WHERE` kun je met `LIKE` zoeken naar delen van 
teksten, of wanneer je iets ongeveer wilt zoeken. Met de joker geef je aan welke teken(s) anders mogen zijn. De procent 
teken <code>%</code> vervangt nul of meerdere tekens.

Let op:
<ul>
<li>Je gebruikt LIKE na WHERE;
<li>De joker varvangt nul of meerdere tekens;
<li>Je moet bij de LIKE aanhalingstekens gebruiken.
</ul>

<p>Bijvoorbeeld, om alle namen te die beginnen met ‘Jo’ (zoals Josette, Johan) gebruik je:</p>
<table width="100%"><tr><td style="text-align:left; vertical-align:top; font-size:1.25rem;" width="35%">
```SQL
SELECT naam
FROM klant
WHERE naam LIKE 'J%';
```
</td><td width="65%">
<table border="1">
  <thead>
    <tr>
      <th>naam</th>
    </tr>
  </thead>
  <tbody>
    <tr><td>Josette Soede</td></tr>
    <tr><td>Jolanda Budding-Doornbos</td></tr>
    <tr><td>Joanne Vlastuin</td></tr>
    <tr><td>Jolanda Knoop - Hoek</td></tr>
    <tr><td>Joost Nieuwboer</td></tr>
    <tr><td>Johan van Nierop</td></tr>
  </tbody>
</table>
</td></tr></table>





<table width="100%"><tr><td style="text-align:left; vertical-align:top; font-size:1.25rem;" width="35%">
Bijvoorbeeld, met de volgende query tonen we de pizza's met een naam die <i>begint met</i> '<b>Quattro</b>':
```SQL
SELECT naam
FROM pizza
WHERE naam LIKE 'Quattro%';
```
</td><td width="65%">
<table border="1">
  <thead>
    <tr>
      <th>naam</th>
    </tr>
  </thead>
  <tbody>
    <tr><td>Quattro formaggi</td></tr>
    <tr><td>Quattro stragioni</td></tr>
  </tbody>
</table>
</td></tr></table>



<table width="100%"><tr><td style="text-align:left; vertical-align:top; font-size:1.25rem;" width="35%">
Of die <i>eindigt op</i> '<b>arma</b>':
```SQL
SELECT naam
FROM pizza
WHERE naam LIKE '%arma';
```
</td><td width="65%">
<table border="1">
  <thead>
    <tr>
      <th>naam</th>
    </tr>
  </thead>
  <tbody>
    <tr><td>Shoarma</td></tr>
    <tr><td>Parma</td></tr>
  </tbody>
</table>
</td></tr></table>


<table width="100%"><tr><td style="text-align:left; vertical-align:top; font-size:1.25rem;" width="35%">
Of waarbij de letter '<b>e</b>' <i>erin voorkomt</i>:
```SQL
SELECT naam
FROM pizza
WHERE naam LIKE '%e%';
```
</td><td width="65%">
  <table border="1">
  <thead>
    <tr>
      <th>naam</th>
    </tr>
  </thead>
  <tbody>
    <tr><td>Margherita</td></tr>
    <tr><td>Napoletana</td></tr>
    <tr><td>Salame</td></tr>
    <tr><td>...</td></tr>
    <tr><td>Combinazione</td></tr>
  </tbody>
</table>

</td></tr></table>

### Verwerkingsopdracht 3.5.1 Alle pizza's waar de letter 'a' in voorkomt

<table width="100%"><tr><td style="text-align:left; vertical-align:top; font-size:1.25rem;" width="35%">

Toon een overzicht van alle pizza's waar de letter '<b>a</b>' in voorkomt:

</td><td width="65%">
    <table border="1">
  <thead>
    <tr>
      <th>naam</th>
    </tr>
  </thead>
  <tbody>
    <tr><td>Margherita</td></tr>
    <tr><td>Napoletana</td></tr>
    <tr><td>Salame</td></tr>
    <tr><td>...</td></tr>
    <tr><td>Combinazione</td></tr>
  </tbody>
</table>

</td></tr></table>

<p>Bekijk <a href="https://rweeda.github.io/PythonIA/docs/IA_sql_oplossingen.html#opgave351" target="_blank">hier</a> de voorbeelduitwerking.</p>
<!-- ANTWOORD:
<pre><code class="language-sql">
SELECT naam
FROM pizza
WHERE naam LIKE '%a%';
</code></pre>
-->


### Verwerkingsopdracht 3.5.2 Alle klanten met een mobiele telefoonnummer

<table width="100%"><tr><td style="text-align:left; vertical-align:top; font-size:1.25rem;" width="35%">
Toon een overzicht met <b>naam</b> en <b>telefoonnummer</b> van elk klant die een 06-nummer heeft opgegeven.
</td><td width="65%">
    <table border="1">
  <thead>
    <tr>
      <th>naam</th>
      <th>telefoon</th>
    </tr>
  </thead>
  <tbody>
    <tr><td>Hanneke Bolier</td><td>06-16915427</td></tr>
    <tr><td>Erika de Vries</td><td>06-79118502</td></tr>
    <tr><td>Josette Soede</td><td>06-56149758</td></tr>
    <tr><td>Antje van de Brink-Cromwi</td><td>06-17101504</td></tr>
    <tr><td>Neeltje Blankenstijn</td><td>06-51872409</td></tr>
    <tr><td>...</td><td>...</td></tr>
  </tbody>
</table>

</td></tr></table>




<p>Bekijk <a href="https://rweeda.github.io/PythonIA/docs/IA_sql_oplossingen.html#opgave352" target="_blank">hier</a> de voorbeelduitwerking.</p>
<!-- ANTWOORD:
<pre><code class="language-sql">
SELECT naam, telefoon
FROM klant
WHERE telefoon LIKE '06%';
</code></pre>
-->




## 3.6: Logische operator AND 
Je kunt de WHERE voorwaarde ook uitbreiden met de logische operatoren AND, OR, NOT of combinaties daarvan. 

Met<b>AND</b> (EN) moet aan <i>alle voorwaarden</i> worden voldaan om een resultaat te krijgen. 



<table width="100%"><tr><td style="text-align:left; vertical-align:top; font-size:1.25rem;" width="35%">
Bijvoorbeeld, met de volgende query tonen we alle klanten die in <b>Enschede</b> wonen en een naam hebben die met <b>'H' begint</b>:
```SQL
SELECT *
FROM klant
WHERE plaats = 'Enschede' AND naam LIKE 'H%';
```
</td><td width="65%">
<table border="1">
  <thead>
    <tr>
      <th>klantnummer</th>
      <th>wachtwoord</th>
      <th>naam</th>
      <th>adres</th>
      <th>postcode</th>
      <th>plaats</th>
      <th>telefoon</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>101</td>
      <td>uqOpgECQ_</td>
      <td>Hanneke Bolier</td>
      <td>Gladioolstraat 11</td>
      <td>3742TC</td>
      <td>Enschede</td>
      <td>06-169X5427</td>
    </tr>
    <tr>
      <td>209</td>
      <td>m1nbsrweOFJxu5</td>
      <td>Hermina de Pater</td>
      <td>Koekoeksbloemlaan 40</td>
      <td>3742EK</td>
      <td>Enschede</td>
      <td>06-6255X908</td>
    </tr>
    <tr>
      <td>221</td>
      <td>Qe4W6Xf70D_YlHR</td>
      <td>Heleen  van Harberden</td>
      <td>Acacialaan 27</td>
      <td>3741WB</td>
      <td>Enschede</td>
      <td>035-85X3955</td>
    </tr>
    <tr>
      <td>401</td>
      <td>dJiorsEkNLE</td>
      <td>Henrike Teeuw</td>
      <td>Dahliastraat 17</td>
      <td>3742RK</td>
      <td>Enschede</td>
      <td>035-8X94605</td>
    </tr>
  </tbody>
</table>

</td></tr></table>



### Verwerkingsopdracht 3.6.1 Pizza's tussen de 8,50 en 10euro

<table width="100%"><tr><td style="text-align:left; vertical-align:top; font-size:1.25rem;" width="35%">
Toon alle pizza's die tussen de €8,50 en €10,- kosten, zoals in het overzicht hiernaast.<br>
Tip: de basisprijs is meer dan 8,50 en minder dan 10 euro.
</td><td width="65%">
<table border="1">
  <thead>
    <tr>
      <th>naam</th>
      <th>basisprijs</th>
    </tr>
  </thead>
  <tbody>
    <tr><td>Calzone (dichte pizza)</td><td>9.0</td></tr>
    <tr><td>Marinara</td><td>8.5</td></tr>
    <tr><td>Mozzarella</td><td>8.5</td></tr>
    <tr><td>Quattro stragioni</td><td>8.5</td></tr>
    <tr><td>Americana</td><td>8.5</td></tr>
    <tr><td>...</td><td>...</td></tr>
    <tr><td>Specialità di Danilo</td><td>9.5</td></tr>
  </tbody>
</table>


</td></tr></table>


<p>Bekijk <a href="https://rweeda.github.io/PythonIA/docs/IA_sql_oplossingen.html#opgave361" target="_blank">hier</a> de voorbeelduitwerking.</p>
<!-- ANTWOORD:
<pre><code class="language-sql">
SELECT naam, basisprijs
FROM pizza
WHERE basisprijs>=8.50 AND basisprijs<=10;
</code></pre>
-->




## 3.7: Logische operator OR (OF)
Je kunt de WHERE voorwaarde ook uitbreiden met de logische operatoren AND, OR, NOT of combinaties daarvan. 


Met <b>OR</b> (OF) moet aan één van de voorwaarden voldaan worden.
<table width="100%">
 <tr><td style="text-align:left; vertical-align:top; font-size:1.25rem;" width="35%">
Bijvoorbeeld, de volgende query toont alle pizza's die met 'M' beginnen OF een basisprijs onder de 7 euro hebben:
```SQL
SELECT naam, basisprijs
FROM pizza
WHERE naam LIKE 'M%' OR basisprijs < 7;
```
   </td>
    <td width="65%">
<table border="1">
  <thead>
    <tr>
      <th>naam</th>
      <th>basisprijs</th>
    </tr>
  </thead>
  <tbody>
    <tr><td>Margherita</td><td>6.0</td></tr>
    <tr><td>Cippola</td><td>6.5</td></tr>
    <tr><td>Marinara</td><td>8.5</td></tr>
    <tr><td>Mozzarella</td><td>8.5</td></tr>
  </tbody>
</table>


 </td>
  </tr>
</table>




### Verwerkingsopdracht 3.7.1 Bestellingen met bestelcode

<table width="100%"><tr><td style="text-align:left; vertical-align:top; font-size:1.25rem;" width="35%">

<p>Toon alle informatie over zowel bestellingen bestelcode 13 <b>en</b> die met bestelcode 30, zoals hiernaast.</p>
</td><td width="65%">
<table border="1">
  <thead>
    <tr>
      <th>bestelcode</th>
      <th>datum</th>
      <th>bestel_tijd</th>
      <th>bezorg_tijd</th>
      <th>bezorgernummer</th>
      <th>klantnummer</th>
      <th>korting</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>13</td>
      <td>2021-12-03</td>
      <td>17:33:00</td>
      <td>17:48:00</td>
      <td>5</td>
      <td>279</td>
      <td>0.0</td>
    </tr>
    <tr>
      <td>30</td>
      <td>2021-12-05</td>
      <td>17:55:00</td>
      <td>18:11:00</td>
      <td>8</td>
      <td>376</td>
      <td>0.0</td>
    </tr>
  </tbody>
</table>



</td></tr></table>




<p>Bekijk <a href="https://rweeda.github.io/PythonIA/docs/IA_sql_oplossingen.html#opgave371" target="_blank">hier</a> de voorbeelduitwerking.</p>
<!-- ANTWOORD:
<pre><code class="language-sql">
SELECT *
FROM bestelling
WHERE bestelcode = 13 OR bestelcode = 30;
</code></pre>
-->




### Verwerkingsopdracht 3.7.2 Alle goedkope of gezonde pizza's

<table width="100%"><tr><td style="text-align:left; vertical-align:top; font-size:1.25rem;" width="35%">
Maak een overzicht van alle pizza's goedkoper zijn dan €7,50 <b>of</b> fruit bevatten.
</td><td width="65%">
    <table border="1">
  <thead>
    <tr>
      <th>pizzacode</th>
      <th>naam</th>
      <th>omschrijving</th>
      <th>basisprijs</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>1</td>
      <td>Margherita</td>
      <td>Tomaat,kaas en oregano</td>
      <td>6</td>
    </tr>
    <tr>
      <td>6</td>
      <td>Cippola</td>
      <td>Tomaat, kaas, uien en oregano</td>
      <td>6.5</td>
    </tr>
    <tr>
      <td>13</td>
      <td>Tropicale</td>
      <td>Tomaat, kaas en fruit cocktail</td>
      <td>8</td>
    </tr>
  </tbody>
</table>

</td></tr></table>




<p>Bekijk <a href="https://rweeda.github.io/PythonIA/docs/IA_sql_oplossingen.html#opgave372" target="_blank">hier</a> de voorbeelduitwerking.</p>
<!-- ANTWOORD:
<pre><code class="language-sql">
SELECT *
FROM pizza
WHERE basisprijs<7.50 OR omschrijving LIKE '%fruit%';
</code></pre>
-->





## 3.8: Logische operator NOT
Met <b>NOT</b> (NIET) mag er aan géén van de voorwaarden voldaan worden.

<table width="100%"><tr><td style="text-align:left; vertical-align:top; font-size:1.25rem;" width="35%">
Bijvoorbeeld, alle klanten die <b>niet</b> in Hengelo wonen:
```SQL
SELECT *
FROM klant
WHERE NOT woonplaats = 'Hengelo';
```
</td><td width="65%">
<table border="1">
  <thead>
    <tr>
      <th>klantnummer</th>
      <th>wachtwoord</th>
      <th>naam</th>
      <th>adres</th>
      <th>postcode</th>
      <th>woonplaats</th>
      <th>telefoon</th>
    </tr>
  </thead>
  <tbody>
    <tr><td>101</td><td>uqOpgECQ_</td><td>Hanneke Bolier</td><td>Gladioolstraat 11</td><td>3742TC</td><td>Enschede</td><td>06-16915427</td></tr>
    <tr><td>103</td><td>id4m9g2_PHp10t</td><td>Erika de Vries</td><td>Banckertlaan 7</td><td>3742MG</td><td>Enschede</td><td>06-79118502</td></tr>
    <tr><td>104</td><td>84t9TPLOZKZ</td><td>Nelleke op den Brouw</td><td>Talmalaan 11</td><td>3741T2</td><td>Enschede</td><td>035-6014464</td></tr>
    <tr><td>...</td><td>...</td><td>...</td><td>...</td><td>...</td><td>...</td><td>...</td></tr>
  </tbody>
</table>

</td></tr></table>


<table width="100%"><tr><td style="text-align:left; vertical-align:top; font-size:1.25rem;" width="35%">
Of bijvoorbeeld, alle pizza's waarbij de letter 'e' er <b>niet</b> in voorkomt:
```SQL
SELECT naam
FROM pizza
WHERE naam NOT LIKE '%e%';
```
</td><td width="65%">
<table border="1">
  <thead>
    <tr>
      <th>naam</th>
    </tr>
  </thead>
  <tbody>
    <tr><td>Prosciutto</td></tr>
    <tr><td>Funghi</td></tr>
    <tr><td>Cippola</td></tr>
    <tr><td>Hawai</td></tr>
    <tr><td>...</td></tr>
  </tbody>
</table>

</td></tr></table>


### Verwerkingsopdracht 3.8.1 Alle pizza's zonder kip

<table width="100%"><tr><td style="text-align:left; vertical-align:top; font-size:1.25rem;" width="35%">
Toon een overzicht van alle pizza's waar <b>geen</b> kip op zit, dus ook geen kipfilet, zoals in het voorbeeld hieronder.

</td><td width="65%">
    | pizzanaam   | omschrijving                                                       |
|-------------|---------------------------------------------------------------------|
| Margherita  | Tomaat, kaas en oregano                                            |
| Napoletana  | Tomaat, kaas, ansjovis, olijven, kappertjes en oregano            |
| Prosciutto  | Tomaat, kaas, ham en oregano                                       |
| Funghi      | Tomaat, kaas, champignons en oregano                               |
| Salame      | Tomaat, kaas, salami en oregano                                    |



</td></tr></table>



<p>Bekijk <a href="https://rweeda.github.io/PythonIA/docs/IA_sql_oplossingen.html#opgave381" target="_blank">hier</a> de voorbeelduitwerking.</p>
<!-- ANTWOORD:
<pre><code class="language-sql"> 
SELECT naam AS pizzanaam, omschrijving
FROM pizza
WHERE omschrijving NOT LIKE '%kip%';
</code></pre>
ook goed:
<pre><code class="language-sql"> 
ANTWOORD: 
SELECT naam, omschrijving
FROM pizza
WHERE NOT omschrijving LIKE '%kip%';
</code></pre>
-->




## 3.9: Meerdere logische operatoren combineren
Je kunt meerdere operatoren combineren. Als je verschillende AND, OR en NOT combineert moet je gebruik maken van haakjes voor de gewenste uitkomst.


<table width="100%"><tr><td style="text-align:left; vertical-align:top; font-size:1.25rem;" width="35%">
Bijvoorbeeld, met de volgende query tonen we de pizza's die tussen de €8,50 <b>en</b> €10,- kosten, <b>of</b> pizza's die geen <b>salami</b> bevatten:
```SQL
SELECT naam, omschrijving, basisprijs
FROM pizza
WHERE (basisprijs>=8.50 AND basisprijs<=10) OR NOT omschrijving LIKE '%salami%';
```
</td><td width="65%">
<table border="1">
  <thead>
    <tr>
      <th>naam</th>
      <th>omschrijving</th>
      <th>basisprijs</th>
    </tr>
  </thead>
  <tbody>
    <tr><td>Margherita</td><td>Tomaat,kaas en oregano</td><td>6.0</td></tr>
    <tr><td>Napoletana</td><td>Tomaat, kaas, ansjovis, olijven, kappertjes en oregano</td><td>7.5</td></tr>
    <tr><td>Prosciutto</td><td>Tomaat, kaas, ham en oregano</td><td>7.5</td></tr>
    <tr><td>Funghi</td><td>Tomaat, kaas, champignons en oregano</td><td>7.5</td></tr>
    <tr><td>...</td><td>...</td><td>...</td></tr>
  </tbody>
</table>

</td></tr></table>


### Verwerkingsopdracht opdracht 3.9.1 Alle pizza's zonder paprika en zonder ui


<table width="100%"><tr><td style="text-align:left; vertical-align:top; font-size:1.25rem;" width="35%">

Luna wil een overzicht van alle pizza's waar <b>geen</b> paprika op zit, maar ook geen <b>ui</b>. 
Ze schrijft daarvoor de volgende query, maar er zitten een paar fouten in. Kan jij het aanpassen zodat de juiste overzicht gegeven wordt, zoals hiernaast?<b>



Tip: Gebruik eventueel commentaar '--' om een deel van je code te verbergen zodat je kunt kijken welke delen wel en niet goed werken.
</td><td width="65%">
   | naam        | omschrijving                                                       |
|-------------|---------------------------------------------------------------------|
| Margherita  | Tomaat, kaas en oregano                                            |
| Napoletana  | Tomaat, kaas, ansjovis, olijven, kappertjes en oregano            |
| Prosciutto  | Tomaat, kaas, ham en oregano                                       |
| Funghi      | Tomaat, kaas, champignons en oregano                               |
| Salame      | Tomaat, kaas, salami en oregano                                    |
 
</td></tr></table>




SELECT naam, omschrijving
FROM pizza
WHERE omschrijving NOT LIKE 'paprika' OR 'uien';




<p>Bekijk <a href="https://rweeda.github.io/PythonIA/docs/IA_sql_oplossingen.html#opgave391" target="_blank">hier</a> de voorbeelduitwerking.</p>
<!-- ANTWOORD:
				<pre><code class="language-sql">
SELECT naam, omschrijving
FROM pizza
WHERE NOT (omschrijving LIKE '%paprika%' OR omschrijving LIKE '%ui%');
</code></pre>																								
Ook goed:							   
<pre><code class="language-sql">
SELECT naam, omschrijving
FROM pizza
WHERE omschrijving NOT LIKE '%paprika%' AND omschrijving NOT LIKE '%ui%';
</code></pre>
-->




### Verwerkingsopdracht 3.9.2 Toon pizza's die voldoen aan meerdere voorwaarden
<table width="100%"><tr><td style="text-align:left; vertical-align:top; font-size:1.25rem;" width="35%">
Toon alle pizza's die minder dan €7,50 kosten, <b>en</b> met de letter 'M' beginnen <b>of</b> letter 'A' eindigen. 

</td><td width="65%">
    <table border="1">
  <thead>
    <tr>
      <th>pizzacode</th>
      <th>naam</th>
      <th>omschrijving</th>
      <th>basisprijs</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>1</td>
      <td>Margherita</td>
      <td>Tomaat,kaas en oregano</td>
      <td>6</td>
    </tr>
    <tr>
      <td>6</td>
      <td>Cippola</td>
      <td>Tomaat, kaas, uien en oregano</td>
      <td>6.5</td>
    </tr>
  </tbody>
</table>

</td></tr></table>


<p>Bekijk <a href="https://rweeda.github.io/PythonIA/docs/IA_sql_oplossingen.html#opgave392" target="_blank">hier</a> de voorbeelduitwerking.</p>
<!-- ANTWOORD:
<pre><code class="language-sql">
SELECT *
FROM pizza
WHERE basisprijs < 7.5 AND (naam LIKE 'M%' OR naam LIKE '%A');
</code></pre>
-->



<!--
## 3.10: Groepsfuncties

In de volgende paragraven leer je hoe je met SQL berekeningen en samenvattingen kunt maken op gegevens in een kolom. Je leert deWe behandelen de volgende functies:

- `MIN()`
- `MAX()`
- `SUM()`
- `AVG()`
- `COUNT(*)`
- `DISTINCT`
-->

## 3.10: `DISTINCT` – Unieke waarden selecteren

Stel dat je alle woonplaatsen wilt zien van de tabel <i>klant</i>.


| plaats     |
|------------|
| Enschede   |
| Enschede   |
| Enschede   |
| Enschede   |
| Hengelo    |
| Enschede   |
| Enschede   |
| ...        |


<p>Je ziet dat er dubbele waarden te zien zijn. Om te voorkomen dat er dubbele waarden worden getoond, kun je DISTINCT gebruiken.</p>
 
<p>Met <code>DISTINCT kolom</code> toon je alleen <b>verschillende (unieke)</b> waarden uit een kolom. </p>


<table width="100%"><tr><td style="text-align:left; vertical-align:top; font-size:1.25rem;" width="35%">

Bijvoorbeeld: alle verschillende plaatsen waar klanten wonen.

```sql
SELECT DISTINCT plaats
FROM klant;
```
</td><td width="65%">

<table border="1">
  <thead>
    <tr>
      <th>plaats</th>
    </tr>
  </thead>
  <tbody>
    <tr><td>Enschede</td></tr>
    <tr><td>Hengelo</td></tr>
  </tbody>
</table>

</td></tr></table>


### Verwerkingsopdracht 3.10.1 Unieke bezorgdatums

<table width="100%"><tr><td style="text-align:left; vertical-align:top; font-size:1.25rem;" width="35%">
Toon alle unieke bezorgdatums in de tabel <i>bestelling</i>.
</td><td width="65%">
  <table border="1">
  <thead>
    <tr>
      <th>bestel_datum</th>
    </tr>
  </thead>
  <tbody>
    <tr><td>2021-12-01</td></tr>
    <tr><td>2021-12-02</td></tr>
    <tr><td>2021-12-03</td></tr>
    <tr><td>2021-12-04</td></tr>
    <tr><td>2021-12-05</td></tr>
    <tr><td>...</td></tr>
    <tr><td>2022-03-03</td></tr>
  </tbody>
</table>

</td></tr></table>



<p>Bekijk <a
href="https://rweeda.github.io/PythonIA/docs/IA_sql_oplossingen.html#opgave231"
target="_blank">hier</a> de voorbeelduitwerking.</p>

<pre><code class="language-sql">
SELECT DISTINCT bestel_datum
FROM bestelling;
</code></pre>



## 3.11: COUNT(*) – Aantal rijen tellen

`COUNT(*)` telt **het aantal rijen** in een tabel.  


<table width="100%"><tr><td style="text-align:left; vertical-align:top; font-size:1.25rem;" width="35%">
Bijvoorbeeld, het aantal bestelling die zijn geplaatst:
```sql
SELECT COUNT(*)
FROM bestelling;
```
</td><td width="65%">
<table border="1">
  <thead>
    <tr>
      <th>COUNT(*)</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>1472</td>
    </tr>
  </tbody>
</table>

</td></tr></table>



### Verwerkingsopdracht 3.11.1

<table width="100%"><tr><td style="text-align:left; vertical-align:top; font-size:1.25rem;" width="35%">
Hoeveel pizza's staan er in de tabel <i>besteldePizza</i>? Maak het overzicht zoals hiernaast.
</td><td width="65%">
    <table border="1">
  <thead>
    <tr>
      <th>aantal_pizzas</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>5833</td>
    </tr>
  </tbody>
</table>

</td></tr></table>

<!--
<pre><code class="language-sql">
SELECT COUNT(*) AS aantal_pizzas
FROM besteldePizza;
</code></pre>
-->
<p>Bekijk <a
href="https://rweeda.github.io/PythonIA/docs/IA_sql_oplossingen.html#opgave231"
target="_blank">hier</a> de voorbeelduitwerking.</p>

## 3.12: COUNT(DISTINCT kolomnaam) – Aantal unieke rijen tellen

<p>Wil je alleen unieke waarden tellen? Dan gebruik je <code>COUNT(DISTINCT kolom)</code>.</p>

<table width="100%"><tr><td style="text-align:left; vertical-align:top; font-size:1.25rem;" width="35%">
Bijvoorbeeld, het aantal klanten die een bestelling hebben geplaatst:
```SQL
SELECT COUNT(DISTINCT klantnummer)
FROM bestelling;
```
</td><td width="65%">

<table border="1">
  <thead>
    <tr>
      <th>COUNT(DISTINCT klantnummer)</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>122</td>
    </tr>
  </tbody>
</table>

</td></tr></table>




### Verwerkingsopdracht 3.12.1

<table width="100%"><tr><td style="text-align:left; vertical-align:top; font-size:1.25rem;" width="35%">
Hoeveel verschillende (unieke) <b>pizzacode</b>'s staan er in de tabel <i>besteldePizza</i>? Maak het overzicht zoals hiernaast.
</td><td width="65%">
    <table border="1">
  <thead>
    <tr>
      <th>aantal_pizzas</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>36</td>
    </tr>
  </tbody>
</table>

</td></tr></table>

<p>Bekijk <a
href="https://rweeda.github.io/PythonIA/docs/IA_sql_oplossingen.html#opgave231"
target="_blank">hier</a> de voorbeelduitwerking.</p>
<!--
<pre><code class="language-sql">
SELECT COUNT(DISTINCT pizzacode) AS aantal_pizzas
FROM besteldePizza;
</code></pre>
-->

## 3.13: MIN() – Laagste waarde

`MIN(kolom)` geeft de **laagste waarde** (minimum) in een kolom terug. <br> 


<table width="100%"><tr><td style="text-align:left; vertical-align:top; font-size:1.25rem;" width="35%">

Bijvoorbeeld: Toon de goedkoopste pizza.

```sql
SELECT MIN(basisprijs) AS goedkoopste_pizza
FROM pizza;
```

</td><td width="65%">
| goedkoopste_pizza |
|-------------------|
| 6              |
</td></tr></table>


### Verwerkingsopdracht 3.13.1 Vroegste bezorging

<table width="100%"><tr><td style="text-align:left; vertical-align:top; font-size:1.25rem;" width="35%">
Toon de vroegste <b>bezorg_tijd</b> in de tabel <i>bestelling</i>.

</td><td width="65%">
    <table border="1">
  <thead>
    <tr>
      <th>vroegste_bezorging</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>17:47:00</td>
    </tr>
  </tbody>
</table>

</td></tr></table>




<p>Bekijk <a
href="https://rweeda.github.io/PythonIA/docs/IA_sql_oplossingen.html#opgave231"
target="_blank">hier</a> de voorbeelduitwerking.</p>
 <!-- ANTWOORD:
SELECT MIN(bezorg_tijd) AS vroegste_bezorging
FROM bestelling;
</code></pre> -->

## 3.14: MAX() – Hoogste waarde


`MAX(kolom)` geeft de **hoogste waarde** (maximum) in een kolom terug.  


<table width="100%"><tr><td style="text-align:left; vertical-align:top; font-size:1.25rem;" width="35%">

Bijvoorbeeld: de duurste pizza.
```sql
SELECT MAX(basisprijs) AS duurste_pizza
FROM pizza;
```

</td><td width="65%">
  
<table border="1">
  <thead>
    <tr>
      <th>duurste_pizza</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>10.5</td>
    </tr>
  </tbody>
</table>

</td></tr></table>

### Verwerkingsopdracht 3.14.1 Duurste bodem

<table width="100%"><tr><td style="text-align:left; vertical-align:top; font-size:1.25rem;" width="35%">
Wat is de hoogste <b>plusprijs</b> voor een pizzabodem? Gebruik de tabel <i>bodem</i> Maak het overzicht zoals hiernaast.

</td><td width="65%">
    <table border="1">
  <thead>
    <tr>
      <th>hoogste_toeslag</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>1</td>
    </tr>
  </tbody>
</table>

</td></tr></table>


<p>Bekijk <a
href="https://rweeda.github.io/PythonIA/docs/IA_sql_oplossingen.html#opgave231"
target="_blank">hier</a> de voorbeelduitwerking.</p>
 <!-- ANTWOORD:
<pre><code class="language-sql"> 
SELECT MAX(plusprijs) AS hoogste_toeslag
FROM bodem;
</code></pre> -->


## 3.15: SUM() – Totaal optellen


`SUM(kolom)` telt **alle waarden in een kolom op**.  


<table width="100%"><tr><td style="text-align:left; vertical-align:top; font-size:1.25rem;" width="35%">

Bijvoorbeeld: de totale waarde van alle pizza’s samen.

```sql
SELECT SUM(basisprijs) AS totaal_waarde
FROM pizza;
```
</td><td width="65%">


| totaal_waarde |
|---------------|
| 293.5         |
</td></tr></table>



### Verwerkingsopdracht 3.15.1

<table width="100%"><tr><td style="text-align:left; vertical-align:top; font-size:1.25rem;" width="35%">
Bereken de totale korting van alle bestellingen in de tabel <i>bestelling</i>. Maak een overzicht zoals hiernaast.

</td><td width="65%">
    <table border="1">
  <thead>
    <tr>
      <th>totaal_korting</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>40</td>
    </tr>
  </tbody>
</table>

</td></tr></table>



<p>Bekijk <a
href="https://rweeda.github.io/PythonIA/docs/IA_sql_oplossingen.html#opgave231"
target="_blank">hier</a> de voorbeelduitwerking.</p>
 <!-- ANTWOORD:
<pre><code class="language-sql"> 
SELECT SUM(korting) AS totaal_korting
FROM bestelling;
</code></pre>
-->


## 3.16: AVG() – Gemiddelde van een kolom

`AVG(kolom)` geeft het **gemiddelde** van de waarden in een kolom.  


<table width="100%"><tr><td style="text-align:left; vertical-align:top; font-size:1.25rem;" width="35%">

Bijvoorbeeld: de gemiddelde prijs van een pizza.


```sql
SELECT AVG(basisprijs) AS gemiddelde_pizza_prijs
FROM pizza;
```
</td><td width="65%">

<table border="1">
  <thead>
    <tr>
      <th>gemiddelde_pizza_prijs</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>8.15277777779</td>
    </tr>
  </tbody>
</table>

</td></tr></table>

### Verwerkingsopdracht 3.16.1 Gemiddelde toeslag

<table width="100%"><tr><td style="text-align:left; vertical-align:top; font-size:1.25rem;" width="35%">
Bereken de gemiddelde toeslag voor bodems in de tabel<i>bodem</i>.
</td><td width="65%">
    <table border="1">
  <thead>
    <tr>
      <th>gemiddelde_bodem_toeslag</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>0.25</td>
    </tr>
  </tbody>
</table>

</td></tr></table>






<p>Bekijk <a
href="https://rweeda.github.io/PythonIA/docs/IA_sql_oplossingen.html#opgave231"
target="_blank">hier</a> de voorbeelduitwerking.</p>
 <!-- ANTWOORD:
<pre><code class="language-sql"> 
SELECT AVG(plusprijs) AS gemiddelde_bodem_toeslag
FROM bodem;
 </code></pre>


### 3.17: Afsluitende Opdrachten


### Afsluitende Opdracht 3.17.1 Menu

<table width="100%"><tr><td style="text-align:left; vertical-align:top; font-size:1.25rem;" width="35%">
Toon van alle pizza's de omschrijving en de naam (in die volgorde).
</td><td width="65%">
    <table border="1">
  <thead>
    <tr>
      <th>omschrijving</th>
      <th>naam</th>
    </tr>
  </thead>
  <tbody>
    <tr><td>Tomaat,kaas en oregano</td><td>Margherita</td></tr>
    <tr><td>Tomaat, kaas, ansjovis, olijven, kappertjes en oregano</td><td>Napoletana</td></tr>
    <tr><td>Tomaat, kaas, ham en oregano</td><td>Prosciutto</td></tr>
    <tr><td>Tomaat, kaas, champignons en oregano</td><td>Funghi</td></tr>
    <tr><td>Tomaat, kaas, salami en oregano</td><td>Salame</td></tr>
    <tr><td>...</td><td>...</td></tr>
    <tr><td>Eigen keuze pizza</td><td>Combinazione</td></tr>
  </tbody>
</table>

</td></tr></table>




<p>Bekijk <a href="https://rweeda.github.io/PythonIA/docs/IA_sql_oplossingen.html#opgave313" target="_blank">hier</a> de voorbeelduitwerking.</p>
<!-- ANTWOORD:
<pre><code class="language-sql">
SELECT omschrijving, naam
FROM pizza;
</code></pre>
-->


### Afsluitende Opdracht 3.14.2 Alle goedkope pizza's met een 'C'

<table width="100%"><tr><td style="text-align:left; vertical-align:top; font-size:1.25rem;" width="35%">

Toon een overzicht van alle pizza's waarvan de naam met 'C' begint maar niet meer kost dan 8 euro.

</td><td width="65%">
    
<table border="1">
  <thead>
    <tr>
      <th>naam</th>
    </tr>
  </thead>
  <tbody>
    <tr><td>Cippola</td></tr>
    <tr><td>Calimero</td></tr>
    <tr><td>Capricciosa</td></tr>
  </tbody>
</table>


</td></tr></table>



<p>Bekijk <a href="https://rweeda.github.io/PythonIA/docs/IA_sql_oplossingen.html#opgave313" target="_blank">hier</a> de voorbeelduitwerking.</p>
<!-- ANTWOORD:
<pre><code class="language-sql">
SELECT naam
FROM pizza
WHERE naam LIKE 'C%' AND basisprijs <= 8.0;
</code></pre>
-->


### Afsluitende Opdracht 3.17.3

<table width="100%"><tr><td style="text-align:left; vertical-align:top; font-size:1.25rem;" width="35%">

Toon een overzicht zoals hiernaast van alle pizza's met een basisprijs van minimaal €9,00 <b>én</b> die het woord 'salami' in de omschrijving bevatten.


</td><td width="65%">
    | naam                   | basisprijs |
| ---------------------- | ---------- |
| Calzone (dichte pizza) | 9.0        |
| Fantasia               | 9.0        |
| Specialità di Danilo   | 9.5        |
</td></tr></table>




<p>Bekijk <a href="https://rweeda.github.io/PythonIA/docs/IA_sql_oplossingen.html#opgave3173" target="_blank">hier</a> de voorbeelduitwerking.</p>
<!-- ANTWOORD:
<pre><code class="language-sql">
SELECT naam, basisprijs
FROM pizza
WHERE basisprijs >= 9
  AND omschrijving LIKE '%salami%';
</code></pre>
-->

### Afsluitende Opdracht 3.17.4 Toon 3 pizza’s zonder vlees, met een ‘a’ in de naam

<table width="100%"><tr><td style="text-align:left; vertical-align:top; font-size:1.25rem;" width="35%">
Toon de eerste drie pizza’s (alfabetisch op naam) die <b>geen</b> vlees (ham, salami, kip) bevatten <b>en</b> een ‘a’ in de naam hebben. Toon de kolommen <b>naam</b> en <b>omschrijving</b>.
</td><td width="65%">
    <table border="1">
  <thead>
    <tr>
      <th>naam</th>
      <th>omschrijving</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Cippola</td>
      <td>Tomaat, kaas, uien en oregano</td>
    </tr>
    <tr>
      <td>Combinazione</td>
      <td>Eigen keuze pizza</td>
    </tr>
    <tr>
      <td>Margherita</td>
      <td>Tomaat,kaas en oregano</td>
    </tr>
  </tbody>
</table>

</td></tr></table>




<p>Bekijk <a href="https://rweeda.github.io/PythonIA/docs/IA_sql_oplossingen.html#opgave3174" target="_blank">hier</a> de voorbeelduitwerking.</p>

<!-- ANTWOORD:
<pre><code class="language-sql">
SELECT naam, omschrijving
FROM pizza
WHERE omschrijving NOT LIKE '%ham%'
  AND omschrijving NOT LIKE '%salami%'
  AND omschrijving NOT LIKE '%kip%'
  AND naam LIKE '%a%'
ORDER BY naam
LIMIT 3;
</code></pre>
-->


### Afsluitende Opdracht 3.17.5 Klanten buiten Enschede met 06-nummer
<table width="100%"><tr><td style="text-align:left; vertical-align:top; font-size:1.25rem;" width="35%">

Tel het aantal klanten die een mobiel nummer (06) hebben maar <b>niet</b> in Enschede wonen. Noem de kolom zoals in het voorbeeld hiernaast.
</td><td width="65%">
<table border="1">
  <thead>
    <tr>
      <th>aantal_klanten</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>25</td>
    </tr>
  </tbody>
</table>
</td></tr></table>



<p>Bekijk <a href="https://rweeda.github.io/PythonIA/docs/IA_sql_oplossingen.html#opgave3175" target="_blank">hier</a> de voorbeelduitwerking.</p>
<!-- ANTWOORD:
<pre><code class="language-sql">
SELECT COUNT(*) AS aantal_klanten
FROM klant
WHERE telefoon LIKE '06%' 
  AND woonplaats <> 'Enschede';
</code></pre>
Ook goed:
<pre><code class="language-sql">
SELECT COUNT(*) AS aantal_klanten
FROM klant
WHERE telefoon LIKE '06%' 
  AND NOT woonplaats = 'Enschede';
</code></pre>
-->


### Afsluitende Opdracht 3.17.6 Pizza’s met ‘special’ of duurder dan €10
<table width="100%"><tr><td style="text-align:left; vertical-align:top; font-size:1.25rem;" width="35%">
Toon de namen van alle pizza’s waarvan de omschrijving het woord 'special' bevat, <b>óf</b> die duurder zijn dan €9,00.

</td><td width="65%">
    <table border="1">
  <thead>
    <tr>
      <th>naam</th>
    </tr>
  </thead>
  <tbody>
      <tr>
      <td>Specialità di Danilo</td>
    </tr>
    <tr>
      <td>Combinazione</td>
    </tr>
  </tbody>
</table>

</td></tr></table>


<p>Bekijk <a href="https://rweeda.github.io/PythonIA/docs/IA_sql_oplossingen.html#opgave3176" target="_blank">hier</a> de voorbeelduitwerking.</p>
<!-- ANTWOORD:
<pre><code class="language-sql">
SELECT naam
FROM pizza
WHERE omschrijving LIKE '%special%'
   OR basisprijs > 9;
</code></pre>
-->

### Afsluitende Opdracht 3.17.7 Bezorgers met naam H maar die NIET met J begint
<table width="100%"><tr><td style="text-align:left; vertical-align:top; font-size:1.25rem;" width="35%">
Toon de namen van de bezorgers met de letter 'H' in hun naam naar <b>niet</b> met de letter 'J' beginnen. Noem de kolom <i>bezorgernaam</i>. Sorteer de namen van hoog naar laag.

</td><td width="65%">
<table border="1">
  <thead>
    <tr>
      <th>bezorgernaam</th>
    </tr>
  </thead>
  <tbody>
    <tr><td>Marleen Hoekstra</td></tr>
    <tr><td>Herman Prent</td></tr>
    <tr><td>Hans Boonstra</td></tr>
    <tr><td>Han Fröling</td></tr>
    <tr><td>Eric Henze</td></tr>
    <tr><td>Ageeth Mooy</td></tr>
    <tr><td>Afhalen</td></tr>
  </tbody>
</table>
</td></tr></table>


<p>Bekijk <a href="https://rweeda.github.io/PythonIA/docs/IA_sql_oplossingen.html#opgave3177" target="_blank">hier</a> de voorbeelduitwerking.</p>
<!-- ANTWOORD:
<pre><code class="language-sql">
SELECT naam AS bezorgernaam
FROM bezorger
WHERE naam LIKE '%H%' AND naam NOT LIKE 'J%'
ORDER BY naam DESC;
</code></pre>
-->

### Afsluitende Opdracht 3.17.8 Totaal aantal bestelde pizza's
<table width="100%"><tr><td style="text-align:left; vertical-align:top; font-size:1.25rem;" width="35%">
Toon het totaal aantal bestelde pizza's, zoals hiernaast. De gegevens komen uit tabel <i>besteldePizza</i>.

</td><td width="65%">
<table border="1">
  <thead>
    <tr>
      <th>aantal_bestelde_pizzas</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>9757</td>
    </tr>
  </tbody>
</table>

</td></tr></table>

<p>Bekijk <a href="https://rweeda.github.io/PythonIA/docs/IA_sql_oplossingen.html#opgave3178" target="_blank">hier</a> de voorbeelduitwerking.</p>
<!-- ANTWOORD:
<pre><code class="language-sql">
SELECT SUM(aantal) AS aantal_bestelde_pizzas
FROM besteldePizza
</code></pre>
-->