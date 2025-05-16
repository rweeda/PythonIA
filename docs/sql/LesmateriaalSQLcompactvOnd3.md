

### Overzicht ONDERWERP 3






## 3.1: Kolom hernoemen met <code>AS</code>

Met `AS` kan je een kolomnaam hernoemen. Dit doe je na de `SELECT`.

Bijvoorbeeld, hieronder wordt de kolom `naam` getoond als `pizzanaam`


``` SQL
SELECT naam AS pizzanaam
FROM pizza;
```


| pizzanaam   |
|-------------|
| Margherita  |
| Napoletana  |
| Prosciutto  |
| Funghi      |
| Salame      |



### Verwerkingsopdracht 3.1.1 Kolom 'naam' hernoemen in 'bezorgernaam'
Toon een overzicht van alle namen van de bezorgers. Noem het kolom `bezorgernaam`.

<p>Bekijk <a href="https://rweeda.github.io/PythonIA/docs/IA_sql_oplossingen.html#opgave311" target="_blank">hier</a> de voorbeelduitwerking.</p>
<!-- ANTWOORD:
<pre><code class="language-sql">
SELECT naam AS bezorgernaam
FROM bezorger;
</code></pre>
-->



## 3.2: Aantal rijen beperken met <code>LIMIT</code>
<p>Met LIMIT kun je bepalen hoeveel rijen er getoond moeten worden.</p>

<p>Met de volgende code toon je alleen de eerste vijf rijen:</p>

SELECT *
FROM pizza
LIMIT 5;


### Verwerkingsopdracht 3.2.1 Alleen de eerste drie pizza's
Toon de naam (<i>pizzanaam</i>) en prijs (<i>basisprijs</i>) van de eerste drie pizza's.

<p>Bekijk <a href="https://rweeda.github.io/PythonIA/docs/IA_sql_oplossingen.html#opgave321" target="_blank">hier</a> de voorbeelduitwerking.</p>
<!-- ANTWOORD:
<pre><code class="language-sql">
SELECT pizzanaam, basisprijs
FROM pizza
LIMIT 3;
</code></pre>
-->




## 3.3: Gegevens sorteren met `ORDER BY`

Met ORDER BY kun je resultaten sorteren.
Hierbij moet je aangeven op welke kolom er gesorteerd moet worden en of het oplopend ('ASC') of juist 
aflopend ('DESC') moet zijn. Geef altijd eerst de SELECT en FROM aan, en daarna de ORDER BY.



Bijvoorbeeld, om de pizza's op oplopend op prijs te sorteren, dus met de goedkoopste pizza bovenaan:
SELECT naam, basisprijs
FROM pizza
ORDER BY basisprijs ASC;


Of om de bezorgers te aflopende sorteren op geboortedaum, dus met de jongste bezorger bovenaaan:
SELECT naam, geboortedatum
FROM bezorger
ORDER BY gebdatum DESC;

Ter herinnering, hieronder de volgorde waarin alle commando's die gebruikt worden moeten staan:
<p><img
src="https://raw.githubusercontent.com/rweeda/PythonIA/main/sql/img/H1_commandos.png"
alt="Commando's voor het ophalen van informatie" width="400"></p>





### Verwerkingsopdracht 3.3.1 de drie duurste pizza's
Geef een overzicht van de pizza's gesorteerd op prijs van laag naar hoog.


<p>Bekijk <a href="https://rweeda.github.io/PythonIA/docs/IA_sql_oplossingen.html#opgave331" target="_blank">hier</a> de voorbeelduitwerking.</p>
<!-- ANTWOORD:
<pre><code class="language-sql">
SELECT naam, basisprijs
FROM pizza
ORDER BY basisprijs 
</code></pre>



Ook goed:
<pre><code class="language-sql">
SELECT naam, basisprijs
FROM pizza
ORDER BY basisprijs ASC
</code></pre>
-->




### Verwerkingsopdracht 3.3.2 De vijf laatste bezorgingen
Geef een overzicht van de pizza's gesorteerd op `bestel_datum`, zoals in het overzicht hieronder. 

| bestelcode | bestel_datum |
|------------|--------------|
| 1469       | 2022-03-03   |
| 1470       | 2022-03-03   |
| 1471       | 2022-03-03   |
| 1473       | 2022-03-03   |
| 1464       | 2022-03-02   |
| 1465       | 2022-03-02   |
| 1466       | 2022-03-02   |
| 1467       | 2022-03-02   |


Tip: eerst aflopend sorteren, dan met LIMIT de bovenste acht bestellingen tonen.

<p>Bekijk <a href="https://rweeda.github.io/PythonIA/docs/IA_sql_oplossingen.html#opgave332" target="_blank">hier</a> de voorbeelduitwerking.</p>
<!-- ANTWOORD:
<pre><code class="language-sql">
ANTWOORD: 
SELECT bestelcode, datum
FROM bestelling
ORDER BY datum DESC
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

Naast de '='-teken kun ook andere operatoren in de WHERE gebruiken. Hier is een overzicht:

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


Bijvoorbeeld, met de volgende query laten we de gegevens zien van klanten die <i>niet</i> in Enschede wonen:
```sql 
SELECT *
FROM klant
WHERE plaats <> 'Enschede';
```

VOEG VOORBEELD TOE




### Verwerkingsopdracht 3.4.1 Dure pizza's
Toon de namen en prijzen van de pizza's die 9,50 euro kosten of meer, zoals in het overzicht hieronder.


| naam                  | basisprijs |
|-----------------------|-------------|
| Specialità di Danilo | 9.5         |
| Combinazione          | 10.5        |


<p>Bekijk <a href="https://rweeda.github.io/PythonIA/docs/IA_sql_oplossingen.html#opgave34" target="_blank">hier</a> de voorbeelduitwerking.</p>
<!-- ANTWOORD:
<pre><code class="language-sql">

</code></pre>
-->



### Verwerkingsopdracht 3.4.2: Geen 8euro pizza's
Toon de namen en prijzen van de pizza's die <b>niet</b> 8 euro kosten.


<p>Bekijk <a href="https://rweeda.github.io/PythonIA/docs/IA_sql_oplossingen.html#opgave35" target="_blank">hier</a> de voorbeelduitwerking.</p>
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
- De LIKE gebruik je in de where
- De joker zet je in ter vervanging van nul of meerdere tekens
- Je moet bij de LIKE aanhalingstekens gebruiken


Bijvoorbeeld, om alle namen te die beginnen met ‘Jo’ (zoals Josette, Johan) gebruik je:

SELECT naam
FROM klant
WHERE naam LIKE 'J%';

| naam                      |
|---------------------------|
| Josette Soede             |
| Jolanda Budding-Doornbos  |
| Joanne Vlastuin           |
| Jolanda Knoop - Hoek      |
| Joost Nieuwboer           |
| Johan van Nierop          |






Bijvoorbeeld, met de volgende query tonen we de pizza's met een naam die <i>begint met</i> 'Quattro':

SELECT naam
FROM pizza
WHERE naam LIKE 'Quattro%';

Of die <i>eindigd op</i> 'arma':

SELECT naam
FROM pizza
WHERE naam LIKE '%arma';

Of waarbij de letter 'e' <i>erin voorkomt</i>:

SELECT naam
FROM pizza
WHERE naam LIKE '%e%';



### Verwerkingsopdracht 3.5.1 Alle pizza's waar de letter 'a' in voorkomt
Toon een overzicht van alle pizza's waar de letter 'a' in voorkomt:

<p>Bekijk <a href="https://rweeda.github.io/PythonIA/docs/IA_sql_oplossingen.html#opgave351" target="_blank">hier</a> de voorbeelduitwerking.</p>
<!-- ANTWOORD:
<pre><code class="language-sql">
SELECT naam
FROM pizza
WHERE naam LIKE '%a%';
</code></pre>
-->


### Verwerkingsopdracht 3.5.2 Alle klanten met een mobiele telefoonnummer.
Toon een overzicht van alle klanten die een 06-nummer hebben opgegeven.


<p>Bekijk <a href="https://rweeda.github.io/PythonIA/docs/IA_sql_oplossingen.html#opgave352" target="_blank">hier</a> de voorbeelduitwerking.</p>
<!-- ANTWOORD:
<pre><code class="language-sql">
SELECT *
FROM klant
WHERE telefoon LIKE '06%';
</code></pre>
-->




## 3.6: Logische operator AND 
Je kunt de WHERE voorwaarde ook uitbreiden met de logische operatoren AND, OR, NOT of combinaties daarvan. 

Met *AND* (EN) moet aan alle voorwaarden worden voldaan om een resultaat te krijgen. 

Bijvoorbeeld, met de volgende query tonen we alle klanten die in Enschede wonen en een naam hebben die met 'H' begint:


SELECT *
FROM klant
WHERE plaats = 'Enschede' AND naam LIKE 'H%';

| klantnummer | wachtwoord     | naam                  | adres                | postcode | plaats    | telefoon     |
|-------------|----------------|------------------------|----------------------|----------|-----------|--------------|
| 101         | uqOpgECQ_      | Hanneke Bolier         | Gladioolstraat 11    | 3742TC   | Enschede  | 06-169X5427  |
| 209         | m1nbsrweOFJxu5 | Hermina de Pater       | Koekoeksbloemlaan 40 | 3742EK   | Enschede  | 06-6255X908  |
| 221         | Qe4W6Xf70D_YlHR| Heleen  van Harberden  | Acacialaan 27        | 3741WB   | Enschede  | 035-85X3955  |
| 401         | dJiorsEkNLE    | Henrike Teeuw          | Dahliastraat 17      | 3742RK   | Enschede  | 035-8X94605  |



### Verwerkingsopdracht 3.6.1 Pizza's tussen de 8,50 en 10euro

Toon alle pizza's die tussen de €8,50 en €10,- kosten:

| naam                   | basisprijs |
|------------------------|-------------|
| Calzone (dichte pizza) | 9.0         |
| Marinara               | 8.5         |
| Mozzarella             | 8.5         |
| Quattro stragioni      | 8.5         |
| Americana              | 8.5         |
| Shoarma                | 9.0         |
| Pollo                  | 9.0         |
| Salmone                | 8.5         |
| Fantasia               | 9.0         |
| Parma                  | 8.5         |
| Pazza                  | 8.5         |
| Inferno                | 8.5         |
| Tropicana              | 8.5         |
| Della Casa             | 8.5         |
| Specialità di Danilo   | 9.5         |

Tip: de basisprijs is meer dan 8.50 en minder dan 10 euro.


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


Met *OR* (OF) moet aan één van de voorwaarden voldaan worden.

Bijvoorbeeld, de volgende query toont alle pizza's die met 'M' beginnen OF een basisprijs onder de 7euro hebben:
```SQL
SELECT naam, basisprijs
FROM pizza
WHERE naam LIKE 'M%' OR basisprijs < 7;
```


| naam       | basisprijs |
| ---------- | ---------- |
| Margherita | 6.0        |
| Cippola    | 6.5        |
| Marinara   | 8.5        |
| Mozzarella | 8.5        |





### Verwerkingsopdracht 3.7.1 Bestellingen met bestelcode
<p>Toon alle informatie over zowel bestellingen bestelcode 13 en die met bestelcode 30, zoals hieronder.</p>

| bestelcode | datum       | bestel_tijd | bezorg_tijd | bezorgernummer | klantnummer | korting |
| ---------- | ----------- | ----------- | ----------- | -------------- | ----------- | ------- |
| 13         | 2021-12-03  | 17:33:00    | 17:48:00    | 5              | 279         | 0.0     |
| 30         | 2021-12-05  | 17:55:00    | 18:11:00    | 8              | 376         | 0.0     |



<p>Bekijk <a href="https://rweeda.github.io/PythonIA/docs/IA_sql_oplossingen.html#opgave371" target="_blank">hier</a> de voorbeelduitwerking.</p>
<!-- ANTWOORD:
<pre><code class="language-sql">
SELECT *
FROM bestelling
WHERE bestelcode = 13 OR bestelcode = 30;
</code></pre>
-->




### Verwerkingsopdracht 3.7.2 Alle goedkope of gezonde pizza's
Maak een overzicht van alle pizza's goedkoper zijn dan €7,50 of fruit bevatten.

<p>Bekijk <a href="https://rweeda.github.io/PythonIA/docs/IA_sql_oplossingen.html#opgave372" target="_blank">hier</a> de voorbeelduitwerking.</p>
<!-- ANTWOORD:
<pre><code class="language-sql">
SELECT *
FROM pizza
WHERE basisprijs<7.50 OR omschrijving LIKE '%fruit%';
</code></pre>
-->





## 3.8: Logische operator NOT
Met `NOT` (NIET) mag er aan géén van de voorwaarden voldaan worden.

Bijvoorbeeld, alle klanten die *niet* in Hengelo wonen:

SELECT *
FROM klanten
WHERE NOT plaats = 'Hengelo'


Bijvoorbeeld, alle pizza's waarbij de letter 'e' er <b>niet</b> in voorkomt:

SELECT naam
FROM pizza
WHERE naam NOT LIKE '%e%';




### Verwerkingsopdracht 3.8.1 Alle pizza's zonder kip

Toon een overzicht van alle pizza's waar <b>geen</b> kip op zit, dus ook geen kipfilet, zoals in het voorbeeld hieronder.

| pizzanaam   | omschrijving                                                       |
|-------------|---------------------------------------------------------------------|
| Margherita  | Tomaat, kaas en oregano                                            |
| Napoletana  | Tomaat, kaas, ansjovis, olijven, kappertjes en oregano            |
| Prosciutto  | Tomaat, kaas, ham en oregano                                       |
| Funghi      | Tomaat, kaas, champignons en oregano                               |
| Salame      | Tomaat, kaas, salami en oregano                                    |



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




## 3.9: Meerdere operatoren combineren
Je kunt meerdere operatoren combineren. Als je de AND, OR en NOT combineert moet je gebruik maken van haakjes voor de gewenste uitkomst.

Bijvoorbeeld, met de volgende query tonen we de pizza's die tussen de  €8,50 en €10,- kosten, of pizza's die geen salami bevatten:

SELECT naam, omschrijving, basisprijs
FROM pizza
WHERE (basisprijs>=8.50 AND basisprijs<=10) OR NOT omschrijving LIKE '%salami%';


### Verwerkingsopdracht opdracht 3.9.1 Alle pizza's zonder paprika en zonder ui

Luna wil een overzicht van alle pizza's waar <b>geen</b> paprika op zit, maar ook geen <b>ui</b>. 
Ze schrijft daarvoor de volgende query, maar er zitten een paar fouten in. Kan jij het aanpassen zodat de juiste overzicht gegeven wordt, zoals hieronder?

Juiste overzicht:
| naam        | omschrijving                                                       |
|-------------|---------------------------------------------------------------------|
| Margherita  | Tomaat, kaas en oregano                                            |
| Napoletana  | Tomaat, kaas, ansjovis, olijven, kappertjes en oregano            |
| Prosciutto  | Tomaat, kaas, ham en oregano                                       |
| Funghi      | Tomaat, kaas, champignons en oregano                               |
| Salame      | Tomaat, kaas, salami en oregano                                    |

Tip: Gebruik eventueel commentaar '--' om een deel van je code te verbergen zodat je kunt kijken welke delen wel en niet goed werken.



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




### Verwerkingsopdracht 3.9.2 Toon pizza's gefiltererd op meerdere voorwaarden

Toon alle pizza's die minder dan €7,50 kosten, en met de letter M beginnen of letter A eindigen. 

<p>Bekijk <a href="https://rweeda.github.io/PythonIA/docs/IA_sql_oplossingen.html#opgave392" target="_blank">hier</a> de voorbeelduitwerking.</p>
<!-- ANTWOORD:
<pre><code class="language-sql">
SELECT *
FROM pizza
WHERE basisprijs < 7.5 AND (naam LIKE 'M%' OR naam LIKE '%A');
</code></pre>
-->



### AFSLUITENDE OPDRACHTEN


### Afsluitende Opdracht 3.1

Toon van alle pizza's de omschrijving en de naam (in die volgorde).

<p>Bekijk <a href="https://rweeda.github.io/PythonIA/docs/IA_sql_oplossingen.html#opgave313" target="_blank">hier</a> de voorbeelduitwerking.</p>
<!-- ANTWOORD:
<pre><code class="language-sql">
SELECT omschrijving, naam
FROM pizza;
</code></pre>
-->


### Afsluitende Opdracht: Alle goedkope pizza's met een 'C'

Toon een overzicht van alle pizza's waarvan de naam met 'C' begint maar niet meer kost dan 8 euro.

| naam         |
|--------------|
| Cippola      |
| Calimero     |
| Capricciosa  |


<p>Bekijk <a href="https://rweeda.github.io/PythonIA/docs/IA_sql_oplossingen.html#opgave313" target="_blank">hier</a> de voorbeelduitwerking.</p>
<!-- ANTWOORD:
<pre><code class="language-sql">
SELECT naam
FROM pizza
WHERE naam LIKE 'C%' AND basisprijs <= 8.0;
</code></pre>
-->


###Afsluitende Opdracht 3.13

Schrijf een SQL-query om alle pizza's te vinden met een basisprijs van minimaal €9,00 én die het woord 'salami' in de omschrijving bevatten.

| naam                   | basisprijs |
| ---------------------- | ---------- |
| Calzone (dichte pizza) | 9.0        |
| Fantasia               | 9.0        |
| Specialità di Danilo   | 9.5        |


<p>Bekijk <a href="https://rweeda.github.io/PythonIA/docs/IA_sql_oplossingen.html#opgave313" target="_blank">hier</a> de voorbeelduitwerking.</p>
<!-- ANTWOORD:
<pre><code class="language-sql">
SELECT naam, basisprijs
FROM pizza
WHERE basisprijs >= 9
  AND omschrijving LIKE '%salami%';
</code></pre>
-->

### Afsluitende Opdracht 3.15 Toon 3 pizza’s zonder vlees, met een ‘a’ in de naam

Toon de eerste drie pizza’s (alfabetisch op naam) die **geen vlees bevatten** en een **‘a’ in de naam** hebben. Toon de kolommen `naam` en `omschrijving`.

<p>Bekijk <a href="https://rweeda.github.io/PythonIA/docs/IA_sql_oplossingen.html#opgave313" target="_blank">hier</a> de voorbeelduitwerking.</p>

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
---

### Afsluitende Opdracht 3.16 Klanten buiten Enschede met 06-nummer

Toon de klantnamen en woonplaatsen van alle klanten die een **mobiel nummer (06)** hebben maar **niet in Enschede** wonen. Noem de kolommen zoals in het voorbeeld hieronder.

| klantnaam           | woonplaats |
|---------------------|------------|
| Josette Soede       | Hengelo    |
| Peter van Tol       | Hengelo    |
| Gerard Schouten     | Hengelo    |
| Dennis Nijhout      | Hengelo    |
| ... | ... |
| Timo Hendriks       | Nijmegen   |

<p>Bekijk <a href="https://rweeda.github.io/PythonIA/docs/IA_sql_oplossingen.html#opgave313" target="_blank">hier</a> de voorbeelduitwerking.</p>
<!-- ANTWOORD:
<pre><code class="language-sql">
SELECT naam AS klantnaam, woonplaats 
FROM klant
WHERE telefoon LIKE '06%' 
  AND woonplaats <> 'Enschede';
</code></pre>


Ook goed:
<pre><code class="language-sql">
SELECT naam AS klantnaam, woonplaats 
FROM klant
WHERE telefoon LIKE '06%' 
  AND NOT woonplaats = 'Enschede';
</code></pre>
-->


### Afsluitende Opdracht 3.17 Pizza’s met ‘special’ of duurder dan €10

Toon de namen van alle pizza’s waarvan de omschrijving het woord **'special'** bevat, **óf** die duurder zijn dan **€10,00**.

<p>Bekijk <a href="https://rweeda.github.io/PythonIA/docs/IA_sql_oplossingen.html#opgave313" target="_blank">hier</a> de voorbeelduitwerking.</p>
<!-- ANTWOORD:
<pre><code class="language-sql">
SELECT naam
FROM pizza
WHERE omschrijving LIKE '%special%'
   OR basisprijs > 10;
</code></pre>
-->

### Afsluitende Opdracht 3.18 Bezorgers met naam die NIET met J begint

Toon de namen van de bezorgers die **niet met de letter J beginnen**. Noem de kolom `bezorger`.

<!-- ANTWOORD:
<pre><code class="language-sql">
SELECT naam AS bezorger
FROM bezorger
WHERE naam NOT LIKE 'J%';
</code></pre>
-->

