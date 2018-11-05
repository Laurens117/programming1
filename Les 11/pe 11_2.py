import datetime
import csv

bestand = 'inloggers.csv'

while True:
    naam = input("Wat is je achternaam: ")
    if naam == 'einde':
        break

    voorl = input("Wat zijn je voorletters: ")
    gbdatum = input("Wat is je geboortedatum: ")
    email = input("Wat is je e-mail adres: ")

    with open ('inloggers.csv', 'a', newline='')as inloggers:
        vandaag = datetime.datetime.today()
        s = vandaag.strftime("%a %d %b %Y at %H:%M")
        output = csv.writer(inloggers, delimiter=';')
        output.writerow([s, voorl, naam, gbdatum, email])