def greet():
    print("Welcome to the lemonade stand")
    print("Fresh lemonade made just for you")
greet()

cup_price=float(input("Please enter the price per cup in dollars: "))
sold=int(input("Enter the number of cups sold: "))

def calculate_total(price,cups):
    total=price*cups
    return total

total_cost=calculate_total(cup_price,sold)
rounded=round(total_cost,2)
print("total_cost: ",rounded)

amount_paid=float(input("Enter the amount payed by the customer: "))
def calculate_change(paid,total):
    change=paid-total
    return change

change_due=calculate_change(amount_paid,rounded)
rounded_change=round(change_due,2)

def thank_you_msg(cups):
    if cups>=5:
        return "Wow, big order! Thank you so much for your support!"
    else:
        return "Thanks for stopping by the stand"

closing_msg=thank_you_msg(sold)
print("")
print("=========LEMONADE STAND RECEIPT==========")
print("Price per cup: ",cup_price)
print("Cups sold: ",sold)
print("Total cost: ",rounded)
print("Amount paid: ",amount_paid)
print("Change due: ",rounded_change)
print(closing_msg)
print("=========================================")