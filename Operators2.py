amount=int(input("enter your amount"))
note1=amount//100
note2=(amount%100)//50
note3=((amount%100)%50)//10
print("number of 100 rs notes = ",note1)
print("number of 50 rs notes = ",note2)
print("number of 10 rs notes = ",note3)