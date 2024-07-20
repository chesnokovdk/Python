from random import choice

def run_game():
    word: str = choice(['apple', 'secret', 'banana'])

    # username: str = input('What is your name? >> ')
    # print(f'Welcome to hangman, {username}!')

    #Setup
    guessed: str =''
    tries: int = 3

    while tries > 0:
        blanks: int = 0

        print('Word: ', end='')
        for char in word:
            if char in guessed:
                print(char, end='')
            else:
                print('_ ', end='')
                blanks+=1

        print() # Adds a blank line, nothing more

        if blanks == 0:
            print('You got it!')
            break

        guess: str = input('Enter a letter: ')

        guess = guess[0]  # homework - find bugs

        if guess in guessed:
            print(f'You already used: "{guess}". Please try with another letter!')
            continue

        guessed += guess

        if guess not in word:
            tries -=1
            print(f'Sorry, that was wrong...({tries} tries remainig)')

            if tries ==0:
                print('No more tries remaining...You loose :(')
                break

if __name__ == '__main__':
    run_game()