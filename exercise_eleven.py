import random

def play_game():

    number = random.randrange(1, 1001)
	
    print('Guess the lucky number between 1 and 1000:')
	
    guess_count = 0

    while True:
        guess = int(input('Your guess: '))
        guess_count += 1

        if guess > number:
            print('Too high. Try again.')
        elif guess < number:
            print('Too low. Try again.')
        else:
            print('Congratulations. You guessed the number!')
			
            if guess_count <= 10:
                print('Either you know the secret or you got lucky!')
            else:
                print('You should be able to do better!')
            break

while True:

    play_game()
	
    again = input('Would you like to play again? (yes/no): ')
	
    if again.lower() != 'yes':
        break