from random import randint, choice, uniform


def QuBa(user_input):
    """
    :param user_input: str, takes user's input
    :return: exit the program, or back to the menu.
    """
    if user_input == 'exit' or user_input == 'quit':
        print("Thanks. Have a good day!")
        exit()
    if user_input == 'back':
        print("OK.")
        return True


def StrawPicker():
    """
    Picks a random name from the list.
    """
    names_list = []
    print("Welcome to the straw picker. Start entering your names. Type 'done' once you're finished.")
    while True:
        names = input(f"Enter your name #{len(names_list)}: ")
        if QuBa(names):
            return
        if len(names) < 1:
            print("Enter name with more than 2 alphabets.")
            continue
        if names == 'done':
            break
        names_list.append(names)
    while True:
        print("The one with the shortest straw is.. " + choice(names_list) + "!")
        yn = input("Roll again? ").lower()
        if yn.startswith('y'):
            continue
        elif yn.startswith('n'):
            yn = input("Enter again? ")
            if yn.startswith('n') or QuBa(yn):
                print("OK. Bye!")
                return
            elif yn.startswith('y'):
                StrawPicker()


def NumberPick():
    """
    Pick a number program
    """
    hilo = 'lowest'
    num_list = []
    High = None
    while True:
        if len(num_list) == 2:
            break
        if High:
            hilo = 'highest'
        vanilla = f'Type in the {hilo} number: '
        nums = input(vanilla)
        if nums.isdigit():
            num_list.append(int(nums))
            High = True
        else:
            print('Enter only numbers.')
    print("The chosen number is... " + str(randint(min(num_list), max(num_list))) + "!")
    start = input("Start again? ").lower()
    if start.startswith('y'):
        NumberPick()
    elif start.startswith('n') or QuBa(start):
        return


def Coin():
    """
    Coin flipping program
    """
    coin = [0, 0, 0]
    print("Press enter to play! Check your score by typing 'score'. ")
    while True:
        coin_flip_val = round(uniform(0, 1), 2)
        ask = input().lower()
        if QuBa(ask):
            return
        if ask.startswith('score'):
            print(f"Heads: {coin[0]}, Tails: {coin[2]}, It's side: {coin[1]}")
        if coin_flip_val < 0.5:
            print('The coin landed on its head!')
            coin[0] += 1
        elif coin_flip_val > 0.5:
            print('The coin landed on its tails!')
            coin[2] += 1
        else:
            print('The coin landed on its side!')
            coin[1] += 1


def RPSf():
    """
    A Rock Paper Scissors program.
    """
    rps_dict = {'r': 0,
                'p': 1,
                's': 2}
    rps_list = ['Rock', 'Paper', 'Scissors']
    count = [0, 0, 0]  # index 0 is for our score, 1 for bot, 2 for draw.
    while True:
        computer = randint(0, 2)
        print(f"\nYour score: {count[0]}. Bot score: {count[1]} . Draw: {count[2]}")  # Prints the score
        user = input("Rock, Paper, Scissors, Go!: ").lower()
        if user not in 'rps' and user not in rps_list:
            if QuBa(user):
                return
            else:
                print("That is not a valid choice. Please try again: ")
                continue
        print(f"The bot chooses {rps_list[computer]}!")
        if (rps_dict[user] + 1) == computer or (computer == 0 and rps_dict[user] == 2):
            print('You lose!')
            count[1] += 1
        elif rps_dict[user] == computer:
            print('Draw')
            count[2] += 1
        else:
            print('You win!')
            count[0] += 1
