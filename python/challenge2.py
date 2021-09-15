print("please choose an option from below:")
print("1:\tlearn python")
print("2:\tgo swimming")
print("3:\tlearn java")
print("4:\thave dinner")
print("5:\tgo to bed")
print("0:\texit")

while True:
	choice=input()

	if choice=="0":
		break
	elif choice in "12345":
		print("you chose {}".format(choice))
	else:
		print("please choose an option from below:")
		print("1:\tlearn python")
		print("2:\tgo swimming")
		print("3:\tlearn java")
		print("4:\thave dinner")
		print("5:\tgo to bed")
		print("0:\texit")
