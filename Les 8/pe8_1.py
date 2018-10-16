def seizoen(maand):
    if maand == 12 or maand == 1 or maand == 2:
        print('Het is winter, het is koud!')
    elif maand == 3 or maand == 4 or maand == 5:
        print('Het is lente, alles groeit weer!  ')
    elif maand == 6 or maand == 7 or maand == 8:
        print('Het is zomer, trek je jas uit!')
    elif maand == 9 or maand == 10 or maand == 11:
        print('Het is herfst, de bladjes vallen!')
    else:
        print('Geen geldige maand!')
        
maand = eval(input("Geef een maandnummer: "))
seizoen(maand)
