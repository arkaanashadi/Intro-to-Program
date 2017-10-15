stack = []
# addition function
def addition():
	r = (stack.pop()) + (stack.pop())
	print (r)
	stack.append(r)

# substraction function
def substraction():
	r = (stack.pop()) - (stack.pop())
	print (r)
	stack.append(r)

# multiplication function
def multiplication():
	r = (stack.pop()) * (stack.pop())
	print (r)
	stack.append(r)

# division function
def division():
	r = (stack.pop()) / (stack.pop())
	print (r)
	stack.append(r)
	
def main():
	# Prints the guide for the commands of the calculator
	print('''operators:
	Addition           = "add"
	Substraction       = "sub"
	Multiplication     = "mul"
	Division           = "div"
	Drop top stack     = "drop"
	Print stack        = "print"
	End the calculator = "end"''')
	
	# Requests for first input and makes sure the input is a number or "end" which ends the program
	inp = input()
	while (inp.isdigit() == False and inp != "end"):
		print("Please input a number or end the calculator")
		inp = input()
	# Ends the calculator
	if (inp == "end"):
		print()
	else:
	# Requests the second input and makes sure its also a number or "end"
		stack.append(float(inp))
		inp = input()
		while (inp.isdigit() == False and inp != "end"):
				print("Please input a number or end the calculator")
				inp = input()			
		if (inp == "end"):
				print()
		else:
			stack.append(float(inp))
	# Checks for operators and executes the operation functions
		while (inp != "end"):
			inp = input()
			if inp in ["add","sub","mul","div"]:
				if (len(stack)<2):
					print("Please input a number or end the calculator")
				else:
					if (inp == "add"):
						addition()
						
					elif (inp == "sub"):
						substraction()
						
					elif (inp == "mul"):
						multiplication()
							
					elif (inp == "div"):
						division()
	# Checks and executes other commands (end, drop, print)
			elif (inp == "end"):
				print("Final results")
				print(stack)
			elif (inp == "drop"):
				stack.pop()
			elif (inp == "print"):
				print(stack)
	# The last check, if the input is not any of the available commands and is not a number
			elif (inp.isdigit() == False):
				print("Please input a number or command")
	# If the input passed all the checks if the input is a number or not then it will be added to the stack
			else:
				stack.append(float(inp))

main()