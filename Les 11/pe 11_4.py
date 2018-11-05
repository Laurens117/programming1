import csv

with open('Productenlijst.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    duurste = 0
    duurste_product = []
    aantal = 600
    goedkoopste = []
    voorraad = 0

    for rij in csv_reader:
        if line_count == 0:
            line_count += 1

        else:
            voorraad += int(rij[3])
            if float(rij[4]) > float(duurste):
                duurste = rij[4]
                duurste_product = rij

            if float(rij[3])<float(aantal):
                aantal = rij[3]
                goedkoopste = rij

print('Het duurste artikel is {} en die kost {} Euro.'.format(duurste_product[2],duurste_product[4]))
print('Er zijn slechts {} exemplaren in voorraad van het product met nummer {}.'.format(goedkoopste[3],goedkoopste[0]))
print('In totaal hebben wij {} producten in ons magazijn liggen.'.format(voorraad))