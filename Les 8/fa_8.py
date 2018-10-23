infile = open('kluizen.txt', 'r')

regel = infile.readlines()

def toon_aantal_kluizen_vrij():
    regels=0
    for line in regel:
        regels+=1
    infile.close()
    print('\n Er zijn nog '+str(12-regels),' kluizen vrij.')

def nieuwe_kluis():
    list=[]
    for i in range(1,13):
        list+=[i]
    for gedeelte in regel:
        regel_split=gedeelte.split(";")
        if int(regel_split[0])in list:
            test=int(regel_split[0])
            test1=list.pop(list.index(test))

    if len(list)==0:
        print("Sorry, alle kluisjes zijn vol.")

    else:
        print('Deze kluisjes zijn nog vrij: '+str(list))
        kies=int(input('Welk kluisje wilt u hebben?: '))
        if kies in list:
            print("U krijgt kluisje "+str(kies))
            code = input("Geef een code op, minimaal 4 characters lang: ")
            if len(code) >= 4:
                print('Gefeliciteerd, u heeft nu een kluisje.')
                outfile=open('kluizen.txt','a')
                outfile.write(str(kies)+';'+str(code)+'\n')
                outfile.close()
            else:
                print('Sorry, uw code is niet goed.')
        else:
            print("Sorry, dit is niet mogelijk!.")

def kluis_openen():

    kluisje = input('Wat is uw kluisnummer:')
    codes = input("Wat is uw code: ")
    kluis= False

    for gedeelte in regel:
        regel_split=gedeelte.split(";")
        #print(regel_split[1].strip())
        if kluisje == regel_split[0] and codes==regel_split[1].strip():
            kluis = True
            print('Het kluisje is nu geopend.')

    if kluis==False:
        print('Dit is niet uw kluisje.')

def kluisteruggeven():
    print('\nSorry, dit is niet mogelijk!')

menu='1: Ik wil weten hoeveel kluizen nog vrij zijn. \n2: Ik wil een nieuwe kluis. \n3: Ik wil even iets uit mijn kluis halen. \n4: Ik geef mijn kluis terug.'
print(menu)

nummer= int(input('Kies een nummer om verder te gaan: '))

if nummer <= 0 or nummer >= 5:
    print("\nSorry, dit is geen geldig getal. Probeer het opnieuw.")
    print('\n1: Ik wil weten hoeveel kluizen nog vrij zijn. \n2: Ik wil een nieuwe kluis. \n3: Ik wil even iets uit mijn kluis halen.\n4: Ik geef mijn kluis terug.')
    nummer = int(input('Kies een nummer om verder te gaan: '))

    if nummer <= 0 or nummer >= 5:
        print('Probeer opnieuw!')
        print(exit())

if nummer ==1:
    toon_aantal_kluizen_vrij()

if nummer ==2:
    nieuwe_kluis()

if nummer ==3:
    kluis_openen()

if nummer == 4:
    kluisteruggeven()