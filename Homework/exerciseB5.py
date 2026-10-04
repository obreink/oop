class Person:
    first_name = "Joe"
    last_name = "Bloggs"
    age = 25
    is_left = False


 class Employee:
     first_name = "Joe"
     last_name = "Bloggs"
     id = 294404
     _salary = 20000
     job_title = "DevOpps Engineer"



def Employee:
    def __init__(self, id, first_name="Jim",last_name="Halpert",job_title="Developer",Salary=25555):
        self.id= id
        self.first_name=first_name
        self.last_name=last_name
        self.job_title= job_title
        self._salary = salary



def get_salary(self,):

    return self._salary




def display(self):
    print(f"Employee id:{self.id},First Name{self.first_name},Last Name: {self.last_name},Salary : {self.get_salary()}")





def cal_net_pay(self):
    taxed = self._salary * 0.42  # calculate tax by multiplying salary and tax percentage


    yearly_take=self._salary - taxed   #remove tax deductions from annual salary
    monthly_take = yearly_take/12     #divide yearly earning by 12 to find salary with tax deducted

    return monthly_take




def cal_bonus(self):
    role = self.job_title

    if role == "manager":
        bonus_percentage = 0.15

    elif role == "intern":
        bonus_percentage = 0.02

    else:
        bonus_percentage = 0.06

    return self._salary * bonus_percentage






if __name__ == "__main__":
    emp1= Employee()
    emp2=Employee(294404,"Dwight","Schrute","Assistant to Reginal Manager",22000 )

#Add a get_salary() method to the  This method should return the salary attribute