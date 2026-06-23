#prime no 
#try out count 
'''number=int(input("Enter a Number: "))
if number<=1:
    print("Not a Number")
else:
    is_prime=True#boolean
    for i in range(2,number):
     if number%1==0:
        is_prime=False
        break
    if is_prime:
       print("Is a Prime Number") 
    else:
       print("Is not a Prime Number")  ''' 
    #point value cant put in range first the number should divisible /2 then it convert to int 
#if the number is greater than its floor division 

#fibonacci series...sum of consecutive number
'''a=0
b=1
c=a+b

a=b
b=c
#balance check screenshot

n=int(input("Enter the Number of Terms:" ))
a=0
b=1
for i in range(n):
   print(a,end=" ")
   c=a+b
   a=b
   b=c'''

#palindrome number
'''num=int(input("Enter a Number: "))
temp=num
rev=0
while temp>0:
   digit=temp%10
   rev=rev*10+digit
   temp=temp//10
if num==rev:
   print("Palindrome Number")
else:
   print("Not a Palindrome Number")'''   
#check the screenshot also (other code) 


#count the number of digits
#count sholud ne increment
'''12345 ....workingg ahn ezuthikune
count=0
temp=0 if 0 count 1 aakum
num >0
if greater count sholud increment
num=num//10
the num is divided by 10 each number loss'''

'''num=int(input("Enter a Number: "))
count=0
temp=abs(num)
#absolute number(abs) that is -12 is +12
if temp==0:
   count=1
else:
   while temp>0:
      count+=1
      temp=temp//10
print("Number of Digits " ,count)'''

#reverse of a number 
#revesre=reve *10+digit

#in the case of sum
#sum=sum*10+digit 
# product of digit*


'''num=int(input("Enter a Number: "))
sum_digits=0
temp=abs(num)
while temp>0:
    digits=temp%10
    sum_digits+=digits
    temp=temp//10
print("Sum of digits",sum_digits)'''

#product
"""num=int(input("Enter a Number: "))
product_digits=1
temp=abs(num)
while temp>0:
    digits=temp%10
    product_digits=product_digits*digits
    temp=temp//10
print("Product of digits:",product_digits)"""

#22/06/2026 Monday
#ATM
"""pin=int(input("Enter the Pin: "))
correct_pin=1234
balance=2300
attempts=0
while attempts<3:
   
    if pin==correct_pin:
        print("Login Successfull")
        while True:
   
            print("\n1.Balance check\n2.Withdrawal\n3.Deposit\n4.Exit")
            choice=int(input("Enter the choice: "))
            if choice==1:
                print("Balance:",balance)
            elif choice==2:
                amount=int(input("Enter the amount to be withdrawn:"))
                if amount<=balance:
                    balance-=amount
                else:
                    print("Insufficient Balance")
            elif choice==3:
                amount=int(input("Enter the amount to be deposited"))
                balance+=amount
                print("Amount Deposited Successfully")
            elif choice==4:
                print("Thank You")
                break
            else:
                print("Invalid Choice")
      
        break
    else:#if corect alla engil nere else il vrum attempt 3 vattame ulu 
        attempts+=1
        print("Incorrect PIN")    
else:#ith while nde else ahn (adym kodutha while nde else)
    print("Account Blocked")"""


#seat booking system
#total_seat =10
#available seat store chynm 
#work until 0

"""available_seats=10

while available_seats>0:
   print("available_seats:",available_seats)
   book_seats=int(input("Enter the number of seats to be booked: "))
   if book_seats<=available_seats:
        available_seats-=book_seats
        print(f"{book_seats}seats are booked successfully")
        remaining_seats=available_seats
        print("Remaining Seats are:",remaining_seats)
   else:
        print("seats are not available")
   choice=input("Do you want to continue (yes/no): ")
   if choice=="no":
       break
print("Booking is closed")"""


#electricity bill ...try out..DONE
#calculator try out...DONE
#fiz and buzz refer youtube 
"""start_value=int(input("Enter the start value: "))#divisiblty check ahn  chyne
end_value=int(input("Enter the end value: "))
for i in range(start_value,end_value+1):
    if i%3==0 and i%5==0:
        print("FizBuzz")
    elif i%3==0:
        print("Fiz")
    elif i%5==0:
        print("Buzz")
    else:
        print(i) 
#try out this with break continue pass """

#find the smallest and largest number in a list(data structure)
"""numbers=[]
n=int(input("Enter the element to be inserted"))
for i in range(n):
   num=int(input(f"Enter number {i+1}: "))
   numbers.append(num)#all are stored in num
largest=numbers[0] #0th index ahnu smalest and laregest  
smallest=numbers[0]
for num in numbers:
      if num>largest:
        largest=num
      if num<smallest:
        smallest=num
print(f"Largest number in the list is {largest}")
print(f"Smallest number in the list is {smallest}")            
#working screenshot il ond
#seperate positive and negative numbers from the list(homework)"""

#Electricity Bill Calculator
#Write a Python program that:

#Asks the user to enter the number of electricity units consumed.
#Calculates the bill using the following rates:
#First 100 units: ₹5 per unit
#Next 100 units (101–200): ₹7 per unit
#Above 200 units: ₹10 per unit
#Displays the total electricity bill.
#Add a fixed service charge of ₹100 to every bill before displaying the final amount.

"""units=int(input("Enter units consumed: "))
if units<=100:
   bill=units*5
elif units<=200:
   bill=(100 * 5) + ((units - 100) * 7)
else:
   bill=(100 * 5) + (100 * 7) + ((units - 200) * 10)
bill += 100#service charge
print("Total Electricity Bill = ₹", bill)"""

#SIMPLE CALCULATOR
#Takes two numbers as input from the user.
#Takes an operator (+, -, *, /) as input.
#Performs the chosen operation.
#Displays the result.
'''
num1=float(input("Enter first number: "))
num2=float(input("Enter second number: "))
operator=input("Enter operator(+,-,*,/): ")
if operator=="+":
    result=num1 + num2
elif operator=="-":
    result=num1-num2
elif operator=="*":
    result=num1*num2
elif operator=="/":
    result=num1/num2
else:
    print("Invalid Operator")
    result=None
if result is not None:
    print("Result =",result)'''

'''QUESTION

#Takes numbers from the user and stores them in a list.
Stops taking input when the user enters 0 (use break).
Ignores negative numbers (use continue).
If the user enters 999, do nothing and move on (use pass).
After all valid numbers are entered, find and display:
The largest number
The smallest number'''

'''
numbers=[]
while True:#Keep running this loop forever until something stops it
    num=int(input("Enter a number: "))
    if num==0:
        break
    if num<0:
        continue
    if num==999:
        pass
    else:
        numbers.append(num)
if len(numbers)>0:
    largest=max(numbers)
    smallest=min(numbers)
    print("Numbers in the list:",numbers)
    print("Largest number:",largest)
    print("Smallest number:",smallest)
else:
    print("No valid numbers entered:")'''


"""numbers=tuple(map(int,input("Enter the numbers to be inserted: ").split(",")))
element=int(input("Enter the element to be count: "))
count=0
for item in numbers:
    if item==element:
        count+=1
print("Tuple elements are ",numbers)  
print(f"Occurence of {element} is : {count}")"""

#input=1 2 3 4 5 6
#target=6
#output=[1,5][2,4][3,3]
numbers=tuple(map(int,input("Enter the numbers to be inserted: ").split(",")))
target=int(input("Enter the target sum: "))
for i in range(len(numbers)):
    for j in range(i,len(numbers)):
        if numbers[i]+ numbers[j]==target:
            print((numbers[i],numbers[j]))






            





