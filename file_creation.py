'''store_data=open("new file.txt","w")#store_data is variable ,open()will opens a file,new file.txt is the file name,w is the write mode,
#if the file doesn't exists python creats it.if it already exists python erases the old content.
store_data.write("Welcome to python programming")
print(store_data)
store_data.close()

read_data=open("new file.txt","r")
print(read_data.read())
read_data.close()

#append will add data to the file
append_data=open("new file.txt","a")
append_data.write("\nPython is an interpreted language")
print(append_data)
append_data.close()

#read displays the content of the file
read_data=open("new file.txt","r")
print(read_data.read())
read_data.close()'''

#context manager use with keyword
#using context manager...it automatically closes
'''with open("newfile.txt","r")as f:
    print("Current Position: ",f.tell())
    f.read(6)
    print("After Read Position: ",f.tell())
    f.seek(4)
    print("After Seek: ",f.tell())
    print(f.read())

with open("illusion.jpg","rb") as data:
      image_read=data.read()
      print(image_read)

#try out pip install pillow and use its functions and use pilow to import image

tech=open("delete_file.txt","x")#x for exclusive creation
print(tech)
tech.close()

file_path="delete_file.txt"
import os
if os.path.exists(file_path):
    os.remove(file_path)
    print(f"{file_path}deleted successfully")
else:
    print("File does not exists.")'''


#serialsiation  python to byte 
#pickle serialsation and json serialisn
#python obje is stored into a file using dump method
#serialisation and deserialistn
#data stored in key value pair
import pickle 
data={
    "students":["Aruna","Liya","Ujwal"],
    "marks":(50,87,90),
    "subjects":{"Maths","English","Python"}
    }

#serialsiation-saving data to file
with open("user_details.pkl","wb") as f:#aliased 'as'
    pickle.dump(data,f)
    print("Data is serialised into user details",data)
    
with open("user_details.pkl","rb") as file:
    loaded_data=pickle.load(file)
    print("Data read from the pickle: ",loaded_data)

dump_data=pickle.dumps(data)
print("Data is Serialsied to Bytes: ",dump_data)


load_data=pickle.loads(dump_data)
print("Data is Desentralised to objects: ",load_data)


#try out json module
#diff btwn pickle and json 
#json --used for sharing data btwn differnt systems for eg sending data from a python backend to react front end 
#pickle module is used for saving python objects ..eg: saving a trained ML model or python object
   
#question 10 differnces betwenn these two pickle and json ..like purpose,extension ,use cases etc.........


#FILE HANDLING PROBLEMS
#Student Record Management System

#Step 1:understand the need 
{
"id":101,
"name":"Aruna",
"marks":86,
"attendance":90
}

#Step 2:create a text file...open(),close(),write()
file=open("students.txt","w")
file.write("101,Aruna,86,90\n")
file.write("102,Goutham,89,92\n")
file.close()
print("Student Records Saved")

#step 3:Read students records...read(),readline(),readlines()
file=open("students.txt","r")
print(file.read())#reads entire file
file.close()

file=open("students.txt","r")
print(file.readline())#reads only first line
file.close()

file=open("students.txt","r")
print(file.readlines())
file.close()

#Step 4: Append new student "a"mode...adds data without deleting old data
file=open("students.txt","w")
file.write("103,Chiipi,87,88")
file.close()

#Step 5: Using with Statement...context manager..here file will close automatically
with open("students.txt","r") as file:
    print(file.read)

file=open("students.txt","r")
print("File Name:",file.name)
print("File Mode:",file.mode)
print("Closed:",file.closed)
file.close()

#Step 7: File Pointer...tell(),seek()
file=open("students.txt","r")
print(file.tell())
file.read(5)
print(file.tell())
file.seek(0)
print(file.tell())
file.close()

#Step 8: OS Module (File and Directory Handling)
import os
os.makedirs("student_records",exist_ok=True)
#creates a directory and shows files
print("Folder is ready")

#Step 9: Exception Handling..try except finally 
try:
    file=open("data.txt","r")
except FileNotFoundError:
    print("File not found")    
finally:
    print("Operation  Completed")    


#Step 10: Binary File
file=open("data.bin","wb")
file.write(b"Student Data")
file.close()

file=open("data.bin","rb")
print(file.read())
file.close()

#Step 11:Serialization.... Pickle Serialization
import pickle
student={
    "id":101,
    "name":"Aruna",
    "marks":86,
    "attendance":90
}
file=open("student.pkl","wb")
pickle.dump(student,file)
file.close()
print("Pickle file created")

file=open("student.pkl","rb")
data=pickle.load(file)
print(data)
file.close()

#Step 12: JSON Module
import json
student={
    "id":101,
    "name":"Aruna",
    "marks":86,
    "attendance":90
}

file=open("student.json","w")
json.dump(student.json,"w")
json.dump(student,file)
file.close()
print("JSON file created")





