"""Get an input from the user. Write a program that gives the sum of the numbers in the inputt. (User does not have to enter digits.
The user can also enter different characters.)"""
data = input("Please Enter Anything: ")
sumOfdigit =0
for digit in data:
	if(digit.isdigit()):
		digit= int(digit) #To convert the numeric characters that receive from the user to an integer number.
		sumOfdigit += digit #sumOfdigit + digit
		#print(sumOfdigit) # if you use the print here, its sum step by step
print("The Sum Of Digits In Your Strigs are: ",sumOfdigit)
		
		
		