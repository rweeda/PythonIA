## 2: Waarden uit een dictionary filteren en in een lijst zetten

<p>Soms wil je alleen bepaalde waarden uit een dictionary hebben, bijvoorbeeld alle getallen, behalve 0. Die waarden sla je in een lijst op. Dat noemen we <i>filteren</i>. Je maakt een nieuwe lege lijst aan en vul je aan met de waarden uit de dictionary die je wilt hebben.</p>

TODO IMAGE AANPASSEN NAAR DICTIONARY
<p><img src="https://course.cs.ru.nl/pythonVO/img/10.2FilterWeekendenEruit_Stroomdiagram.png" alt="Figuur: Stroomdiagram waarden eruit filteren" width="400"></p>


<p>In het voorbeeld hieronder voegen we elk Zuid-Amerikaanse stad toe aan een nieuwe lijst <code>zuidAmerikaLijst</code>:</p>



```python
steden = {
    "Amsterdam": {"land": "Nederland", "inwoners": 921000, "werelddeel": "Europa"},
    "Buenos Aires": {"land": "Argentinië", "inwoners": 2890000, "werelddeel": "Zuid-Amerika"},
    "Rome": {"land": "Italië", "inwoners": 2873000, "werelddeel": "Europa"},
    "São Paulo": {"land": "Brazilië", "inwoners": 12330000, "werelddeel": "Zuid-Amerika"},
    "Tokyo": {"land": "Japan", "inwoners": 13960000, "werelddeel": "Azië"}
}

zuidAmerikaLijst =[]                                # maak een lege lijst
for stad, gegevens in steden.items():               # loop door de dictionary en haal de gegevens voor elke stad op
	if gegevens["werelddeel"] == "Zuid-Amerika":    # als de werelddeel Zuid-Amerika is
		zuidAmerikaLijst.append( stad )	            #voeg stad toe aan zuidAmerikaLijst

print("Lijst met Zuid-Amerikaanse steden:", zuidAmerikaLijst)
```

<p>Toelichting:</p>
<ul>
    <li>We maken een nieuwe lijst aan: <code>zuidAmerikaLijst</code>.</li>
    <li>Met een <code>for</code>-loop doorlopen we ieder stad in de dictionary</li>
    <li>Als we een stad tegenkomen die in Zuid-Amerika ligt, dan voegen we die aan <code>zuidAmerikaLijst</code> toe.</li>
</ul>
Na afloop hebben we dus onze oorspronkelijke dictionary en een nieuwe lijst <code>zuidAmerikaLijst</code> met de Zuid-Amerikaanse steden.

### Opdracht 16.5 Miljoenensteden

Doorloop de dictionary en lever een lijst op met miljoenensteden (steden met meer dan 1000000 inwoners). Print de lijst om te controleren of vier van de steden erin voorkomen.


```python
steden = {
    "Amsterdam": {"land": "Nederland", "inwoners": 921000, "werelddeel": "Europa"},
    "Buenos Aires": {"land": "Argentinië", "inwoners": 2890000, "werelddeel": "Zuid-Amerika"},
    "Rome": {"land": "Italië", "inwoners": 2873000, "werelddeel": "Europa"},
    "São Paulo": {"land": "Brazilië", "inwoners": 12330000, "werelddeel": "Zuid-Amerika"},
    "Tokyo": {"land": "Japan", "inwoners": 13960000, "werelddeel": "Azië"}
}


```

<p>Klik <a href="https://rweeda.github.io/PythonIA/docs/IA_H15_oplossingen.html#opgave165">hier</a> voor een voorbeelduitwerking.</p>

<!-- ANTWOORD
miljoenenstedenLijst =[]                            # maak een lege lijst
for stad, gegevens in steden.items():               # loop door de dictionary en haal de gegevens voor elke stad op
	if gegevens["inwoners"] > 1000000 :              # als er meer dan 1 miljoen inwoners zijn
		miljoenenstedenLijst.append( stad )	        # voeg stad toe aan miljoenenstedenLijst

print("Lijst met miljoenensteden:", miljoenenstedenLijst)
-->


### Opdracht 16.6 Lijst van alle dieren in de Savanne

Druk een lijst af van alle dieren in de `Dierentuin' die in de Savanne verblijven.


```python
dierentuin = {
    "Leeuw": {"soort": "Zoogdier", "verblijf": "Savanne", "dieet": ["vlees"], "aantal": 2},
    "Pinguïn": {"soort": "Vogel", "verblijf": "Poolgebied", "dieet": ["vis", "kril"], "aantal": 15},
    "Python": {"soort": "Reptiel", "verblijf": "Terrarium", "dieet": ["muizen", "ratten"], "aantal": 3},
    "Olifant": {"soort": "Zoogdier", "verblijf": "Savanne", "dieet": ["planten", "fruit", "bladeren"], "aantal": 1},
    "IJsbeer": {"soort": "Zoogdier", "verblijf": "Poolgebied", "dieet": ["vlees"], "aantal": 2}
}
```


<p>Bekijk <a href="https://rweeda.github.io/PythonIA/docs/IA_H10_oplossingen.html#opgave166" target="_blank">hier</a> de voorbeelduitwerking.</p>

<!--
dierentuin = {
    "Leeuw": {"soort": "Zoogdier", "verblijf": "Savanne", "dieet": ["vlees"], "aantal": 2},
    "Pinguïn": {"soort": "Vogel", "verblijf": "Poolgebied", "dieet": ["vis", "kril"], "aantal": 15},
    "Python": {"soort": "Reptiel", "verblijf": "Terrarium", "dieet": ["muizen", "ratten"], "aantal": 3},
    "Olifant": {"soort": "Zoogdier", "verblijf": "Savanne", "dieet": ["planten", "fruit", "bladeren"], "aantal": 1},
    "IJsbeer": {"soort": "Zoogdier", "verblijf": "Poolgebied", "dieet": ["vlees"], "aantal": 2}
}

savanneLijst = []                                 # maak een lege lijst
for dier, gegevens in dierentuin.items():        # loop door de dictionary en haal de gegevens voor elk dier op
    if gegevens["verblijf"] == "Savanne":         # als het verblijf Savanne is
        savanneLijst.append(dier)                  # voeg het dier toe aan savanneLijst

print(savanneLijst)
-->

### Opdracht 16.7 Lijst van alle dieren die vlees eten

Druk een lijst af van alle dieren in de `Dierentuin' die vlees eten.



```python
dierentuin = {
    "Leeuw": {"soort": "Zoogdier", "verblijf": "Savanne", "dieet": ["vlees"], "aantal": 2},
    "Pinguïn": {"soort": "Vogel", "verblijf": "Poolgebied", "dieet": ["vis", "kril"], "aantal": 15},
    "Python": {"soort": "Reptiel", "verblijf": "Terrarium", "dieet": ["muizen", "ratten"], "aantal": 3},
    "Olifant": {"soort": "Zoogdier", "verblijf": "Savanne", "dieet": ["planten", "fruit", "bladeren"], "aantal": 1},
    "IJsbeer": {"soort": "Zoogdier", "verblijf": "Poolgebied", "dieet": ["vlees"], "aantal": 2}
}

```

    ['L', 'e', 'e', 'u', 'w', 'I', 'J', 's', 'b', 'e', 'e', 'r']



<p>Bekijk <a href="https://rweeda.github.io/PythonIA/docs/IA_H10_oplossingen.html#opgave16.7" target="_blank">hier</a> de voorbeelduitwerking.</p>

<!--
dierentuin = {
    "Leeuw": {"soort": "Zoogdier", "verblijf": "Savanne", "dieet": ["vlees"], "aantal": 2},
    "Pinguïn": {"soort": "Vogel", "verblijf": "Poolgebied", "dieet": ["vis", "kril"], "aantal": 15},
    "Python": {"soort": "Reptiel", "verblijf": "Terrarium", "dieet": ["muizen", "ratten"], "aantal": 3},
    "Olifant": {"soort": "Zoogdier", "verblijf": "Savanne", "dieet": ["planten", "fruit", "bladeren"], "aantal": 1},
    "IJsbeer": {"soort": "Zoogdier", "verblijf": "Poolgebied", "dieet": ["vlees"], "aantal": 2}
}

vleesDiet = []                                 # maak een lege lijst
for dier, gegevens in dierentuin.items():        # loop door de dictionary en haal de gegevens voor elk dier op
    if "vlees" in gegevens["dieet"]:            # als er vlees in het dieet van het dier zit
        vleesDiet.append(dier)                  # voeg het dier toe aan vleesDiet

print(vleesDiet)
-->

### Opdracht 16.x Lijst van alle benodigde eten

<p>Maak een lijst van alle eten dat gehaald moet worden voor de dieren. Druk de lijst af.</p>


```python
dierentuin = {
    "Leeuw": {"soort": "Zoogdier", "verblijf": "Savanne", "dieet": ["vlees"], "aantal": 2},
    "Pinguïn": {"soort": "Vogel", "verblijf": "Poolgebied", "dieet": ["vis", "kril"], "aantal": 15},
    "Python": {"soort": "Reptiel", "verblijf": "Terrarium", "dieet": ["muizen", "ratten"], "aantal": 3},
    "Olifant": {"soort": "Zoogdier", "verblijf": "Savanne", "dieet": ["planten", "fruit", "bladeren"], "aantal": 1},
    "IJsbeer": {"soort": "Zoogdier", "verblijf": "Poolgebied", "dieet": ["vlees"], "aantal": 2}
}

```

    ['vlees', 'vis', 'kril', 'muizen', 'ratten', 'planten', 'fruit', 'bladeren', 'vlees']


<p>Bekijk <a href="https://rweeda.github.io/PythonIA/docs/IA_H10_oplossingen.html#opgave16.X" target="_blank">hier</a> de voorbeelduitwerking.</p>

<!-- ANTWOORD

dierentuin = {
    "Leeuw": {"soort": "Zoogdier", "verblijf": "Savanne", "dieet": ["vlees"], "aantal": 2},
    "Pinguïn": {"soort": "Vogel", "verblijf": "Poolgebied", "dieet": ["vis", "kril"], "aantal": 15},
    "Python": {"soort": "Reptiel", "verblijf": "Terrarium", "dieet": ["muizen", "ratten"], "aantal": 3},
    "Olifant": {"soort": "Zoogdier", "verblijf": "Savanne", "dieet": ["planten", "fruit", "bladeren"], "aantal": 1},
    "IJsbeer": {"soort": "Zoogdier", "verblijf": "Poolgebied", "dieet": ["vlees"], "aantal": 2}
}


voedingLijst = []                                 # maak een lege lijst
for dier, gegevens in dierentuin.items():        # loop door de dictionary en haal de gegevens voor elk dier op
    voedingLijst.append(gegevens["dieet"])                   
print(voedingLijst)

OF


voedingLijst = []                                 # maak een lege lijst
for dier, gegevens in dierentuin.items():        # loop door de dictionary en haal de gegevens voor elk dier op             
    voedingLijst += gegevens["dieet"]     
print(voedingLijst)


>

