#matrislerde işlemler
def my_matrix_addition(m_1,m_2): 
    result=[]
    for row in range(len(m_1)):
        result.append([])
        for column in range(len(m_1[0])):
            result[row].append(m_1[row][column]+m_2[row][column])
    return result

matrix_1=[[4,6,3],[8,5,6]] 
matrix_2=[[5,2,3],[6,2,9]]
r=my_matrix_addition(matrix_1,matrix_2)
r
#-----------------------------------------------------------------------
def my_matrix_substraction(m_1,m_2): 
    result=[]
    for row in range(len(m_1)):
        result.append([])
        for column in range(len(m_1[0])):
            result[row].append(m_1[row][column]-m_2[row][column])
    return result
matrix_1=[[4,6,3],[8,5,6]] 
matrix_2=[[5,2,3],[6,2,9]]
r=my_matrix_substraction(matrix_1,matrix_2)
r
#-----------------------------------------------------------------------
def my_matrix_scalar_product(alpha,m_1): 
    result=[]
    for row in range(len(m_1)):
        result.append([])
        for column in range(len(m_1[0])):
            result[row].append(m_1[row][column]*alpha)
    return result
matrix_1=[[4,6,3],[8,5,6]] 
alpha=10
r=my_matrix_scalar_product(alpha,matrix_1)
r
#-----------------------------------------------------------------------
def f_1(matrix_1,i):    
    return matrix_1[i]

def f_2(matrix_1,j):    
    my_j_th_col=[]
    for row in matrix_1:
        for indis in range(len(row)):
            if(indis==j):
                my_j_th_col.append(row[indis])
    return my_j_th_col
   
#-----------------------------------------------------------------------
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
    
  
def my_matrix_multiply(m_1,m_2):
    result=[]
    for row in range(len(m_1)):
        result.append([])
        for column in range(len(m_2[0])):
            a=f_1(m_1,row)
            b=f_2(m_2,column)
            c=my_vector_inner_product(a,b)
            result[row].append(c)
    return result
matrix_1=[[1,2],[3,4]]
matrix_2=[[5,6,7],[8,9,10]]
r=my_matrix_multiply(matrix_1,matrix_2)
