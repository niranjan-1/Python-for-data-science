name= input("please enter the name:")
age = int(input ("HOW OLD ARE YOU,{0} ?".format(name)))
print (age)

#if age >= 18:
#	print("You are old enough to vote")
##else:
#	print("please come back in {0} years".format(18-age))
if age<18:
	print("please come back in {} years".format(18-age))
elif age >= 125:
	print("sorry yoda, you die in return of the jedi")
else:
	print("you are old enough to vote")
	print("please put an X in the box :")

print(input("enter some key to exit"))