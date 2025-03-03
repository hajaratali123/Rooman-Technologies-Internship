patient_data ={
    "name":"ali",
    "age":25,
    "city":"beijing",
}

print(patient_data)
patient_data["ocupation"]="engineer"

print(patient_data)

for key,value in patient_data.items():
    print(f"{key} : {value}")

patient_data["contact number"]=8596585565
print(patient_data)


del patient_data["contact number"]
print(patient_data)

patient_data["age"]=23

print(patient_data)
