Verilen L = [1, 2, 3, 4, 5, 6,7,8,……….225] listesine, lambda, map, reduce, filter fonk kullanarak,
from functools import reduce
from math import sqrt
from statistics import variance, mean

liste = [i for i in range(1, 256)]
x = []
# a)sayılardan 3’e tam bölünenleri
uc = lambda sayi: sayi % 3

for i in liste:
    if uc(i) == 0:
        print(i)


# b)çift olan sayuların toplamını
sonuc = list(filter(lambda x: x % 2 == 0, liste))
toplam = 0
for i in range(0, len(sonuc)):
    toplam = toplam + sonuc[i]

print(toplam)

# c)ortalamının %10  üstüne olanları

print(list(filter(lambda sayi: (sayi > (mean(liste) + mean(liste) * 0.1)), liste)))

# d) listede sayilarin kupleirni ve toplamini
kup = list(map(lambda x: x ** 3, liste))
print(kup)

toplam = reduce(lambda x, y: x + y, liste)
print(toplam)

# e)Sayıların varyans ve standard sapmasını bulan programı yazınız
varyans = lambda liste, ort: sum([x ** 2 for x in [i - ort for i in liste]]) / float(
    len(liste)
)
print(varyans(liste, mean(liste)))


std_sapma = lambda liste: sqrt(variance(liste, mean(liste)))
std_sapma2 = lambda liste: sqrt(varyans(liste, mean(liste)))

print(std_sapma(liste))
print(std_sapma2(liste))
