#define an empty list which will hold our dictionary
list_items= []
#While loop, and the condition is True
while True:
	#User 1st input
	item= input ("Please enter \"done\" when finished or another item below: \n")
	

	# Define a conditional statement to break at "Done" input
	if item == "done" or item=="Done":
		break
	#return to the loop
	#User input
	price= input ("Please enter the price of the item below: \n")
	quant= input ("Please enter quantity of the item below: \n")

	#Required by the example
	price_items= int(price)*int(quant)

	#Add a dictionary to enter multiple variables
	dict={}
	#Add 1st key 
	dict["item"]=item
	#Add 2nd key
	dict["price"]=price
	#Add 3rd key
	dict["quantity"]=quant
	#And the last key
	dict["all"]=price_items
	#Append our dictionary to the list_items
	list_items.append(dict)

#Define new variable that shall be used later to calculate the sum of "all" key in the dictionary
total = 0
#Use for loop as required in the task but also to iterate over the values where i is now the dict
for i in list_items:
#print reciept
	print (i["quantity"], i["item"], i["price"], i["all"])
	#Now we use total which will iterate over "all" key and add the values up (Note to self: I used i)
	total += i["all"]
	#print the total price
print ("total:  ", total, " K.D")


