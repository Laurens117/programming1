def tafels(x,y):
    for i in range(x,y):
        for j in range(1, 11):
            print('{:02}'.format(i),'x','{:02}'.format(j),'=','{:02}'.format(i*j))

tafels(1,11)

