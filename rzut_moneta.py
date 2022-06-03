# impor necessary lirary
import random
import time

# define variables
user = 0
computer = 0
attempt = 0

print("Welcome in the game orzel or reszka!")
print(" o - orzel")
print(" r - reszka")
print(" 0 - exit")


while True:
    # user choose orzel or reszka
    x = input("Orzel or reszka? ")

    
    if x =="0": break
    elif x=="o": x="orzel"
    elif x=="r": x="reszka"
    else:
        print("Please choose orzel or reszka!")
        print(" o - orzel")
        print(" r - reszka")
        print(" 0 - koniec")

        continue

    y = random.choice(["orzel","reszka"])
    
    # loop for countdown time
    for i in range (0,3):
        print(3-i)
        time.sleep(1)

    # return a result and add point for user or computer
    print("The result of following attempt: ", y)

    if x == y:
        user += 1
    else:
        computer += 1

    attempt += 1

    # Summary after following attempt
    print("Result after " , attempt," attempts.")
    print("User: ", user)
    print("Computer: ", computer)

print("After ", attempt, " attempts there are following results: ")
print("User: ", user)
print("Computer: ", computer)
