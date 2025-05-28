## 6: Som van waarden uit een dictionary to bepalen
<p>Met een <code>for</code>-loop kun je ook bepalen wat de som van alle waarden in de dictionary is.
    Je gebruikt daarvoor een variabele om de som bij te houden. Je doorloopt de dictionary en elk getal tel je op bij de som. Om te beginnen is de som 0. Na afloop is dat de som van alle waarden in de dictionary.</p>

<p>Met het voorbeeld hieronder bepalen we de som van het aantal inwoners:</p>




```python
steden = {
    "Amsterdam": {"land": "Nederland", "inwoners": 921000, "werelddeel": "Europa"},
    "Buenos Aires": {"land": "Argentinië", "inwoners": 2890000, "werelddeel": "Zuid-Amerika"},
    "Rome": {"land": "Italië", "inwoners": 2873000, "werelddeel": "Europa"},
    "São Paulo": {"land": "Brazilië", "inwoners": 12330000, "werelddeel": "Zuid-Amerika"},
    "Tokyo": {"land": "Japan", "inwoners": 13960000, "werelddeel": "Azië"}
}

som = 0
for stad in steden:
	som += steden[stad]["inwoners"]
print("Het totaal aantal inwoners is:", som)
```

    De som van de inwoners is: 32974000



### Opdracht 16.X Totaal aantal dieren

<p>Bepaal hoeveel dieren er in totaal in de dierentuin zijn.</p>

<p>De verwachtte uitvoer is: "<i>Het totaal aantal dieren is: 23</i>"</p>


```python
dierentuin = {
    "Leeuw": {"soort": "Zoogdier", "verblijf": "Savanne", "dieet": ["vlees"], "aantal": 2},
    "Pinguïn": {"soort": "Vogel", "verblijf": "Poolgebied", "dieet": ["vis", "kril"], "aantal": 15},
    "Python": {"soort": "Reptiel", "verblijf": "Terrarium", "dieet": ["muizen", "ratten"], "aantal": 3},
    "Olifant": {"soort": "Zoogdier", "verblijf": "Savanne", "dieet": ["planten", "fruit", "bladeren"], "aantal": 1},
    "IJsbeer": {"soort": "Zoogdier", "verblijf": "Poolgebied", "dieet": ["vlees"], "aantal": 2}
}


```

    Het totaal aantal dieren is: 23


<p>Bekijk <a href="https://rweeda.github.io/PythonIA/docs/IA_H16_oplossingen.html#opgave16XX" target="_blank">hier</a> de voorbeelduitwerking.</p>

<!-- ANTWOORD:
totaal = 0
for dier in dierentuin:
    totaal += dierentuin[dier]["aantal"]

print("Het totaal aantal dieren is:", totaal)
>


### Opdracht 16.X Aantal zoordieren

<p>Bepaal hoeveel zoogdieren dierentuin heeft.</p>

<p>De verwachte uitvoer is: "<i>Het aantal zoogdieren in de dierentuin is: 5"</i></p>



```python
dierentuin = {
    "Leeuw": {"soort": "Zoogdier", "verblijf": "Savanne", "dieet": ["vlees"], "aantal": 2},
    "Pinguïn": {"soort": "Vogel", "verblijf": "Poolgebied", "dieet": ["vis", "kril"], "aantal": 15},
    "Python": {"soort": "Reptiel", "verblijf": "Terrarium", "dieet": ["muizen", "ratten"], "aantal": 3},
    "Olifant": {"soort": "Zoogdier", "verblijf": "Savanne", "dieet": ["planten", "fruit", "bladeren"], "aantal": 1},
    "IJsbeer": {"soort": "Zoogdier", "verblijf": "Poolgebied", "dieet": ["vlees"], "aantal": 2}
}


```

    Aantal zoogdieren in de dierentuin: 5


<p>Bekijk <a href="https://rweeda.github.io/PythonIA/docs/IA_H16_oplossingen.html#opgave16XX" target="_blank">hier</a> de voorbeelduitwerking.</p>

<!-- ANTWOORD:
aantal_zoogdieren = 0
for dier in dierentuin:
    if dierentuin[dier]["soort"] == "Zoogdier":
        aantal_zoogdieren += dierentuin[dier]["aantal"]
print("Aantal zoogdieren in de dierentuin:", aantal_zoogdieren)
# Het aantal zoogdieren in de dierentuin is: 5
-->

### Opdracht 16.X Gemiddeld aantal diersoort van elk soort

<p>Onze dierentuin heeft een aantal van elk diersoort: 2 leeuwen, 15 pinguins, 3 pythons, etc. Hoeveel exemplaren zijn er van elk diersoort gemiddeld?</p>

<p>Tip: dit bereken je door de totaal aantal dieren te delen door het aantal diersorten.</p>

<p>Verwachtte uitvoer: "<i>Het gemiddelde aantal dieren per diersoort is: 4.6</i>"</p>


```python
dierentuin = {
    "Leeuw": {"soort": "Zoogdier", "verblijf": "Savanne", "dieet": ["vlees"], "aantal": 2},
    "Pinguïn": {"soort": "Vogel", "verblijf": "Poolgebied", "dieet": ["vis", "kril"], "aantal": 15},
    "Python": {"soort": "Reptiel", "verblijf": "Terrarium", "dieet": ["muizen", "ratten"], "aantal": 3},
    "Olifant": {"soort": "Zoogdier", "verblijf": "Savanne", "dieet": ["planten", "fruit", "bladeren"], "aantal": 1},
    "IJsbeer": {"soort": "Zoogdier", "verblijf": "Poolgebied", "dieet": ["vlees"], "aantal": 2}
}



som = 0
for dier in dierentuin:
    som += dierentuin[dier]["aantal"]
print("Het totaal aantal dieren is:", som)

print("Het totaal aantal diersoorten is:", len(dierentuin) )

gemiddeld = som / len(dierentuin)
print("Het gemiddelde aantal dieren per diersoort is:", gemiddeld)

```

    Het totaal aantal dieren is: 23
    Het gemiddelde aantal dieren per diersoort is: 4.6


<p>Bekijk <a href="https://rweeda.github.io/PythonIA/docs/IA_H16_oplossingen.html#opgave16XX" target="_blank">hier</a> de voorbeelduitwerking.</p>
<!-- ANTWOORD>
