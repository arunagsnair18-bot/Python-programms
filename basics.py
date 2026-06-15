"""print("Welcome to Python programming")
user_data="python is a programming language"
print(user_data)


print("Hello World!")
print("Welcome")


salary =30000
salary+=5000
print("salary")

amount=1100
if amount > 1200:
    print("Free Delivery")

marks=75
age=18
if marks>=75 and age>:
    print("Admission Granted")
else:
    print("Admission Denied")


print("Hi Aruna")

name=input("what is your name")
hobby=input("what is your hobby")

print("I am " + name + " and I love " + hobby)"""

#TASK:
#Hi, I'm (name), a passioante(profession) with a keen interest in (interest).
#Let's connect!"

"""name = input("What is your name?")
profession = input("What is your passionate profession?")
interest = input("What is your keen interest")

print("Hi, I am " + name + ", a passionate "+ profession + " with a keen interest in " + interest )"""
    


#Smart ATM Authentication System

"""customer_name=(input("Enter the Customer Name :"))
card_number=(input("Enter ATM card number:"))
pin=int(input("Enter PIN Number:"))
account_type=input("Enter account type(savings/current):")
available_balance=float(input("Enter Available Balance:")) 
withdrawal_amount=float(input("Enter Withdrawal Amount:"))
#membership operator
valid_account=["Savings","Current"]
valid_account=account_type in valid_account
print("Valid Account Type:",valid_account)
stored_pin=1234
pin_verified=entered_pin=stored_pin
sufficient_balance=withdrawal_amount<=available_balance
balance_positive=available_balance>0

print("PIN Verfied: ",pin_verified)
print("available_balance:",available_balance)
print("Avaiable Balance Greater Than Zero:",balance_positive)

#Logical Operator
transaction_status=(
    pin_verified and
    valid_account and
    sufficient_balance and 
    balance_positive
)

if transaction_status:
    print("Transaction Status: Successfull")
else:
    print("Transaction Status: Failed")

#Identity Operator
account1=account_type
account2=account_type

print("Account1 is Account2:",account1 is account2)
print("Account1 is not account2:",account1 is not account2)

#arithematic operator
remaining_balance=available_balance-withdrawal_amount
print("Remaining Balance:", remaining_balance)

#assignment operator
balance=available_balance
balance-=withdrawal_amount
balance+=1000
balance*=1
print("Balance after assignment operations:",balance)

#type() function
print("Datatype of Customer Name:",type(customer_name))
print("Datatype of PIN:",type(entered_pin))
print("Datatype of Available Balance:",type(available_balance))
print("Datatype of Withdrawal Amount:",type(withdrawal_amount))
print("Datatype of Account Type:", type(account_type))

#isinstance() function
print("Is Balance Float:",isinstance(available_balance,float))
print("Is Withdrawal Amount:",isinstance(withdrawal_amount,float))
print("Is Customer Name String:",isinstance(customer_name,str))

#id() Function
print("ID of Balance:",id(available_balance))
print("ID of Remaining Balance:",id(remaining_balance))
print("ID of Account Type:",id(account_type))"""


#basics
#Online Food Ordering System
#inputs
"""customer_name=input("Enter the name:")
food_name=input("Enter food item:")
quantity=int(input("Enter quantity:"))
price_per_item=float(input("Enter price of each item:"))
distance=float(input("Enter the distance,KM:"))

#calculations
total_food_cost=quantity*price_per_item
delivery_charge=distance*5.0
final_bill_amount=total_food_cost*delivery_charge

#display details
print("\nOrder Details")
print("Customer Name:",customer_name)
print("Type:",type(customer_name))
print("Memory Address:",id(customer_name))

print("\nFood Name:",food_name)
print("Type:",type(food_name))
print("Memory Address:",id(food_name))

print("\nQuantity:",quantity)
print("\nType:",type(quantity))
print("\nMemory Address:",id(quantity))

print("\nPrice Per Item:",price_per_item)
print("\nType:",type(price_per_item))
print("\nMemory Address:",id(price_per_item))


print("\nDistance:",distance)
print("\nType:",type(distance))
print("\nMemory Address:",id(distance))

#implicit conversion demonstartion
final_bill_amount=total_food_cost+delivery_charge

print("Final Bill Amount:", final_bill_amount)
print("Type:",type(total_food_cost))

#isinstance()
print("\nChecking Data Types")
print("Quantity is integer:",isinstance(quantity,int))
print("Price is Float:",isinstance(price_per_item,float))
print("Final bill is float:",isinstance(total_food_cost,float))

print(f"\nFinal Bill=₹{total_food_cost:2f}")"""

first="Hello"
second="World"
result=first+" "+second
print(result)

message="Good"
message+="Morning"
print(message)

age = 25 
print("Age: " + str(age))
 
