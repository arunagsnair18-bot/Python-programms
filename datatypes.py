"""student_name=input("Enter the student name: ")
student_id=int(input("Enter the student id: "))
student_mark=float(input("Enter the student mark: "))
is_present=bool(input("Is present or not(T/F): "))
languages_known=input("Enter the languages known: ").split(",")


print("The student name is ",student_name)
print("The student id is ",student_id)
print("The student mark is ",student_mark)
print("present or not ",is_present)
print("languages known are ",languages_known)

print(type(student_name))
print(type(student_id))
print(type(student_mark))
print(type(is_present))
print(type(languages_known))

num1=10
num2=10

print(id(num1))
print(id(num2))

list1=[10,20]
list2=[10,20]

print(id(list1))
print(id(list2))


print(isinstance(num1,int))
print(isinstance(list1,list))
print(isinstance(list2,list))
print(isinstance([100,200],list))
print(isinstance((100,200),int))


#PETROL PUMP BILLING SYSTEM

customer_name = input("Enter Customer Name: ")
vehicle_number = input("Enter Vehicle Number: ")
fuel_type = input("Enter Fuel Type: ")

liters = float(input("Enter Liters Filled: "))
price_per_liter = float(input("Enter Price Per Liter: "))

premium_card = input("Premium Card (True/False): ") == "True"

# Fuel amount
total_amount = liters * price_per_liter

# GST
gst = total_amount * 5 / 100

# Final amount
final_amount = total_amount
final_amount += gst

# Premium discount
if premium_card and final_amount > 3000:
    final_amount -= 200

# Bill print
print("-------- PETROL BILL --------")
print("Customer Name:", customer_name)
print("Vehicle Number:", vehicle_number)
print("Fuel Type:", fuel_type)
print("Fuel Amount:", total_amount)
print("GST Amount:", gst)
print("Final Bill Amount:", final_amount)

# type()
print("Datatype of liters:", type(liters))
print("Datatype of premium card:", type(premium_card))

# isinstance()
print("Is liters float?", isinstance(liters, float))
print("Is premium card boolean?", isinstance(premium_card, bool))

# id()
print("ID of Total Amount:", id(total_amount))
print("ID of Final Amount:", id(final_amount))  #THE END

#DATA TYPES
#STRING
a = ""
print(type(a))
 
number=("123")
print(type(number))

a=1
print(type(a))

a=-2
print(type(a))

a=2.7
type(a)
print(type(a))

e=3.00
type(e)
print(type(a))

a="5"
type(a)
print(type(a))

b=5
print(type(b))

c="5.11"
print(type(c))

d=5.11
print(type(d))

#TASK
a="5"
b=5

type(a)

bool_true=True
type(bool_true)
print(type(bool_true))

bool_false=False
print(type(bool_false))

#LIST
Fruits=["apple","mango","mangosteen"]
print(type(Fruits))

list_test=["190","chair","honey"]
print(list_test[1])
print(list_test[2])
print(list_test[2])
print(list_test[0])

Brand=["gucci","alen solley","zara"]
print(Brand[1])

list_test=["190","chair","honey"]
list_test[1]="table"
print(list_test)

#TUPLE
Fruits=("apple","mango","mangosteen")
print(type(Fruits))

list_fruits=("apple","mango","mangosteen")
tuple_fruits=("apple","mango","mangosteen")
type(list_fruits)

a=True
print(type(a))

b="True"
print(type(b))

c=[12,10.9,"apple"]
print(type(c))

d=["banana",1.56,False]
print(type(d))
print(d[1]=mango)"""

"""customer_name=input("Enter the customer name: ")
vehicle_number=input("Enter the vehicle number: ")
fuel_type=input("Enter the fuel type: ")
liters=float(input("Enter litres filled: "))
price_per_liter=float(input("Enter price per liter: "))
total_amount = liters * price_per_liter
premium_card=input("Premium Card(True/False): ")=="True"
gst=total_amount * 5/100
final_amount=total_amount+gst
final_amount += 0
if premium_card and final_amount > 3000: final_amount -= 200
print(type(liters))
print(type(premium_card))
print(isinstance(liters,float))
print(isinstance(premium_card,bool))
print(id(total_amount))
print(id(final_amount))
print("customer name: ",customer_name)
print("vehicle_number: ",vehicle_number)
print("fuel_type: ",fuel_type)
print("fuel_amount: ",total_amount)
print("premium_card: ",premium_card)
print("gst amount: ",gst)
print("final_bill_amount: ",final_amount)

print(type(liters))
print(type(premium_card))

print(isinstance(liters,float))
print(isinstance(premium_card,bool))

print(id(total_amount))
print(id(final_amount))"""


#Dictionary
#collection of elements 
#here 'elements' are key / value pairs 
student={"name":"John" , "age": 18 , "is_enrolled": True}
print(type(student))
print (student["name"])

print (student["age"])


