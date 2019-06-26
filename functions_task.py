#This program checks the date of birth
#Import current date function from the datetime library
from datetime import date
current_date= date.today()
print ("Today's date is ", current_date)


if :

	print ("you entered %s-%s-%s" %(birth_year, birth_month, birth_day))

else:

	print ("You enter wrong formats, please run the program again") 




# define check_birthdate
def check_birthdate (year, month, day):
	
	#prompt the user to enter required variables

	year, month, day= input ("Please enter your birthdate here (YYYY-MM-DD) : \n").split()

	"""Note: I want the user to enter inputs seperated by dashes instead of spaces in the CLI window as this will save time and effort and the use of spaces is not friendly or clear to the user
    please help on this one???
    Also I want to ask for the user input inside the function"""

	#Check if all variable format are as required

	if  len (year)==4 and year.isnumeric() and len (month)<=2 and month.isnumeric() and len(day)<=2 and day.isnumeric() and check_birthdate(year, month, day)<=current_date and check_birthdate(year, month, day)>0:
		#Check birth date is not in the future and additionally checks if date formate is correct
		print (" True ")

	
	# False message

	else:
		print ("False. You entered values with wrong format; please enter your date of birth again \n ")
		year, month, day= input ("Please enter your birthdate here (YYYY-MM-DD) : \n").split()
	return check_birthdate


check_birthdate (year, month, day)

#[Previous line repeated 996 more times] RecursionError: maximum recursion depth exceeded








