'''
1 for snake
-1 for water
0 for gun
'''
import random

computer=random.randint(-1,1)
youstr=input("Enter your choice:")
youDict={"snake":1, "water":-1, "gun":0}
you= youDict[youstr]
if(computer==-1):
    print("Computer's choice: Water")
elif(computer==0):
    print("Computer's choice: Gun")
else:
    print("Computer's choice: Snake")



if(computer==-1 and you==1):
    print("You won")
elif(computer==-1 and you==0):
    print("You lose")
elif(computer==-1 and you==-1):
    print("Again")
elif(computer==0 and you==1):
    print("You lose")
elif(computer==0 and you==-1):
    print("You won")
elif(computer==0 and you==0):
    print("Again")
elif(computer==-1 and you==1):
    print("You won")
elif(computer==-1 and you==0):
    print("You lose")
elif(computer==-1 and you==-1):
    print("Again")



