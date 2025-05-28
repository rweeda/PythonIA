<!-- Herschreven versie van H16_IA_6_gegevensTellen.md -->

## 6: Aantal gegevens in geneste dictionary tellen

<p>Met <code>len()</code> kun je bepalen hoe veel gegevens een (geneste)dictionary bevat. Je geeft dan tussen de haakjes de dictionary mee. Bekijk het voorbeeld: </p>




```python
steden = {
    "Amsterdam": {"land": "Nederland", "inwoners": 921000, "werelddeel": "Europa"},
    "Buenos Aires": {"land": "Argentinië", "inwoners": 2890000, "werelddeel": "Zuid-Amerika"},
    "Rome": {"land": "Italië", "inwoners": 2873000, "werelddeel": "Europa"},
    "São Paulo": {"land": "Brazilië", "inwoners": 12330000, "werelddeel": "Zuid-Amerika"},
    "Tokyo": {"land": "Japan", "inwoners": 13960000, "werelddeel": "Azië"}
}

print("Aantal steden:", len(steden))
```

    Aantal steden: 5


### Opdracht 16.6.1 Aantal diersoorten tellen

<p>Print hoeveel diersoorten er in de dierentuin zijn, dus Leeuw, Pinguïn, Python, etc.</p>

<p>De verwachte uitvoer is:<br>
<i>Er zijn 5 verschillende diersoorten in de dierentuin.</i></p>



```python
dierentuin = {
    "Leeuw": {"soort": "Zoogdier", "verblijf": "Savanne", "dieet": ["vlees"], "aantal": 2},
    "Pinguïn": {"soort": "Vogel", "verblijf": "Poolgebied", "dieet": ["vis", "kril"], "aantal": 15},
    "Python": {"soort": "Reptiel", "verblijf": "Terrarium", "dieet": ["muizen", "ratten"], "aantal": 3},
    "Olifant": {"soort": "Zoogdier", "verblijf": "Savanne", "dieet": ["planten", "fruit", "bladeren"], "aantal": 1},
    "IJsbeer": {"soort": "Zoogdier", "verblijf": "Poolgebied", "dieet": ["vlees"], "aantal": 2}
}


```



<p>Bekijk <a href="https://rweeda.github.io/PythonIA/docs/IA_16_oplossingen.html#opgave1661" target="_blank">hier</a> de voorbeelduitwerking.</p>

<!-- ANTWOORD 
dierentuin = {
    "Leeuw": {"soort": "Zoogdier", "verblijf": "Savanne", "dieet": ["vlees"], "aantal": 2},
    "Pinguïn": {"soort": "Vogel", "verblijf": "Poolgebied", "dieet": ["vis", "kril"], "aantal": 15},
    "Python": {"soort": "Reptiel", "verblijf": "Terrarium", "dieet": ["muizen", "ratten"], "aantal": 3},
    "Olifant": {"soort": "Zoogdier", "verblijf": "Savanne", "dieet": ["planten", "fruit", "bladeren"], "aantal": 1},
    "IJsbeer": {"soort": "Zoogdier", "verblijf": "Poolgebied", "dieet": ["vlees"], "aantal": 2}
}


print("Er zijn", len(dierentuin), "verschillende diersoorten in de dierentuin.")

-->
