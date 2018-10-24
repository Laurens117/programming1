import random

count = 0

def monopolyworp(count):

    worp1 = random.randrange(1, 7)
    worp2 = random.randrange(1, 7)
    som = worp1+worp2
    print (worp1,"+",worp2,"=",som)

    if worp1==worp2:
        count+=1
        if count==3:
            print("direct naar de gevangenis")
        else:
            monopolyworp(count)

monopolyworp(count)