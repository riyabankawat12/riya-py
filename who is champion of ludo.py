import random
while True:
    a=input("press enter to roll the dice")
    user_roll=random.randint(1,6)
    computer_roll=random.randint(1,6)
    print("you rolled",user_roll)
    print("computer roll",computer_roll)
    if (user_roll==6 or computer_roll==6):
        break
    if (user_roll==6 and computer_roll!=6):
        print("user won")
    elif(user_roll!=6 and computer_roll==6):
        print("computer won")
    elif(user_roll==6 and computer_roll==6):
        print ("its a tie")