# GuessNo.

"""write a program to guess a no. in 9 chances only
"""
num = 25   #let your target number be 25
print("Hello User\n"+"-----Welcome to Guessing Game-----")
print("you have only 9 chances to guess the number")
guess = 1

for guess in range(1,10):
    n = int(input())
    if n>25:
        print("Your number is higher than the target no.,TRY AGAIN!!\n"+"HINT: try something below")
    elif n<25:
        print("Your number  is lower than the target no.,TRY AGAIN!!\n"+"HINT: try something above")
    else:
        print("you rocks dude in ",guess,"no of guesses")
        break
    print(9-guess,"guess left")

print("GAME OVER .....")






























