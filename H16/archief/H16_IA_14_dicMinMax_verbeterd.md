<!-- Verbeterde versie van H16_IA_13_dicMinMax.md -->

## 14: Kleinste en grootste waarde uit een dictionary bepalen

<p>Om te bepalen wat de kleinste of grootste waarde in een dictionary is gebruik je het <i>minimumplan</i> (Deze is behandeld in <a href="https://moodle.informatica-actief.nl/mod/url/view.php?id=82097">Onderwerp 10.5</a>).


<p>Met een <code>for</code>-loop kun je ook bepalen wat het kleinste (of grootste) getal is dat in een dictionary voorkomt. Je gebruikt hiervoor een variabele om bij te houden wat de kleinste waarde is die je tot dan toe gezien hebt. Kom je nog een kleinere waarde tegen, dan sla je die kleinere waarde op in je variabele. Om te beginnen is de eerste waarde gelijk aan oneindig: <code>float(inf)</code>.</p>


TODO NEW AFBEELDING
<p><img src="https://course.cs.ru.nl/pythonVO/img/10.5Kleinste_Stroomdiagram.jpg" alt="Figuur: Stroomdiagram kleinste" width="400"></p>




```python
steden = {
    "Amsterdam": {"land": "Nederland", "inwoners": 921000, "werelddeel": "Europa"},
    "Buenos Aires": {"land": "Argentinië", "inwoners": 2890000, "werelddeel": "Zuid-Amerika"},
    "Rome": {"land": "Italië", "inwoners": 2873000, "werelddeel": "Europa"},
    "São Paulo": {"land": "Brazilië", "inwoners": 12330000, "werelddeel": "Zuid-Amerika"},
    "Tokyo": {"land": "Japan", "inwoners": 13960000, "werelddeel": "Azië"},
}

# Initialiseer het huidige minimum
min_inwoners = float(inf) # begin met oneindig groot
kleinste_stad =  ""       # er is geen stad

# Doorloop alle steden in de dictionary
for stad in stad_namen:
    # Vergelijk het aantal inwoners met het huidige minimum
    if steden[stad]["inwoners"] < min_inwoners:
        min_inwoners = steden[stad]["inwoners"] 	 	
        kleinste_stad = stad

print("De stad met de minste inwoners is", kleinste_stad, "met", min_inwoners, "inwoners.")
```


### 16.14.1 Kleinst aantal exemplaren

Schrijf een programma dat de dierentuin dictionary doorloopt en print van welk dier het minst voorkomen, en welk dier dat is.

<p>De verwachte uitvoer is:<br>
<i></i></p>
```python
dierentuin = {
    "Leeuw": {"soort": "Zoogdier", "verblijf": "Savanne", "dieet": ["vlees"], "aantal": 2},
    "Pinguïn": {"soort": "Vogel", "verblijf": "Poolgebied", "dieet": ["vis", "kril"], "aantal": 15},
    "Python": {"soort": "Reptiel", "verblijf": "Terrarium", "dieet": ["muizen", "ratten"], "aantal": 3},
    "Olifant": {"soort": "Zoogdier", "verblijf": "Savanne", "dieet": ["planten", "fruit", "bladeren"], "aantal": 1},
    "IJsbeer": {"soort": "Zoogdier", "verblijf": "Poolgebied", "dieet": ["vlees"], "aantal": 2}
}
```

<p>Bekijk <a href="https://rweeda.github.io/PythonIA/docs/IA_H10_oplossingen.html#opgave16141" target="_blank">hier</a> de voorbeelduitwerking.</p>

<!--
ANTWOORD



dierentuin = {
    "Leeuw": {"soort": "Zoogdier", "verblijf": "Savanne", "dieet": ["vlees"], "aantal": 2},
    "Pinguïn": {"soort": "Vogel", "verblijf": "Poolgebied", "dieet": ["vis", "kril"], "aantal": 15},
    "Python": {"soort": "Reptiel", "verblijf": "Terrarium", "dieet": ["muizen", "ratten"], "aantal": 3},
    "Olifant": {"soort": "Zoogdier", "verblijf": "Savanne", "dieet": ["planten", "fruit", "bladeren"], "aantal": 1},
    "IJsbeer": {"soort": "Zoogdier", "verblijf": "Poolgebied", "dieet": ["vlees"], "aantal": 2}
}

# Startwaarden instellen:
# - min_aantal wordt op een heel hoog getal gezet, zodat elke echte waarde kleiner zal zijn
# - dier_met_minste houdt bij van welk dier dit is
min_aantal = float("inf")
dier_met_minste = ""

# Loop door elk dier en bijbehorende informatie in de dictionary
for dier, info in dierentuin.items():
    # Vergelijk het aantal met het huidige minimum
    if info["aantal"] < min_aantal:
        # Als dit dier minder exemplaren heeft, sla dat dan op
        min_aantal = info["aantal"]
        dier_met_minste = dier

# Toon het resultaat netjes in een zin
print("Het dier met het minste aantal is de", dier_met_minste, "met", min_aantal, "exemplaren.")

-->

### 16.14.2 Meeste exemplaren
<p>Schrijf een programma dat de dierentuin dictionary doorloopt en print van welk dier er het meest zijn, en welk dier dat is.</p>

<p>Tip: gebruik <code>float(-inf)</code> om het maximum op -oneindig te initialiseren.</p>

<p>De verwachte uitvoer is:<br>
<i></i></p>
```python
dierentuin = {
    "Leeuw": {"soort": "Zoogdier", "verblijf": "Savanne", "dieet": ["vlees"], "aantal": 2},
    "Pinguïn": {"soort": "Vogel", "verblijf": "Poolgebied", "dieet": ["vis", "kril"], "aantal": 15},
    "Python": {"soort": "Reptiel", "verblijf": "Terrarium", "dieet": ["muizen", "ratten"], "aantal": 3},
    "Olifant": {"soort": "Zoogdier", "verblijf": "Savanne", "dieet": ["planten", "fruit", "bladeren"], "aantal": 1},
    "IJsbeer": {"soort": "Zoogdier", "verblijf": "Poolgebied", "dieet": ["vlees"], "aantal": 2}
}
```
<p>Bekijk <a href="https://rweeda.github.io/PythonIA/docs/IA_H10_oplossingen.html#opgave16142" target="_blank">hier</a> de voorbeelduitwerking.</p>

<!--
ANTWOORD
# Startwaarden instellen:
# - max_aantal wordt op 0 gezet, omdat elk dier minstens 1 exemplaar heeft
# - dier_met_meeste houdt bij van welk dier dit is
max_aantal = 0
dier_met_meeste = ""

# Loop door elk dier en bijbehorende informatie in de dictionary
for dier, info in dierentuin.items():
    # Vergelijk het aantal met het huidige maximum
    if info["aantal"] > max_aantal:
        # Als dit dier meer exemplaren heeft, sla dat dan op
        max_aantal = info["aantal"]
        dier_met_meeste = dier

# Toon het resultaat netjes in een zin
print("Het dier met het meeste aantal is de", dier_met_meeste, "met", max_aantal, "exemplaren.")


-->
