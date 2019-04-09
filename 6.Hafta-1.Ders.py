from decimal import Decimal

class Item(object):
    def __init__(self,n,v,w,v_w):
        self.name=n
        self.value=v
        self.weight=w
        self.v_w=v_w
    def __repr__(self):
        return "Adı: %s  Değeri: %d Ağırlığı: %d"%(self.name,self.value,self.weight)
def get_items():
    items=[]
    items.append(Item('Clock',175,10,17.5))
    items.append(Item('Painting',90,9,10))
    items.append(Item('Radio',20,4,5))
    items.append(Item('Vase',50,2,25))
    items.append(Item('Book',10,1,1))
    items.append(Item('Computer',200,20,10))
    return items

def print_items(items):
    for item in items:
        print(item.name,item.value)

def sort_items(items):
    return sorted(items,key=lambda Item:Item.value,reverse=True)

def test():
    items=get_items()
    print_items(items)
    print("Sorted Items")
    items=sort_items(items)
    print_items(items)

def hırsızList(items,maxWeight):
    result=[]
    totalValue,totalWeight=0,0
    for i in range(len(items)):
        if(totalWeight+items[i].weight<=maxWeight):
            result.append(items[i])
            totalWeight=totalWeight+items[i].weight
            totalValue=totalValue+items[i].value
    return (result,totalValue)

def print_result(items2):
    for item in items2[0]:
        print(item.name)
    print(items2[1])
test()
Item1=get_items()
Item2=hırsızList(Item1,20)
print_result(Item2)
