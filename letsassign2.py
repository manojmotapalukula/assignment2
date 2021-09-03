#program to find prime or not


num=int(input("enter a number"))
for i in range (2,num):
    if num % i ==0:
        print(f"{num} is Not a prime number")
        break
else:
    print(f"{num} is a prime number")

#using flag
    
num=int(input("enter a number"))
flag=0
for i in range (2,num):
    if num % i ==0:
        print(f"{num} is Not a prime number")
        flag=1
        break
if flag==0:
    print(f"{num} is a prime number")

#output
'''
enter a number 11
11 is a prime number

enter a number 21
21 is Not a prime number
'''


