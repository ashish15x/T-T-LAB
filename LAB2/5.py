import random
def select_random_number(lower_limit, upper_limit):
    return random.randint(lower_limit, upper_limit)
def play_game():
    ready=int(input("Enter 1 if you want to play 0 to exit : "))
    if(ready ==0):
        {
            exit()
        }
    lower_limit = int(input("Enter lower limit: "))
    upper_limit = int(input("Enter upper limit: "))
    random_number = select_random_number(lower_limit, upper_limit)
    chances = int(input("Enter number of chances "))
    while chances > 0:
        user_guess = int(input("Enter your guess: "))
        if user_guess == random_number:
            print("You guessed the right number.")
            break
        elif user_guess > random_number:
            print("Too high.")
        else:
            print("Too low.")
        chances -= 1
        if chances == 0:
            print("Sorry, you ran out of chances. The correct number was: ", random_number)
while True:
    print("\nNew Game:")
    play_game()
    