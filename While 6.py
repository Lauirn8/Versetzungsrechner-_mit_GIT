


sz = int(input("Bitte eine Startzahl angeben: "))
ez = int(input("Bitte eine Endzahl angeben: "))
sw = int(input("Geben sie eine Schrittweite an: "))

i = 0
summiert = 0
for i in range(sz,ez,sw):
    print(i)
    summiert += i

print(summiert)


