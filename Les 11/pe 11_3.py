import csv

with open('Scorelijst.csv', mode='r') as csv_file:
    scorelijst = csv.reader(csv_file, delimiter=';')
    winning=0
    winnaar=[]

    for rij in scorelijst:
        if int(rij[2])>int(winning):
            winning = rij[2]
            winnaar = rij
    print("De hoogste score is: {} op {} behaald door {}".format(winnaar[2],winnaar[1], winnaar[0]))