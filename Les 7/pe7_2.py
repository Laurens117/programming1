def split_txt(filename):
    file = open(filename, "r")
    for line in file:
        lst = line.split(",")
        print('{} Heeft kaartnummer: {}'.format(lst[1].strip(),lst[0]))

split_txt('kaartnummers')