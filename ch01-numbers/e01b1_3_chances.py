import random


def guessing_game():

    chosen_number = random.randint(0, 100)

    for i in range(3):
        guess = int(input('Guess a number: '))
        if guess > chosen_number:
            print('Too High')
        elif guess < chosen_number:
            print('Too Low')
        else:
            print('Just Right')
            break

    if guess != chosen_number:
        print("You didn't guess in time")


if __name__ == '__main__':

    guessing_game()
