import random
from random_word import RandomWords

print('''
      Enter 1 for single player mode.
      Enter 2 for double player mode.
''')
n= int(input("Enter your choice:"))

try:
    if n==1:

        def get_random_word(min_length, max_length):
         while True:
          word = r.get_random_word()
          if word and min_length <= len(word) <= max_length:
            return word

        r= RandomWords()
        random_word= get_random_word(4,6)
        print("Game starts!\nGuess the word. You have 10 attempts.")
        print(f"Length of the word: {len(random_word)}")
        count=0
        for i in range(10):
            guess= input("Enter your guessed letter:")
            j=0
            for letter in random_word:
                j=j+1
                if guess==letter:
                    print(f"Correct guess! The position of letter in the word is {j}")
                    count=count+1
                    break
            else:
                print("Wrong choice!")

            if count==len(random_word):
                print("Congratulations,You Won!")
                print(f"The word was:{random_word}")
                break
        
        else:
            print("Bad Luck,You Lost!")
            print(f"The word was:{random_word}")

    elif n==2:
        word= input("Player 1 please enter a word:")
        print("Game starts!\nPlayer 2 guess the word. You have 10 attempts.")
        print(f"Length of the word: {len(word)}")
        count=0
        for i in range(10):
            guess= input("Enter your guessed letter:")
            j=0
            for letter in word:
                j=j+1
                if guess==letter:
                    print(f"Correct guess! The position of letter in the word is {j}")
                    count=count+1
                    break
            else:
                print("Wrong choice!")

            if count==len(word):
                print("Congratulations,Player 2 Won!")
                print(f"The word was:{word}")
                break
        
        else:
            print("Congratulations,Player 1 Won!")
            print(f"The word was:{word}")

    else:
        print("Invalid choice.Try again!")

except ValueError as v:
    print(v)
                





