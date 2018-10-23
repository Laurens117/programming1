invoer = "5-9-7-1-7-8-3-2-4-8-7-9"
getallen=invoer.split("-")
volgorde=getallen.sort()
getallen1 = [int(i) for i in getallen]
som= sum(getallen1)

a = 'Gesorteerde list van ints:'
b = 'Grootste getal:'
c = 'en Kleinste getal:'
d = 'Aantal getallen:'
e = 'en Som van de getallen:'
f = 'Gemiddelde:'

print('{}, {}'.format(a,getallen1),'\n', b, str(max(getallen1)), c, str(min(getallen1)))
print(d, str(len(getallen1)),e,str(som))
print(f, str(som / len(getallen1)))
