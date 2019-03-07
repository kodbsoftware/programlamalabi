#Selection sort sıralama algoritması ile arrayın sıralanması ve binary search arama algoritması ile arama işlemi
def my_search_selection(my_array):
    swap_count=0
    for i in range(len(my_array)-1,0,-1):
        positionOfMax=0
        for location in range(i,i+1):
            if(my_array[location]>my_array[positionOfMax]):
                positionOfMax=location
        temp=my_array[location]
        my_array[location]=my_array[positionOfMax]
        my_array[positionOfMax]=temp
        swap_count=swap_count+1
    print("number of exchange :",swap_count)
    return

my_arr=[21,12,13,44,25,2,7,16,14,35]
my_search_selection(my_arr)
print(my_arr)
#-----------------------------------------------------------------------
def my_binary_search(my_sorted_array,item):
    first=0
    last=len(my_sorted_array)-1
    found=False
    s=0
    while first<=last and not found:
        midpoint=(first+last)//2
        #print("first - last",first,last)
        s=s+1
        if(my_sorted_array[midpoint]==item):
            found=True
        else:
            if(item<my_sorted_array[midpoint]):
                last=midpoint-1
            else:
                first=midpoint+1
    return found,midpoint,s

my_binary_search(my_arr,25)  
