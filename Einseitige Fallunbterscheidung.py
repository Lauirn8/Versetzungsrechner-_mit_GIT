gefahren = input("geben sie die gefahren Geschwindigkeit in KM/H an: ")
if int(gefahren) >30:
    differenz = int(gefahren) -30
    print("Sie sind zu schnell gefahren. Ihre gefahrene Geschwindigkeit lag bei ",gefahren,"KM/H, dies sind", differenz,"KM/H mehr als erlaubt.")
    