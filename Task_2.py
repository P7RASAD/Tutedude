
s1 = int(input("enter number:?"))
if s1 % 2 == 0:
    print(s1,("This number is Even"))
else:
    print(s1,("This number is Odd"))

#calculate sum
total = 0
for i in range(1, 51):
    total = total + i
print("The sum of number from 1 to 50 is:", total)
