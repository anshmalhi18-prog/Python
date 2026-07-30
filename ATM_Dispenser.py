print("========ATM DISPENSER=========")
total_100=total_50=total_20=total_10=total_1=0
customer_served=0
total_dispensed=0

serving=True
while serving:
    name=input("Enter customer name: ")
    amount=int(input(f"Hello {name} enter your withdrawl amount"))
    if amount<=0:
        print("Invalid amount, please enter a positive number")
        continue
    print(f"Dispensing{amount} units for{name}")
    remaining=amount
    idx=1
    while idx<=6:
        if idx==1: value=100
        elif idx==2: value=50
        elif idx==3: value=20
        elif idx==4: value=10
        elif idx==5: value=5
        else: value=1
        count=remaining//value
        if count>0:
            print(f"{count}*{value}-unit notes={count*value}")
            remaining=remaining-count*value
            if value==100: total_100+=count
            elif value==50: total_50+=count
            elif value==20: total_20+=count
            elif value==10: total_10+=count
            elif value==5: total_5+=count
            else: total_1+=count
        idx=idx+1
    customer_served+=1
    total_dispensed+=amount
    print(f"Transaction Complete,{name}")
    again=input("Next customer? yes/no").strip().lower()
    if again!="yes":
        serving=False
print("==========Denomination Report==========")
for slot in range(1,7):
    if slot==1: value,total=100,total_100
    elif slot==1: value,total=50,total_50
    elif slot==1: value,total=20,total_20
    elif slot==1: value,total=10,total_10
    elif slot==1: value,total=5,total_5
    else: value,total=1,total_1
    if total>0:
        print(f"{value}-unit notes dispensed:{total}",end="")
        print()
print(f"Customers served:{customer_served}")
print(f"Total Dispensed {total_dispensed} units")
print("ATM SESSION CLOSED")