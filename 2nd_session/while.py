pocet_mnau = int(input("Kolikrát mám zamňoukat?\n"))

# nase promenna counter, iniciovana na hodnotu 0
counter = 0

# jednoduchy while loop, ktery vyprinti "mňau" a jeho cislo,
# dokud nedosahne zadaneho poctu mňau z inputu 
while counter < pocet_mnau:
    print(f"mňau číslo {counter}")
    counter += 1