list100 = []
list = []


for i in range(1,101):
    list100.append(i)

toplam = int(sum(list100))
sonuc1 = int(pow(toplam,2))


for a in list100:

   us = int(pow(a,2))
   list.append(us)

sonuc2 = int(sum(list))

print(sonuc1-sonuc2)
