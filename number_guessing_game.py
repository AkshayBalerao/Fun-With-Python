import random

def number_guessing_game():
    number_to_guess = random.randint(1, 50)
    attempts = 0
    last_guess = None

    print("Welcome to the Number Guessing Game!")
    print("I have selected a number between 1 and 50. Can you guess what it is?")

    while True:
        guess = int(input("Enter your guess: "))
        attempts += 1

        if guess < number_to_guess:
            if number_to_guess - guess <= 2:
                print("A bit low! You're very close.")
            elif number_to_guess - guess <= 5:
                print("Low! You're close.")
            else:
                print("Too low! Try again.")
        elif guess > number_to_guess:
            if guess - number_to_guess <= 2:
                print("A bit high! You're very close.")
            elif guess - number_to_guess <= 5:
                print("High! You're close.")
            else:
                print("Too high! Try again.")
        else:
            print(f"Congratulations! You guessed the correct number {number_to_guess} in {attempts} attempts.")
            break

        if last_guess is not None:
            if abs(number_to_guess - guess) < abs(number_to_guess - last_guess):
                print("HINT: Your guess is nearer to the target than your last guess. Great improvement!")
            else:
                print("HINT: Your guess is farther from the target than your last guess. Try to get closer.")
                
        last_guess = guess 
    print("\n")
    if attempts==1:
        print("**** Amazing! You guessed it on your first try! ****")
    elif(attempts in range(2,5)):
        print("**** Well done! You figured it out in a few tries ****")
    elif(attempts in range(5,8)):
        print("**** Nice work! You got it in a good number of attempts ****")
    else:
        print("**** Excellent persistence! You kept trying and got it! ****")
    print("\n")
if __name__ == "__main__":
    number_guessing_game()