pangram= "The quick brown fox jumps over the lazy dog"
letter = sorted (pangram)
print(letter)


numbers= [2.3,4.5,8.7,3.1,9.2,1.6]
sorted_numbers= sorted(numbers)
print(sorted_numbers)
print(numbers)

numbers.sort()
print(numbers)

missing_letter= sorted("The quick brown fox jumps over the lazy dog")
print(missing_letter)


names=["graham",
"jhon",
"terry",
"eric",
"Terry",
"michale"]
names.sort(key = str.casefold)
print(names)