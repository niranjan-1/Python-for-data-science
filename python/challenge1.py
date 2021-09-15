answer=5
print("guess the number")
guess=int(input())
if guess==answer:
    print("you got it first time")
else:
    if guess<answer:
        print("guess higher")
    else:
        print("guess lower")
    guess=int (input())
    if guess== answer:
        print("you got it first time")
    else:
        print("sorry, you guessed it wrong")
    
print(input("press any key to exit"))
