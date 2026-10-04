class Person:

    def __init__(self, first_name, last_name, age, is_left):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.is_left = is_left


#Amend your previous program in which the user creates a Person to use your parameterised constructor. Your
#program should now create and fill the object in one action, rather than creating a default Person and then filling it
#with values one at a time.

first_name=input("Enter first name ")
last_name=input("Enter last name")
age=int(input("Enter age"))
is_left=input("are you left handed :Y/N")


person= Person()