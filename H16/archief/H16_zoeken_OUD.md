

## Waarde in een geneste dictionary zoeken

<p>Om te bepalen of een waarde in een geneste dictionary voorkomt, moet je eerst met de sleutel de geneste dictionary ophalen, en dan daarin kijken of een bepaalde waarde voorkomt.</p> <p><i>Ter herhaling staat onderaan deze pagina hoe <code>in</code> en <code>.values()</code> gebruikt kunnen worden.</p>
<p>
In het voorbeeld hieronder:
<ul>
<li>geeft <code>steden.values()</code> alle waardes van de dictionary (dus de dictionaries van Amsterdam, Parijs en Berlijn);
<li>en checkt <code>stad_info["land"] == "Nederland"</code> of het *land* gelijk is aan "Nederland".
</ul>
</p>

```python
steden = {
    "Amsterdam":{"land": "Nederland", "inwoners": 921000},
    "Parijs": {"land": "Frankrijk", "inwoners": 2148000},
    "Berlijn": {"land": "Duitsland", "inwoners": 3769000}
}

for stad_info in steden.values():
    if stad_info["land"] == "Nederland": # Is stad van een land gelijk aan Nederland?
        print("Deze stad ligt in Nederland:", stad_info)    

```



## Herhaling - Dictionary bekijken met <code>in</code>

<p>We hebben eerder geleerd dat je met <code>in</code> kunt bepalen of een sleutel in een dictionary voorkomt.</p>


```python
steden = {
    "Amsterdam":"Nederland",
    "Parijs":"Frankrijk",
    "Berlijn":"Duitsland"
}

if "Parijs" in steden:	# Is 'Parijs' een sleutel in de dctionary? 
    print("Parijs in steden!")
else:
    print("Parijs niet in steden!")


```

    Parijs in steden!
    dict_values(['Nederland', 'Frankrijk', 'Duitsland'])


## Herhaling - Dictionary waarden ophalen met <code>.values()</code>
<p>We hebben ook geleerd dat je met <code>.values()</code> kunt de waarde bij een sleutel in een dictionary kan krijgen.</p>


```python
steden = {
    "Amsterdam":"Nederland",
    "Parijs":"Frankrijk",
    "Berlijn":"Duitsland"
}
print(steden.values())
```


### Opdracht 3769000 inwoners zoeken

Bepaal of er een stad is die precies 376000 inwoners heeft.


```python
steden = {
    "Amsterdam":{"land": "Nederland", "inwoners": 921000},
    "Parijs": {"land": "Frankrijk", "inwoners": 2148000},
    "Berlijn": {"land": "Duitsland", "inwoners": 3769000}
}

for stad_info in steden.values():
    if stad_info["inwoners"] == 3769000: # Is het aantal inwoners gelijk aan 3769000? 
        print("Gevonden:", stad_info)
```

    gevonden: {'land': 'Duitsland', 'inwoners': 3769000}

