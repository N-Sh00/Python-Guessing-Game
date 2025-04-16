from random import randint

target_num = randint(1,100)
attempts = ""
print(target_num)
win = False

difficulty = input("SELECT THE DIFFICULTY:\nEASY\nMEDIUM\nHARD\n").lower()
if difficulty == "easy":
    attempts = 10
elif difficulty == "medium":
    attempts = 8
elif difficulty == "hard":
    attempts = 5

while win == False:
    player_guess = int(input(f"Guess a number between 1 to 100. you have {attempts} attempts left.\n"))

    if player_guess == target_num:
        print("Congrats! YOU WON!!!!")
        win = True
    elif player_guess > target_num:
        print("Too high")
        attempts -= 1
        print(f"You have {attempts} attempts left!")
    elif player_guess < target_num:
        print("Too low")
        attempts -= 1
        print(f"You have {attempts} attempts left!")

    if attempts == 0:
        print(f"THE CORRECT ANSEWR WAS {target_num}! YOU LOSE!")
        exit()
