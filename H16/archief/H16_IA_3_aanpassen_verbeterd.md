
<!--H16_aanpassen-->
## 3: Een waarde in een geneste dictionary aanpassen

Je kunt ook een waarde aanpassen in een geneste dictionary. Dit doe je door met vierkante haken aan te geven welke sleutels je nodig hebt om bij de juiste waarde te komen. Daarna geef je met een '='-teken aan wat de nieuwe waarde wordt. Bijvoorbeeld, met de volgende regel wordt het aantal inwoners van Parijs aangepast:<br><br>
<code>steden["Parijs"]["inwoners"] = 2200000</code>

### Opdracht 16.3.1 Aantal inwoners van Berlijn aanpassen

<p>Schrijf code om "Duitsland" te vervangen door de afkorting "DL". Print daarna het land om te controleren of de wijziging is doorgevoerd.</p>

<p>De verwachte uitvoer is:<br><i>DL</i></p>


```python
steden = {
    "Amsterdam":{"land": "Nederland", "inwoners": 921000},
    "Parijs": {"land": "Frankrijk", "inwoners": 2148000},
    "Berlijn": {"land": "Duitsland", "inwoners": 3769000},
}

steden["Berlijn"]["land"] = "DL"
print(steden["Berlijn"]["land"])

```




<p>Klik <a href="https://rweeda.github.io/PythonIA/docs/IA_H15_oplossingen.html#opgave1631">hier</a> voor een voorbeelduitwerking.</p>
<!-- steden["Berlijn"]["land"] = "DL"
print(steden["Berlijn"]["land"])   # Geeft "DL"
-->


### Opdracht 16.3.2: Er is een Python geboren

<p>Mooi nieuws, in de dierentuin is een Python geboren.</p>

<ol type="a">
<li>Pas het aantal Pythons aan naar 4;</li>
<li>Print het aantal Pythons.</li>
</ol>

```python
dierentuin = {
    "Leeuw": {"soort": "Zoogdier", "verblijf": "Savanne", "dieet": ["vlees"], "aantal": 2},
    "Pinguïn": {"soort": "Vogel", "verblijf": "Poolgebied", "dieet": ["vis", "kril"], "aantal": 15},
    "Python": {"soort": "Reptiel", "verblijf": "Terrarium", "dieet": ["muizen", "ratten"], "aantal": 3}
}
```


<p>Klik <a href="https://rweeda.github.io/PythonIA/docs/IA_H15_oplossingen.html#opgave1632">hier</a> voor een voorbeelduitwerking.</p>
<!-- ANTWOORD
# Pas het aantal Pythons aan naar 4
dierentuin["Python"]["aantal"] = 4
print(dierentuin)
-->


