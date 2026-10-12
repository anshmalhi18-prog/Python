test_dict={"a":2,"b":2,"c":2,"d":1}
print("Original Dictionary: ",test_dict)

k=2
result=0

for key in test_dict:
    if test_dict[key] == k:
        result=result+1

print("The total frequency of 2 is: ",result)
