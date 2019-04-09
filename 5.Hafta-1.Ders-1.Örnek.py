def carpan(a):
    carpanlar=""
    asal=[]
    asalmı=False
    for i in range(2,int(a/2),+1):
        for j in range(2,i,+1):
            if(i%j!=0):
                asalmı=True
            else:
                asalmı=False
                break
        if(asalmı==True):
            asal.append(i)    
    while(a%2==0):
        a/=2
        carpanlar+="2"
    for k in range(len(asal)):
       while(a%asal[k]==0):
           a/=asal[k]
           carpanlar+=str(asal[k])
    print(carpanlar)

carpan(300)
