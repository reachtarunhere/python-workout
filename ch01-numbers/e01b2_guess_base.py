import random


def guessing_game():

    random_base = random.randint(2, 16)
    chosen_number = random.randint(0, 100)

    while True:
        guess = int(input(f'Guess a number in base {random_base}: '),
                    base=random_base)
        if guess > chosen_number:
            print('Too High')
        elif guess < chosen_number:
            print('Too Low')
        else:
            print('Just Right')
            break


if __name__ == '__main__':

    guessing_game()
