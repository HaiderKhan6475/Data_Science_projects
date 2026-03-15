"""k #02: Employee Salary & Bonus Analyzer

Scenario:
a. Take number of employees as input.


b. For each employee, take input:
Name
Salary

Years of Experience
c. Determine Bonus based on experience:
Experience ≥ 10 → Bonus = 20% of salary
Experience ≥ 5 → Bonus = 10%
Experience ≥ 2 → Bonus = 5%
Otherwise → No bonus

d. Store data in dictionary:
{
  "Ali": {"salary":50000, "experience":5, "bonus":5000}
}
e. Store salaries in a list
f. Find and display:

Employee with highest salary
Average salary
Total bonus paid"""

#a. Take number of employees as input.
num_of_employees = int(input("Enter the number of employees:"))
#b. For each employee, take input:
#Name
#Salary

data = {}
salary_list = []

total_bonus = 0
max_salary = 0
for employees in range(num_of_employees):
    name = input("Enter the name of an employee:")
    salary = int(input("Enter the salary of an employee:"))
    experience = int(input("Enter years of experience: "))

    if experience >= 10:
        #Experience ≥ 10 → Bonus = 20% of salary
        bonus = (20/100)*salary
    elif experience >= 5:

        #Experience ≥ 5 → Bonus = 10%
        bonus = (10/100)*salary
    elif experience >= 2:
        #Experience ≥ 2 → Bonus = 5%
        bonus = (5/100)*salary
    else:
        bonus = 0

    employee_info = {
        "Name":name,
        "Salary":salary,
        "Experience":experience,
        "Bonus":bonus
    }

    data[name] = employee_info
    #e. Store salaries in a list
    salary_list.append(salary)

    total_bonus += bonus


#f. Find and display:
#Employee with highest salary
#3Average salary
#Total bonus paid"""
    if salary > max_salary:
        max_salary = salary
        max_employee = name
average_salary = sum(salary_list) / len(salary_list)
#display:
print("\nEmployee Data:")
print(data)

print("\nEmployee with highest salary:", max_employee)
print("Highest salary:", max_salary)

print("Average salary:", average_salary)

print("Total bonus paid:", total_bonus)
