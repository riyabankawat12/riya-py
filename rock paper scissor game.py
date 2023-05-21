import random
options=["R","P","S"]
user_choic= input("R for rock, P for paper, S for scissors")
computer_choic= random.choice(options)
if user_choic not in options:
    print ("invalid choice!")
if (user_choic==computer_choic):
    print("its a tie")
elif(user_choic=='R' and computer_choic=='S'):
    print("user win")
elif (user_choic=='R'and computer_choic=="P"):
    print("computer win")
elif (user_choic=="S" and computer_choic=="P"):
    print("user win")
elif (user_choic=="S" and computer_choic=="R"):
    print ("computer win")
elif (user_choic=="P" and computer_choic=="R"):
    print("user win")
elif (user_choic=="P" and computer_choic=="S"):
    print("computer won")
