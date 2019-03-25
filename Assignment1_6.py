print("program which accept number from user and check whether that number is positive or negative or zero")
print("\n")

def Check(no):
	if no>0:
		print("it is positive number")
	elif no==0:
		print("it is zero")
	else:
		print("it is negative number")

no=int(input("Enter Number->"))
Check(no)