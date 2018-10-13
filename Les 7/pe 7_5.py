def gemiddelde(zin):
    woorden=zin.split()
    totaallengtewoord=0
    for woord in woorden:
        totaallengtewoord+=len(woord)
    gemiddelde_word = totaallengtewoord*1./len(woorden)
    print("De gemiddelde lengte van de woorden in de zin:", gemiddelde_word)


zin= input('Type hier een zin: ')
gemiddelde(zin)

