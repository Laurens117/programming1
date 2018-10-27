from tkinter import *

import requests
import xmltodict

def station_vertrektijd(station):
    auth_details = ('wavzaly@gmail.com', 'BUzy418n3IeT2CnfNbOOM8Qb_Wpz86LeMkWDWzUL4M4iWNvcJEFfkw')
    api_url = 'http://webservices.ns.nl/ns-api-avt?station='+station
    response = requests.get(api_url, auth=auth_details)

    vertrekXML = xmltodict.parse(response.text)
    print('Dit zijn de vertrekkende treinen:')

    for vertrek in vertrekXML['ActueleVertrekTijden']['VertrekkendeTrein']:
        eindbestemming = vertrek['EindBestemming']

        vertrektijd = vertrek['VertrekTijd']      # 2016-09-27T18:36:00+0200
        vertrektijd = vertrektijd[11:16]          # 18:36

        print('Om '+vertrektijd+' vertrekt een trein naar '+ eindbestemming)

def Stations():
    station = stationEntry.get()
    bestemming = station_vertrektijd(station)



root = Tk()

stationEntry = Entry(master=root)
stationEntry.pack()

button = Button(master=root, text="Druk hier", command=Stations)
button.pack()

label = Label(master=root)
label.pack()

root.mainloop()