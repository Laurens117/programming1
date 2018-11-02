import requests
import xmltodict

def station_vertrektijd(station):
    auth_details = ('wavzaly@gmail.com', 'BUzy418n3IeT2CnfNbOOM8Qb_Wpz86LeMkWDWzUL4M4iWNvcJEFfkw')
    api_url = 'http://webservices.ns.nl/ns-api-avt?station='+station
    response = requests.get(api_url, auth=auth_details)

    vertrekXML = xmltodict.parse(response.text)
    print('Dit zijn de vertrekkende treinen:')
    print(vertrekXML)

    tijdEnBestemmingen =[]
    x=int()
    try:
        for vertrek in vertrekXML['ActueleVertrekTijden']['VertrekkendeTrein']:
            eindbestemming = str(vertrek['EindBestemming'])

            vertrektijd = vertrek['VertrekTijd']      # 2016-09-27T18:36:00+0200
            vertrektijd = vertrektijd[11:16]
            spoor = vertrek['VertrekSpoor']['#text']# 18:36
            tijdEnBestemmingen.append((vertrektijd, eindbestemming, spoor))
            print('Om '+vertrektijd+' vertrekt een trein naar '+ eindbestemming+' op spoor '+spoor)
            x=x+1
            if x ==20:
                break
    except KeyError:
        print('foutmelding')
    return tijdEnBestemmingen