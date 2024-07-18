import math

sayac = 0


def prime_check(x):
    is_prime = True
    if x == 2:
        return is_prime
    else:
        for i in range(2, int(math.sqrt(x)) + 1):
            if x % i == 0:
                is_prime = False
                break
        return is_prime


i = 2
while True:
    if prime_check(i) == True:
        sayac += 1
        print(sayac, ".", i)
    if sayac == 10001:
        break
    i += 1
