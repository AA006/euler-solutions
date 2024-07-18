a=1
b=1
c=0

for i in range(31):
    a,b = b, a+b
    if b%2==0:
        c+=b
        print(c)
