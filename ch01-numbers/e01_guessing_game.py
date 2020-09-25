import random


def guessing_game():

    chosen_number = random.randint(0, 100)

    for i in range(3):
        guess = int(input('Guess a number: '))
        if guess > chosen_number:
            print(f'Your guess of {guess} is too high!')
        elif guess < chosen_number:
            print(f'Your guess of {guess} is too low!')
        else:
            print(f'Right!  The answer is {guess}')
            break


if __name__ == '__main__':

    guessing_game()
