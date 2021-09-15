# farm_animals={"sheep","cow","hen"}
# print(farm_animals)
# for animal in farm_animals:
# 	print(animal)

# print("="*80)
# wild_animal=set(['lion','tiger','panther','elephant','hare'])
# print(wild_animal)

# for animal in wild_animal:
# 	print(animal)

# farm_animals.add('horse')
# wild_animal.add('horse')
# print(farm_animals)
# print(wild_animal)

empty_set= set()
empty_set_2= {}
empty_set.add("a")
#empty_set_2.add("a")


# even= set(range(0,40,2))
# print(even)
# square_tuple =(4,6,9,16,25)
# squares= set(square_tuple)
# print(sorted(squares))
# even =set(range(0,40,2))
# print(sorted(even))
# print(len(even))

# square_tuple =(4,6,9,16,25)
# squares= set(square_tuple)
# print(squares)
# print(len(squares))

# print(even.union(squares))
# print(len(even.union(squares)))

# print(squares.union(even))

# print("-"*80)
# print(even.intersection(squares))
# print(even &  squares)
# print(squares.intersection(even))
# print(squares & even)


# even =set(range(0,40,2))
# print(sorted(even))
# square_tuple=(4,6,9,16,25)
# print(sorted(square_tuple))

# print('even minus squares')
# print(sorted(even.difference(square_tuple)))
# #print(sorted(even-square_tuple))
# print('squares minus even')
# # print(square_tuple.difference(even))
# #print(square_tuple - even)
# print("="*80)

# print(sorted(even))
# print(square_tuple)
# even.difference_update(square_tuple)
# print(sorted(even))

# even =set(range(0,40,2))
# print(sorted(even))
# square_tuple=(4,6,9,16,25)
# squares = set(square_tuple)
# print(squares)

# print('symmetric even minus squares')
# print((even.symmetric_difference(squares)))

# print('symmetric squares minus even')
# print((squares.symmetric_difference(even)))

# squares.discard(4)
# squares.discard(16)
# squares.discard(8)
# print(squares)
# #squares.remove(8)

# try:
# 	squares.remove(8)
# except KeyError:
# 	print("The item 8 is not number of the set")

# even =set(range(0,40,2))
# print(sorted(even))
# square_tuple=(4,6,16)
# squares = set(square_tuple)
# print(squares)

# if squares.issubset(even):
# 	print("squares is subset of even")
# if even.issuperset(squares):
# 	print("even is superset of squares")

even = frozenset(range(0,100,2))
print(even)