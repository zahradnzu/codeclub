
Hb = float(input("Jakou má pacient hodnotu hemoglobinu v g/l?\n"))
sex = input("Jaké má pacient pohlaví? M/F\n").strip().lower()

if sex != "m" and sex != "f":
    print("špatné pohlaví")
else:
    if sex == "f":
        if Hb < 120:
            print("anémie:(")
        elif Hb > 160:
            print("to je zas mocinky:(")
        else:
            print("vpoho :)")
    if sex == "m":
        if Hb < 135:
            print("anémie:(")
        elif Hb > 170:
            print("to je zas mocinky:(")
        else:
            print("vpoho :)")