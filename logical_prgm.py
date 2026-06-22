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
# product of digigt *


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

#ATM
num=int(input("Enter the Number: "))
correct_pin=1234
balance=2300
attempts=0
while attempts<3:
    pin=int(input("Enter the pin: "))
    if pin==correct_pin:
        print("Login Successfull")
        while True:
            print("\n")
 