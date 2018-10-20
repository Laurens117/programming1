def kaartnummers(filename):
    file = open(filename, "r")
    number_of_lines = 0
    mylist = []
    for line in file:
        number_of_lines += 1
        lst = line.split(",")
        kaartnummer = lst[0]
        naam = lst[1]
        mylist.append(lst[0])
    regel_nummer = mylist.index(max(mylist)) + 1
    print('Deze file telt', number_of_lines, 'regels.')
    print('Het grootste kaartnummer is:', max(mylist), 'en staat op regel', regel_nummer)

kaartnummers('kaartnummers')