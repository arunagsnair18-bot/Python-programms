#College Admission Management System
"""name=input("Enter the student name:")
int=int(input("Enter the age:"))
course=input("Python")
marks=int("Enter the marks:")

#names in list
name=["Aruna","Abhiram","Goutham","Anupama"] 

#courses in tuple
courses=("Python","Java","C","Javascript")

#cities in set
set={
    "Tvm","Ernakulam","Palakkad"
}

#student details in dict
dict={
    name:"Aruna",
    age:20,
    course:"Python",
    place:"Tvm",
    }"""

"""for i in range(10):
    print("\nStudent", i + 1)

name=input("Enter Name:")
age=int(input("Enter Age:"))
city=input("Enter Cousre:")
course=input("Enter course:")
marks=float(input("Enter Marks: "))

name.append(name)
city.add(city)

students[name] = {
        "Age": age,
        "Course": course,
        "Marks": marks
    }

print("\nNames List:")
print(names)

print("\nAvailable Courses:")
print(course)
      
print("\nUnique Cities:")
print(city)


#calculate average mark

total=0
for name in students:
     total = total + students[name]["Marks"]

     average=total/10

print("\nAverage Mark=",average)

topper=names[0]
lowest=names[0]

for name in names:"""#ENIK MANASILAVANILAAAA




#ONLINE SHOPPING MANAGEMENT SYSTEM
"""product=input("Enter product name: ")
price=float(input("Enter the price:"))
brand=input("Enter brand name: ")

print("\nAvailable Products: ")
for product,price in product.items():
    print(products, ":",price)"""



# Online Shopping Management System

# Dictionary for products and prices
products = {}

# Tuple for categories
categories = ("Electronics", "Clothing", "Books", "Food")

# Set for unique brands
brands = set()

# List for shopping cart
cart = []

# Accept product details
n = int(input("How many products do you want to add? "))

for i in range(n):
    name = input("Enter product name: ")
    price = float(input("Enter product price: "))
    brand = input("Enter brand name: ")

    products[name] = price
    brands.add(brand)

# Display products
print("\nAvailable Products:")
for product, price in products.items():
    print(product, ":", price)

# Search for a product
search = input("\nEnter product to search: ")

if search in products:
    print("Product Found!")
    print("Price:", products[search])
else:
    print("Product Not Found!")

# Add products to cart
while True:
    item = input("\nEnter product to add to cart (or 'done' to finish): ")

    if item.lower() == "done":
        break

    if item in products:
        cart.append(item)
        print(item, "added to cart.")
    else:
        print("Product not available.")

# Calculate total bill
total = 0

for item in cart:
    total += products[item]

# Apply discount
if total > 50000:
    discount = total * 0.20
elif total > 20000:
    discount = total * 0.10
else:
    discount = total * 0.05

final_bill = total - discount

# Sort products by price
sorted_products = sorted(products.items(), key=lambda x: x[1])

print("\nProducts Sorted by Price:")
for product, price in sorted_products:
    print(product, ":", price)

# Purchase summary
print("\n----- PURCHASE SUMMARY -----")

print("Products Purchased:")
for item in cart:
    print(item, "-", products[item])

print("Total Amount:", total)
print("Discount:", discount)
print("Final Amount:", final_bill)

print("\nCategories:")
print(categories)

print("\nUnique Brands:")
print(brands)




















