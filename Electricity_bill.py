#[Unit 50,2.60,25] [50-100,3.25,35] [100-200,5.26,45] [>200,8.45,75]
units=int(input("Enter your electricity units you consumed"))
if units<50:
    amount=units*2.60
    tax=25
elif units<=100:
    amount=units*3.25
    tax=35
elif units<=200:
    amount=units*5.26
    tax=45
else:
    amount=units*8.45
    tax=75
total=amount+tax
print("Your electricity bill = ",total)