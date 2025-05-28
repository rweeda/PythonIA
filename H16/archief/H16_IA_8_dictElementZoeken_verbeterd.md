<!-- Verbeterde versie van H16_IA_8_dictElementZoeken.md -->

## 8: Dictionary doorzoeken naar een bepaalde waarde

## Zoeken naar een sleutelwaarde
Het zoeken naar een sleutelwaarde kan met <code>in</code>.


```python
steden = {
    "Amsterdam":{"land": "Nederland", "inwoners": 921000},
    "Parijs": {"land": "Frankrijk", "inwoners": 2148000},
    "Berlijn": {"land": "Duitsland", "inwoners": 3769000}
}
if "Parijs" in steden:	# Is 'Parijs' een sleutel in de dictionary? 
    print("Parijs in steden!")
else:
    print("Parijs niet in steden!")

```



## Zoeken of een specifiek waarde voldoet
<p>Om een geneste dictionary te doorzoeken of er een specifieke waarde in voorkomt, gebruik je een logische vlag (op dezelfde manier als in <i>Onderwerp '7.3 Logische vlag'</i>). Je houdt een Boolean <code>gevonden</code> bij, die eerst <code>False</code> is. Je doorloopt de dictionary en als je de waarde vindt, zet je de vlag op <code>True</code>.</p>



<p><img src="https://course.cs.ru.nl/pythonVO/img/16.3_genesteDict_voorkomensTellen_stroomdiagram.png" alt="Figuur: Stroomdiagram zoeken" width="400"></p>

<p>Om te bepalen of een waarde in een geneste dictionary voorkomt, moet je eerst met de sleutel de geneste dictionary ophalen, en dan daarin kijken of een bepaalde waarde voorkomt.</p>


<p>In het voorbeeld hieronder bekijken we er een waarde voorkomt die voldoet aan een bepaalde voorwaarde. In dit geval zoeken we of er een stad is waarvan het aantal <code>inwoners</code> minder is dan 1 miljoen.</p>




```python
steden = {
    "Amsterdam":{"land": "Nederland", "inwoners": 921000},
    "Parijs": {"land": "Frankrijk", "inwoners": 2148000},
    "Berlijn": {"land": "Duitsland", "inwoners": 3769000}
}

gevonden = False	#logische vlag: waarde nu nog niet gevonden

for stad_info in steden.values(): # loop door de waardes van de dictionary
    if stad_info["inwoners"] < 1000000:  #als de waarde aan de voorwaarde voldoet
        gevonden = True # zet de vlag op True

if gevonden == True: # als de vlag op True staat
	print("Stad met minder dan 1 miljoen inwoners gevonden!") # print bevestiging dat waarde is gevonden
else:
	print("Geen stad met minder dan 1 miljoen inwoners gevonden.") # of print dat de waarde niet is gevonden

```


<p>Toelichting:
<ul>
    <li>om te beginnen is de waarde nog niet gevonden, dus <code>gevonden</code> is
        <code>False</code>;
    <li>we doorlopen de dictionary met een <code>for</code>-loop;</li>
    <li><code>steden.values()</code> geeft alle waardes van de dictionary (dus de dictionaries van Amsterdam, Parijs en Berlijn);
    <li>we controleren de voorwaarde, it dit geval met <code>stad_info["inwoners"] < 1000000"</code>;
    </li>
    <li>komen we de een waarde tegenkomen die aan de voorwaarde voldoet, dan wordt <code>gevonden</code>
        <code>True</code>;
    </li>
    <li>is <code>gevonden</code> na afloop nog steeds <code>False</code>, dan weet je dat er geen waarde in de dictionary voorkomt die aan de voorwaarde voldoet.</li>
</ul>
</p>


### Opdracht 16.8.1 Zoeken of er een waarde is die aan een voorwaarde voldoet

<p>Bepaal of minstens één stad in de dictionary is die meer dan 2 miljoen (2000000) inwoners heeft, en print dan of dat zo is of niet.</p>



```python
steden = {
    "Amsterdam": {"land": "Nederland", "inwoners": 921000, "werelddeel": "Europa"},
    "Buenos Aires": {"land": "Argentinië", "inwoners": 2890000, "werelddeel": "Zuid-Amerika"},
    "Rome": {"land": "Italië", "inwoners": 2873000, "werelddeel": "Europa"},
    "São Paulo": {"land": "Brazilië", "inwoners": 12330000, "werelddeel": "Zuid-Amerika"},
    "Tokyo": {"land": "Japan", "inwoners": 13960000, "werelddeel": "Azië"}
}
```

<p>Klik <a href="https://rweeda.github.io/PythonIA/docs/IA_H15_oplossingen.html#opgave1681">hier</a> voor een voorbeelduitwerking.</p>
<!-- ANTWOORD
steden = {
    "Amsterdam": {"land": "Nederland", "inwoners": 921000, "werelddeel": "Europa"},
    "Buenos Aires": {"land": "Argentinië", "inwoners": 2890000, "werelddeel": "Zuid-Amerika"},
    "Rome": {"land": "Italië", "inwoners": 2873000, "werelddeel": "Europa"},
    "São Paulo": {"land": "Brazilië", "inwoners": 12330000, "werelddeel": "Zuid-Amerika"},
    "Tokyo": {"land": "Japan", "inwoners": 13960000, "werelddeel": "Azië"}
}
gevonden = False	#logische vlag: waarde nu nog niet gevonden

for stad_info in steden.values():
    if stad_info["inwoners"] > 2000000:  #als de waarde aan de voorwaarde voldoet
        gevonden = True # zet de vlag op True

if gevonden == True: # als de vlag op True staat
	print("Stad met meer dan 2 miljoen inwoners gevonden!") # print bevestiging dat waarde is gevonden
else:
	print("Geen stad met meer dan 2 miljoen inwoners gevonden.") # of print dat de waarde niet is gevonden

-->


### Opdracht 16.8.2 Check op kleine groepen

<p>Schrijf code die met een logische vlag <code>gevonden</code> de dierentuin dictionary doorloopt, en deze op <code>True</code> zet als er voor een diersoort 3 of minder dieren zijn. Na afloop van de loop druk je af of er een waarde is gevonden dat aan de voorwaarde voldoet (dit laatste is al voor je voorgegeven).</p>


<p>De verwachte uitvoer is:<br>
<i> Diersoort met 3 of minder gevonden!</i></o>

```python
dierentuin = {
    "Leeuw": {"soort": "Zoogdier", "verblijf": "Savanne", "dieet": ["vlees"], "aantal": 2},
    "Pinguïn": {"soort": "Vogel", "verblijf": "Poolgebied", "dieet": ["vis", "kril"], "aantal": 15},
    "Python": {"soort": "Reptiel", "verblijf": "Terrarium", "dieet": ["muizen", "ratten"], "aantal": 3}
}
# HIER JE CODE SCHRIJVEN







if gevonden == True: # als de vlag op True staat
	print("Diersoort met 3 of minder gevonden!") # print bevestiging dat waarde is gevonden
else:
	print("Geen diersoort met 3 of minder gevonden.") # of print dat de waarde niet is gevonden


```

   


<p>Bekijk <a href="https://rweeda.github.io/PythonIA/docs/IA_H10_oplossingen.html#opgave1682" target="_blank">hier</a> de voorbeelduitwerking.</p>


<!-- ANTWOROD:

```python
dierentuin = {
    "Leeuw": {"soort": "Zoogdier", "verblijf": "Savanne", "dieet": ["vlees"], "aantal": 2},
    "Pinguïn": {"soort": "Vogel", "verblijf": "Poolgebied", "dieet": ["vis", "kril"], "aantal": 15},
    "Python": {"soort": "Reptiel", "verblijf": "Terrarium", "dieet": ["muizen", "ratten"], "aantal": 3}
}

gevonden = False	#logische vlag: waarde nu nog niet gevonden

for dier_info in dierentuin.values():
    if dier_info["aantal"] <= 3:  #als de waarde aan de voorwaarde voldoet
		gevonden = True # zet de vlag op True
if gevonden == True: # als de vlag op True staat
	print("Diersoort met 3 of minder gevonden!") # print bevestiging dat waarde is gevonden
else:
	print("Geen diersoort met 3 of minder gevonden.") # of print dat de waarde niet is gevonden
```

-->