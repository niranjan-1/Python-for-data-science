available_exist = ["north","south","east","west"]
print("Avaialable Exits are {0},{1},{2},{3}".format(available_exist))
chosen_exit=""
while chosen_exit not in available_exist:
	chosen_exit= input("please choose a direction: ")
	if chosen_exit.casefold() == "quit":
		print("Game over")
		break

else:
	print("aren't you glad you got out of there")
print (input())