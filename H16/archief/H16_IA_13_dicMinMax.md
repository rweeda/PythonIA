## 5: Kleinste en grootste waarde uit een dictionary bepalen
<p>Met een <code>for</code>-loop kun je ook bepalen wat het kleinste (of grootste) getal is dat in een dictionary voorkomt. Je gebruikt daarvoor een variabele om bij te houden wat de kleinste waarde is die je tot dan toe gezien hebt. Kom je nog een kleinere waarde tegen, dan sla je die kleinere waarde op in je variabele. Om te beginnen is de eerste waarde de kleinste waarde tot dan toe.</p>


TODO IMAGE

<p><img src="https://course.cs.ru.nl/pythonVO/img/10.5Kleinste_Stroomdiagram.jpg" alt="Figuur: Stroomdiagram kleinste" width="400"></p>







```python
steden = {
    "Amsterdam": {"land": "Nederland", "inwoners": 921000, "werelddeel": "Europa"},
    "Buenos Aires": {"land": "Argentinië", "inwoners": 2890000, "werelddeel": "Zuid-Amerika"},
    "Rome": {"land": "Italië", "inwoners": 2873000, "werelddeel": "Europa"},
    "São Paulo": {"land": "Brazilië", "inwoners": 12330000, "werelddeel": "Zuid-Amerika"},
    "Tokyo": {"land": "Japan", "inwoners": 13960000, "werelddeel": "Azië"},
}

# Zet de sleutels (stedenamen) in een lijst
stad_namen = list(steden.keys())

# Initialiseer minimum met de eerste stad
min_inwoners = steden[stad_namen[0]]["inwoners"]
kleinste_stad = stad_namen[0]

# Loop met while door de rest van de steden
for stad in stad_namen:
    # Vergelijk het aantal inwoners met de huidige minimum

    if steden[stad]["inwoners"] < min_inwoners:
        min_inwoners = steden[stad]["inwoners"] 	 	
        kleinste_stad = stad

print(f"De stad met de minste inwoners is {kleinste_stad} met {min_inwoners} inwoners.")
```

    De stad met de minste inwoners is Dorpje met 13000 inwoners.
    De stad met de minste inwoners is Dorpje met 13000 inwoners.



### Opdracht 10.7 De meeste likes
<p>Een groepje meiden wil hun aantal likes bij TikTok vergelijken. Hun likes staan in een lijst:
    <!--<pre class="python">
likes_lijst = [102, 110, 502, 234, 340, 20]
</pre>-->

</p>
<p>Bepaal wat het grootste aantal likes is. Hiervoor gebruik je een <code>for</code>-loop zoals in het vorige voorbeeld gedaan is, maar in plaats van naar het kleinste ga je op zoek naar de grootste.</p>



```python
likes_lijst = [102, 110, 502, 234, 340, 20]
```


<p>Bekijk <a href="https://rweeda.github.io/PythonIA/docs/IA_H10_oplossingen.html#opgave1051" target="_blank">hier</a> de voorbeelduitwerking.</p>
