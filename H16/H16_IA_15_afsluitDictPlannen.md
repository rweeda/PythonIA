## Onderwerp 16: Afsluitende opdrachten

<p>Met de volgende afsluitende opdrachten kun je kijken hoe goed je de stof beheerst. Controleer steeds je eigen oplossing met de voorbeelduitwerking.</p>

<p>Voor de volgende afsluitende opdrachten maken we steeds gebruik van de dictionary <code>profielen</code>. Deze dictionary bevat gegevens over verschillende gebruikers van een social media-platform. Elke gebruikersnaam (zoals "skydiver_22" of "techie99") is een sleutel in de dictionary. De bijbehorende waarde is een geneste dictionary met vier onderdelen:
<ul>
<li>"bio": een korte beschrijving van de gebruiker (string),
<li>"volgers": het aantal volgers van de gebruiker (integer),
<li>"posts": het aantal berichten dat de gebruiker heeft geplaatst (integer),
<li>"interesses": een lijst van onderwerpen waarin de gebruiker geïnteresseerd is (list van strings).
</ol></p>

```python
profielen = {
    "skydiver_22": {
        "bio": "Ik hou van katten en gamen",
        "volgers": 134,
        "posts": 47,
        "interesses": ["dieren", "games", "fotografie"]
    },
    "dancequeen": {
        "bio": "Altijd aan het dansen",
        "volgers": 245,
        "posts": 82,
        "interesses": ["muziek", "games", "vloggen"]
    },
    "bookworm": {
        "bio": "Ik lees elke dag",
        "volgers": 98,
        "posts": 133,
        "interesses": ["boeken", "schrijven", "fotografie"]
    },
    "techie99": {
        "bio": "Fan van programmeren en robots",
        "volgers": 187,
        "posts": 59,
        "interesses": ["programmeren", "AI", "games"]
    }
}






### Afsluitende Opdracht 16.X Profielen met meer dan 100 volgers
<p>Schrijf een programma dat print welke profielen meer dan 100 volgers hebben.</p>

<p>Verwachte uitvoer:<br>
<i>Profiel skydiver_22 heeft meer dan 100 volgers<br>
Profiel dancequeen heeft meer dan 100 volgers<br>
Profiel techie99 heeft meer dan 100 volgers</i></p>



```python
profielen = {
    "skydiver_22": {
        "bio": "Ik hou van katten en gamen",
        "volgers": 134,
        "posts": 47,
        "interesses": ["dieren", "games", "fotografie"]
    },
    "dancequeen": {
        "bio": "Altijd aan het dansen",
        "volgers": 245,
        "posts": 82,
        "interesses": ["muziek", "games", "vloggen"]
    },
    "bookworm": {
        "bio": "Ik lees elke dag",
        "volgers": 98,
        "posts": 133,
        "interesses": ["boeken", "schrijven", "fotografie"]
    },
    "techie99": {
        "bio": "Fan van programmeren en robots",
        "volgers": 187,
        "posts": 59,
        "interesses": ["programmeren", "AI", "games"]
    }
}

```

    Profiel skydiver_22 heeft meer dan 100 volgers
    Profiel dancequeen heeft meer dan 100 volgers
    Profiel techie99 heeft meer dan 100 volgers



<p>Bekijk <a href="https://rweeda.github.io/PythonIA/docs/IA_H16_oplossingen.html#AfOpgave16X" target="_blank">hier</a> de voorbeelduitwerking.</p>

<!--ANTWOORD
profielen = {
    "skydiver_22": {
        "bio": "Ik hou van katten en gamen",
        "volgers": 134,
        "posts": 47,
        "interesses": ["dieren", "games", "fotografie"]
    },
    "dancequeen": {
        "bio": "Altijd aan het dansen",
        "volgers": 245,
        "posts": 82,
        "interesses": ["muziek", "games", "vloggen"]
    },
    "bookworm": {
        "bio": "Ik lees elke dag",
        "volgers": 98,
        "posts": 133,
        "interesses": ["boeken", "schrijven", "fotografie"]
    },
    "techie99": {
        "bio": "Fan van programmeren en robots",
        "volgers": 187,
        "posts": 59,
        "interesses": ["programmeren", "AI", "games"]
    }
}

for profiel, gegevens in profielen.items():
    if gegevens["volgers"] > 100:
        print("Profiel", profiel, "heeft meer dan 100 volgers")


-->



### Afsluitende Opdracht 16.X Games als interesse

Schrijf een functie die de dictionary doorloopt en een lijst oplevert van alle profielen die 'games' als interesse hebben.


### Afsluitende Opdracht 16.X Totaal aantal volgers

### Afsluitende Opdracht Profielen met top 3 aantal volgers (gesorteerd)
Gebruik sort
maak lijst met append, en dan lijst.sort (nieuwlijst = sorted.lijst)

### Afsluitende Opdracht Gemiddeld aantal posts (aantal posts/aantal profielen)

### Afsluitende Opdracht 16.X Alle profielen met minder dan 60 posts verwijderen uit dictionary


### Schrijf een functie die een gebruiker vraagt om een profielnaam, bio en interesses. Als deze profiel niet bestaat, voeg die toe aan de dictionary met volgers en posts moet 0 zijn. Als de profiel al wel bestaat, geef een foutmelding

### Bij iedereen aantal volgers ophogen met 1

### Schrijf een functie die de gebruiker om een interesse vraagt, en de dictionary doorzoekt naar alle profielen die die interesse hebben

### Een lijst van alle interesses (elk interesse mag maar 1 keer voorkomen)

### Een lijst van alle profielen met >100 volgers en die van fotografie houden

### Alle bio's afdrukken van mensen die wel als interesse programmeren hebben OF die meer posts dan volgers hebben 

### Alle profielen met meer dan 10000 posts verwijderen (spam)
del (kan niet in for-loop) - eerst de keys bepalen, en dan nieuwe forloop--- denken we



### Afsluitende Opdracht 10.2 Stemmingen
<p>Schrijf een programma om te bepalen hoeveel van je vrienden gelukkig zijn.</p>
<ol style="list-style-type: lower-alpha">
    <li>Schrijf een functie die aan vijf van je vrienden vraagt om hun stemming met een emoticon (of emoji) weer te geven. Zet de emoticons één voor één in een lijst. Lever de lijst op met een return.</li>
    <li>Roep de functie aan in je hoofdprogramma en test of deze werkt door de lijst te printen.</li>
    <li>Schrijf een functie die de lijst met een loop doorloopt en telt hoe vaak de ':)'-smiley in de lijst voorkomt. Je <b>moet</b> een loop met een teller gebruiken. Lever het aantal smileys op met een return.</li>
    <li>Roep je telfunctie aan in je hoofdprogramma en druk af hoeveel smileys er gevonden zijn.
    </li>
</ol>






```python
### FUNCTIEDEFINITIES



### HOOFPROGRAMMA

```


<p>Bekijk <a href="https://rweeda.github.io/PythonIA/docs/IA_H10_oplossingen.html#AfOpgave102" target="_blank">hier</a> de voorbeelduitwerking.</p>






### Afsluitende Opdracht 10.3 Cijferlijst opleuken

<p>Stel, dit is jouw (dramatische) cijferlijst:</p>
<p><code>cijferLijst = [5.0, 5.5, 2.3, 4.6, 6.1, 5.6, 9.8]</code></p>

<p>Maak een nieuwe cijferlijst waarbij elk cijfer met 0.5 punt opgehoogd is. Na afloop druk je de nieuwe cijferlijst af.</p>

<p>Het is dus de bedoeling dat na afloop het volgende wordt afgedrukt:<i> [5.5, 6.0, 2.8, 5.1, 6.6, 6.1, 9.8]</i></p>

<p>Tips:
</p>
<ul>
    <li>doorloop de lijst met een <code>for</code>-loop en print elk cijfer uit.
    </li>
    <li>hoog het cijfer met 0.5 punten op. Zet het opgehoogde cijfer in een nieuwe lijst.
    </li>
    <li>zorg dat er geen cijfer boven de 10 uitkomt. Als het cijfer na ophoging boven de 10 uitkomt, stel het dan gelijk aan 10.
    </li>
</ul>
<p></p>




```python
cijferLijst = [9.8, 5.5, 2.3, 4.6, 6.1, 5.6]
```


<p>Bekijk <a href="https://rweeda.github.io/PythonIA/docs/IA_H10_oplossingen.html#AfOpgave103" target="_blank">hier</a> de voorbeelduitwerking.</p>




### Afsluitende Opdracht 10.4 Meeste regen
<p>Janneke hield voor de maand februari dagelijks bij hoeveel regen er gevallen is. Wat was de meeste regen die er op een dag gevallen was en op welke datum was dat? Je moet hiervoor een of twee <code>for</code>-loops gebruiken.</p>


<p>Aanwijzingen:
</p>
<ul>
    <li>doorloop de lijst met een <code>for</code>-loop en bepaal wat de meeste regen is die er gevallen is.
    </li>
    <li>doorloop de lijst met een <code>for</code>-loop en zoek op welke index die voorkomt.
    </li>
    <li>pas de index aan naar een datum.
    </li>
</ul>
<p></p>




```python
regenlijst = [ 0, 10, 15, 20, 18, 15, 13, 14, 16, 34, 12, 10, 0, 0, 0, 1, 2, 0, 4, 8, 0, 0, 1, 2, 1, 10, 8, 1 ]
```


<p>Bekijk <a href="https://rweeda.github.io/PythonIA/docs/IA_H10_oplossingen.html#AfOpgave104" target="_blank">hier</a> de voorbeelduitwerking.</p>




### Afsluitende Opdracht 10.5 Loonstrookje
<p>Piet heeft de afgelopen maand zijn dagloon in een lijst bijgehouden. Schrijf een programma dat de lijst met een loop doorloopt en zijn maandloon bepaalt (de som van alle lonen in de lijst).</p>



```python
loonlijst = [24.00, 28.50, 45.80, 45.80, 23.10, 32.15]

```

<p>Bekijk <a href="https://rweeda.github.io/PythonIA/docs/IA_H10_oplossingen.html#AfOpgave105" target="_blank">hier</a> de voorbeelduitwerking.</p>


### Afsluitende Opdracht 10.6 Foutieve metingen
<p>In een fabriek wordt in een lijst bijgehouden hoeveel storingen er zijn. Helaas is er wat misgegaan en komen er nu foute waarden in de lijst voor. Kijk maar:</p>
<p><code>storingenlijst = [ 0, 3, -1, 4, 3, 2, -1 ]</code></p>
<p>Jouw taak is om de lijst te doorlopen en de negatieve waarden eruit te filteren: maak een nieuwe lijst zonder de negatieve waarden. Je nieuwe lijst moet er dus zo uit komen te zien:</p>
<p><code>storingenlijst = [ 0, 3, 4, 3, 2 ]</code></p>






```python
storingenlijst = [ 0, 3, -1, 4, 3, 2, -1 ]

```


<p>Bekijk <a href="https://rweeda.github.io/PythonIA/docs/IA_H10_oplossingen.html#AfOpgave106" target="_blank">hier</a> de voorbeelduitwerking.</p>




### Afsluitende Opdracht 10.7 Gemiddelde bepalen
<p>Schrijf een functie die een lijst getallen binnenkrijgt, deze met een loop doorloopt en de gemiddelde waarde van alle elementen oplevert. Let op: als er geen waarden in de lijst staan, kun je geen gemiddelde berekenen en moet je programma, in plaats van een berekening maken, het volgende printen: "<i>Fout, geen gegevens</i>".</p>






```python
### FUNCTIEDEFINITIES


### HOOFDPROGRAMMA
getallenlijst = [4,5,6,3,5,6]

```


<p>Bekijk <a href="https://rweeda.github.io/PythonIA/docs/IA_H10_oplossingen.html#AfOpgave107" target="_blank">hier</a> de voorbeelduitwerking.</p>





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

