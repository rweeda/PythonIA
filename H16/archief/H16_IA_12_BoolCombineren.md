
## 12: Logische operatoren combineren

<p>Gebruik je meer dan twee logische operatoren, gebruik dan altijd haakjes zodat je de juiste informatie krijgt. In het voorbeeld hieronder zie je dat <code>(A and B) or C</code>  wat anders betekend dan <code>A and (B or C)</code>:</p>


```python
steden = {
    "Amsterdam": {"land": "Nederland", "inwoners": 921000, "werelddeel": "Europa"},
    "Buenos Aires": {"land": "Argentinië", "inwoners": 2890000, "werelddeel": "Zuid-Amerika"},
    "Rome": {"land": "Italië", "inwoners": 2873000, "werelddeel": "Europa"},
    "São Paulo": {"land": "Brazilië", "inwoners": 12330000, "werelddeel": "Zuid-Amerika"},
    "Tokyo": {"land": "Japan", "inwoners": 13960000, "werelddeel": "Azië"},

}

#haakjes om de and: (A and B) or C
for stad, gegevens in steden.items():	#voor elke stad in de dictionary steden
    if (steden[stad]["inwoners"] < 1000000 and steden[stad]["werelddeel"]=="Europa") or steden[stad]["werelddeel"]=="Azië":	# steden met (minder dan 1 miljoen inwoners EN in Europa), OF de steden in Azië
        print("(",stad, "heeft minder dan 1 miljoen inwoners EN ligt in Europa ) OF ligt in Azië.")

#haakjes om de or: A and (B or C)
for stad, gegevens in steden.items():	#voor elke stad in de dictionary steden
    if steden[stad]["inwoners"] < 1000000 and (steden[stad]["werelddeel"]=="Europa" or steden[stad]["werelddeel"]=="Azië"):	# steden met minder dan 1 miljoen inwoners EN  (in Europa OF in Azië)
        print(stad, "heeft minder dan 1 miljoen inwoners  EN ( ligt in Europa OF ligt in Azië ).")
```

    ( Amsterdam heeft minder dan 1 miljoen inwoners EN ligt in Europa) OF ligt in Azië.
    ( Tokyo heeft minder dan 1 miljoen inwoners EN ligt in Europa) OF ligt in Azië.
    Amsterdam heeft minder dan 1 miljoen inwoners  EN (ligt in Europa OF ligt in Azië).


### Opdracht 16.12.1 Zoogdieren zoeken met combinaties van AND en OR

Schrijf een programma dat de diersoorten print die aan de volgende eisen voldoet:
<ol type="a">
<li>Het is een zoogdier, of het verblijft in de savanne en er zijn meer dan 3 exemplaren van.
<li>Het is een zoogdier of het verblijft in de savanne, en er zijn meer dan 3 exemplaren van.
</ol>
Leg uit waarom bij de tweede niets wordt afgedrukt.

<p>Tip: gebruik haakjes!</p>


```python
dierentuin = {
    "Leeuw": {"soort": "Zoogdier", "verblijf": "Savanne", "dieet": ["vlees"], "aantal": 2},
    "Pinguïn": {"soort": "Vogel", "verblijf": "Poolgebied", "dieet": ["vis", "kril"], "aantal": 15},
    "Python": {"soort": "Reptiel", "verblijf": "Terrarium", "dieet": ["muizen", "ratten"], "aantal": 3},
    "Olifant": {"soort": "Zoogdier", "verblijf": "Savanne", "dieet": ["planten", "fruit", "bladeren"], "aantal": 1},
    "IJsbeer": {"soort": "Zoogdier", "verblijf": "Poolgebied", "dieet": ["vlees"], "aantal": 2}
}


```

<p>Bekijk <a href="https://rweeda.github.io/PythonIA/docs/IA_H10_oplossingen.html#opgave16121" target="_blank">hier</a> de voorbeelduitwerking.</p>

<!-- ANTWOORD
for diersoort, gegevens in dierentuin.items():	#voor elk dier in de dictionary dierentuin
    if gegevens["soort"] == "Zoogdier" or (gegevens["verblijf"] == "Savanne" and gegevens["aantal"] > 3 ):	#dieren die zoogdieren zijn OF (in de savanne verblijven EN meer dan 3 exemplaren)
        print(diersoort, "is een zoogdier OF ( verblijft in de savanne EN er zijn meer dan 3 exemplaren ).")


for diersoort, gegevens in dierentuin.items():	#voor elk dier in de dictionary dierentuin
    if (gegevens["soort"] == "Zoogdier" or gegevens["verblijf"] == "Savanne") and gegevens["aantal"] > 3:    #dieren die (zoogdieren zijn OF in de savanne verblijven) EN meer dan 3 exemplaren
        print(diersoort, "is een ( zoogdier OF verblijft in de savanne ) EN er zijn meer dan 3 exemplaren.")
       
       
Bij de tweede wordt niets afgedrukt omdat aan de eerste eis alleen Leeuw, Olifant en IJsbeer voldaan, maar van geen van die zijn er meer dan 3 exemplaren      
        -->

### Opdracht 16.12.2 Zoogdieren zoeken met combinaties van AND, OR en NOT

Schrijf een programma dat de diersoorten print die aan de volgende eisen voldoet:
<ol type="a">
<li>Het is een zoogdier maar verblijft niet in de Savanne of Terrarium
<li>Het is een zoogdier of, het verblijft in de savanne maar er zijn niet minder dan 3 exemplaren van.
</ol>
Verklaar elk van je antwoorden.
<p>Tip: gebruik haakjes!</p>

<p>De verwachte uitvoer is:<br>
<i>
    IJsbeer is een zoogdier en verblijft niet in de savanne of terrarium.<br>
    Pinguïn is geen zoogdier of verblijft in de savanne en er zijn niet minder dan 3.<br>
    Python is geen zoogdier of verblijft in de savanne en er zijn niet minder dan 3.<br>
    </i>

```python
dierentuin = {
    "Leeuw": {"soort": "Zoogdier", "verblijf": "Savanne", "dieet": ["vlees"], "aantal": 2},
    "Pinguïn": {"soort": "Vogel", "verblijf": "Poolgebied", "dieet": ["vis", "kril"], "aantal": 15},
    "Python": {"soort": "Reptiel", "verblijf": "Terrarium", "dieet": ["muizen", "ratten"], "aantal": 3},
    "Olifant": {"soort": "Zoogdier", "verblijf": "Savanne", "dieet": ["planten", "fruit", "bladeren"], "aantal": 1},
    "IJsbeer": {"soort": "Zoogdier", "verblijf": "Poolgebied", "dieet": ["vlees"], "aantal": 2}
}

```



<p>Bekijk <a href="https://rweeda.github.io/PythonIA/docs/IA_H10_oplossingen.html#opgave1622" target="_blank">hier</a> de voorbeelduitwerking.</p>

<!-- ANTWOORD


#A and not (B or C)
for dier, gegevens in dierentuin.items():	#voor elk dier in de dictionary dierentuin
    if gegevens["soort"] == "Zoogdier" and not (gegevens["verblijf"] == "Savanne" or gegevens["verblijf"] == "Terrarium"):    #dieren die zoogdieren zijn en niet in de savanne of terrarium verblijven
        print(dier, "is een zoogdier en verblijft niet in de savanne of terrarium.")
# Verklaring: Er zijn drie zoogdieren (Leeuw, Olifant, IJsbeer), daarvan verblijft alleen de IJsbeer niet in de savanne of terrarium

#not A or (b and not C)
for dier, gegevens in dierentuin.items():	#voor elk dier in de dictionary dierentuin
    if not gegevens["soort"] == "Zoogdier" or (gegevens["verblijf"] == "Savanne" and not gegevens["aantal"] < 3):       #dieren die niet zoogdieren zijn of in de savanne verblijven en niet minder dan 3 zijn
        print(dier, "is geen zoogdier of verblijft in de savanne en er zijn niet minder dan 3.")
# Verklaring: Er zijn 2 dieren die geen zoogdieren zijn (Pinguïn, Python), dus die voldoen. Daarnaast zijn er twee die in de savanne verblijven (Leeuw en Olifant) maar daarvan zijn er niet genoeg exemplaren.
 -->

### Opdracht 16.12.3: Zoek zoogdieren en vogels die geen vis eten

Schrijf een programma dat alle diersoorten print die zoogdieren en vogels er zijn, maar die geen vis eten.

<p>De verwachte uitvoer is:<br>
<i>Leeuw is een Zoogdier of een vogel die geen vis eet<br>
Olifant is een Zoogdier of een vogel die geen vis eet<br>
IJsbeer is een Zoogdier of een vogel die geen vis eet</i>



<p>Bekijk <a href="https://rweeda.github.io/PythonIA/docs/IA_H10_oplossingen.html#opgave1123" target="_blank">hier</a> de voorbeelduitwerking.</p>

<!--
ANTWOORD
dierentuin = {
    "Leeuw": {"soort": "Zoogdier", "verblijf": "Savanne", "dieet": ["vlees"], "aantal": 2},
    "Pinguïn": {"soort": "Vogel", "verblijf": "Poolgebied", "dieet": ["vis", "kril"], "aantal": 15},
    "Python": {"soort": "Reptiel", "verblijf": "Terrarium", "dieet": ["muizen", "ratten"], "aantal": 3},
    "Olifant": {"soort": "Zoogdier", "verblijf": "Savanne", "dieet": ["planten", "fruit", "bladeren"], "aantal": 1},
    "IJsbeer": {"soort": "Zoogdier", "verblijf": "Poolgebied", "dieet": ["vlees"], "aantal": 2}
}


for dier, gegevens in dierentuin.items():	#voor elk dier in de dictionary dierentuin
    if (gegevens["soort"] == "Zoogdier" or gegevens["soort"] == "Vogel") and not "vis" in gegevens["dieet"] :
        print(dier, "is een Zoogdier of een Vogel die geen vis eet")

-->
<!--
Opdracht 16.X Aantal niet-vegetarische slangen of pinguins
<p>Schrijf een programma dat bepaalt hoeveel zoogdieren en vogels er zijn die geen fruit eten, en deze afdrukt.</p>

<p>Verwachte uitvoer: <i>Aantal zoogdieren of vogels in de dierentuin die geen fruit eten: 20</i></p>


```python
dierentuin = {
    "Leeuw": {"soort": "Zoogdier", "verblijf": "Savanne", "dieet": ["vlees"], "aantal": 2},
    "Pinguïn": {"soort": "Vogel", "verblijf": "Poolgebied", "dieet": ["vis", "kril"], "aantal": 15},
    "Python": {"soort": "Reptiel", "verblijf": "Terrarium", "dieet": ["muizen", "ratten"], "aantal": 3},
    "Olifant": {"soort": "Zoogdier", "verblijf": "Savanne", "dieet": ["planten", "fruit", "bladeren"], "aantal": 1},
    "IJsbeer": {"soort": "Zoogdier", "verblijf": "Poolgebied", "dieet": ["vlees"], "aantal": 2}
}


```

    Aantal zoogdieren of vogels in de dierentuin: 20


<p>Bekijk <a href="https://rweeda.github.io/PythonIA/docs/IA_H10_oplossingen.html#opgave16.X" target="_blank">hier</a> de voorbeelduitwerking.</p>

ANTWOORD:
teller = 0	#teller op 0 zetten
for dier, gegevens in dierentuin.items():	#voor elk dier in de dictionary dierentuin
    if (gegevens["soort"] == "Zoogdier" or gegevens["soort"] == "Vogel") and not""vis" in gegevens["dieet"] :	#dieren die zoogdieren of vogels zijn, maar geen fruit eten
        teller += gegevens["aantal"]	#teller optellen met het aantal dieren
print("Aantal zoogdieren of vogels in de dierentuin:", teller)
-->



<!-- NOK
## any() - controleert of er een entiteit is die aan minimaal een van de eisen voldoet.

Als je meerdere voorwaarden met een <code>of</code> in een keer wilt controleren, kan je <code>any()</code>. Met <code>any()</code> bepaal je als minstens één waarde aan de voorwaarde voldoet


Dan controleer je of minstens één van deze twee dingen klopt... maar alleen voor dat ene info object. Je controleert dus één stad, niet alle steden.


Voorbeeld 1: Staat er minstens één stad in Europa?
```python

for gegevens in steden.values():
    if any([ info["werelddeel"] == "Europa", info["inwoners"] > 1_000_000 ])


```
Toelichting:
<ul>
<li><code>steden.values()</code> geeft alle binnenste dictionaries.
<li>Voor elke <code>infogegevens</code> wordt gecontroleerd of aan de voorwaarde voldoet: werelddeel is "Europa";
<li>any() geeft True als één of meer steden in Europa liggen.



<!--
<li><code>all()</code>:	als alle waarden aan de voorwaarde voldoen
</ul>
-->

