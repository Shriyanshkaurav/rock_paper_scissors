import random

user_score = 0
computer_score = 0

options = ["rock", "paper", "scissior"]

while True:
    input_user = input(" Type Rock/Paper/scissior or Q to Quit : ").lower()
    if input_user == 'q':
        break
    if input_user not in options:
        continue  
    
    random_number = random.randint(0,2)
    computer_pick = options[random_number] 
    print("Computer Pick ",computer_pick + ".")

    if input_user == "rock" and computer_pick == "scissior":
        print("You win!!")
        user_score += 1
            
    elif input_user == "paper" and computer_pick == "rock":
        print("You win!!")
        user_score += 1
        
    elif input_user == "scissior" and computer_pick == "paper":
        print("You win!!")
        user_score += 1
        
    else:
        print("You lost!!")
        computer_score+=1



print("You win ",user_score," times ")
print("computer wins ",computer_score," times ")    
print("Goodbye!")     