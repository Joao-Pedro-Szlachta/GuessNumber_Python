# Guess Number
# It generate a random value and the user will try to guess the number

import random


class GuessNumber:

  def __init__(self):
    self.random_value = 0
    self.min_value = 1
    self.max_value = 100
    self.try_again = True

  def iniciate(self):
    self.genRandomNumber()
    self.askRandomValue()

    while (self.try_again is True):
      if (int(self.guess_value) > self.random_value):
        print('Guess lower')
        self.askRandomValue()
      elif (int(self.guess_value) < self.random_value):
        print('Guess higher')
        self.askRandomValue()
      else:
        self.try_again = False
        print('CONGRATULATION, YOU GUESSED IT')

  def askRandomValue(self):
    self.guess_value = input('Guess the number: ')

  def genRandomNumber(self):
    self.random_value = random.randint(self.min_value, self.max_value)


guessNumber = GuessNumber()
guessNumber.iniciate()
