from people import  Employee


employee = {}

while len(employee) < 5:

    employee_id = int(input("Enter Employee ID: "))

    if employee_id in employee:
        print("An Employee with that id already exists. Enter another id.")
        continue   # go back and ask for the id again

    employee_fname = input("Enter first name: ")
    employee_lname = input("Enter last name: ")
    job_title = input("Enter job title: ")
    salary = float(input("Enter salary: "))

    employee[employee_id] = Employee(employee_id, employee_fname, employee_lname, job_title, salary)