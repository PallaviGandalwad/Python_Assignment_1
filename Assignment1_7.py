print("\n")

def Check(No):

	if((No % 5)==0):
		return True 
	else:
		return False


 
No=int(input("Enter Number->"))
if(Check(No) == True):
	print(True)
else:
	print(False)