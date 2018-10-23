def vier_letter_string():
    lijst = (input("Geef lijst met minimaal 10 strings: "))

    outfile = open("woorden.txt", "w")
    outfile.write(lijst)
    outfile.close()
    infile = open("woorden.txt", 'r')
    regel = infile.readlines()


    for words in regel:
        woorden = words.split("\", \"")
        outfile = open("strings.txt", 'a')
        print('De nieuw-gemaakte lijst met alle vier-letter strings is: ')
        for woord in woorden:
            if len(woord) == 4:
                return woord

vier_letter_string()