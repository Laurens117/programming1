def code(invoerstring):
    string =""
    for letter in invoerstring:
        string+=chr(ord(letter) + 3)
    print(string)

code("RutteAlkmaarDen Helder")
