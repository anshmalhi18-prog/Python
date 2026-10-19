basket1={"apple","banana","mango","apple"}
basket2={"kiwi","pear","kiwi","apple"}

print("Basket 1: ",basket1)
print("Basket 2: ",basket2)

basket1.add("orange")
print("Basket 1 after adding orange: ",basket1)

all_fruits=basket1.union(basket2)
print("All fruits: ",all_fruits)

common_fruits=basket1.intersection(basket2)
print("Common Fruits in both baskets: ",common_fruits)




import array as arr

fruit_counts=arr.array('i',[3,5,2,4])
print("Fruit counts array: ",fruit_counts)

fruit_counts.insert(0,1)
fruit_counts.append(6)

count_of_4=fruit_counts.count(4)
print("The number of times four appears: ",count_of_4)

fruit_counts.reverse()
print("Reverse fruit count array: ",fruit_counts)

print("============== CLASS FRUIT BASKET ORGANISER ================")
print("Basket 1: ",basket1)
print("Basket 2: ",basket2)
print("Common fruits: ",common_fruits)
print("Fruit count: ",fruit_counts)