import math
def rownanie_okregu(a=5,b=3,x=5,y=6):
    wynik = (x-a)**2+(y-b)**2
    r = math.sqrt(wynik)
    return r

print(rownanie_okregu())
