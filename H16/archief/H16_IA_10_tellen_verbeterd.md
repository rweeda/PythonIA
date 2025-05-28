<!-- Verbeterde versie van H16_IA_10_tellen.md -->

## 10: Aantal voorkomens van een specifiek gegeven in een dictionary tellen

<p>Wil je tellen hoe vaak iets voorkomt in een (geneste)dictionary, dan moet je een teller bijhouden. Doorloop de dictionary op zoek naar het gegeven dat je zoekt. Elke keer als je het gezochte gegeven tegenkomt, hoog je de teller op. Bekijk het voorbeeld hieronder waarbij we tellen hoeveel miljoenensteden er zijn (steden met meer dan 1000000 inwoners):</p>

<p><img src="https://course.cs.ru.nl/pythonVO/img/16.3_genesteDict_voorkomensTellen_stroomdiagram.png" alt="Figuur: Stroomdiagram voorkomens tellen" width="400"></p>



```python
steden = {
    "Amsterdam": {"land": "Nederland", "inwoners": 921000, "werelddeel": "Europa"},
    "Buenos Aires": {"land": "Argentinië", "inwoners": 2890000, "werelddeel": "Zuid-Amerika"},
    "Rome": {"land": "Italië", "inwoners": 2873000, "werelddeel": "Europa"},
    "São Paulo": {"land": "Brazilië", "inwoners": 12330000, "werelddeel": "Zuid-Amerika"},
    "Tokyo": {"land": "Japan", "inwoners": 13960000, "werelddeel": "Azië"}
}

aantalMiljoenensteden = 0	#teller begint op 0
for stad in steden:
	if steden[stad]["inwoners"] > 1000000:	#als de inwoners meer zijn dan 1 miljoen
		aantalMiljoenensteden += 1	#teller ophogen zodra element gevonden is

print("Aantal miljoenensteden is:", aantalMiljoenensteden)

```

<p>Toelichting:</p>
<ul>
    <li>zet een teller op 0.</li>
    <li>met een <code>for</code>-loop doorloop je ieder geneste dictionary (stad) in de dictionary <code>steden</code>;</li>
    <li>als je in de geneste dictionary de waarde vindt dat aan de voorwaarde voldoet, dan hoog je de teller op.
    </li>
</ul>


### Opdracht 16.10.1 Aantal Zuid-Amerikaanse landen tellen

<p>Schrijf een programma dat telt hoeveel Zuid-Amerikaanse landen er in onze `steden`-dictionary voorkomen. Druk dit aantal af.</p>

<p>De verwachte uitvoer is:<br>
<i>Aantal Zuid-Amerikaanse steden is: 2</i></p>




```python
steden = {
    "Amsterdam": {"land": "Nederland", "inwoners": 921000, "werelddeel": "Europa"},
    "Buenos Aires": {"land": "Argentinië", "inwoners": 2890000, "werelddeel": "Zuid-Amerika"},
    "Rome": {"land": "Italië", "inwoners": 2873000, "werelddeel": "Europa"},
    "São Paulo": {"land": "Brazilië", "inwoners": 12330000, "werelddeel": "Zuid-Amerika"},
    "Tokyo": {"land": "Japan", "inwoners": 13960000, "werelddeel": "Azië"}
}
```


<p>Bekijk <a href="https://rweeda.github.io/PythonIA/docs/IA_H10_oplossingen.html#opgave16101" target="_blank">hier</a> de voorbeelduitwerking.</p>

### Opdracht 16.10.2 Aantal soorten in het Poolgebied

<p>Bepaal hoeveel soorten er om het Poolgebied verblijven. Print dit.</p>

<p>De verwachte uitvoer is:<br> <i>Aantal dieren in het Poolgebied: 2</i></p>


```python
dierentuin = {
    "Leeuw": {"soort": "Zoogdier", "verblijf": "Savanne", "dieet": ["vlees"], "aantal": 2},
    "Pinguïn": {"soort": "Vogel", "verblijf": "Poolgebied", "dieet": ["vis", "kril"], "aantal": 15},
    "Python": {"soort": "Reptiel", "verblijf": "Terrarium", "dieet": ["muizen", "ratten"], "aantal": 3},
    "Olifant": {"soort": "Zoogdier", "verblijf": "Savanne", "dieet": ["planten", "fruit", "bladeren"], "aantal": 1},
    "IJsbeer": {"soort": "Zoogdier", "verblijf": "Poolgebied", "dieet": ["vlees"], "aantal": 2}
}


```

<p>Bekijk <a href="https://rweeda.github.io/PythonIA/docs/IA_H10_oplossingen.html#opgave16102" target="_blank">hier</a> de voorbeelduitwerking.</p>


<!--
ANTWOORD:
dierentuin = {
    "Leeuw": {"soort": "Zoogdier", "verblijf": "Savanne", "dieet": ["vlees"], "aantal": 2},
    "Pinguïn": {"soort": "Vogel", "verblijf": "Poolgebied", "dieet": ["vis", "kril"], "aantal": 15},
    "Python": {"soort": "Reptiel", "verblijf": "Terrarium", "dieet": ["muizen", "ratten"], "aantal": 3},
    "Olifant": {"soort": "Zoogdier", "verblijf": "Savanne", "dieet": ["planten", "fruit", "bladeren"], "aantal": 1},
    "IJsbeer": {"soort": "Zoogdier", "verblijf": "Poolgebied", "dieet": ["vlees"], "aantal": 2}
}

aantal_poolgebied = 0

for dier, info in dierentuin.items():
    if info["verblijf"] == "Poolgebied":
        aantal_poolgebied += 1

print("Aantal dieren in het Poolgebied:", aantal_poolgebied)

-->