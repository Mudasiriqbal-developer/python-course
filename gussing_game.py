# python .\gussing_game.py

import random

def play_game():
   luky_num = random.randint(1, 50)

   while True:
      user_num = int(input("Guess the luck num: "))

      if user_num == luky_num:
        print("Congratulation You won. Game over!! ")
        break
      elif user_num < luky_num:
       print("Too low. ")
      else:
       print("Too high: ")


play_game()
