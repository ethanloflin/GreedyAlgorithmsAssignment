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

print(greedy_fruit(items,2000))
