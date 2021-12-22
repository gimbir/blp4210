# 2. Bir dizinin içindeki en buyuk tek ve en küçük tek sayı arasındaki farkın karesini bulan  python  kodunu fonksiyon kullanarak yazın.

import random


def hesap(liste):
    # Yontem 1
    # liste = sorted(liste)
    # return liste

    # Yontem 2
    ek = liste[0]
    for i in range(0, len(liste)):
        if liste[i] < ek:
            ek = liste[i]

    return ek

    # Yontem 3
    # return min(liste)


liste = [random.randrange(1, 50, 1) for i in range(50)]

print(liste)
print(hesap(liste))
