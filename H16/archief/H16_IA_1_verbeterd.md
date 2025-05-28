## 1: Inleiding geneste dictionary's

Een dictionary kan ook binnenin een andere dictionary zitten; dit heet een <b>geneste dictionary</b>. Met een geneste dictionary kan je handig data van meerdere dingen op een gestructureerde manier opslaan. Dit leggen we uit aan de hand van een voorbeeld. We hebben een aantal dictionary's met informatie over steden, bijvoorbeeld over Amsterdam, Parijs en Berlijn. Deze dictionary's houden we samen bij in een grote dictionary: <code>steden</code>.


Hieronder zie je een dictionary <b>stad</b> met informatie over de stad, zoals <b>naam</b>, <b>land</b> en aantal <b>inwoners</b>. Hier is <b>naam</b> een sleutel en <b>Amsterdam</b> de bijbehorende waarde. Ter herinnering, met <code>stad["land"]</code> krijg je "Nederland".
```python
stad = {
    "naam": "Amsterdam",
    "land": "Nederland",
    "inwoners": 921000
}

print(stad)           #print de hele dictionary
print(stad["land"])   #print het land van de stad
```


Als je van meerdere steden een dictionary hebt, kun je ze samen in een geneste dictionary bijhouden. Hieronder zie je een voorbeeld van een geneste dictionary <code>steden</code> met de gegevens van Amsterdam, Parijs en Berlijn. Met <code>print()</code> kun je de inhoud van een geneste dictionary te printen, geef dan de naam van de dictionary tussen haakjes mee.


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





### Opdracht 16.3 Kennismaken met de geneste dictionary `dierentuin`

Bekijk de `dierentuin` dictionary hieronder en beantwoord, *zonder het schrijven van code* de onderstaande vragen:
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

<p>Klik <a href="https://rweeda.github.io/PythonIA/docs/IA_H15_oplossingen.html#opgave163">hier</a> voor een voorbeelduitwerking.</p>


### Opdracht 16.1.1: Gegevens in `dierentuin` printen
<p>De dictionary <code>dierentuin</code> bevat gegevens over verschillende dieren in een dierentuin.
Elke *diernaam* (zoals "Leeuw" of "Olifant") is een *sleutel* in de dictionary.
De bijbehorende waarde is een *geneste dictionary* met informatie over dat dier:
<ul>
<li>"soort": het type dier (bijv. zoogdier, vogel, reptiel),
<li>"verblijf": het gebied of verblijf waar het dier woont,
<li>"dieet": een lijst met dingen die het dier eet,
<li>"aantal": het aantal dieren van die soort in de dierentuin.
</ul>
</p>
<p>Print alle informatie over de dierentuin.</p>


<i>
Verwachte uitvoer:
Alle informatie over de dierentuin: {'Leeuw': {'soort': 'Zoogdier', 'verblijf': 'Savanne', 'dieet': ['vlees'], 'aantal': 2}, 'Pinguïn': {'soort': 'Vogel', 'verblijf': 'Poolgebied', 'dieet': ['vis', 'kril'], 'aantal': 15}, 'Python': {'soort': 'Reptiel', 'verblijf': 'Terrarium', 'dieet': ['muizen', 'ratten'], 'aantal': 3}}</i>

```python
dierentuin = {
    "Leeuw": {"soort": "Zoogdier", "verblijf": "Savanne", "dieet": ["vlees"], "aantal": 2},
    "Pinguïn": {"soort": "Vogel", "verblijf": "Poolgebied", "dieet": ["vis", "kril"], "aantal": 15},
    "Python": {"soort": "Reptiel", "verblijf": "Terrarium", "dieet": ["muizen", "ratten"], "aantal": 3}
}

```

<p>Klik <a href="https://rweeda.github.io/PythonIA/docs/IA_H15_oplossingen.html#opgave164">hier</a> voor een voorbeelduitwerking.</p>
<!-- ANTWOORD
#a: Print de verblijf over de dierentuin
print("Alle informatie over de dierentuin:", dierentuin)
-->




## 2: Gegevens ophalen uit een geneste dictionary

<p>De gegevens van meerdere steden kun je ook in een dictionary opslaan.  Dit is een geneste dictionary, omdat elke stad (<b>Amsterdam, Parijs, Berlijn</b>) zijn eigen dictionary heeft met extra informatie.<br>
<img src="https://raw.githubusercontent.com/rweeda/PythonIA/main/img/dictionary_steden.png" width="500">


<p>Met <code>steden["Parijs"]</code> haal je de dictionary van Parijs op. Door deze uit te breiden met een tweede sleutel <b>land</b> haal je uit de dictionary van Parijs een specifieke waarde op:<br><br> <code>steden["Parijs"]["land"]</code>.</p>


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
De verwachte uitvoer is:<i>
Alle informatie over de Pinguïn: {'soort': 'Vogel', 'verblijf': 'Poolgebied', 'dieet': ['vis', 'kril'], 'aantal': 15}
<br>
De verblijf van de Pinguïn is: Poolgebied</i>
</p>


```python
dierentuin = {
    "Leeuw": {"soort": "Zoogdier", "verblijf": "Savanne", "dieet": ["vlees"], "aantal": 2},
    "Pinguïn": {"soort": "Vogel", "verblijf": "Poolgebied", "dieet": ["vis", "kril"], "aantal": 15},
    "Python": {"soort": "Reptiel", "verblijf": "Terrarium", "dieet": ["muizen", "ratten"], "aantal": 3}
}
```

<p>Klik <a href="https://rweeda.github.io/PythonIA/docs/IA_H15_oplossingen.html#opgave164">hier</a> voor een voorbeelduitwerking.</p>
<!-- ANTWOORD
#b: Print alle informatie over de Pinguïn
print("Alle informatie over de Pinguïn:", dierentuin["Pinguïn"])
#c: Print de verblijf van de Pinguïn 
print("De verblijf van de Pinguïn is:", dierentuin["Pinguïn"]["verblijf"])
-->



<!--H16_aanpassen-->
### Een waarde in een geneste dictionary aanpassen

Je kunt ook een waarde in een geneste dictionary aan passen. Hiervoor geef je met vierkante haken aan om welk sleutel en welk gegevenstype het gaat. Daarna geef je met een '='-teken aan wat de nieuwe waarde wordt. Bijvoorbeeld, met de volgende regel wordt het aantal inwoners van Parijs aangepast:<br><br>
<code>steden["Parijs"]["inwoners"] = 2200000</code>

### Opdracht 16.2 Aantal inwoners van Berlijn aanpassen

<p>Schrijf code om "Duitsland" te vervangen door de afkorting "DL". Print daarna de land om de aanpassing te controleren.</p>

<p>Verwachte uitvoer: <i>DL</i></p>


```python
steden = {
    "Amsterdam":{"land": "Nederland", "inwoners": 921000},
    "Parijs": {"land": "Frankrijk", "inwoners": 2148000},
    "Berlijn": {"land": "Duitsland", "inwoners": 3769000},
}

steden["Berlijn"]["land"] = "DL"
print(steden["Berlijn"]["land"])

```




<p>Klik <a href="https://rweeda.github.io/PythonIA/docs/IA_H15_oplossingen.html#opgave162">hier</a> voor een voorbeelduitwerking.</p>
<!-- steden["Berlijn"]["land"] = "DL"
print(steden["Berlijn"]["land"])   # Geeft "DL"
-->


### Opdracht 16.2.1: Er is een Python geboren

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


<p>Klik <a href="https://rweeda.github.io/PythonIA/docs/IA_H15_oplossingen.html#opgave164">hier</a> voor een voorbeelduitwerking.</p>
<!-- ANTWOORD
# Pas het aantal Pythons aan naar 4
dierentuin["Python"]["aantal"] = 4
print(dierentuin)
-->


------------------------
<!--H16_toevoegen-->

## Dictionary toevoegen

Om een dictionary in te voegen in een bestaande dictionary geef je de nieuwe sleutel op met de bijbehorende dictionary als waarde.

Voorbeeld: Stel we willen een dictionary met informatie over Madrid toevoegen. Madrid ligt in Spanje en heeft 3400000 inwoners. 
De *sleutel* is 'Madrid' en de bijbehorende dictionary: <code>{"land": "Spanje", "inwoners": 3400000} </code>

Met de volgende code voegen we Rome en de bijbehorende dictionary toe aan <code>steden</code>:


<code>steden["Madrid"] =  {"land": "Spanje", "inwoners": 3400000} </code>
print(steden)


Bijvoorbeeld:<br><br> 

<p>Bekijk 
<a href="
https://pythontutor.com/render.html#code=steden%20%3D%20%7B%0A%20%20%20%20%22Amsterdam%22%3A%7B%22land%22%3A%20%22Nederland%22,%20%22inwoners%22%3A%20921000%7D,%0A%20%20%20%20%22Parijs%22%3A%20%7B%22land%22%3A%20%22Frankrijk%22,%20%22inwoners%22%3A%202148000%7D,%0A%20%20%20%20%22Berlijn%22%3A%20%7B%22land%22%3A%20%22Duitsland%22,%20%22inwoners%22%3A%203769000%7D%0A%7D%0A%0Asteden%5B%22Madrid%22%5D%20%3D%20%20%7B%22land%22%3A%20%22Spanje%22,%20%22inwoners%22%3A%203400000%7D&cumulative=false&curInstr=4&heapPrimitives=nevernest&mode=display&origin=opt-frontend.js&py=311&rawInputLstJSON=%5B%5D&textReferences=false">hier</a> een visualisatie in Python Tutor.</p>
<!-- Druk op <i>Next</i> in de onderstaande visualisatie om te zien hoe de dictionary met gegevens over Madrid wordt toegevoegd aan de <code>steden</code> dictionary.-->

<!--<iframe width="1000" height="600" frameborder="0" src="https://pythontutor.com/iframe-embed.html#code=steden%20%3D%20%7B%0A%20%20%20%20%22Amsterdam%22%3A%7B%22land%22%3A%20%22Nederland%22,%20%22inwoners%22%3A%20921000%7D,%0A%20%20%20%20%22Parijs%22%3A%20%7B%22land%22%3A%20%22Frankrijk%22,%20%22inwoners%22%3A%202148000%7D,%0A%20%20%20%20%22Berlijn%22%3A%20%7B%22land%22%3A%20%22Duitsland%22,%20%22inwoners%22%3A%203769000%7D%0A%7D%0A%0Asteden%5B%22Madrid%22%5D%20%3D%20%20%7B%22land%22%3A%20%22Spanje%22,%20%22inwoners%22%3A%203400000%7D&codeDivHeight=400&codeDivWidth=350&cumulative=false&curInstr=4&heapPrimitives=nevernest&origin=opt-frontend.js&py=311&rawInputLstJSON=%5B%5D&textReferences=false"> </iframe> -->







### Opdracht 16.1 Olifant toevoegen

<p>Er zijn zes dieren van het soort Olifant gearriveerd in de dierentuin. </p>
<ol type="a">
<li>Voeg de Olifant-soort toe aan de dierentuin dictionary. De dictionary met informatie is in commentaar gegegeven;
<li>Print de geneste dictionary met informatie over de Olifant;
<li>Print het aantal Olifanten dat er zijn;
<li>Tot slot, print alle informatie over het dierentuin.
</ol>

```python
dierentuin = {
    "Leeuw": {"soort": "Zoogdier", "verblijf": "Savanne", "dieet": ["vlees"], "aantal": 2},
    "Pinguïn": {"soort": "Vogel", "verblijf": "Poolgebied", "dieet": ["vis", "kril"], "aantal": 15},
    "Python": {"soort": "Reptiel", "verblijf": "Terrarium", "dieet": ["muizen", "ratten"], "aantal": 3}
}


#{"soort": "Zoogdier", "verblijf": "Savanne",  "dieet": ["planten", "fruit", "bladeren"], "aantal": 6}


```

<p>Klik <a href="https://rweeda.github.io/PythonIA/docs/IA_H15_oplossingen.html#opgave161">hier</a> voor een voorbeelduitwerking.</p>

<!-- ANTWOORD
#a: Voeg olifant toe
dierentuin["Olifant"] = {"soort": "Zoogdier", "verblijf": "Savanne",  "dieet": ["planten", "fruit", "bladeren"],
        "aantal": 6}

#b: Print de geneste dictionary met informatie over de Olifant;
print(dierentuin["Olifant"])

#c: Print het aantal Olifanten dat er zijn;
print(dierentuin["Olifant"]["aantal"])

#d: Print alle informatie over het dierentuin.
print(dierentuin)
-->



<!--H16_verwijderen-->

### Gegevens uit een geneste dictionary verwijderen

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



### Opdracht 16.1 Olifant verwijderen

De Olifanten zijn overgeplaatst naar een ander dierentuin.
<ol type="a">
<li>Verwijder de Olifant-soort uit de dierentuin dictionary;
<li>Print alle informatie over het dierentuin om te controleren of het verwijderen is goedgegaan.
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
<p>Klik <a href="https://rweeda.github.io/PythonIA/docs/IA_H15_oplossingen.html#opgave161">hier</a> voor een voorbeelduitwerking.</p>

<!-- ANTWOORD
del dierentuin["Olifant"]
print(dierentuin)   
-->


<!--

### Afsluitende Opdracht: Gegevens aan de <code>dierentuin</code> dictionary toevoegen
<p>Er komt een nieuwe dier naar de dierentuin! Voeg deze aan de dictionary toe.</p>
<ol type="a">
<li>Vraag de gebruiker om een nieuw dier naar de dierentuin te brengen. Vraag hoe het dier heet.
<li>Controleer of het dier niet al in de dictionary staat. Als die er al in staat, geef een foutmelding.
<li>Vraag van welk soort het is, waar het moet verblijven, wat het eet (een ding), en hoeveel ervan gebracht worden.</li>
<li>Schrijf een functie die het <code>dier</code>, <code>soort</code>, <code>verblijf</code>, <code>dieet</code> en <code>aantal</code> meekrijgt als parameter en deze toevoegt aan de dictionary. Vergeet niet van het ingevoerde <code>aantal</code> eerst nog een integer te maken.
<li>Print de dictionary.
</ol>

Uitbreidingstip: Wil je als dieet een lijst laten invoeren? Vraag de gebruiker om de dieetwensen gescheiden door een komma (',')  te laten invoeren en gebruik <code>.split(",")</code> om deze in een lijst te zetten:<br>
<code> dieet = input("Voer het dieet in (gescheiden door komma's): ").split(",")</code>


```python
dierentuin = {
    "Leeuw": {"soort": "Zoogdier", "verblijf": "Savanne", "dieet": ["vlees"], "aantal": 2},
    "Pinguïn": {"soort": "Vogel", "verblijf": "Poolgebied", "dieet": ["vis", "kril"], "aantal": 15},
    "Python": {"soort": "Reptiel", "verblijf": "Terrarium", "dieet": ["muizen", "ratten"], "aantal": 3}
}

# Functie om een nieuw dier toe aan de dierentuin toe te voegen



# Vraag de gebruiker om de gegevens van het nieuwe dier in te voeren

```

    Het dier is toegevoegd aan de dierentuin.
    {'Leeuw': {'soort': 'Zoogdier', 'verblijf': 'Savanne', 'dieet': ['vlees'], 'aantal': 2}, 'Pinguïn': {'soort': 'Vogel', 'verblijf': 'Poolgebied', 'dieet': ['vis', 'kril'], 'aantal': 15}, 'Python': {'soort': 'Reptiel', 'verblijf': 'Terrarium', 'dieet': ['muizen', 'ratten'], 'aantal': 3}, 'dg': {'soort': 'sdf', 'verblijf': 'dsf', 'dieet': 'sfd', 'aantal': 33}}


ANTWOORD LINK
-->
<!-- ANTWOORD
dierentuin = {
    "Leeuw": {"soort": "Zoogdier", "verblijf": "Savanne", "dieet": ["vlees"], "aantal": 2},
    "Pinguïn": {"soort": "Vogel", "verblijf": "Poolgebied", "dieet": ["vis", "kril"], "aantal": 15},
    "Python": {"soort": "Reptiel", "verblijf": "Terrarium", "dieet": ["muizen", "ratten"], "aantal": 3}
}

# Functie om een nieuw dier toe aan de dierentuin toe te voegen
def voegDierToe(naam, soort, verblijf, dieet, aantal):
    dierentuin[naam] = {
            "soort": soort,
            "verblijf": verblijf,
            "dieet": dieet,
            "aantal": aantal
        }
    print("Het dier is toegevoegd aan de dierentuin.")
    print(dierentuin)

# Vraag de gebruiker om de gegevens van het nieuwe dier in te voeren
ingevoerde_dier = input("Voer een naam in van een dier: ")
if ingevoerde_dier in dierentuin:
    print("Er is al een", ingevoerde_dier, "in de dierentuin.")
else:
    soort = input("Voer het soort in: ")
    verblijf = input("Voer het verblijf in: ")
    dieet = input("Voer het dieet in: ")
    aantal = int(input("Voer het aantal in: "))

    voegDierToe(ingevoerde_dier, soort, verblijf, dieet, aantal)
    
    -->
