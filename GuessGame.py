import random
number = random.randint(1, 100)
guess = ""
count = 0
while guess != number and count != 7:
   guess = int(input("Guess the number: "))
   count += 1
   if guess == number:
       print("You did it! Congrats")
       print(f"You've guessed that in {count} guesses")
   elif count == 7:
       print("Game Over!")
   elif guess > number:
       print("Too high!")   
   elif guess < number:
       print("Too Low!")
