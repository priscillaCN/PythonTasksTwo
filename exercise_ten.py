import random

def play_game():

    number = random.randrange(1, 1001)
	
    print('Guess the lucky number between 1 and 1000:')

    while True:
        guess = int(input('Your guess: '))

        if guess > number:
            print('Too high. Try again.')
        elif guess < number:
            print('Too low. Try again.')
        else:
            print('Congratulations. You guessed the number!')
            break


while True:
    play_game()
	
    again = input('Would you like to play again? (yes/no): ')
	
    if again.lower() != 'yes':
        break