# x^3 -2x^2 -5= 0 denekleminin [2,4] aralığındaki iterasyonu

def iterayon(x):
    result = x**3 - 2*x**2 - 5
    return result
x=3
if x==3 and iterayon(x)>0:
    print("Yeni Iterasyon Araligimiz : [2,3]")
    if x==2.5 and iterayon(x)>0:
        print("Yeni Iterasyon Araligimiz : [2,2.5]")
    else:
        print("Yeni Iterasyon Araligimiz : [2.5,3]")
        if x==2.75 and iterayon(x)>0:
            print("Yeni Iterasyon Araligimiz : [2.5,2.75]")
        else:
            print("Yeni Iterasyon Aralıgimiz : [2.75,3]")
            if x==2.625 and iterayon(x)>0:
                print("Yeni Iterasyon Araligimiz : [2.5,2.625]")
            else :
                print("Yeni Iterasyon Araligimiz : [2.625,2.75]")
else:
    print("Yeni Iterasyon Araligimiz : [3,4]")
