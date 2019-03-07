#vektorlerde işlemler
def my_vector_scalar_product(alpha,v):
    size=len(v)
    my_result=[]
    for i in range(size):
        my_result.append(0)
    for i in range(size):
        my_result[i]=alpha*v[i]
    return my_result

    
def my_vector_substraction(v,w):
    size=len(v)
    my_result=[]
    for i in range(size):
        my_result.append(0)
    for i in range(size):
        my_result[i]=v[i]-w[i]
    return my_result


def my_vector_addition(v,w):
    size=len(v)
    my_result=[]
    for i in range(size):
        my_result.append(0)
    for i in range(size):
        my_result[i]=v[i]+w[i]
    return my_result
    
    
def my_vector_inner_product(v,w):
    size=len(v)
    my_result=[]
    for i in range(size):
        my_result.append(0)
    
    for i in range(size):
        my_result[i]=v[i]*w[i]
    t=0
    for i in range(size):
        t=t+my_result[i]
    return t
    
    
a=[1,2,3,2,4,6]
b=[11,22,33,22,44,66]

print(my_vector_addition(a,b))
print(my_vector_substraction(a,b))
alpha=5
beta=10
c=my_vector_scalar_product(alpha,a)
d=my_vector_scalar_product(beta,b)
e=my_vector_addition(c,d)
f=my_vector_substraction(a,b)
g=my_vector_inner_product(e,f)
print(c,"\n",d,"\n",e,"\n",f,"\n",g)


x=[21,2]
y=[30,15]
print(my_vector_inner_product(x,y))
