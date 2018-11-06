import xmltodict

def XML_lezer(bestand):
    with open(bestand) as XML_bestand:
        string = XML_bestand.read()
        XML_dictionary = xmltodict.parse(string)
        return XML_dictionary

dict = XML_lezer("Productenlijst")
producten = dict['artikelen']['artikel']

for product in producten:
    print(product['naam'])