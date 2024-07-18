list1 = []
list2 = []
num3=0

for i in range(100, 1000):
    list1.append(i)
    list2.append(i)
for num in list1:
    for num2 in list2:
        num3 = num * num2
        if int(str(num3))==int(str(num3)[::-1]):
            print(num3)
