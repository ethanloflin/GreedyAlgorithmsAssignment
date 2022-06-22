items = [('avacado', 2.2, 170),('pomelo',8,1500), ('durian',22,1500),('cucumber',0.26,15),('lynchee', 0.4,20),('star apple',1,200)]

def greedy_fruit(items,capacity):
    items = sorted(items,key=lambda item:item[1],reverse=True)
    chosen_fruits = {}
    profit = 0
    for i in range(len(items)):
        name,value,weight = items[i]
        num_of_fruit = (capacity - capacity % weight)/weight
        chosen_fruits[name] = num_of_fruit
        capacity = capacity % weight
        profit+= num_of_fruit*value
    return round(profit,2),chosen_fruits

def greedy_fruit_dantzig(items,capacity):
    items = sorted(items,key=lambda item:item[1]/item[2],reverse=True)
    chosen_fruits = {}
    profit = 0
    for i in range(len(items)):
        name,value,weight = items[i]
        num_of_fruit = (capacity - capacity % weight)/weight
        chosen_fruits[name] = num_of_fruit
        capacity = capacity % weight
        profit+= num_of_fruit*value
    return round(profit,2),chosen_fruits

print(greedy_fruit(items,2000))
print(greedy_fruit_dantzig(items,2000))

def dynamic_fruit(items,capacity):
    bag = [0 for i in range(capacity+1)]
    for i in range(capacity+1):
        for j in range(len(items)):
            _,value,weight = items[j]
            if(weight < i):
                bag[i] = max(bag[i],bag[i-weight]+value)
    return round(bag[capacity])

print(dynamic_fruit(items,2000))
