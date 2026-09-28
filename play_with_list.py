list1=[1,5,10,25,60,24,8]
print("The original list is equal to: ",list1)

count=0
for i in list1:
    count=count+i


average=(count/len(list1))
print("The sum of the numbers in the list is: ",count)
print("The average of the numbers in the list is: ",average)

list1.sort()
print(list1)

print("Smallest= ",list1[0])

print("Biggest=",list1[-1])