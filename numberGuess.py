# Number Guess Mini Project
import random

lowest_number = 1 
highest_number = 100 
answer = random.randint(lowest_number,highest_number)
guesses = 0
is_running = True

print("Python Guessing Game : ")
print(f"select a number between {lowest_number} and {highest_number}")


while is_running :
   guess = input("enter your Guess :") 
   if guess.isdigit():
       guess = int(guess)
       guesses = guesses + 1
       
       if guess < lowest_number or guess > highest_number:
          print("That number is out of range ") 
          print("please select a number between {lowest_number} and {highest_number}")
       elif guess < answer:
            print("Too Low .... Try Again ")
       elif guess > answer:
           print("Too high .... Try Again ")
       else:
           print(f"correct The answer was {answer}")
           print(f"Number of guesses: {guesses}")
           is_running = False
   else :
       print("invalid Guess")
       print(f"please select a number between {lowest_number} and {highest_number}")
