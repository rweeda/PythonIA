### Een geneste dictionary doorlopen met een <code>for</code>-loop

<p>Met een <code>for</code>-loop en <code>.items()</code> kun je alle sleutels één voor één doorlopen, om bijvoorbeeld de bijbehorende dictionary af te drukken:</p>




```python
steden = {
    "Amsterdam": {"land": "Nederland", "inwoners": 921000},
    "Parijs": {"land": "Frankrijk", "inwoners": 2148000},
    "Berlijn": {"land": "Duitsland", "inwoners": 3769000}
}

# Door de steden lopen en alle gegevens printen
for stad, gegevens in steden.items():
    print( stad,  "ligt in", gegevens['land'], "en heeft", gegevens['inwoners'], "inwoners.")

```

### Opdracht geneste dictionary doorlopen met een for-loop

Gebruik een <code>for</code>-loop om alle dieren uit de dierentuin dictioanry en hun gegevens netjes af te drukken.


```python
dierentuin = {
    "Leeuw": {"soort": "Zoogdier", "verblijf": "Savanne", "dieet": ["vlees"], "aantal": 2},
    "Pinguïn": {"soort": "Vogel", "verblijf": "Poolgebied", "dieet": ["vis", "kril"], "aantal": 15},
    "Python": {"soort": "Reptiel", "verblijf": "Terrarium", "dieet": ["muizen", "ratten"], "aantal": 3}
}

```

<p>Klik <a href="https://rweeda.github.io/PythonIA/docs/IA_H15_oplossingen.html#opgave164">hier</a> voor een voorbeelduitwerking.</p>
<!-- ANTWOORD
# Druk de informatie van alle dieren (netjes) af
print("Alle dieren:")
for dier, gegevens in dierentuin.items():
    print(dier, "is van het soort", gegevens['soort'], "leeft in", gegevens['verblijf'], "en er zijn er", gegevens['aantal'], "van.")

-->
