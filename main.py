import random

def guess(x):
    rand_num = random.randint(1, x)
    guess = 0
    while guess != rand_num:
        guess = int(input(f'Enter a number between 1 and {x}:'))
        if guess < rand_num:
            print(f'The guess is too low. Try again!')
        elif guess > rand_num:
            print(f'The guess is too high. Try again')

    print(f'Yay! We have guessed the number {rand_num} correctly') 

if __name__=="__main__": 
        guess(10)              