from random import randint

num= randint(1,20)
print("Game starts!")
user_num =int(input("Guess the number:"))

i=1
count=0
while(i>0):
    if(user_num>num):
     print("Lower number please")
     user_num= int(input("Guess the number:"))
     count+=1

    elif(user_num<num):
        print("Higher number please")
        user_num= int(input("Guess the number:"))
        count+=1

    else:
        count+=1
        print("You have successfully guessed the number")
        break

    i+=1

print(f"Number of attempts taken to guess the number: {count}")
print("Game ended!")



