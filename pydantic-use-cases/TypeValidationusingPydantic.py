from pydantic import BaseModel

class Patient(BaseModel):
    name : str
    age : int
    weight : float


# here we clearly see that we dont need to write similar code again again in the different function.
# code reusibity increase.
def insert_data_into_DB(patient : Patient):

    print(patient.name)
    print(patient.age)
    print(patient.weight)

    print('Data has been Inserted Successfully!')

def update_data_into_DB(patient : Patient):

    print(patient.name)
    print(patient.age)
    print(patient.weight)

    print('Data has been Updated Successfully!')

dictionary = {
    'name' : 'uzaif', 
    'age' : 25, 
    'weight' : 62.4
} 

# here we are unpack the dictionary first before passing it.
# patient = Patient.model_validate(**dictionary)

# here we dont need to unpack the dictionary, because model_validate function.
patient = Patient.model_validate(dictionary)

insert_data_into_DB(patient)
update_data_into_DB(patient)

