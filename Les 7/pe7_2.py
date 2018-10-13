filename = "kaartnummers"
file = open(filename, "r")
for line in file:
    lst = line.split(",")
    print('{} Heeft kaartnummer: {}'.format(lst[1].strip(),lst[0]))
