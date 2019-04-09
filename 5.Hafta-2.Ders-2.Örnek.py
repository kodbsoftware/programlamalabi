def asd(a):
    sonuc=[]
    toplam=0
    for i in range(len(a)):
        for j in range(i+1,len(a)):
            for k in range(i,j+1):
                toplam+=a[k]
            sonuc.append(toplam)
            toplam=0

    print(sonuc)
    buyuk=0
    for l in range(len(sonuc)):
        if(sonuc[l]>buyuk):
            buyuk=sonuc[l]
    return buyuk

liste=[4,-3,2,-1,-2,6,-5]
print(asd(liste))
