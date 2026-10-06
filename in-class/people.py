



class Employee:
    def __init__(self,first_name,last_name,id,salary,job_title):
        self.first_name=first_name
        self.last_name=last_name
        self.id=id
        self._salary=salary
        self.job_title=job_title

    def get_salary(self,):

        return self._salary

    def display(self):
        print(f"Employee id= {self.id}")
        print(f"Employee Name ={self.first_name}")
        print(f"Employee Surname ={self.last_name}")
        print(f"Employee Salary ={self._salary}")
        print(f"Employee Title ={self.job_title}")

    def calc_net_pay(self):
        tax= self._salary * 0.42  #calculate tax by annual salary and tax percentage
        yearly_income= self._salary-tax
        monthly_income= yearly_income/12

        return monthly_income






    def calc_bonus(self):



        if "Manager" in job_title:

            bonus_rate = 0.15

        elif "Intern" in job_title:

            bonus_rate = 0.02

        else:
            bonus_rate= 0.06

        return self._salary * bonus_rate


    def get_highest_pay(self,id,salary):

        highest_salary = 0
        if highest_salary > self._salary:
            highest_salary = self._salary



        return










    def get_lowest_pay(self,id, salary ):

        lowest_salary = min(self._salary)



        return








if __name__ == "__main__":
    employees = {} #dictionary to hold all employees


    while len(employees)< 5:
        employee_id=int(input("Enter Employee id:"))

        if employee_id  in employees:
            print("An employee with existing id already exists.Try Again")


        else:



        employee_name=input("Enter Employee Name")
        employee_lname=input("Enter employee Surname")
        employee_salary=float(input("Enter Employee Salary"))
        employee_title=input("Choose Employee title  |Manager| Intern| Other| ").lower()




