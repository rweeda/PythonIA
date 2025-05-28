<!-- Verbeterde versie van H16_IA_11_Bool.md -->

## 11: Logische opertoren AND, OR en NOT

<p>Met <code>and</code>, <code>or</code> and <code>not</code> kun je condities samenstellen, bijvoorbeeld als je zoekt naar bepaalde informatie. Deze heten *logische operatoren*.</p>

<p>In het voorbeeld hieronder zie je het verchil tussen een <code>and</code> en een <code>or</code>. Als je de code uitvoerd zie je dat de <code>and</code> maar één stad oplevert, terwijl je met de <code>or</code> alle steden krijgt.</p>


```python
steden = {
    "Amsterdam": {"land": "Nederland", "inwoners": 921000, "werelddeel": "Europa"},
    "Buenos Aires": {"land": "Argentinië", "inwoners": 2890000, "werelddeel": "Zuid-Amerika"},
    "Rome": {"land": "Italië", "inwoners": 2873000, "werelddeel": "Europa"},
    "São Paulo": {"land": "Brazilië", "inwoners": 12330000, "werelddeel": "Zuid-Amerika"},
    "Tokyo": {"land": "Japan", "inwoners": 13960000, "werelddeel": "Azië"},

}

for stad, gegevens in steden.items():	#voor elke stad in de dictionary steden
    if steden[stad]["inwoners"] > 1000000 and steden[stad]["werelddeel"]=="Europa": # steden met meer dan 1 miljoen inwoners en in Europa
        print(stad, "heeft meer dan 1 miljoen inwoners EN ligt in Europa.")

for stad, gegevens in steden.items():	#voor elke stad in de dictionary steden
    if steden[stad]["inwoners"] > 1000000 or steden[stad]["werelddeel"]=="Europa":	# steden met meer dan 1 miljoen inwoners of in Europa
        print(stad, "heeft meer dan 1 miljoen inwoners OF ligt in Europa.")

```

<p>In het voorbeeld hieronder zie wat er gebeurt als je een <code>not</code> combineert met een <code>and</code> of <code>or</code>.</p>


```python
steden = {
    "Amsterdam": {"land": "Nederland", "inwoners": 921000, "werelddeel": "Europa"},
    "Buenos Aires": {"land": "Argentinië", "inwoners": 2890000, "werelddeel": "Zuid-Amerika"},
    "Rome": {"land": "Italië", "inwoners": 2873000, "werelddeel": "Europa"},
    "São Paulo": {"land": "Brazilië", "inwoners": 12330000, "werelddeel": "Zuid-Amerika"},
    "Tokyo": {"land": "Japan", "inwoners": 13960000, "werelddeel": "Azië"},

}

for stad, gegevens in steden.items():	#voor elke stad in de dictionary steden
    if steden[stad]["inwoners"] > 1000000 and not steden[stad]["werelddeel"]=="Europa": #steden met meer dan 1 miljoen inwoners en niet in Europa
        print(stad, "heeft meer dan 1 miljoen inwoners EN ligt NIET in Europa.")

for stad, gegevens in steden.items():	#voor elke stad in de dictionary steden
    if steden[stad]["inwoners"] > 1000000 or not steden[stad]["werelddeel"]=="Europa": # steden met meer dan 1 miljoen inwoners of niet in Europa
        print(stad, "heeft meer dan 1 miljoen inwoners OF ligt NIET in Europa.")	

```


### 16.11.1 Opdracht logische operatoren <code>and</code> en <code>or</code>

Schrijf een programma dat de diersoorten print die aan de volgende eisen voldoet:
<ol type="a">
<li>Het is een zoogdier en het verblijft in de savanne. Tip: hier zijn er twee van.
<li>Het is een zoogdier of het vervlijft in de savanne. Tip: hier zijn er 6 van.
</ol>

<!--
<p>Verwachte uitvoer:
<i>
    Leeuw is een zoogdier EN verblijft in de savanne.
    Olifant is een zoogdier EN verblijft in de savanne.
    Leeuw is een zoogdier OF verblijft in de savanne.
    Olifant is een zoogdier OF verblijft in de savanne.
    IJsbeer is een zoogdier OF verblijft in de savanne.
    Leeuw is een zoogdier OF ( verblijft in de savanne EN er zijn meer dan 3 dieren ).
    Olifant is een zoogdier OF ( verblijft in de savanne EN er zijn meer dan 3 dieren ).
    IJsbeer is een zoogdier OF ( verblijft in de savanne EN er zijn meer dan 3 dieren ).
    </i>
-->

```python
dierentuin = {
    "Leeuw": {"soort": "Zoogdier", "verblijf": "Savanne", "dieet": ["vlees"], "aantal": 2},
    "Pinguïn": {"soort": "Vogel", "verblijf": "Poolgebied", "dieet": ["vis", "kril"], "aantal": 15},
    "Python": {"soort": "Reptiel", "verblijf": "Terrarium", "dieet": ["muizen", "ratten"], "aantal": 3},
    "Olifant": {"soort": "Zoogdier", "verblijf": "Savanne", "dieet": ["planten", "fruit", "bladeren"], "aantal": 1},
    "IJsbeer": {"soort": "Zoogdier", "verblijf": "Poolgebied", "dieet": ["vlees"], "aantal": 2}
}



```



<p>Bekijk <a href="https://rweeda.github.io/PythonIA/docs/IA_H10_oplossingen.html#opgave16111" target="_blank">hier</a> de voorbeelduitwerking.</p>

<!-- ANTWOORD
for diersoort, gegevens in dierentuin.items():	#voor elk dier in de dictionary dierentuin
    if gegevens["soort"] == "Zoogdier" and gegevens["verblijf"] == "Savanne":	#dieren die zoogdieren zijn EN in de savanne verblijven
        print(diersoort, "is een zoogdier EN verblijft in de savanne.")

for diersoort, gegevens in dierentuin.items():	#voor elk dier in de dictionary dierentuin
    if gegevens["soort"] == "Zoogdier" or gegevens["verblijf"] == "Savanne":	#dieren die zoogdieren zijn OF in de savanne verblijven
        print(diersoort, "is een zoogdier OF verblijft in de savanne.")
        -->
