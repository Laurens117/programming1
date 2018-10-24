def vier_letter_string():

    while True:
        woord=input("Geef een string van vier letters: ")
        print(woord,"heeft", str(len(woord)), "letters.")
        if len(woord)== 4:
            print('Inlezen van correcte string:', woord, 'is geslaagd!')
            break

vier_letter_string()