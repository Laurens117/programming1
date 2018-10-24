def namen():
    namenlijst = {}
    count = 0
    naam = input("Geef een naam: ")

    while naam!='':
        if namenlijst.get(naam):
            namenlijst[naam] = namenlijst[naam] + 1
        else:
            namenlijst[naam] = 1
        count = count + 1
        naam = input("Volgende naam: ")

    for name in namenlijst:
        if namenlijst[name] >= 2:
            print('Er zijn ' + str(namenlijst[name]) + ' studenten met de naam ' + str(name))
        else:
            print('Er is '+ str(namenlijst[name])+' student met de naam '+str(name))
namen()
