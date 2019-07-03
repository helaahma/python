from datetime import date

class Employee(object):
	"""Employee class for represinting employment information"""
	
	#1st method initate the class
	def __init__(self, name, age, salary, get_working_years):
		self.name= name
		self.age= age
		self.salary= salary
		self.get_working_years= get_working_years

	#2nd method using self which refers to the intiated arguments

	def get_working_years(self):
		self.get_working_years= ((current_date.year-datetime.year))
		return self.get_working_years


	#3rd method __str__ returns useful information to the HR 
	def __str__(self):

		return "Employee: {}, age: {}, salary: {}, working years: {}".format(self.name, str(self.age), str(self.salary), str(self.get_working_years))


class Manager(Employee):
	"""Initiate a new class that inherits from Employee"""

	#Additional method for Manager
	def bonus_percentage(self):
		self.bonus_percentage= bonus_percentage
		
	#Additional method for Manager
	def get_bonus(self):
		self.get_bonus=int(bonus_percentage)*int(salary)
		return self.get_bonus
		#doesn't print in __str__ method!!!!!!!!!!!!!!!!????????

	#Additional method for Manager
	def __str__(self):
		return "Manager: {}, age: {}, salary: {}, working years: {}, bonus:{}".format(self.name, str(self.age), str(self.salary), str(self.get_working_years), str(self.get_bonus())



current_date= date.today()


name_list_employee=[]
age_list_employee=[]
salary_list_employee=[]
years_list_employee=[]
accumulate_employee=zip(name_list_employee, age_list_employee, salary_list_employee, years_list_employee)
employees=[Employee(name,age,salary,employment_date) for (name,age,salary,employment_date) in accumulate_employee]
#Employee(name_employee, age_employee, salary_employee)
#Manager(name_manager, age_manager, salary_manager, year)

name_list_manager=[]
age_list_manager=[]
salary_list_manager=[]
years_list_manager=[]
bonus_manager=[]
accumulate_manager=zip(name_list_manager, age_list_manager, salary_list_manager, years_list_manager,bonus_manager)
managers=[Employee(name,age,salary,employment_date, get_bonus) for (name,age,salary,employment_date, get_bonus) in accumulate_manager]
#Welcome message
print ("\t Welcome to HR Pro 2019\n")

while True:
	#User input 
	hr=input("\t Choose an action to do:\n \t\t1. show employees\n \t\t2. show managers\n \t\t3. add an employee\n \t\t4. add a manager\n \t\t5. exit\n\nWhat would you like to do?  ")

	#Conditional statement 
	if (hr=="show employees" or hr=="1"):
		#I want to store all the values the user enters in a list ???????????????????????????
		print (employee.__str__())
	elif (hr=="show managers" or hr=="2"):
		#I want to store all the values the user enters in a list ???????????????????????????
		print (manager.__str__())
	elif (hr=="add an employee" or hr=="3"):
		name_employee=input("Please enter the name: \n")
		#employees.append(name_employee)
		age_employee=input("Please enter the age: \n")
		#employees.append(age_employee)
		salary_employee=input("Please enter the salary: \n")
		#employees.append(salary_employee)
		year=input("employment date YYYY: \n")
		#employees.append(year)
		employee=Employee(name_employee, age_employee, salary_employee, year)
		print("Employee added succesfully: \n")
		print()
		add_employee= print (employee.__str__())
		#employees.append(add_employee)
		#new
		


	elif (hr=="add a manager" or hr=="4"):
		
		name_manager=input("Please enter the manager's name: \n")
		#managers.append(name_manager)
		age_manager=input("Please enter the manager's age: \n")
		#managers.append(age_manager)
		salary_manager=input("Please enter the manager's salary: \n")
		#managers.append(salary_manager)
		year=input("employment date YYYY: \n")
		#managers.append(year)
		percentage=input ("bonus percentage: \n ")
		manager=Manager(name_manager, age_manager, salary_manager, year)
		print("Employee added succesfully: \n")
		print()
		add_manager= print (manager.__str__())
		#managers.append(add_manager)

		

	else:
		exit= input("Would you like to exit the program? \n")

		if exit== "yes" or exit=="Y" or exit=="y" or exit=="Yes" or exit=="YES":

			print ("Good buy!")
			
			quit()
		else:

			True


