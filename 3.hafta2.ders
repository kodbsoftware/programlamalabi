# arrayin frekans tablosunu bulup return eden fonksiyon
my_list=[8,4,6,7,2,8,4,8,4]
print(my_list)

def frequency_table(list1):
    freq={}
    for i in list1:
        if(i in freq):
            freq[i]=freq[i]+1
        else:
            freq[i]=1
    return freq


frequency_table(my_list)

def frequency_table_2(list2):
    frequency_list=[]
    for i in range(len(list2)):
        s=False
        for j in range(len(frequency_list)):
            if(list2[i]==frequency_list[j][0]):
                frequency_list[j][1]=frequency_list[j][1]+1
                s=True
        if(s==False):
                frequency_list.append([list2[i],1])
    return frequency_list
        
print(frequency_table_2(my_list))
