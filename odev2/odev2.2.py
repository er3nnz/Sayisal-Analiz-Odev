# 𝑥^3 + 4𝑥^2 − 10 = 0 denekleminin [1,2] aralığındaki iterasyonu

def iterayon(x):
    result = 𝑥**3 + 4*𝑥**2 - 10
    return result


x=float(1.5)
if x==1.5 and iterayon(x)>0:
    print("Yeni Iterasyon Araligimiz : [1,1.5]")
    if x==1.25 and iterayon(x)>0:
        print("Yeni Iterasyon Araligimiz :[1,1.25]")
    else:
        print("Yeni Iterasyon Araligimiz :[1.25,1.50]")
        if x==1.375 and iterayon(x)>0:
            print("Yeni Iterasyon Araligimiz : [1.375,1.50]")
        else:
            print("Yeni Iterasyon Araligimiz : [1.25,1.375]")
            if x==1.3125 and iterayon(x)>0:
                print("Yeni Iterasyon Araligimiz : [1.25,1.3125]")
            else:
                print("Yeni Iterasyon Araligimiz : [1.3125,1.375]")
else:
    print("Yeni Iterasyon Araligimiz : [1.5,2]")