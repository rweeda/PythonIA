## ONDERWERP 6







## Volgorde van commando's voor het ophalen van informatie
<p>In dit onderwerp leer je twee nieuwe commando's: GROUP BY en HAVING.</p>
<p>Er zijn zeven commando's die je kunt gebruken om informatie op te halen. De commando’s zijn:</p>


<p><img
src="https://raw.githubusercontent.com/rweeda/PythonIA/main/sql/img/H1_commandos.png"
alt="Commando's voor het ophalen van informatie" width="600"></p>

<p>
Je hoeft niet alle commando's te gebruiken, maar ze staan wel <b>altijd in
deze volgorde</b>.</p>


### Verwerkingsopdracht 4.1.1 Volgorde van onderdelen

Zet de onderdelen van een SQL-query in de juiste volgorde:
FROM – HAVING - ORDER BY – LIMIT - GROUP BY - SELECT – WHERE

<p>Bekijk <a href="https://rweeda.github.io/PythonIA/docs/IA_sql_oplossingen.html#opgave411" target="_blank">hier</a> de voorbeelduitwerking.</p>
<!-- ANTWOORD:
SELECT
FROM
WHERE
ORDER BY
LIMIT
-->


# GROUP BY

<p>
GROUP BY groepeert rijen die dezelfde waarde hebben in één of meer kolommen. Daarna kun je functies zoals COUNT(), SUM(), AVG()  MAX() of MIN() (deze heb je in <a href="https://moodle.informatica-actief.nl/course/view.php?id=1193#section-7">onderwerp 4</a> geleerd) <b>per groep</b> toepassen, in plaats van op de hele tabel. Tussen haakjes geef je aan op welk kolom de functie moet worden toegepast.<br>

Bij GROUP BY staat vaak in de vraag het wordt 'per'. Bijvoorbeeld, hoeveel 'per' bestelling, of 'per klant'.
</p>

<table width="100%"><tr><td style="text-align:left; vertical-align:top; font-size:1.25rem;" width="35%">

Voorbeeld. De query hieronder geeft een overzicht van het aantal keer dat elk bodem besteld is. Het groepeert alle <b>bodemcode</b>, en telt dan met COUNT hoe vaak elke bodemcode is besteld:

```SQL
SELECT bodemcode, COUNT(aantal) AS aantal_besteld
FROM besteldepizza
GROUP BY bodemcode;
```
</td><td width="65%">

<table border="1">
  <thead>
    <tr>
      <th>bodemcode</th>
      <th>aantal_besteld</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>1</td>
      <td>2788</td>
    </tr>
    <tr>
      <td>2</td>
      <td>2905</td>
    </tr>
    <tr>
      <td>3</td>
      <td>140</td>
    </tr>
  </tbody>
</table>

</td></tr></table>


<table width="100%"><tr><td style="text-align:left; vertical-align:top; font-size:1.25rem;" width="35%">
Voorbeeld. De query hieronder geeft een overzicht van het totaal aantal bestelling per pizza. Deze groepeert <b>pizzacode</b>, en telt dan met SUM alle aantallen bij elkaar op.
```SQL
SELECT pizzacode, SUM(aantal) AS totaal_besteld
FROM besteldePizza
GROUP BY pizzacode;
```
</td><td width="65%">

<table border="1">
  <thead>
    <tr>
      <th>pizzacode</th>
      <th>totaal_besteld</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>1</td>
      <td>315</td>
    </tr>
    <tr>
      <td>2</td>
      <td>284</td>
    </tr>
    <tr>
      <td>3</td>
      <td>224</td>
    </tr>
    <tr>
      <td colspan="2" style="text-align:center;">…</td>
    </tr>
  </tbody>
</table>

</td></tr></table>











### Verwerkingsopdracht Bestelde pizzasoorten


<table width="100%"><tr><td style="text-align:left; vertical-align:top; font-size:1.25rem;" width="35%">
<p>Toon van elk soort pizza (<b>pizzacode</b>) hoeveel er gemiddeld gelijktijdig besteld worden, zoals in het overzicht hiernaast. De gegevens komen uit tabel <i>besteldepizza</i>.


</td><td width="65%">
<table border="1">
  <thead>
    <tr>
      <th>pizzacode</th>
      <th>gemiddeld_aantal</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>1</td>
      <td>1.7119565217391304</td>
    </tr>
    <tr>
      <td>2</td>
      <td>1.7423312883435582</td>
    </tr>
    <tr>
      <td>3</td>
      <td>1.6115107913669064</td>
    </tr>
    <tr>
      <td>4</td>
      <td>1.7692307692307692</td>
    </tr>
    <tr>
      <td>5</td>
      <td>1.5813953488372092</td>
    </tr>
    <tr>
      <td colspan="2" style="text-align:center;">...</td>
    </tr>
  </tbody>
</table>

</td></tr></table>


<p>Bekijk <a
href="https://rweeda.github.io/PythonIA/docs/IA_sql_oplossingen.html#opgave491"
target="_blank">hier</a> de voorbeelduitwerking.</p>
 <!-- ANTWOORD:
<pre><code class="language-sql"> 
SELECT pizzacode, AVG(aantal) AS gemiddeld_aantal
FROM besteldepizza
GROUP BY pizzacode;
</code></pre>
-->





### Verwerkingsopdracht Aantal bestellingen per bodemcode


<table width="100%"><tr><td style="text-align:left; vertical-align:top; font-size:1.25rem;" width="35%">
<p>Tel het aantal bestellingen per bodemcode, zoals in het overzicht hiernaast. De gegevens komen uit tabel <i>besteldepizza</i>.</p>

</td><td width="65%">
<table border="1">
  <thead>
    <tr>
      <th>bodemcode</th>
      <th>aantal_besteld</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>1</td>
      <td>2788</td>
    </tr>
    <tr>
      <td>2</td>
      <td>2905</td>
    </tr>
    <tr>
      <td>3</td>
      <td>140</td>
    </tr>
  </tbody>
</table>

</td></tr></table>


<p>Bekijk <a
href="https://rweeda.github.io/PythonIA/docs/IA_sql_oplossingen.html#opgave491"
target="_blank">hier</a> de voorbeelduitwerking.</p>
 <!-- ANTWOORD:
<pre><code class="language-sql"> 
SELECT bodemcode, COUNT(*) 
FROM besteldepizza 
GROUP BY bodemcode;
</code></pre>
-->



### Verwerkingsopdracht Meest pizza's van één soort

<table width="100%"><tr><td style="text-align:left; vertical-align:top; font-size:1.25rem;" width="35%">
<p>Toon een overzicht van het grootst aantal pizza’s van één soort per bestelling (<b>bestelcode</b>), zoals hiernaast.</p>

</td><td width="65%">
<table border="1">
  <thead>
    <tr>
      <th>bestelcode</th>
      <th>max_aantal</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>1</td>
      <td>1</td>
    </tr>
    <tr>
      <td>2</td>
      <td>3</td>
    </tr>
    <tr>
      <td>3</td>
      <td>2</td>
    </tr>
    <tr>
      <td colspan="2" style="text-align:center;">...</td>
    </tr>
  </tbody>
</table>

</td></tr></table>


<p>Bekijk <a
href="https://rweeda.github.io/PythonIA/docs/IA_sql_oplossingen.html#opgave491"
target="_blank">hier</a> de voorbeelduitwerking.</p>
 <!-- ANTWOORD:
<pre><code class="language-sql">
SELECT bestelcode, MAX(aantal) AS max_aantal
FROM besteldePizza
GROUP BY bestelcode;
</code></pre>
-->




## GROUP BY HAVING

Met HAVING kun je de resultaten *na* het groeperen filteren.  Hiermee kun je voorwaarden stellen aan groepen, iets wat niet met WHERE kan (want WHERE werkt vóór het groeperen). In HAVING kan je groepsfuncties gebruiken, zoals COUNT(), AVG(), SUM(), MAX() en MIN().


<table width="100%"><tr><td style="text-align:left; vertical-align:top; font-size:1.25rem;" width="35%">
Voorbeeld. De volgende query toont alleen bodems die meer dan één keer zijn besteld. HAVING filtert op het aantal per groep.

```sql
SELECT bodemcode, COUNT(*) as aantal_besteld_per_bodem
FROM besteldepizza
GROUP BY bodemcode
HAVING COUNT(*) > 1;
```
</td><td width="65%">
<table border="1">
  <thead>
    <tr>
      <th>bodemcode</th>
      <th>aantal_besteld_per_bodem</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>1</td>
      <td>2788</td>
    </tr>
    <tr>
      <td>2</td>
      <td>2905</td>
    </tr>
    <tr>
      <td>3</td>
      <td>140</td>
    </tr>
  </tbody>
</table>
</td></tr></table>



### Verwerkingsopdracht
<table width="100%"><tr><td style="text-align:left; vertical-align:top; font-size:1.25rem;" width="35%">
Voorbeeld. De volgende query toont alleen bodems die meer dan één keer zijn besteld. HAVING filtert op het aantal per groep.

```sql
SELECT bodemcode, COUNT(*) as aantal_besteld_per_bodem
FROM besteldepizza
GROUP BY bodemcode
HAVING COUNT(*) > 1;
```
</td><td width="65%">
<table border="1">
  <thead>
    <tr>
      <th>bodemcode</th>
      <th>aantal_besteld_per_bodem</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>1</td>
      <td>2788</td>
    </tr>
    <tr>
      <td>2</td>
      <td>2905</td>
    </tr>
    <tr>
      <td>3</td>
      <td>140</td>
    </tr>
  </tbody>
</table>
</td></tr></table>
bezorgernummer
3

</td></tr></table>


### Verwerkingsopdracht Ervaren bezorgers



<table width="100%"><tr><td style="text-align:left; vertical-align:top; font-size:1.25rem;" width="35%">
De manager wil weten welke bezorgers veel ervaring hebben. Een bezorger geldt als "ervaren" als hij of zij meer dan 150 bestellingen heeft bezorgd. Toon het overzicht zoals hiernaast.
</td><td width="65%">
 <table border="1">
        <thead>
            <tr>
                <th>Bezorgernummer</th>
            </tr>
        </thead>
        <tbody>
            <tr><td>0</td></tr>
            <tr><td>2</td></tr>
            <tr><td>3</td></tr>
            <tr><td>4</td></tr>
            <tr><td>5</td></tr>
            <tr><td>6</td></tr>
            <tr><td>7</td></tr>
            <tr><td>8</td></tr>
        </tbody>
    </table>
</td></tr></table>
<p>Bekijk <a
href="https://rweeda.github.io/PythonIA/docs/IA_sql_oplossingen.html#opgave491"
target="_blank">hier</a> de voorbeelduitwerking.</p>
 <!--
<pre><code class="language-sql">
SELECT bezorgernummer
FROM bestelling
GROUP BY bezorgernummer
HAVING COUNT(*) > 150;
</code></pre>
-->


### Verwerkingsopdracht Bodems met meer dan 2000 bestellingen
<table width="100%"><tr><td style="text-align:left; vertical-align:top; font-size:1.25rem;" width="35%">

<p>Geef een overzicht van de bodems met meer dan 2000 bestellingen, zoals in het overzicht hiernaast.
Tip: tel het aantal bestellingen bodem en toon alleen de bodems die meer dan 2000 keer zijn besteld.</p>


</td><td width="65%">
<table border="1">
  <thead>
    <tr>
      <th>bodemcode</th>
      <th>aantal_bestellingen</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>1</td>
      <td>2788</td>
    </tr>
    <tr>
      <td>2</td>
      <td>2905</td>
    </tr>
  </tbody>
</table>

</td></tr></table>
<p>Bekijk <a
href="https://rweeda.github.io/PythonIA/docs/IA_sql_oplossingen.html#opgave491"
target="_blank">hier</a> de voorbeelduitwerking.</p>
 <!--
<pre><code class="language-sql">
SELECT bodemcode, COUNT(*) AS aantal_bestellingen
FROM besteldePizza
GROUP BY bodemcode
HAVING COUNT(*) > 2000;
</code></pre>
-->



# Verschil tussen WHERE en HAVING
Met zowel de WHERE als HAVING kun je een voorwaarde geven om gegevens te filteren. Er is een belangrijke verschil tussen WHERE en HAVING:
<ul>
<li>WHERE werkt op individuele rijen, en werkt dus *vóór* het groeperen met GROUP BY.
<li>HAVING werkt op een groep gegevens, dus *na* een GROUP BY.
</ul>




### Verwerkingsopdracht Verschil tussen WHERE en HAVING

<ol type="a">
<li>Schrijf een query met WHERE die alleen bestellingen met bodemcode 1 is, zoals hieronder links te zien is;

<li>Schrijf een query met GROUP BY en HAVING die alleen bodems toont die meer dan 1 keer zijn besteld, zoals hieronder rechts te zien is;

<li>Vergelijk de resultaten en leg in je eigen woorden uit wat het verschil is.
</ol>


<table>
<tr><td>
    <table border="1">
    <thead>
        <tr>
        <th>besteldepizzacode</th>
        <th>pizzacode</th>
        <th>bestelcode</th>
        <th>bodemcode</th>
        <th>formaatcode</th>
        <th>aantal</th>
        </tr>
    </thead>
    <tbody>
        <tr>
        <td>7</td><td>25</td><td>2</td><td>1</td><td>4</td><td>1</td>
        </tr>
        <tr>
        <td>15</td><td>25</td><td>4</td><td>1</td><td>1</td><td>1</td>
        </tr>
        <tr>
        <td>18</td><td>19</td><td>5</td><td>1</td><td>4</td><td>3</td>
        </tr>
        <tr>
        <td colspan="6" style="text-align: center;">...</td>
        </tr>
        <tr>
        <td>5832</td><td>24</td><td>1470</td><td>1</td><td>4</td><td>3</td>
        </tr>
    </tbody>
    </table>
</td><td>
    <table border="1">
    <thead>
        <tr>
        <th>bodemcode</th>
        <th>aantal</th>
        </tr>
    </thead>
    <tbody>
        <tr>
        <td>1</td>
        <td>2788</td>
        </tr>
        <tr>
        <td>2</td>
        <td>2905</td>
        </tr>
        <tr>
        <td>3</td>
        <td>140</td>
        </tr>
    </tbody>
    </table>

</table>



<p>Bekijk <a
href="https://rweeda.github.io/PythonIA/docs/IA_sql_oplossingen.html#opgave491"
target="_blank">hier</a> de voorbeelduitwerking.</p>
 <!--
<ol type="a">
<li>WHERE-filter op rij-niveau:<br><pre><code class="language-sql">
SELECT * 
FROM besteldepizza
WHERE bodemcode = 1;
</pre>
<li>HAVING-filter op groep-niveau<br>
<pre><code class="language-sql">
SELECT bodemcode, COUNT(*) AS aantal
FROM besteldepizza
GROUP BY bodemcode
HAVING COUNT(*) > 1;</pre>
<li>Her verschil tussen WHERE en HAVING:
<ul>
<li>WHERE gebruik je als je rijen wilt uitsluiten voordat je gaat tellen of groeperen.
<li>HAVING gebruik je als je groepen wilt filteren nadat je hebt geteld of iets hebt samengevat.
</ul>
</ol>
-->

### Verwerkingsopdracht Bodems die vaak zijn besteld (maar zonder kleine bestellingen)

<p>Bij deze opdracht moet je bedenken welke voorwaarde je in de WHERE en welke in de HAVING moet gebruiken.</p>



<table width="100%"><tr><td style="text-align:left; vertical-align:top; font-size:1.25rem;" width="35%">
<ol type="a">
<li>Toon per bodemcode hoeveel pizza’s er in totaal zijn besteld, maar reken alleen bestellingen mee waarbij meer dan 1 pizza is besteld.
<li>Toon alleen de bodems waarvan het totaal meer dan 2000 is.
</ol>
De informatie komt uit tabel <i>besteldePizza</i>.

</td><td width="65%">
<table border="1">
  <thead>
    <tr>
      <th>bodemcode</th>
      <th>aantal_bestellingen</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>1</td>
      <td>2788</td>
    </tr>
    <tr>
      <td>2</td>
      <td>2905</td>
    </tr>
  </tbody>
</table>

</td></tr></table>
<p>Bekijk <a
href="https://rweeda.github.io/PythonIA/docs/IA_sql_oplossingen.html#opgave491"
target="_blank">hier</a> de voorbeelduitwerking.</p>
 <!--
<pre><code class="language-sql">
SELECT bodemcode, SUM(aantal) AS totaal_besteld
FROM besteldePizza
WHERE aantal > 1             -- filter op rij-niveau vóór de GROUP BY
GROUP BY bodemcode
HAVING SUM(aantal) > 2000;    -- filter ná de GROUP BY
</code></pre>
-->


## Samenvatting
<ul>
<li>De GROUP BY groepeert rijen met dezelfde waarden in een kolom zodat groepsfuncties zoals SUM(), COUNT() of MAX() daarop kunnen worden toegepast.
<li>De HAVING filtert de groepen na een GROUP BY;
<li>De WHERE filtert vóór het groeperen;
<li>Hieronder staat de volgorde waarin de SQL commando's moeten staan:
<p><img
src="https://raw.githubusercontent.com/rweeda/PythonIA/main/sql/img/H1_commandos.png"
alt="Commando's voor het ophalen van informatie" width="500"></p></li>
</ul>




# Afsluitende Opdrachten

### Afsluitende Opdracht Aantal bestellingen per bodem
<table width="100%"><tr><td style="text-align:left; vertical-align:top; font-size:1.25rem;" width="35%">

Toon een overzicht van het aantal bestellingen per bodem (<b>bodemcode</b>). De informatie komt uit tabel <i>besteldePizza</i>. Sorteer deze zodat de meest bestelde bodem bovenaan staat, zoals hiernaast. 
</td><td width="65%">
<table border="1">
  <thead>
    <tr>
      <th>bodemcode</th>
      <th>aantal_besteld_per_bodem</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>2</td>
      <td>2905</td>
    </tr>
    <tr>
      <td>1</td>
      <td>2788</td>
    </tr>
    <tr>
      <td>3</td>
      <td>140</td>
    </tr>
  </tbody>
</table>

</td></tr></table>
<p>Bekijk <a
href="https://rweeda.github.io/PythonIA/docs/IA_sql_oplossingen.html#opgave491"
target="_blank">hier</a> de voorbeelduitwerking.</p>
 <!--
<pre><code class="language-sql">
SELECT bodemcode, COUNT(*) AS aantal_besteld_per_bodem
FROM besteldePizza
GROUP BY bodemcode 
ORDER BY aantal_besteld_per_bodem DESC;
</code></pre>
-->




### Afsluitende Opdracht Bekijk hoe vaak een specifieke bodem is gebruikt

<table width="100%"><tr><td style="text-align:left; vertical-align:top; font-size:1.25rem;" width="35%">
  <p>
    Hoe vaak is <b>bodemcode</b> gebruikt in <i>bestellingen</i>?<br>
    Toon alleen het resultaat als deze bodem meer dan 1 keer is gebruikt. Sorteer het resultaat aflopend op het aantal bestellingen en geef alleen de bovenste regel weer, zoals in het overzicht hiernaast.<br>
    Tip: Groepeer op <b>bodemcode</b>.
  </p>


</td><td width="65%">
<table border="1">
  <thead>
    <tr>
      <th>bodemcode</th>
      <th>aantal_besteld</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>2</td>
      <td>2905</td>
    </tr>
  </tbody>
</table>

<!--Tips:
    <li>Filter de data op <code>bodemcode = 2</code>.</li>
    <li>Groepeer op <code>bodemcode</code>.</li>
    <li>Gebruik <code>HAVING</code> om alleen bodems te tonen die meer dan 1 keer zijn besteld.</li>
    <li>Sorteer het resultaat aflopend op het aantal bestellingen.</li>
    <li>Geef alleen de bovenste regel weer.</li>
  </ul>
-->

</td></tr></table>
<p>Bekijk <a
href="https://rweeda.github.io/PythonIA/docs/IA_sql_oplossingen.html#opgave491"
target="_blank">hier</a> de voorbeelduitwerking.</p>

<!--
    <pre><code>
    SELECT bodemcode, COUNT(*) AS aantal_besteld
FROM besteldepizza
WHERE bodemcode = 2
GROUP BY bodemcode
HAVING COUNT(*) > 1
ORDER BY aantal_besteld DESC
LIMIT 1;
    </code></pre>
-->




### Afsluitende Opdracht Totale aantal pizza’s per klant

<table width="100%"><tr><td style="text-align:left; vertical-align:top; font-size:1.25rem;" width="35%">
Toon per klant (klantnummer) hoeveel pizza’s hij/zij in totaal heeft besteld (dus over alle bestellingen bij elkaar).
</td><td width="65%">
<table border="1">
  <thead>
    <tr>
      <th>klantnummer</th>
      <th>totaal_aantal</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>101</td>
      <td>87</td>
    </tr>
    <tr>
      <td>103</td>
      <td>62</td>
    </tr>
    <tr>
      <td>104</td>
      <td>66</td>
    </tr>
    <tr>
      <td colspan="2" style="text-align:center;">...</td>
    </tr>
    <tr>
      <td>474</td>
      <td>105</td>
    </tr>
  </tbody>
</table>

</td></tr></table>
<p>Bekijk <a
href="https://rweeda.github.io/PythonIA/docs/IA_sql_oplossingen.html#opgave491"
target="_blank">hier</a> de voorbeelduitwerking.</p>
 <!--
<pre><code class="language-sql">
SELECT bestelling.klantnummer, SUM(besteldePizza.aantal)
FROM bestelling
JOIN besteldePizza ON bestelling.bestelcode = besteldePizza.bestelcode
GROUP BY bestelling.klantnummer;
</code></pre>
-->




### AFLSUITENDE OPDRACHT Meest bestelde pizzabodem


<table width="100%"><tr><td style="text-align:left; vertical-align:top; font-size:1.25rem;" width="35%">

Schrijf een query die de meest bestelde pizzabodem toont. Tip: Sorteer en beperk daarna het overzicht tot 1 rij.

</td><td width="65%">
<table border="1">
  <thead>
    <tr>
      <th>bodemcode</th>
      <th>aantal_besteld</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>2</td>
      <td>2905</td>
    </tr>
  </tbody>
</table>

</td></tr></table>
<p>Bekijk <a
href="https://rweeda.github.io/PythonIA/docs/IA_sql_oplossingen.html#opgave491"
target="_blank">hier</a> de voorbeelduitwerking.</p>
 <!--
<pre><code class="language-sql">
SELECT bodemcode, COUNT(*) as aantal_besteld
FROM besteldepizza
GROUP BY bodemcode
ORDER BY aantal_besteld DESC
LIMIT 1;
</code></pre>
-->
