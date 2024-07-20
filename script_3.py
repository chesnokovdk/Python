import random


# def roll_dice(amount: int = 2, sum1: int = 0) -> list[int]:
def roll_dice(amount: int = 2, sum1: int = 0):
    if amount <= 0:
        raise ValueError
    sum1 = 0
    rolls: list[int] = []
    for i in range(amount):
        random_roll:int = random.randint(1, 6)
        rolls.append(random_roll)
        sum1 += random_roll

    return rolls, sum1

def main():
    while True:
        try:
            user_input: str = input('How many dice would you like to roll? ')

            if user_input.lower() == 'exit':
                print('Thanks for playing')
                break
            sum = 0
            print(*roll_dice(int(user_input)), sep=', ')
            l, s = roll_dice(int(user_input),sum)
            print(*l, sep=', ')
            print('Total = ', s)
        except ValueError:
            print('Please enter a valid number!')

if __name__ == '__main__':
    main()