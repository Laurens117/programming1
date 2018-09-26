def kwadraten_som(grondgetallen):
    som = 0
    for grondgetal in grondgetallen:

        if grondgetal >= 0:
            kwadraat = grondgetal ** 2
            som= som + kwadraat
    return som

grondgetallen = [4, 5, 3, -81]
print(kwadraten_som(grondgetallen))



