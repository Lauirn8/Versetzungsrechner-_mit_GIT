stationen = int(input("Geben sie an wie viele Stationen sie fahren möchten: "))

if stationen > 3:
   normal = print("Sie brauchen das normales Ticket")
elif stationen <= 3:
   klein = print("Sie brauchen das kleine Ticket")

ausgabe = normal if stationen >= 4 else klein