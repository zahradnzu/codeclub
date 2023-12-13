Hb = float(input("Jakou má pacient hodnotu hemoglobinu v g/l?\n"))

if Hb < 120:
    print("anémie:(")
elif Hb > 160:
    print("je to moc:(")
else:
print("dobrý :)")

