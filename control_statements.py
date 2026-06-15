"""for variable in sequence:
    code to be executed"""
"""for variable in sequence:#in memebership opertr
    code to be executed
word = input("Enter a word: ")
for letter in word:
    print(letter)

for element in [1,2,3,4]:
    print(element)"""

#using range()
"""for variable in range(start,stop,skip):
    code to be executed"""
"""for element in range(11):
    print(element)"""

"""for element in range(5,16):#end-1
       print(element)


for element in range(10,26,5):
       print(element)

for element in range(1,10,-1):
       print(element)#it will not work

for element in range(10,0,-1):#1 kurj kkkurj vrnm o/p
       print(element)

for element in range(17,3,-3):
       print(element)


#multipilcation table of a given number
num=int(input("Enter the number:"))
for i in range(1,11):
       #print(i,"*",num,"=",num*i)# or
       print(f"{i} * {num} = {num*i}")#printing using formatting string"""


#while loop initializtn,while condition,updation
"""while condition:
       code to be executed"""

"""value=1
while value<=10:
       print(value)
       value += 1"""

"""num=int(input("Enter the iteration: "))
value=1
sum=0
iteration = int(input("Enter the number of iteration"))
while value <= iteration:
    sum+=value
    value+=1
print(sum)"""

#reverse a number
#step 1: getting the last digit
#eg 165 % 10=5(remainder)
#step 2:remove the last digit 
#165/10=16(quoitnt)
# step 3: built a reversed number
#reverse=0
#reverse=reverse*10+digit    
#0*10+5
#5*10+6


"""number=int(input("Enter the number to get reversed"))
reverse=0
while number>0:
    remainder = number%10
    reverse=reverse*10+remainder
    number//=10
print(reverse)

#number=165"""





    



