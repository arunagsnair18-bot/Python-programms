#for_loop.py
"""numbers=range(1,11)
for num in numbers:
    if num<5:
        print("numbers is less than 5")
    else:
        print(num)"""

"""test_score=[20, 50, 60 ,14 ,65]
pass_mark=40
for score in test_score:
    if score<=pass_mark:
        print("Fail")
    else:
        print("Pass")"""

#Employee Salary Report Generator
"""total_salary=0
for employee in range(1,6):
    salary=float(input(f"Enter Salary of Employee {employee}: "))
    total_salary+=salary
print("Total salary expenditure:", total_salary)"""

#Student Attendance Counter
"""present=0
absent=0
for student in range(1,11):
    attendance=input(f"student {student} attendence(P/A):")
    if attendance=="P":
        present+=1
    else:
        absent+=1    
print("total present students:",present)  
print("total absent  students: ",absent)"""

#Supermarket Billing System
"""price=0
total_bill =0
for customer in range(1,6):
    price=int(input(f"Item {customer} Price: "))
    total_bill+=price
print("Total Bill Amount: ",total_bill)"""    

#Cricket Score Analyzer
"""total_runs=0
for balls in range(1,7):
    runs=int(input(f"Enter runs scored in {balls} ball: "))
    total_runs+=runs
print("Total Runs Scored: ",total_runs)"""

#Library Book Collection Counter
"""total_books=0
for books in range(1,8):
    books=int(input(f"section {books} Books:"))
    total_books+=books
print("Total Book in each section:",total_books)"""    

#Online Exam Marks Calculator
"""total_marks=0
average_marks=0
for subject in range(1,6):
    marks=int(input(f"Subject {subject} Marks:"))
    total_marks+=marks
    average_marks=total_marks/5
    
print("Total Mark:",total_marks)    
print("Average Mark:",average_marks)"""

#Daily Temperature Monitor
"""highest_temp=0
for temp in range(1,8):
    temp=int(input(f"Day {temp} Temperature: "))
    if temp>highest_temp:
        highest_temp=temp
    
print("Highest Temperature: ",highest_temp,"C")"""

#Mobile Recharge Collection System
"""total_collection=0
for recharge in range(1,11):
    recharge=int(input(f"Customer {recharge} Recharge: "))
    total_collection+=recharge
print("Total Colection: ",total_collection )"""    

#Water Consumption Tracker
"""total_water=0
for water in range(1,8):
    consumption=int(input(f"Day {water} Consumption: "))
    total_water+=consumption
print("Total Water Consumed: ",total_water,"Liters")"""


#Factory Production Report
"""total_production=0
for record in range(1,13):
    production=int(input(f"Month {record} Production:"))
    total_production+=production
print("Total Annual Production: ",total_production ,"Units")"""    








