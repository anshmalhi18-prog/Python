def calculate_change(paid,price):
    change=paid-price
    return change

snack_price=25
print("===========SNACK VENDING MACHINE============")
print(f"The snack cost is {snack_price} per unit")
print("Accepted coins are: 1, 5, 10, 25")
print("\n")
total_inserted=0
coins_inserted=0

while True:
    coin=int(input("Insert a coin(1, 5, 10, 25) "))
    if coin!=1 and coin!=5 and coin!=10 and coin!=25:
        print("Invalid coin")
        print("Try again")
        continue
    coins_inserted=coins_inserted+1
    total_inserted=total_inserted+coin
    print(f"Inserted: {coin} Total so far: {total_inserted}\n")
    if total_inserted>=snack_price:
        print("Enough money inserted\n")
        break
change_due= calculate_change(total_inserted,snack_price)
print("Dispensing ypur snack...")
if change_due==0:
    pass
else:
    print(f"Here is your change: {change_due} units")

print("\n=========PURCHASE SUMMARY============")
print("Snack Price: ",snack_price)
print("Coins Inserted: ",coins_inserted)
print("Total Paid: ",total_inserted)
print("Change Given: ",change_due)
print("=======================================")
print("Thanks for your purchase!!!")