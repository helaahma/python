
#Ask the user for inputs

Number= input ("Please enter an integer: \n")
Number=int(Number)
Noun= input ("Please enter a noun (plural): \n")
Noun= Noun.lower()
Name= input ("Please enter a name: \n")
Name= Name.capitalize()
Sentence= input ("Please enter a sentence: \n")
Sentence= Sentence.capitalize()
Verb= input ("Please enter a verb: \n")
Verb= Verb.lower()

#print  
print ("""\t It was %02d o'clock when I heard a knock at the door.
\t I opened the door and there was a box full of %s 
\t with a note saying \"From Mr. %s\".
\t Just as I closed the door I heard a scream \"%s\".
\t I froze in place and all I could do was %s.
""" %(Number, Noun, Name, Sentence, Verb))