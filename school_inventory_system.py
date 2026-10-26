items=["Pencil","Eraser","Notebook","Sharpener","Glue"]
stock_count=[12,0,8,5,3]

inventory={item: count for item, count in zip(items,stock_count)}
print("Full inventory: ",inventory)

in_stock=[item for item in items if inventory[item]>0]
print("Items in stock: ",in_stock)

chosen_item=input("Which item do you want to buy: ")
if chosen_item not in inventory or inventory[chosen_item]==0:
    print(chosen_item,"is out of stock")
    exit()

prices=[10,5,40,15,20]
markup=int(input("Enter the markup amount to add to every price: "))

markup_price=list(map(lambda p:p+markup,prices))
print("Markup price is: ",markup_price)

item_index=items.index(chosen_item)
chosen_item=markup_price[item_index]
print("Price of ",chosen_item,"After markup: ",chosen_item)

inventory[chosen_item] =- 1
print(chosen_item,"Purchased!")
print("Remaining Stock: ",inventory[chosen_item])