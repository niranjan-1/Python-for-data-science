shopping_list = ["milk","pasta","eggs","spam","bread","rice"]
item_to_find= "bread"
found_at= None


#	if shopping_list [i]==item_to_find:
#		found_at=index
#		break
if item_to_find in shopping_list:
	found_at = shopping_list.index(item_to_find)
	print("item found at position {}".format(found_at))
else:
	print("item not found")