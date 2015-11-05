#Problem #1
#Users are the worst- they are always forgetting how to use the software properly. 
#Write a program that barks at the user every time they enter in the same input twice. 
#You must use a while loop to continually ask the user for input, and you must use a for loop to 
#iterate through the list of user inputs.

quit = ""
inputList = []
while not quit:
	userData = raw_input("Enter a unique data string (Q to quit): ")
	userData = str(userData)
	if str.upper(userData) == "Q":
		break
	else:
		if len(inputList) == 0:
			inputList.append(userData)
		else:
			for index in range(len(inputList)):
				if userData == inputList[index]:
					print("*woof* *woof*")
					break
				else:
					inputList.append(userData)