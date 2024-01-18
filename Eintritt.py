alter = int(input("geben sie bitte ihr alter an: "))

if alter < 6:
    print("Die Eintrittskosten betragen 0€.")

if alter >= 6 and alter <= 17:
    print("Die Eintrittskosten betragen 5€.")

if alter >= 18:
    print("Die Eintrittskosten betragen 8€.")


preis = 0 if alter < 6 else 5 if alter >= 6 and alter <= 17 else 8 if alter >= 18

