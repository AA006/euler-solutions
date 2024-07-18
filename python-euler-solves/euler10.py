
import math

sayac = 0


def Primee(x):
    prime = True
    if x == 2:
        return prime
    else:
        for i in range(2, math.isqrt(x) + 1):
            if x % i == 0:
                prime = False
                break
        return prime

snc = 0

i = 2
while True:
    if Primee(i) == True:
        sayac += 1
        snc = snc + i
        print(sayac, ".", i, "\n",snc)
    if i == 2000000:
        break
    i += 1
