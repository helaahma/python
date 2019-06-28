#list

skills= ["communication", "management", "leadership", "adaptability", "technical", "sleeping"]

#dictionary

cv= {}

#User inputs

name= input("Please enter your name below: \n")
age= input ("Please enter your age below: \n")
experience= input("Please enter your years of experience below: \n")
cv["skills"]=" "

#User selection

print (" 1-%s \n 2-%s \n 3-%s \n 4-%s \n 5-%s \n 6-%s" %(skills[0],skills[1],skills[2],skills[3], skills[4],skills[5]))
skill1= input ("Please select one of the above skills: \n")
cv["skills"]= skills[int(skill1)-1]
skill2= input ("Please select one more skill from the same list of skills: \n")

#append

cv["skills"]= skills[int(skill1)-1], skills[int(skill2)-1]
#Condition
if age < 35 and experience > 5 and cv ["skills"]== skills[0:4]:
	print ("Congratulations %s, you meet our criteria." %name)
else:
	#Just for fun
	print ("Sorry, we don't want you:)") 


