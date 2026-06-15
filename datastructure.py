#tuple
"""tuple1=(10,20,30)
print(tuple1)
nested_tuple=((1,2,3,4),20,"Aruna","tvm")
print(nested_tuple)"""


#try out indexing and slicing
#try out immutabiliity

"""person=("Aruna",20,"Tvm")
name,age,place=person
#tuple unpacking
print(name)
print(age)
print(place)"""

"""number=(10,20,30,40,50)
#here a=10 b=20 c=30 40 50 vrnm
a,b,*c=number
print(a)
print(b)
print(c)

d,*e,f=number
print(d)
print(e)
print(f)"""

"""value=(2,3,4,5,6,2,2,5,6,6,3,4,3,5)
print(len(value))
print(value.count(6))
print(value.count(5))
print(value.index(3))
print(value[3])#index starts from zero"""

"""user_data=input("Enter a String")
count=0
for item in user_data:
     count+=1
print(count)"""

# print first non repeating character 
"""text=("Enter a  String")
for ch in text:
     if text.count(ch)== 1:
          print("First non repeating ")"""

"""user_input=input("Enter a String")
for item in user_input:
     if user_input.count(item)==1:
          print("First Non Repeating character:",item)
          break
else:
     print("There is no non  repeating characters")"""

#sets are mutable and non indexing and doesnt allow duplicates
#union intersection difference
"""student1={"English","Hindi","Malayalam"}
student2={"English","Hindi","German"}
student3={"german","Python","Hindi"}
student1.add("Urdu")#through hashing algorithm(we cannot add to a certain position in sets)
print(student1)
student1.update(["Django","R"])#can include multiple values
print(student1)
student2.add("Japanise")

print(student2)
student1.add("Malayalam")
print(student1)

student1.remove("Hindi")
print(student1)

student1.remove("Java")
print(student1)"""

"""student1.discard("Hindi")
print(student1)

student1.pop("English","Malayalam")#removes any random element
print(student1)

student1.discard("Hindi")
print(student1)"""

#union intersection difference
#& and
#union rndilum common
"""student1={"English","Hindi","Malayalam"}
student2={"English","Hindi","German"}
student3={"german","Python","Hindi"}

print(student1.union(student2))
print(student1.intersection(student2))
print(student1.difference(student2))

print(student1 | student3)
print(student1 & student3)
print(student1 - student3)

set1={1,2,3}
set2={7,8,9}
set3={4,5,6}

print(set1.isdisjoint(set2))#two sets are disjoint if they have no common elements
print(set2.isdisjoint(set1))

#frozen set
#is immutable,unordered collectn of unique elelments
fs1=frozenset("aruna")
fs2=frozenset([12,23,45])
fs3=frozenset((11,23,45))

print(fs1)
print(fs2)
print(fs3)"""

#dictionary key value pair (keys are immutable)
#dictinaory works as based on key
"""student={
    "name":"Aruna",
    "age": 20,
    "place":"TVM"
}
print(student)
print(student["name"])
print(student.get("marks"))
student["marks"]=60
print(student)
student.pop("age")
print(student)#to remove 'age' key
del student["name"]
print(student)

info=dict(city="TVM",location="Kerala")
print(info.keys())
print(info.values())
print(info)

#try out update function for multiple insertions

student.update({"nation":"india","state":"kerala"})
print(student)"""

#nested dictionary
"""employee={
    "emp1":{
        "name":"Aruna",
        "age":20     
    },
    "emp2":{
        "name":"Gouthu",
        "age":25
    },
    "emp3":{
        "name":"Karuna",
        "age":24
    },
    "emp4":{
        "name":"Karun",
        "age":32
    }
    
}
print(employee["emp3"]["age"])
print(employee["emp3"]["name"])"""