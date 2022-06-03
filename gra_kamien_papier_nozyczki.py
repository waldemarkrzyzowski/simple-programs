# import necessary library
import random
import time


# enter number of games and defines variables    
amount = int(input("How many times do you want to play? "))
computer_points = 0
user_points = 0

# loop for executes amount times, user and computer choose an item
for i in range(amount):
    print("Round nr; ", i+1)
    user_choice = input("Stone paper scissors: ")
    possible_choices = ['stone','paper','scissors']
    computer_choice = random.choice(possible_choices)

    print("User choose: ",user_choice,"Computer choose: ",computer_choice)

    # check potentian combinations and add points  
    if user_choice == computer_choice:
        print("Tt's a draw, user and computer  ", user_choice," ")
    elif user_choice =="stone":
        if computer_choice =="paper":
            print("Computer win")
            computer_points+=1
        else:
            print("User win")
            user_points+=1
    elif user_choice =="paper":
        if computer_choice =="scissors":
            print("Computer win")
            computer_points+=1
        else:
            print("User win")
            user_points+=1
    elif user_choice =="scissors":
        if computer_choice =="stone":
            print("Computer win")
            computer_points+=1
        else:
            print("User win")
            user_points+=1
    time.sleep(3)
    
# Summary computer and user points and print the winner of the competition
print("Summary")
print("Computer got ",computer_points," points.")
print("User got ",user_points," points.")
if computer_points > user_points:
    print("Computer won!")
elif computer_points < user_points:
    print("User won!")
else:
    print("It's a draw!")
