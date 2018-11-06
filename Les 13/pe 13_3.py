import xmltodict

def XML_lezer(bestand):
    with open(bestand) as XML_bestand:
        string = XML_bestand.read()
        xmldictionary = xmltodict.parse(string)
        return xmldictionary

dict = XML_lezer("Stationlijst")

stations = dict['Stations']['Station']
print('Dit zijn de codes en types van de 4 stations:')

for i in stations:
    print('{:4} - {}'.format(i ['Code'],i ['Type']))
print('\nDit zijn alle stations met één of meer synoniemen:')

for i in stations:
    if i ['Synoniemen'] is not None:
        print('{:4} - {}'.format(i ['Code'], i ['Synoniemen']))
print('\nDit is de lange naam van elk station:')

for i in stations:
    print('{:4} - {}'.format(i ['Code'],i ['Namen']['Lang']))