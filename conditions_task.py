
var1= input("Please enter 1st integer: \n")
var2= input("Please enter 2nd integer: \n")


oper1=input("Please enter 1st operator (+,-,*,/): \n")
oper2=input("Please enter 2nd operator (+,-,*,/): \n")

if (var1.isdigit()==True and var2.isdigit() == True) and (oper1=="+" or oper1=="-" or oper1=="*" or oper1=="/") and (oper2=="+" or oper2=="-" or oper2=="*" or oper2=="/"):
	print ("You entered two integers. Operator 1 is %s and operator 2 is %s" %(oper1, oper2))
else:
	print ("Operation is invalid \n")