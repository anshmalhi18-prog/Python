a=10
b=12
c=12
print(not(a==b))
print(not(b==c))

x="python"
y="coding"
if not(a==b):
    print(x,"and",y,"are different")

n=4
m=5
if not((n==1)==(m==5)):
    print("Hello")

a=int(input("Enter a number"))
if not(a%2==0):
    print(a,"is a odd number")