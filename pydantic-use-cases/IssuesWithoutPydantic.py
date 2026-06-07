

def inert_into_DB(name : str, age : int):

    # we can handle this by using the manual constriants, but what if there are multiple varaibles.
    # That is why this is not scalable.
    if type(name) == str and type(age) == int:
        print(name)
        print(age)
        print('Inserted Data into the Database!')
    else:
        raise TypeError('Gives the correct type of input')
    
    

def update_from_DB(name : str, age : int):

    # we can handle this by using the manual constriants, but what if there are multiple varaibles.
    # That is why this is not scalable.
    # Type Validation
    if type(name) == str and type(age) == int:
        # here we put a constraint on the data value
        # Data validation
        if age > 0:
            print(name)
            print(age)
            print('Update the Data into the Database!')
        else:
            raise ValueError('Give the correct input value of age')
        
    else:
        raise TypeError('Gives the correct type of input')

# when I am calling this function this is not show any error because the python is the dynamic type language same variable can save any type of data.
inert_into_DB('uzaif', 'tweenty-six')

# when we are writing the datatype in front of the varaible str, int, it will show in the structure but programmer still do this is mistake, it will also not giving any error.
inert_into_DB('uzaif', '26')

