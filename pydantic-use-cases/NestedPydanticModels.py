from pydantic import BaseModel


class Address(BaseModel):
    city : str
    state : str
    pin_code : str 

class Patient(BaseModel):

    name : str
    age : int 
    gender : str 
    address : Address


# print the details of the patient.
def print_details(patient):
    print(patient.name)
    print(patient.address.city)
    print(patient.address.state)
    print(patient.address.pin_code)

address_dict = {
    'city' : 'Delhi', 
    'state' : 'New Delhi', 
    'pin_code' : '110025'
}

# create an object of Address class.
address1 = Address(**address_dict)

patient_dict = {
    'name' : 'uzaif', 
    'age' : 26,
    'gender' : 'Male',
    'address' : address1
}

# create an object of the class Patient.
patient = Patient(**patient_dict)

# print the object.
# print(patient)

print_details(patient)