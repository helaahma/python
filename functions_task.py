#This program checks the date of birth
#Import current date function from the datetime library
from datetime import date
current_date= date.today()
print ("Today's date is ", current_date)

#PART 1 of 3: Break check_birthdate(age_year,age_month, age_day)<=current_date and check_birthdate(age_year, age_month, age_day)>0
current_year= current_date.year
current_month= current_date.month
current_day= current_date.day



def check_birthdate (age_year, age_month, age_day):
	

	#Check if all variable format are as required
	#variable.isnumeric deleted since lines 42, 43, 44 deals with this problem now. 
	if len (str(age_year))==4 and len (str(age_month))<=2 and len(str(age_day))<=2 and ((current_year+current_month+current_day)-(age_year+age_month+age_day))>0:#PartII:Check if the date provided by the user is indeed in the past
		#Check birth date is not in the future and additionally checks if date formate is correct

		return True

	
	# False message

	else:
	
		return False

def calculate_age (age_year, age_month, age_day):

	age_year= current_year-int(age_year)
	age_month=current_month-int(age_month)
	age_day= current_day-age_day

	#I'm using %s instead of %d to print the exact numbers instead of printing 0's on the left
	print (" You are %s year, %s month, and %s day old" %(str(age_year), str(age_month), str(age_day)))

#prompt the user to enter required variables
age_year, age_month, age_day = input ("Please enter your birthdate here (YYYY-MM-DD) : \n").split()
age_year= int(age_year)
age_month=int(age_month)
age_day= int(age_day)
#partIII: Added to insure the program won't accept (-) values
assert (int(age_year) >0), 'Number must be > than 0 Re-run the program'
assert (int(age_month) >0), 'Number must be > than 0 Re-run the program'
assert (int(age_day)>0), 'Number must be > than 0 Re-run the program'


"""Note: I want the user to enter inputs seperated by dashes instead of spaces in the CLI window as this will save time and effort and the use of spaces is not friendly or clear to the user
 	please help on this one???
 	Also I want to ask for the user input inside the function"""
# define check_birthdate


if check_birthdate (age_year, age_month, age_day)== True:
	calculate_age(age_year, age_month, age_day)
else:
	print ("False. You entered values with wrong format; please enter your date of birth again \n ")





