"""Get an input from the user. Number of upper case letters, lower case numbers, number of digits and other
Write a program that gives character count."""
data = input("Please Enter Anything")
digit = 0 # !!!!!!!!!!!!!!!!!! I want to use the "for". Because of this my veriable have begin at zero 
upper = 0
lower = 0
other = 0
for i in data:
	if(i.isupper()):
		upper +=1 #so that each time a large letter appears, the variable takes +1

	elif(i.islower()):
		lower+=1 #so that each time a lower letter appears, the variable takes +1

	elif(i.isdigit()):
		digit+=1 #so that each time a digit appears, the variable takes +1
	else:
		other+=1 #so that each time a other chracter appears, the variable takes +1
print("You Special Chracter Count is:",other)		
print("Your Count Of Digit is: ",digit)
print("Your Count Of Upper is: ",upper)
print("Your Count Of Lower is: ",lower)