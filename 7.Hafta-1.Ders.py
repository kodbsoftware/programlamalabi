import random
import pylab
import numpy

# def ZarAt():
#     """Return a random int between 1-6"""
#     return random.choice([1,2,3,4,5,6])

# def Tane(n):
#     result=''
#     for i in range(n):
#         result= result+str(ZarAt())+" "
#     print(result)

# Tane(10)

# def at(atmaSayısı):
#     heads=0
#     for i in range(atmaSayısı):
#         if random.choice(('H','T')) == 'H':
#             heads+=1
#     return heads/atmaSayısı
# def atSim(numFlipsPerTrial, denemeSayısı):
#     fracHeads=[]
#     for i in range(denemeSayısı):
#         fracHeads.append(at(numFlipsPerTrial))
#         mean=sum(fracHeads)/len(fracHeads)
#     return mean

# print(atSim(10,10000))
def yazıtura(enaz,encok):
    deneme=[]
    ybölüt=[]
    yeksit=[]
    for i in range(enaz,encok+1):
        deneme.append(2**i)
    for dene in deneme:
        ysayısı=0
        tsayısı=0
        for n in range(dene):
            if(random.choice(('Y','T'))=='Y'):
                ysayısı+=1
            else:
                tsayısı+=1
        ybölüt.append(ysayısı/tsayısı)
        yeksit.append(abs(ysayısı-tsayısı))
    pylab.title('Yazı-Tura Farkı')
    pylab.xlabel('Deneme Sayısı')
    pylab.plot(deneme,yeksit)
    pylab.figure()
    pylab.title('Yazı/Tura Oranı')
    pylab.xlabel('Deneme Sayısı')
    pylab.plot(deneme,ybölüt)
