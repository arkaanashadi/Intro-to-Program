stack = []

# Addition Function
def add(x,y):
	return y+x
		
# Substraction Function
def sub(x,y):
	return y-x

# Multiplication Function
def mult(x,y):
	return y*x

# Division Function
def div(x,y):
	return y/x

# RPN Main Function
def main ():
	#Initial Input
	inp = input()
	# Makes sure the first input is a number or "end" which ends the program
	while(inp.isdigit() == False and inp != "end"):
		print("Try again")
		inp = input()
	
	# Checks for "end" which ends the program
	if (inp == "end"):
		print()
	# If the input is verified as a number, it is then added 
	# into the stack and the next input is requested
	else:
		stack.append(int(inp))
		inp = input()
		
		while(inp.isdigit() == False and inp != "end"):
				print("Try again")
				inp = input()
				
		if (inp == "end"):
				print()
		else:
			stack.append(int(inp))
		while (inp != "end"):
			inp = input()
			if (inp == "add"):
				r = (add(int(stack.pop()),int(stack.pop())))
				print (r)
				stack.append(r)
				
			elif (inp == "sub"):
				r = sub(int(stack.pop()),int(stack.pop()))
				print (r)
				stack.append(r)
				
			elif (inp == "mul"):
				r = mult(int(stack.pop()),int(stack.pop()))
				print (r)
				stack.append(r)
				
			elif (inp == "div"):
				r=div(int(stack.pop()),int(stack.pop()))
				print (r)
				stack.append(r)
				
			elif (inp == "end"):
				print()
			
			elif (inp == "print"):
				print(stack)
				
			elif (inp.isdigit() == False):
				print("Try again")
				
			else:
				stack.append(int(inp))
				
main()