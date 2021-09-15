sampleText='python is a powerful language'
vowels= frozenset("aeiou")
finalset= set(sampleText).difference(vowels)
print(finalset)

finalList= sorted(finalset)
print(finalList)