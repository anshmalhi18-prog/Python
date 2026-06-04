cost=float(input("Enter the actual cost of the product"))
sell=float(input("Enter the selling cost of the product"))
profit=sell-cost
loss=cost-sell
if sell>cost:
    print("You are in profit")
    print("profit=",profit)
else:
    print("You are in loss")
    print("loss=",loss)