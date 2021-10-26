from back import *

# Menu
peek = ['a', 'b', 'c', 'd']

print(
    "Welcome to almighty bot of Sarah's! This time, we are experimenting with random picker tools.\nChoose which random picker tool you want to pick.")
while True:
    picker = input("\n(A) Straw picker\n(B) Random number picker\n(C) Coin flipper\n(D) Rock paper scissors\n").lower()
    if picker == 'a':
        StrawPicker()
    if picker == 'b':
        NumberPick()
    if picker == 'c':
        Coin()
    if picker == 'd':
        RPSf()
    if QuBa(picker):
        print("Thanks. Have a good day!")
    if picker not in peek:
        print('Please enter with only A, B, C, D')
