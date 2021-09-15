with open("sample.txt",'w') as tables:
	for i in range(2,13):
		for j in range(1,13):
			print("{1:>2} times {0} is {1} ".format(i,j,i*j),file=tables)

		print("_"*20, file=tables)