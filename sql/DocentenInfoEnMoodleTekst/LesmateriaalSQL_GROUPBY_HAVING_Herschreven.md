## ONDERWERP 6

## Rekenen

Je kunt rekenen met de waarden in een kolom. Hiervoor gebruik je `+`, `-`, `*`, `/` in de SELECT-instructie.

| Symbool | Betekenis       | Voorbeeld            | Uitleg                                      |
|---------|------------------|----------------------|----------------------------------------------|
| `+`     | Optellen         | `basisprijs + 1.00`  | Tel 1 euro bij de basisprijs op              |
| `-`     | Aftrekken        | `basisprijs - 0.50`  | Trek 50 cent van de basisprijs af            |
| `*`     | Vermenigvuldigen | `basisprijs * 2`     | Vermenigvuldig de basisprijs met twee        |
| `/`     | Delen            | `basisprijs / 2`     | Deel de prijs door twee                      |

### Voorbeeld: Prijsverhoging
De query hieronder telt bij de **basisprijs** een prijsverhoging van €1,00 op:

```sql
SELECT naam, basisprijs + 1.00 AS totaalprijs
FROM pizza;
```

### Verwerkingsopdracht: Prijs met bezorgkosten

Toon per pizza de basisprijs, een bezorgtoeslag van €0,50, en het totaalbedrag.

```sql
SELECT naam, basisprijs, basisprijs + 0.50 AS totaalprijs
FROM pizza;
```

### Verwerkingsopdracht: Totaalprijs per bestelling

Stel dat elke pizza €8,00 kost (ongeacht soort of formaat). Toon per bestelling het aantal (uit de tabel `besteldePizza`) en de berekende totaalprijs.

```sql
SELECT aantal, aantal * 8.00 AS totaalprijs
FROM besteldePizza;
```

## Volgorde van commando's voor het ophalen van informatie

Je leert hier de commando’s `GROUP BY` en `HAVING`. Een SQL-query kan meerdere onderdelen bevatten, die altijd in deze volgorde staan:

`SELECT` – `FROM` – `WHERE` – `GROUP BY` – `HAVING` – `ORDER BY` – `LIMIT`

Niet elk onderdeel is verplicht, maar de volgorde is dat wel.

### Verwerkingsopdracht: Volgorde van onderdelen

Zet de onderdelen van een SQL-query in de juiste volgorde:
`FROM` – `HAVING` – `ORDER BY` – `LIMIT` – `GROUP BY` – `SELECT` – `WHERE`

## GROUP BY

`GROUP BY` groepeert rijen die dezelfde waarde hebben in één of meer kolommen. Daarna kun je met functies zoals `COUNT()`, `SUM()`, `AVG()` of `MAX()` berekeningen doen per groep.

Als er in een vraag staat: "Hoeveel per bestelling?" of "per klant", dan gebruik je meestal `GROUP BY`.

### Voorbeeld: Aantal bestellingen per bodemcode

```sql
SELECT bodemcode, COUNT(aantal) AS aantal_besteld
FROM besteldePizza
GROUP BY bodemcode;
```

### Voorbeeld: Totaal aantal per pizzasoort

```sql
SELECT pizzacode, SUM(aantal) AS totaal_besteld
FROM besteldePizza
GROUP BY pizzacode;
```

### Verwerkingsopdracht: Gemiddeld aantal per pizzasoort

Toon per pizzasoort (`pizzacode`) hoeveel er gemiddeld tegelijk zijn besteld.

```sql
SELECT pizzacode, AVG(aantal) AS gemiddeld_aantal
FROM besteldePizza
GROUP BY pizzacode;
```

### Verwerkingsopdracht: Aantal bestellingen per bodemcode

```sql
SELECT bodemcode, COUNT(*) 
FROM besteldePizza 
GROUP BY bodemcode;
```

### Verwerkingsopdracht: Meeste pizza’s van één soort per bestelling

```sql
SELECT bestelcode, MAX(aantal) AS max_aantal
FROM besteldePizza
GROUP BY bestelcode;
```

## GROUP BY + HAVING

Gebruik `HAVING` om groepen te filteren **nadat** ze zijn gegroepeerd met `GROUP BY`. Je gebruikt `HAVING` in combinatie met functies zoals `COUNT()`, `SUM()`, `AVG()`, ...

### Voorbeeld: Alleen bodems die meer dan 1 keer zijn besteld

```sql
SELECT bodemcode, COUNT(*) AS aantal_besteld_per_bodem
FROM besteldePizza
GROUP BY bodemcode
HAVING COUNT(*) > 1;
```

### Verwerkingsopdracht: Alleen combinaties van bodemcode en omschrijving die meer dan 2 keer voorkomen

```sql
SELECT bodemcode, omschrijving, COUNT(*) AS aantal
FROM besteldePizza
GROUP BY bodemcode, omschrijving
HAVING COUNT(*) > 2;
```

### Verwerkingsopdracht: Bodems met meer dan 2000 bestellingen

```sql
SELECT bodemcode, COUNT(*) AS aantal_bestellingen
FROM besteldePizza
GROUP BY bodemcode
HAVING COUNT(*) > 2000;
```

## Verschil tussen WHERE en HAVING

- `WHERE` filtert individuele rijen **voordat** er gegroepeerd wordt.
- `HAVING` filtert **groepen** die zijn ontstaan door `GROUP BY`.

### Voorbeeldvergelijking:

```sql
-- Filter op rij-niveau
SELECT * 
FROM besteldePizza
WHERE bodemcode = 1;

-- Filter op groep-niveau
SELECT bodemcode, COUNT(*) AS aantal
FROM besteldePizza
GROUP BY bodemcode
HAVING COUNT(*) > 1;
```

## Verwerkingsopdracht: Bodems die vaak zijn besteld (maar zonder kleine bestellingen)

Toon per bodemcode hoeveel pizza’s er in totaal zijn besteld, maar reken alleen bestellingen mee waarbij meer dan 1 pizza is besteld. Toon alleen bodems waarvan het totaal boven de 2000 ligt.

```sql
SELECT bodemcode, SUM(aantal) AS totaal_besteld
FROM besteldePizza
WHERE aantal > 1
GROUP BY bodemcode
HAVING SUM(aantal) > 2000;
```

## Samenvatting

- Je kunt rekenen met kolomwaarden in SQL.
- `GROUP BY` groepeert rijen met gelijke waarden zodat functies zoals `COUNT()`, `SUM()` of `MAX()` op de groepen toegepast kunnen worden.
- `HAVING` filtert groepen na `GROUP BY`.
- SQL-onderdelen moeten in vaste volgorde worden gebruikt: `SELECT`, `FROM`, `WHERE`, `GROUP BY`, `HAVING`, `ORDER BY`, `LIMIT`.

## Afsluitende opdrachten

### Aantal bestellingen per bodem (sorteer van meest naar minst)

```sql
SELECT bodemcode, COUNT(*) AS aantal_besteld_per_bodem
FROM besteldePizza
GROUP BY bodemcode 
ORDER BY aantal_besteld_per_bodem DESC;
```

### Hoe vaak is een specifieke bodem gebruikt (alleen als dit meer dan 1 keer is gebeurd)

```sql
SELECT bodemcode, COUNT(*) AS aantal_besteld
FROM besteldePizza
WHERE bodemcode = 2
GROUP BY bodemcode
HAVING COUNT(*) > 1
ORDER BY aantal_besteld DESC
LIMIT 1;
```

### Totaal aantal pizza’s per klant

```sql
SELECT bestelling.klantnummer, SUM(besteldePizza.aantal)
FROM bestelling
JOIN besteldePizza ON bestelling.bestelcode = besteldePizza.bestelcode
GROUP BY bestelling.klantnummer;
```

### Meest bestelde pizzabodem

```sql
SELECT bodemcode, COUNT(*) AS aantal_besteld
FROM besteldePizza
GROUP BY bodemcode
ORDER BY aantal_besteld DESC
LIMIT 1;
```
