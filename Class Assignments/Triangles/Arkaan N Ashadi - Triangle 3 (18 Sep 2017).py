x=6
y=1
for i in range(1, 14):
	if (i<6):
		print((' '*x)+('*'*y))
		x=x-1
		y+=2
	else:
		print((' '*x)+('*'*y))
		x=x+1
		y=y-2 