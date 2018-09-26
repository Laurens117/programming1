def stand_prijs(afstandkm):
    prijs = 0.80
    vastebedrag = 15
    nieuweprijs = 0.60

    if afstandkm >= abs(50):
        afstandkm = afstandkm * nieuweprijs + vastebedrag
    else:
        afstandkm= afstandkm * prijs
    if afstandkm <0:
        afstandkm = 0
    return afstandkm

def ritprijs(leeftijd, weekendrit, afstandkm):
    if weekendrit is 'weekendrit':
        return True
    else:
        return False
