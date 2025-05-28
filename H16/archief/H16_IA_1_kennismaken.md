## 1: Inleiding geneste dictionary's

Een dictionary kan ook binnenin een andere dictionary zitten; dit heet een <b>geneste dictionary</b>. Een geneste dictionary is handig om gegevens van meerdere objecten overzichtelijk en gestructureerd op te slaan. Dit leggen we uit aan de hand van een voorbeeld. We hebben een aantal dictionary's met informatie over steden, bijvoorbeeld over Amsterdam, Parijs en Berlijn. Deze dictionary's houden we samen bij in één grote dictionary: <code>steden</code>.


Hieronder zie je een dictionary <b>stad</b> met informatie over de stad, zoals <b>naam</b>, <b>land</b> en aantal <b>inwoners</b>. Hier is <b>naam</b> een sleutel en <b>Amsterdam</b> de bijbehorende waarde. Ter herinnering, met <code>stad["land"]</code> krijg je "Nederland".
```python
stad = {
    "naam": "Amsterdam",
    "land": "Nederland",
    "inwoners": 921000
}

print(stad)           # Print de hele dictionary
print(stad["land"])   # Print het land van de stad
```


Als je van meerdere steden een dictionary hebt, kun je ze samen in één geneste dictionary bijhouden. Hieronder zie je een voorbeeld van een geneste dictionary <code>steden</code> met de gegevens van Amsterdam, Parijs en Berlijn. Met <code>print()</code> kun je de inhoud van een geneste dictionary afdrukken. Geef dan de naam van de dictionary mee tussen haakjes.


```python
steden = {
    "Amsterdam":{"land": "Nederland", "inwoners": 921000},
    "Parijs": {"land": "Frankrijk", "inwoners": 2148000},
    "Berlijn": {"land": "Duitsland", "inwoners": 3769000}
}

print(steden)
```

    {'Amsterdam': {'land': 'Nederland', 'inwoners': 921000}, 'Parijs': {'land': 'Frankrijk', 'inwoners': 2148000}, 'Berlijn': {'land': 'Duitsland', 'inwoners': 3769000}}


<!-- <p>De onderstaande visualisatie laat zien hoe een geneste dictionary eruit ziet.<br>

<iframe width="1000" height="500" frameborder="0" src="https://pythontutor.com/iframe-embed.html#code=steden%20%3D%20%7B%0A%20%20%20%20%22Amsterdam%22%3A%7B%22land%22%3A%20%22Nederland%22,%20%22inwoners%22%3A%20921000%7D,%0A%20%20%20%20%22Parijs%22%3A%20%7B%22land%22%3A%20%22Frankrijk%22,%20%22inwoners%22%3A%202148000%7D,%0A%20%20%20%20%22Berlijn%22%3A%20%7B%22land%22%3A%20%22Duitsland%22,%20%22inwoners%22%3A%203769000%7D%0A%7D&codeDivHeight=400&codeDivWidth=350&cumulative=false&curInstr=4&heapPrimitives=nevernest&origin=opt-frontend.js&py=311&rawInputLstJSON=%5B%5D&textReferences=false"> </iframe> -->





### Opdracht 16.1.1 Kennismaken met de geneste dictionary `dierentuin`

Bekijk de dictionary `dierentuin` hieronder en beantwoord de volgende vragen, *zonder code te schrijven*:
<ol type=alpha>
<li>Wat is de naam van het verblijf van de olifant?</li>
<li>Hoeveel pinguïns zijn er in de dierentuin?</li>
<li>Hoeveel soorten dieren zijn er in de dierentuin?</li>
<li>Wat is het dieet van de Python?</li>
<li>Wat is het datatype van dieet?</li>
</ol>

```python
dierentuin = {
    "Leeuw": {"soort": "Zoogdier", "verblijf": "Savanne", "dieet": ["vlees"], "aantal": 2},
    "Pinguïn": {"soort": "Vogel", "verblijf": "Poolgebied", "dieet": ["vis", "kril"], "aantal": 15},
    "Python": {"soort": "Reptiel", "verblijf": "Terrarium", "dieet": ["muizen", "ratten"], "aantal": 3}
}
```

<!-- ANTWOORDEN
<ol type="a">
<li>Savanne
<li>15
<li>3, namelijk: Zoogdier, Vogel, Reptiel
<li>muizen en ratten</li>
<li>een lijst</li>
</ol>
--> 

<p>Klik <a href="https://rweeda.github.io/PythonIA/docs/IA_H15_oplossingen.html#opgave1611">hier</a> voor een voorbeelduitwerking.</p>


### Opdracht 16.1.2 Gegevens in `dierentuin` printen
<p>De dictionary <code>dierentuin</code> bevat informatie over verschillende dieren in de dierentuin.
Elke *diernaam* (zoals "Leeuw" of "Olifant") is een *sleutel* in de dictionary.
De bijbehorende waarde is een *geneste dictionary* met informatie over dat dier:
<ul>
<li>"soort": het type dier (bijv. zoogdier, vogel, reptiel),
<li>"verblijf": het gebied of verblijf waar het dier woont,
<li>"dieet": een lijst met dingen die het dier eet,
<li>"aantal": het aantal dieren van die soort in de dierentuin.
</ul>
</p>
<p>Print de volledige inhoud van de dictionary <code>dierentuin</code>.</p>



Verwachte uitvoer:<br><i>
Alle informatie over de dierentuin: {'Leeuw': {'soort': 'Zoogdier', 'verblijf': 'Savanne', 'dieet': ['vlees'], 'aantal': 2}, 'Pinguïn': {'soort': 'Vogel', 'verblijf': 'Poolgebied', 'dieet': ['vis', 'kril'], 'aantal': 15}, 'Python': {'soort': 'Reptiel', 'verblijf': 'Terrarium', 'dieet': ['muizen', 'ratten'], 'aantal': 3}}</i>

```python
dierentuin = {
    "Leeuw": {"soort": "Zoogdier", "verblijf": "Savanne", "dieet": ["vlees"], "aantal": 2},
    "Pinguïn": {"soort": "Vogel", "verblijf": "Poolgebied", "dieet": ["vis", "kril"], "aantal": 15},
    "Python": {"soort": "Reptiel", "verblijf": "Terrarium", "dieet": ["muizen", "ratten"], "aantal": 3}
}

```

<p>Klik <a href="https://rweeda.github.io/PythonIA/docs/IA_H15_oplossingen.html#opgave1612">hier</a> voor een voorbeelduitwerking.</p>
<!-- ANTWOORD
dierentuin = {
    "Leeuw": {"soort": "Zoogdier", "verblijf": "Savanne", "dieet": ["vlees"], "aantal": 2},
    "Pinguïn": {"soort": "Vogel", "verblijf": "Poolgebied", "dieet": ["vis", "kril"], "aantal": 15},
    "Python": {"soort": "Reptiel", "verblijf": "Terrarium", "dieet": ["muizen", "ratten"], "aantal": 3}
}
#a: Print de verblijf over de dierentuin
print("Alle informatie over de dierentuin:", dierentuin)
-->


