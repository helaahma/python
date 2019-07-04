import os
from datetime import date
current_date= date.today()
current_date=current_date.year

class Employee(object):
	"""Employee class for represinting employment information"""
	
	#1st method initate the class
	def __init__(self, name, age, salary,years):
		self.name= name
		self.age= age
		self.salary= salary
		self.years=years

	#2nd method using self which refers to the intiated arguments

	def get_working_year(self):
		
		return (current_date-int(self.years))


	#3rd method __str__ returns useful information to the HR 
	def __str__(self):

		return "Employee: {}, age: {}, salary: {}, working years: {}".format(self.name, str(self.age), str(self.salary), str(self.get_working_year())) 


class Manager(Employee):
	"""Initiate a new class that inherits from Employee and adds to the Manager newly created class"""
	def __init__(self,name, age, salary, years,bonus_percentage):
		Employee.__init__(self,name, age, salary, years)
		self.bonus_percentage= bonus_percentage
	
		
	#Additional method for Manager
	def get_bonus(self):

		return self.bonus_percentage*self.salary

	#Additional method for Manager
	def __str__(self):
		return "Manager: {}, age: {}, salary: {}, working years: {}, bonus:{}".format(self.name, str(self.age), str(self.salary), str(self.get_working_year()), str(self.get_bonus()))






"""
For reference: 
# name_list_employee=[]
# age_list_employee=[]
# salary_list_employee=[]
# years_list_employee=[]
# accumulate_employee=zip(name_list_employee, age_list_employee, salary_list_employee, years_list_employee)
# employees=[Employee(name,age,salary,year) for (name,age,salary, years) in accumulate_employee]
"""
employees = []
"""
Deleted but kept for my reference:

#Employee(name_employee, age_employee, salary_employee)
#Manager(name_manager, age_manager, salary_manager, year)

"""

"""
For reference:
name_list_manager=[]
age_list_manager=[]
salary_list_manager=[]
years_list_manager=[]
bonus_manager=[]
accumulate_manager=zip(name_list_manager, age_list_manager, salary_list_manager, years_list_manager,bonus_manager)
managers=[Employee(name,age,salary,year, percentage) for (name,age,salary,years, bonus_percentage) in accumulate_manager]"""

managers=[]
#Welcome 
print ("\t \n Welcome to HR Pro 2019\n")

while True:
	#User input 
	hr=input("\t Choose an action to do:\n \t\t1. show employees\n \t\t2. show managers\n \t\t3. add an employee\n \t\t4. add a manager\n \t\t5. exit\n\nWhat would you like to do? \n ")

	#Conditional statement 

	if (hr=="show employees" or hr=="1"):

		#This conditional statement is to improve my program

		if len(employees)==0:
			print ("\t Sorry, employees list is empty!\n")
		else:
			# iterate through the list of employees (required)
			for e in employees:
				print("\t", e)
				print("")

	#similarly,  

	elif (hr.lower()=="show managers" or hr=="2"):
		
		if len(managers)==0:
			print ("\t Sorry, managers list is empty!\n")
		else:
		
			for m in managers:
				print("\t", m)
				print("")
		
	elif (hr.lower()=="add an employee" or hr=="3"):
		name_employee=input("Please enter the name: \n")
		""" 
		This is kept form my reference
		#employees.append(name_employee)
		"""
		age_employee=input("Please enter the age: \n")
		""" 
		This is kept form my reference
		#employees.append(age_employee)
		"""
		salary_employee=input("Please enter the salary: \n")
		""" 
		This is kept form my reference
		#employees.append(salary_employee)
		"""

		year=input("employment date YYYY: \n")
		""" 
		This is kept form my reference
		#employees.append(year)
		"""
		employee=Employee(name_employee, age_employee, salary_employee, year) #This create instance of class Employee
		print("Employee added succesfully: \n")
		print("")
		add_employee= print (employee.__str__())
		employees.append(employee)
		
		


	elif (hr.lower()=="add a manager" or hr=="4"):
		
		name_manager=input("Please enter the manager's name: \n")
		""" 
		This is kept form my reference
		#managers.append(name_manager)
		"""
		age_manager=input("Please enter the manager's age: \n")
		""" 
		This is kept form my reference
		#managers.append(age_manager)
		"""
		salary_manager=int(input("Please enter the manager's salary: \n"))
		""" 
		This is kept form my reference
		#managers.append(salary_manager)
		"""
		year=input("employment date YYYY: \n")
		""" 
		This is kept form my reference
		#managers.append(year)
		"""
		percentage=(float(input ("bonus percentage: \n "))/100) #This will ensure correct calc.
		manager=Manager(name_manager, age_manager, salary_manager, year, percentage)
		print("Employee added succesfully: \n")
		print("")
		add_manager= print (manager.__str__())
		managers.append(manager)

		

	else:
		exit= input("Would you like to exit the program? \n")

		if exit== "yes" or exit=="Y" or exit=="y" or exit=="Yes" or exit=="YES":

			os.system('clear') #clear the terminal window before exiting
			print ("Good buy!") 
			quit() #exit()
		"""	
		for reference:
		else:

			True #This will allow the program to  re-run (while loop power!)

			No need!"""


