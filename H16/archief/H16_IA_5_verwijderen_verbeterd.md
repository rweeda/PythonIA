<!-- Herschreven versie van H16_IA_5_verwijderen.md -->


<!--H16_verwijderen-->

## 5: Gegevens verwijderen

<p>Met <code>del</code> kun je gegevens verwijderen uit een dictionary. Je zet er de naam van de dictionary achter met tussen vierkant haken <code>[ ]</code> de sleutel van de gegevens dat je wilt verwijderen. In het voorbeeld hieronder verwijderen we de sleutel 'Berlijn' en de bijbehorende gegevens.</p> 


```python
steden = {
    "Amsterdam":{"land": "Nederland", "inwoners": 921000},
    "Parijs": {"land": "Frankrijk", "inwoners": 2148000},
    "Berlijn": {"land": "Duitsland", "inwoners": 3769000},
}

del steden["Berlijn"]   # Verwijder de stad Berlijn (sleutel) uit de dictionary
print(steden)   # Print de dictionary
```



### Opdracht 16.5.1 Olifant verwijderen

De Olifanten zijn overgeplaatst naar een ander dierentuin.
<ol type="a">
<li>Verwijder de olifant-soort uit de dierentuin dictionary;
<li>Print alle informatie over het dierentuin om te controleren of het dier inderdaad is verwijderd.
</ol>

```python
dierentuin = {
    "Leeuw": {"soort": "Zoogdier", "verblijf": "Savanne", "dieet": ["vlees"], "aantal": 2},
    "Pinguïn": {"soort": "Vogel", "verblijf": "Poolgebied", "dieet": ["vis", "kril"], "aantal": 15},
    "Python": {"soort": "Reptiel", "verblijf": "Terrarium", "dieet": ["muizen", "ratten"], "aantal": 3},
    "Olifant": {"soort": "Zoogdier", "verblijf": "Savanne",  "dieet": ["planten", "fruit", "bladeren"],
        "aantal": 6}
}

```
<p>Klik <a href="https://rweeda.github.io/PythonIA/docs/IA_H15_oplossingen.html#opgave1651">hier</a> voor een voorbeelduitwerking.</p>

<!-- ANTWOORD
del dierentuin["Olifant"]
print(dierentuin)   
-->

