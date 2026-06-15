
# Hospital Patient Record System

# Tuple of departments
departments = ("Cardiology", "Neurology", "Orthopedics", "Pediatrics")

# Input patient details
n = int(input("Enter number of patients: "))

for i in range(n):
    print(f"\nPatient {i + 1}")

    patient_id = input("Enter Patient ID: ")
    name = input("Enter Name: ")
    age = int(input("Enter Age: "))
    department = input("Enter Department: ")
    disease = input("Enter Disease: ")
    
    unique_diseases.add(disease)

    patient_records[patient_id] = {
        "name": name,
        "age": age,
        "department": department,
        "disease": disease
    }
    # Search patient record
search_id = input("\nEnter Patient ID to search: ")

if search_id in patient_records:
    print("\nPatient Record Found")
    print(patient_records[search_id])
else:
    print("Patient not found.")

#count patients per department
department_count = {}

for patient in patient_records.values():
    dept = patient["department"]

    if dept in department_count:
        department_count[dept] += 1
    else:
        department_count[dept] = 1

#sort patients based on age
sorted_patients = sorted(
    patient_records.items()
        patient_records.items(),
    key=lambda x: x[1]["age"]
)
