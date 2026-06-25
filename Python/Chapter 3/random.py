import random
computer = random.choice([-1,0,1])
you = int (input("Enter -1 for rock, 0 for paper, 1 for scissors: "))

if computer==you:
  print("It's a tie")
else:
    if(computer ==-1 and you ==1):
       print("You win")  

    elif(computer ==-1 and you ==0):
       print("You lose")

    elif(computer ==1 and you ==-1):
       print("You lose")

    elif(computer ==1 and you ==0):
       print("you win")

    elif(computer ==0 and you==1):
       print("You lose")

    elif(computer ==0 and you ==-1):
       print("You win")