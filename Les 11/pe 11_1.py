try:
    aantal_personen = eval(input('Met hoeveel personen ga je op reis? '))
    bedrag = 4356 / aantal_personen
    print(bedrag)

    if aantal_personen <0:
        print("Negatieve getallen zijn niet toegestaan!")

except ValueError:
    print("Gebruik cijfers voor het invoeren van het getal!")

except ZeroDivisionError:
    print("Delen door nul kan niet!")

except:
    print("Onjuiste invoer!")