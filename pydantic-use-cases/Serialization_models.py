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

# we can export our models into 2 format 
# into a Dictionary format.
# into a JSON format.

# dictionary format.
dict_format = patient.model_dump()
print(dict_format)
print(type(dict_format))

# JSON format.
json_format = patient.model_dump_json()
print(json_format)
print(type(json_format))

# There are multiple cases what we want to exclude during, there are parameters called exclude and include used during dumping the object.

# The include and exclude parameters let you control which fields appear in the output.

temp1 = patient.model_dump(include={"name", "age"})
print(temp1)

temp2 = patient.model_dump(exclude={"weight"})
print(temp2)

# PATCH endpoint
patient.model_dump(exclude_unset=True)

# Clean API response
patient.model_dump(exclude_none=True)