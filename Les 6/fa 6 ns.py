def standaardprijs(afstandKM):
    global prijs
    if 50 > afstandKM > 0:
        prijs = afstandKM * 0.80
    elif afstandKM > 50:
        prijs = 15 + afstandKM * 0.60
    elif afstandKM < 0:
        prijs = 0
    return prijs


def bepaal_weekend(dag):
    if dag == 'zaterdag' or dag == 'zondag':
        return True
    else:
        return False


afstandKM = eval(input('Hoeveel km gaat u reizen?: '))
dag = input('Welke dag gaat u reizen?: ')
leeftijd = int(input('Wat is uw leeftijd?: '))

weekendrit = bepaal_weekend(dag)
prijs = standaardprijs(afstandKM)


def ritprijs(leeftijd, weekendrit, afstandKM):
    if leeftijd < 12 or leeftijd >= 65:
        if weekendrit:
            nieuwe_prijs = prijs * 0.65
        else:
            nieuwe_prijs = prijs * 0.70
    else:
        if weekendrit:
            nieuwe_prijs = prijs * 0.60
        else:
            nieuwe_prijs = prijs
    return nieuwe_prijs


nieuwe_prijs = ritprijs(leeftijd, weekendrit, afstandKM)
print('U kunt €', nieuwe_prijs, 'betalen.')
