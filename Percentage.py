print("Please enter marks obtained in four subjects out of 100")
math=int(input("Math = "))
sci=int(input("Science = "))
geo=int(input("Geography = "))
eng=int(input("English = "))
total=math+sci+geo+eng
percent=(total/400)*100
print("total marks = ",total)
print("percentage = ",percent)