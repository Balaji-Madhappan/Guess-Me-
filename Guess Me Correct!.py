#This is a guess the number game.
import random
from playsound import playsound

guessesTaken = 0

print('Hello! What is your name?')
myName = input()
number = random.randint(2,45)
print('Well, ' + myName + ', I am thinking of a number between 2 and 45.')
while guessesTaken < 5:

     print('Take a guess.') # There are four spaces in front of print.

     guess = input()

     guess = int(guess)
     guessesTaken = guessesTaken + 1
     
     if guess < number:

         print('Your guess is too low.') # There are eight spaces in front of print.



     if guess > number:

         print('Your guess is too high.')

     if guess == number:

        break

if guess == number:

      guessesTaken = str(guessesTaken)

      print('Good job, ' + myName + '! You guessed my number in ' + guessesTaken + ' guesses!')
      playsound("reveille-sound-effect.mp3")

if guess != number:

      number = str(number)
      print('Nope. The number I was thinking of was ' + number)
      playsound("wine-glass-breaking-sound-effect.mp3")
      
