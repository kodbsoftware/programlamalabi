#fibonacci sayısı, faktoriyel alma ve üs alma islemlerinin hem normal döngü hemde recursive fonksiyon ile yapımı
def fibo_loop(n):
    a,b=0,1
    if(n==0):
        return 0
    for i in range(n-1):
        a,b=b,a+b
    return b

fibo_loop(7)
#-----------------------------------------------------------
def fibo_recursive(n):
    if(n<2):
        return n
    else:
        return fibo_recursive(n-1)+fibo_recursive(n-2)
    
fibo_recursive(7)
#-----------------------------------------------------------
def factorial(n):
    s=1
    for i in range(1,n+1):
        s=s*i
    return s

factorial(5)
#-----------------------------------------------------------
def factorial_recursive(n):
    if(n==1):
        return n
    else:
        return n*factorial_recursive(n-1)
    
factorial_recursive(5)
#-----------------------------------------------------------
def power(m,n):
    s=m
    for i in range(1,n):
        s=s*m
    return s

power(5,2)
#-----------------------------------------------------------
def power_recursive(m,n):
    if(n==0):
        return 1
    elif(n==1):
        return m
    elif(n%2==0):
        return power_recursive(m*m,n//2)
    elif(n%2!=0):
        return power_recursive(m*m,n//2)*m

power_recursive(5,3)
