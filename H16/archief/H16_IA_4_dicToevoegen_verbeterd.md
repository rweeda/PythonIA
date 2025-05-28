
<!--H16_toevoegen-->

## 4: Dictionary toevoegen

Om een dictionary in te voegen in een bestaande dictionary geef je de nieuwe sleutel op met de bijbehorende dictionary als waarde.

Voorbeeld: Stel we willen een dictionary met informatie over Madrid toevoegen. Madrid ligt in Spanje en heeft 3400000 inwoners. 
De *sleutel* is 'Madrid' en de bijbehorende dictionary: <code>{"land": "Spanje", "inwoners": 3400000} </code>

Met de onderstaande code voegen we Madrid met de bijbehorende gegevens toe aan de dictionary <code>steden</code>:


<code>steden["Madrid"] =  {"land": "Spanje", "inwoners": 3400000} </code>
print(steden)


Bijvoorbeeld:<br><br> 

<p>Bekijk 
<a href="
https://pythontutor.com/render.html#code=steden%20%3D%20%7B%0A%20%20%20%20%22Amsterdam%22%3A%7B%22land%22%3A%20%22Nederland%22,%20%22inwoners%22%3A%20921000%7D,%0A%20%20%20%20%22Parijs%22%3A%20%7B%22land%22%3A%20%22Frankrijk%22,%20%22inwoners%22%3A%202148000%7D,%0A%20%20%20%20%22Berlijn%22%3A%20%7B%22land%22%3A%20%22Duitsland%22,%20%22inwoners%22%3A%203769000%7D%0A%7D%0A%0Asteden%5B%22Madrid%22%5D%20%3D%20%20%7B%22land%22%3A%20%22Spanje%22,%20%22inwoners%22%3A%203400000%7D&cumulative=false&curInstr=4&heapPrimitives=nevernest&mode=display&origin=opt-frontend.js&py=311&rawInputLstJSON=%5B%5D&textReferences=false">hier</a> een visualisatie in Python Tutor.</p>
<!-- Druk op <i>Next</i> in de onderstaande visualisatie om te zien hoe de dictionary met gegevens over Madrid wordt toegevoegd aan de <code>steden</code> dictionary.-->

<!--<iframe width="1000" height="600" frameborder="0" src="https://pythontutor.com/iframe-embed.html#code=steden%20%3D%20%7B%0A%20%20%20%20%22Amsterdam%22%3A%7B%22land%22%3A%20%22Nederland%22,%20%22inwoners%22%3A%20921000%7D,%0A%20%20%20%20%22Parijs%22%3A%20%7B%22land%22%3A%20%22Frankrijk%22,%20%22inwoners%22%3A%202148000%7D,%0A%20%20%20%20%22Berlijn%22%3A%20%7B%22land%22%3A%20%22Duitsland%22,%20%22inwoners%22%3A%203769000%7D%0A%7D%0A%0Asteden%5B%22Madrid%22%5D%20%3D%20%20%7B%22land%22%3A%20%22Spanje%22,%20%22inwoners%22%3A%203400000%7D&codeDivHeight=400&codeDivWidth=350&cumulative=false&curInstr=4&heapPrimitives=nevernest&origin=opt-frontend.js&py=311&rawInputLstJSON=%5B%5D&textReferences=false"> </iframe> -->







### Opdracht 16.4.1 Olifant toevoegen

<p>Er zijn zes dieren van het soort olifant gearriveerd in de dierentuin. </p>
<ol type="a">
<li>Voeg de olifant-soort toe aan de dierentuin dictionary. De dictionary met gegevens staat in een commentaarregel;
<li>Print de geneste dictionary met informatie over de Olifant;
<li>Print het aantal Olifanten dat er zijn;
<li>Tot slot, print alle informatie over de dierentuin.
</ol>

```python
dierentuin = {
    "Leeuw": {"soort": "Zoogdier", "verblijf": "Savanne", "dieet": ["vlees"], "aantal": 2},
    "Pinguïn": {"soort": "Vogel", "verblijf": "Poolgebied", "dieet": ["vis", "kril"], "aantal": 15},
    "Python": {"soort": "Reptiel", "verblijf": "Terrarium", "dieet": ["muizen", "ratten"], "aantal": 3}
}


#{"soort": "Zoogdier", "verblijf": "Savanne",  "dieet": ["planten", "fruit", "bladeren"], "aantal": 6}


```

<p>Klik <a href="https://rweeda.github.io/PythonIA/docs/IA_H15_oplossingen.html#opgave1641">hier</a> voor een voorbeelduitwerking.</p>

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


