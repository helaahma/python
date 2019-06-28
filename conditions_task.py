
#Define 2 variables and one operator
var1= input("Please enter 1st integer: \n")
var2= input("Please enter 2nd integer: \n")
oper=input("Please enter an operator (+,-,*,/): \n")

#Conditions
if (var1.isdigit()==True and var2.isdigit() == True) and oper== "+":
	print ("the result of %s %s %s=" %(var1,oper,var2), int(var1)+int(var2))
elif (var1.isdigit()==True and var2.isdigit() == True) and oper=="*":
	print ("the result of %s %s %s= "%(var1,oper,var2), int(var1)*int(var2))
elif (var1.isdigit()==True and var2.isdigit() == True) and oper=="-":
	print ("the result of %s %s %s=" %(var1,oper,var2), int(var1)-int(var2))
elif (var1.isdigit()==True and var2.isdigit() == True) and oper=="/":
	print ("the result of %s %s %s=" %(var1,oper,var2), int(var1)/int(var2))
else:
	print ("Operation is invalid \n")