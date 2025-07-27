"""
Question 1 
Write a Program to check if a given Number is Positive,Negative and Zero
"""
num=int(input("Enter the Number: "))
if num>0:
    print("Number is Positive")
elif num<0:
    print("Number is Negative")
else:
    print("Number is Zero")


"""
Question 2
Write a program to check if a given number is odd or even
"""
num=int(input("Enter the Number: "))
if num%2==0:
    print("Number is even")
else:
    print("Number is Odd")


"""
Question 3
Given two non-genative values ,print true if they have the same last digit, such as with 27 and 57 
"""
num=int(input("Enter the Number: "))
last_two_digit=num%100
if last_two_digit==27 or last_two_digit==57:
    print(True)
else:
    print(False)


"""
Question 4
Write a program to print numbers from 1 to 10 in a single row with one tab space
"""
i=1
while i<=10:
    print(i,end="   ")
    i=i+1


"""
Question 5
Write a program to print even number between 23 and 57.Each number should be printed in a seperate row
"""
num1=23
num2=57
for i in range(num1,num2+1):
    if i%2==0:
        print(i)


"""
Question 6
Write a program to check if a given number is prime or not 
"""
num = int(input("Enter a number: "))
flag = False
if num == 1:
    print(f"{num}, is not a prime number")
elif num > 1:
    for i in range(2, num):
        if (num % i) == 0:
            flag = True
            break
if flag:
    print(f"{num}, is not a prime number")
else:
    print(f"{num}, is a prime number")



"""
Question 7
Write a program to print prime number between 10 and 99.
"""
num1=10
num2=99
for num in range(num1,num2+1):
    if num>1:
        for i in range(2,num):
            if num%i==0:
                break
        else:
            print(num)


"""
question 8
Write a program to print sum of all the digit of a given Number
"""
num=int(input("Enter the Number: "))
sum=0
while num>0:
    r=num%10
    sum=sum+r
    num=num//10
print(sum)


"""
Question 9
Write a program to reverse a given number and print
"""
num=int(input("Enter the Number: "))
reversed_num=0
while num>0:
    digit=num%10
    reversed_num=reversed_num*10+digit
    num=num//10
print("Reversed number is ",reversed_num)


"""
Question 10
Write a program to find if the given number is palindrom or not
"""
num=int(input("Enter the Number: "))
temp=num
reversed_num=0
while temp>0:
    digit=temp%10
    reversed_num=reversed_num*10+digit
    temp=temp//10
if num==reversed_num:
    print("Number is Palindrom")
else:
    print("Number is not palindrom")