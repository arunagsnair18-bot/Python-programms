"""num=int(input("Enter the number: "))
if num>0:
    print("Positive number")
else:
    print("Negative number")


#to check wheather a character is vowel or not
vowel_check=input("Enter the character: ")#'in' chechk wheather ath ondo illeee?
if vowel_check in "aeiouAEIOU":
   print("vowel")
else:
    print("consonants")

#to check wheather a number is odd or even
odd_even=int(input("Enter a number: "))
if odd_even%2 ==0:
    print("Number is even")
else:
    print("Number is odd")

#to check wheather a person is child,teenager,adult,senior citizen

age=int(input("Enter the age: "))
if age<=13:
    print("Child")
elif age<18:
    print("Teenager")
elif age<60:
    print("Adult: ")
else:
    print("Senior citizen: ")

#nested if
#program to check wheather the given number is posituve and even,or positive or odd otherwise or negative
num=int(input("Enter the number: "))
if num>0:
    if num%2==0:
        print("Number is positive and even")
    else:
        print("Number is positive and odd")  
else:
    print("Number is negative") 

#to check wheather the number is 3 digit or not
num=int(input("Enter the number: "))
if num>99 and num<1000:
    print("The entered number is 3 digit ")
else:
    print("The entered number is not 3 digit")
#to check the balance Simple ATM Program
balance_amount=50000
withdraw_amount=int(input("Enter the withdraw amount: "))
if withdraw_amount<balance_amount:
    print("Withdrawal Successfull")
else:
    print("Insufficinet balance")

#SMART ATM Authentication System
#Create an ATM system that verifies PIN and allows withdrawal if sufficient balance exists.correct_pin=1234balance=10000
pin=int(input("Enter the PIN: "))
if pin == correct_pin:
print("PIN Verified")else:
print("Invalid PIN")amount=int(input("Enter Withdrawal Amount: "))
if amount<= balance:
print("Withdrawal Successful")else:
print("Insufficient Balance")

#Online Shopping Discount Calculator
#Calculate the final bill after applying discountspurchase_amount=10000
purchase_amount=float(input("Enter purchase amount: "))premium_member=input("premium number(yes/no): ")if purchase_amount>=10000:    discount=20elif purchase_amount >=5000:    discount=10else:    discount=5if premium_member.lower()== "yes": discount +=5 discount_amount=purchase_amount * discount/100final_bill=purchase_amount - discount_amountprint("Discount Applied:", discount, "%")print("Final Bill Amount:",final_bill)

#University Admission Eligibility Checker
# #check wheather a student is eligible for admission:
higher_secondary=float(input("Enter Higher Secondary Percentage: "))
maths_percentage=float(input("Enter Maths Percentage: "))
entrance_score=float(input("Enter Entrance Exam Score: "))
if higher_secondary >=75 and maths_percentage >= 70 and entrance_score >=80:
print("Admission Status: Eligible")
print("suggested course:Computer Science")
else:
print("Admission Status:Not Eligible")"""


#Loan Approval System#Determine wheather a loan can be approved 
"""age=int(input("Enter the age: "))
salary=float(input("Enter the salary: "))
credit_score=int(input("Enter the credit score: "))
loan_status=input("Existing Loan (yes/no): ")
if age>=30 and salary>=40000 and credit_score>=700 and loan_status.lower()=="no":
    print("Loan Status: Approved")
else:
    print("Loan Status: Rejected")"""

#HOSPITAL PATIENT PRIORITY SYSTEM
# Assign treatement prioriy to patients

"""age=int(input("Enter the age: "))
condition= input("Enter condition(critical/severe/mild): ")
if condition=="critical":
    priority ="Emergency priority"
elif condition=="severe":
    priority="High priority"
else:
    priority="Normal priority"
print("priority category: ", priority)"""


#EMPLOYEE BONUS MANAGEMENT SYSTEM
#Calculate employee bonus based on performance

"""years =int(input("Enter years of service: "))
performance=input("Enter performance rating(Excellent): ")
attendance=float(input("Enter attendance percentage: "))
salary=50000
if performance=="Excellent" and attendance>=90:
    bonus_percentage=20

elif performance=="Good" and attendance>=80:
    bonus_percentage=10

else:
    bonus_percentage=5
bonus_percentage= salary * bonus_percentage/100
bonus_amount=10000
print("Bonus Percentage: ", bonus_percentage,"%")
print("Bonus Amount: ₹", bonus_amount)"""

#Smart Traffic Fine System

"""Helmet=input("Helmet Worn(yes/no): ")
seatbelt=input("Seatbelt Used(yes/no): ")
speed=input("Speed Limit Violated(yes/no): ")
license_valid=input("Valid License(yes/no):")
fine=0
if Helmet =="no":
    fine += 500
    if seatbelt =="no":
        fine += 500
if speed=="yes":
    fine +=1000
    if license_valid =="no":
        fine+=2000

print(f"Total Fine: ₹{fine}") #ctrl+alt+4"""     

#Cinema Ticket Booking System 
"""age=int(input("Enter the age:"))
seat_type=input("Seat Type(Normal/Premium):")
day_type=input("Day Type(Weekday/Weekend):")
student=input("Student (Yes/No):")

if seat_type =="normal":
    cost=200
else:
    cost=300

if day_type=="weekend":
     cost +=50

if student=="yes":
     cost -=70
print(f"Final Ticket Cost: ₹{cost}")"""        

#Scholarship Eligibility System 
"""family_income=float(input("Enter Family Income:"))
academic_percentage=float(input("Enter Academic Percentage:"))
attendance_percentage=float(input("Enter Attendance Percentage:"))

if family_income<=180000 and academic_percentage>=92 and attendance_percentage>=96:
     print("\nScholarship Status:Full Scholarship")
elif family_income<=250000 and academic_percentage>=80 and attendance_percentage>=86:
     print("\nScholarship Status:Partial Scholarship")
else:
     print("\nScholarship Status:No Scholarship")"""

#Student Performance Analytics System
marks1=int(input("Enter Mark 1:"))
marks2=int(input("Enter Mark 2:"))
marks3=int(input("Enter Mark 3:"))
marks4=int(input("Enter Mark 4:"))
marks5=int(input("Enter Mark 5:"))
total=marks1 + marks2 +marks3 +marks4 +marks5
percentage=total/5

if marks1>=40 and marks2>=40 and marks3>=40 and marks4>=40 and marks5>=40:
    result="Pass"
    promotion="Eligible"
else:
    result="Fail"
    promotion="Not Eligible"

if percentage>=90:
    grade="A+"
elif percentage>=80:
    grade="A"
elif percentage>=70:
    grade="B"    
elif percentage>=60:
    grade="C"
elif percentage>=50:
    grade="D"
else:
    grade="F"         

print("\nTotal Marks:",total)
print("\nPercentage:",percentage)
print("\nGrade:",grade)
print("\nResult:",result)
print("\nPromotion Status:",promotion)





