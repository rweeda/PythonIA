<!-- Herschreven versie van H16_IA_2_opvragen.md -->



## 2: Informatie opvragen uit een geneste dictionary

<p>Je kunt gegevens van meerdere steden samen opslaan in een geneste dictionary.  Elke stad, zoals (<b>Amsterdam, Parijs, Berlijn</b>), heeft dan een eigen dictionary met specifieke informatie.<br>
<img src="https://raw.githubusercontent.com/rweeda/PythonIA/main/img/dictionary_steden.png" width="500">


<p>Met <code>steden["Parijs"]</code> haal je de dictionary met gegevens over Parijs op. Door hier een tweede sleutel aan toe te voegen, zoals <b>land</b>, kun je een specifieke waarde opvragen:</p><p><code>steden["Parijs"]["land"]</code>.</p>


```python
steden = {
    "Amsterdam":{"land": "Nederland", "inwoners": 921000},
    "Parijs": {"land": "Frankrijk", "inwoners": 2148000},
    "Berlijn": {"land": "Duitsland", "inwoners": 3769000}
}

print(steden["Parijs"])   # Geeft {"land": "Frankrijk", "inwoners": 2148000}
print(steden["Parijs"]["land"])   # Geeft "Frankrijk"
```





### Opdracht 16.2.1: Gegevens uit `dierentuin` printen

<p>Hieronder staat in dictionary <code>dierentuin</code> gegevens over verschillende dieren in een dierentuin.
<ol type="a">
<li>Print alle informatie over de <b>pinguïn</b>.</li>
<li>Print het verblijf van de <b>pinguïn</b>.</li>
</ol>

<p>
<p>De verwachte uitvoer is:<br>
<i>
Alle informatie over de Pinguïn: {'soort': 'Vogel', 'verblijf': 'Poolgebied', 'dieet': ['vis', 'kril'], 'aantal': 15}
<br>
Het verblijf van de Pinguïn is: Poolgebied</i>
</p>


```python
dierentuin = {
    "Leeuw": {"soort": "Zoogdier", "verblijf": "Savanne", "dieet": ["vlees"], "aantal": 2},
    "Pinguïn": {"soort": "Vogel", "verblijf": "Poolgebied", "dieet": ["vis", "kril"], "aantal": 15},
    "Python": {"soort": "Reptiel", "verblijf": "Terrarium", "dieet": ["muizen", "ratten"], "aantal": 3}
}
```

<p>Klik <a href="https://rweeda.github.io/PythonIA/docs/IA_H15_oplossingen.html#opgave1621">hier</a> voor een voorbeelduitwerking.</p>
<!-- ANTWOORD
#b: Print alle informatie over de Pinguïn
print("Alle informatie over de Pinguïn:", dierentuin["Pinguïn"])
#c: Print de verblijf van de Pinguïn 
print("Het verblijf van de Pinguïn is:", dierentuin["Pinguïn"]["verblijf"])
-->
