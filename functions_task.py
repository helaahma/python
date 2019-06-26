#This program checks the date of birth
#Import current date function from the datetime library
from datetime import date
current_date= date.today()
print ("Today's date is ", current_date)


def check_birthdate (age_year, age_month, age_ay):
	

	#Check if all variable format are as required

	if  len (age_year)==4 and age_year.isnumeric() and len (age_month)<=2 and age_month.isnumeric() and len(age_day)<=2 and age_day.isnumeric() and check_birthdate(age_year,age_month, age_day)<=current_date and check_birthdate(age_year, age_month, age_day)>0:
		#Check birth date is not in the future and additionally checks if date formate is correct

		return True

	
	# False message

	else:
	
		return False

def calculate_age (age_year, age_month, age_day):

	user_age= (((current_date.year- int(age_year)) + (current_date.month-int(age_month)) + (current_date.day-int(age_day))))


#prompt the user to enter required variables
age_year, age_month, age_day= input ("Please enter your birthdate here (YYYY-MM-DD) : \n").split()


"""Note: I want the user to enter inputs seperated by dashes instead of spaces in the CLI window as this will save time and effort and the use of spaces is not friendly or clear to the user
 	please help on this one???
 	Also I want to ask for the user input inside the function"""
# define check_birthdate


if check_birthdate (age_year, age_month, age_day)== True:
	print (calculate_age)

else:
	print ("False. You entered values with wrong format; please enter your date of birth again \n ")





