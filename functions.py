#functions.py
'''def function_name(parameters):
  code to be executed'''

"""def greeting(user_name,age):
    print(f"Welcome,{user_name} You are {age} old.")#f for format

user_name=input("Enter Name: ")
age=int(input("Enter age: "))
greeting(user_name,age)


def addition(num1,num2):
    return num1+num2

num1=int(input("Enter first number: "))
num2=int(input("Enter second number: "))
print(addition(num1,num2))"""
#result=addition(num1,num2)
#print(result)

"""def welcome():
    print("welcome Aruna")
welcome()

def book_tickets(movie_name,customer_name,seat,ticket_price):
    #total=seat*ticket_price
    return f"{customer_name} booked {seat} tickets for {movie_name}. total_amount={seat}"
           
print(book_tickets("Blast","Aruna","3","250")) 
print(book_tickets(3,200,"Alen","super"))"""

"""def addition(num1,num2):
    print(num1+num2)

addition(2,4)"""



#The docstring is stored as documentation for the function and is not printed automatically when the function runs. 
#You must access it with greet.__doc__ or help(greet).
def greet(name):
    """Return a greeting message."""
    return f"Hello, {name}!"

print(greet("Alice"))
print(greet.__doc__)