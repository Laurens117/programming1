def convert(celsius):
    f = celsius*1.8+ 32
    return f

header=( "{:>4} {:>7}".format('F','C'))
print(header)

def table():
    celsius= range(-30, 41, 10)
    for c in celsius:
        f = convert(c)
        text = "{:>6} {:>7}".format(f,float(c))
        print(text)
table()
