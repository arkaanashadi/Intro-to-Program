stack = []

def add(x,y):
		result = y+x
		stack.append(result)
		print(result)
		
def sub(x,y):
		result = y-x
		stack.append(result)
		print(result)
		
def mult(x,y):
		result = y*x
		stack.append(result)
		print(result)
	
def div(x,y):
		result = y/x
		stack.append(result)
		print(result)

inp = input()
if (inp == "end"):
	print()
else:
	stack.append(int(inp))
	print(stack)
	inp = input()
	stack.append(int(inp))
	
	while (inp != "end"):
		
		inp = input()
		
		if (inp == "add"):
			add(int(stack.pop()),int(stack.pop()))
			print(stack)
		elif (inp == "sub"):
			sub(int(stack.pop()),int(stack.pop()))
			print(stack)
		elif (inp == "mul"):
			mult(int(stack.pop()),int(stack.pop()))
			print(stack)
		elif (inp == "div"):
			div(int(stack.pop()),int(stack.pop()))
			print(stack)
		elif (inp == "end"):
			print()
		else:
			stack.append(int(inp))