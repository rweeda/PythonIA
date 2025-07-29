### 4.12: Afsluitende Opdrachten


### Afsluitende Opdracht 4.12.1

<table width="100%"><tr><td style="text-align:left; vertical-align:top; font-size:1.25rem;" width="35%">
Toon van de drie duuste pizza's de <b>naam</b> en <b>basisprijs</b> zoals in het overzicht hiernaast.
</td><td width="65%">
<table border="1" cellpadding="4" cellspacing="0">
  <thead>
    <tr>
      <th>naam</th>
      <th>basisprijs</th>
    </tr>
  </thead>
  <tbody>
    <tr><td>Combinazione</td><td>10.5</td></tr>
    <tr><td>Specialità di Danilo</td><td>9.5</td></tr>
    <tr><td>Calzone (dichte pizza)</td><td>9</td></tr>
  </tbody>
</table>


</td></tr></table>




<p>Bekijk <a href="https://rweeda.github.io/PythonIA/docs/IA_sql_oplossingen.html#opgave4121" target="_blank">hier</a> de voorbeelduitwerking.</p>
<!-- ANTWOORD:
<pre><code class="language-sql">
SELECT naam, formaatcode, basisprijs
FROM pizza
ORDER BY basisprijs DESC
LIMIT 3;
</code></pre>
-->

### Afsluitende Opdracht 4.12.2 Vijf goedkoopste pizza's
<table width="100%"><tr><td style="text-align:left; vertical-align:top; font-size:1.25rem;" width="35%">
Geef de namen en prijzen van de vijf goedkoopste pizza’s die minder dan €8 kosten. Sorteer ze oplopend op prijs, zoals in het overzicht hiernaast.
</td><td width="65%">
<table border="1" cellpadding="4" cellspacing="0">
  <thead>
    <tr>
      <th>naam</th>
      <th>basisprijs</th>
    </tr>
  </thead>
  <tbody>
    <tr><td>Napoletana</td><td>7.5</td></tr>
    <tr><td>Prosciutto</td><td>7.5</td></tr>
    <tr><td>Funghi</td><td>7.5</td></tr>
    <tr><td>Salame</td><td>7.5</td></tr>
    <tr><td>Borromea</td><td>7.5</td></tr>
  </tbody>
</table>


</td></tr></table>




<p>Bekijk <a href="https://rweeda.github.io/PythonIA/docs/IA_sql_oplossingen.html#opgave4122" target="_blank">hier</a> de voorbeelduitwerking.</p>

<!--
SELECT naam, basisprijs
FROM pizza
WHERE basisprijs < 8
ORDER BY basisprijs DESC
LIMIT 5;
-->


### Afsluitende Opdracht 4.12.3 Gemiddelde prijs
<table width="100%"><tr><td style="text-align:left; vertical-align:top; font-size:1.25rem;" width="35%">
<p>Toon de gemiddelde prijs van alle pizza’s zonder ham. Hernoem de kolom zoals in het overzicht hiernaast.</p>
<p>Tip: begin met een overzicht van alle pizza’s zonder ham.</p>
</td><td width="65%">
  <table border="1">
    <tr>
      <th>gemiddelde_prijs_zonder_ham</th>
    </tr>
    <tr>
      <td>8.07</td>
    </tr>
  </table>

</td></tr></table>




<p>Bekijk <a href="https://rweeda.github.io/PythonIA/docs/IA_sql_oplossingen.html#opgave4123" target="_blank">hier</a> de voorbeelduitwerking.</p>

<!--
SELECT avg(basisprijs) AS gemiddelde_prijs_zonder_ham
From pizza
WHERE omschrijving NOT LIKE '%ham%';

-->

### Afsluitende Opdracht 4.12.4
<table width="100%"><tr><td style="text-align:left; vertical-align:top; font-size:1.25rem;" width="35%">
Hoeveel unieke woonplaatsen zijn er onder klanten die geen 06-nummer hebben opgegeven?
</td><td width="65%">
<table border="1" cellpadding="4" cellspacing="0">
  <thead>
    <tr>
      <th>woonplaatsen_zonder_06</th>
    </tr>
  </thead>
  <tbody>
    <tr><td>3</td></tr>
  </tbody>
</table>


</td></tr></table>




<p>Bekijk <a href="https://rweeda.github.io/PythonIA/docs/IA_sql_oplossingen.html#opgave4124" target="_blank">hier</a> de voorbeelduitwerking.</p>

<!--

SELECT COUNT(DISTINCT woonplaats) AS woonplaatsen_zonder_06
FROM klant
WHERE telefoon NOT LIKE '06%';

-->


### Afsluitende Opdracht 4.12.5
<table width="100%"><tr><td style="text-align:left; vertical-align:top; font-size:1.25rem;" width="35%">
<p>Toon hoeveel pizza’s tussen de €7 en €10 kosten (inclusief 7 en 10). Hernoem de kolom zoals in het overzicht hiernaast.</p>
<p>Tip: maak eerst een juist overzicht van de pizza’s die aan de voorwaarden voldoen.</p>

</td><td width="65%">
  <table border="1">
    <tr>
      <th>Aantal</th>
    </tr>
    <tr>
      <td>33</td>
    </tr>
  </table>

</td></tr></table>




<p>Bekijk <a href="https://rweeda.github.io/PythonIA/docs/IA_sql_oplossingen.html#opgave4125" target="_blank">hier</a> de voorbeelduitwerking.</p>

<!--

SELECT COUNT(pizzacode) AS aantal
FROM pizza
WHERE basisprijs >= 7 AND basisprijs <= 10;

-->


### Afsluitende Opdracht 4.12.6 Totale toeslagen
<table width="100%"><tr><td style="text-align:left; vertical-align:top; font-size:1.25rem;" width="35%">
<p>Wat is het totaal van alle toeslagen (<b>plusprijs</b>) voor formaat met een prijs hoger dan €1? De gegevens komen uit tabel <i>formaat</i>. Toon het overzicht zoals hiernaast.</p>
</td><td width="65%">
<table border="1" cellpadding="4" cellspacing="0">
  <thead>
    <tr>
      <th>totaal_toeslagen</th>
    </tr>
  </thead>
  <tbody>
    <tr><td>1.5</td></tr>
  </tbody>
</table>


</td></tr></table>




<p>Bekijk <a href="https://rweeda.github.io/PythonIA/docs/IA_sql_oplossingen.html#opgave4126" target="_blank">hier</a> de voorbeelduitwerking.</p>

<!--

SELECT SUM(plusprijs) AS totaal_toeslagen
FROM formaat
WHERE plusprijs > 1;

-->


### Afsluitende Opdracht 4.12.7
<table width="100%"><tr><td style="text-align:left; vertical-align:top; font-size:1.25rem;" width="35%">
<p>Je wilt weten wat de hoogste prijs is van een pizza die iets met vis te maken heeft (bijvoorbeeld in de omschrijving) of waarvan de naam eindigt op de letter 'a'.</p>
<p>Tip: maak eerst een juist overzicht van de pizza's die aan de voorwaarden voldoen.</p>
</td><td width="65%">
<table border="1">
    <tr>
      <th>duurste</th>
    </tr>
    <tr>
      <td>9</td>
    </tr>
  </table>

</td></tr></table>




<p>Bekijk <a href="https://rweeda.github.io/PythonIA/docs/IA_sql_oplossingen.html#opgave4127" target="_blank">hier</a> de voorbeelduitwerking.</p>

<!--
SELECT max(basisprijs) AS duurste
FROM pizza
WHERE omschrijving LIKE "%vis%" OR naam LIKE "%a";

-->