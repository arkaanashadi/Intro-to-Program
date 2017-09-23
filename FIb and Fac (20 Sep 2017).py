funct = input("what to do?")
x = int(input())

def factorial():
	y = 1
	for i in range(1,(x+1)):
		y = y*i
	print(y)
	
def fibonacci():
	stack = [0,1]
	for i in range(1,x+1):
		stack.append(stack[-1]+stack[-2])
	print(stack)
	
	
if funct == "fac":
	factorial()
elif funct == "fib":
	fibonacci()
else:
	print("invalid")