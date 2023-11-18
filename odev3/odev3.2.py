
# 𝑓(x) = 4e^-1/2x − x  x=2 için 4 iterasyonla çözümü...

import  math

x=2

def mevcutDeger(x):
    result = 4*pow(math.e,-1/2*x)-x
    return result

def mevcutTurev(x):
    result=-2*pow(math.e,-1/2*x)-1
    return result


def tahmin(x,mevcutDeger,mevcutTurev):
    i = 0
    while i < 4:
        ıterasyon = x - mevcutDeger(x) / mevcutTurev(x)
        print(f"{i + 1}.nci Iterasyon: {ıterasyon}")
        x = ıterasyon
        i += 1


tahmin(2,mevcutDeger,mevcutTurev)
