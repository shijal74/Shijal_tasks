import random
print("\n1,paper='p',\n2,rock='r',\n3,scissor='s'")
def getu():
    ch = input("Enter your choice:").strip().lower()
    while ch not in ['r', 'p', 's']:
        ch = input("Invalid choice. Enter again:").strip().lower()
    return ch
def getc():
    return random.choice(['r', 'p', 's'])
def de(user, com):
    if user == com:
        return "It is a tie!"
    elif (user == 'r' and com == 's') or (user == 's' and com == 'p') or (user == 'p' and com == 'r'):
        return "You win"
    else:
        return "Computer wins"
def run():
    while True:
        user = getu()
        com = getc()
        print("You chose:", user)
        print("Computer chose:", com)
        print(de(user, com))
        play_again = input("Do you want to play again? (y/n):").strip().lower()
        if play_again != 'y':
            print("Thank you")
            break
run()
