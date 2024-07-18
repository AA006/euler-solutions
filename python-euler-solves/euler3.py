n=600851475143
bolen=2
list=[]

while n>1:
    if n%bolen == 0:
        list.append(bolen)
        n //= bolen
    else:
        bolen+=1
print(list)