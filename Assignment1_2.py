print("\n")
#print("Write a program which contains one function named as ChkNum() which accept one parameter as number. If number is even then it should display “Even number” otherwise display “Odd number” on console.")

def ChkNum(No):
	if (No % 2 == 0):
		print(No,"is Even number")
	else:
		print(No,"is Odd number")

ChkNum(int(input("Enter Number->")))