Hb = float(input("Jakou má pacient hodnotu hemoglobinu v g/l?\n"))
sex = input("Jaké má pacient pohlaví? M/F\n").strip().lower()

if (Hb < 120 and sex == "f") or (Hb < 135 and sex == "m"):
    print("anémie")
elif Hb > 160 and sex == "f" or Hb > 170 and sex == "m":
    print("je to moc:(")
else:
    print("vpoho:)")