import random
def main():

    games = int(input("How many games do you want to play?\n"))
    for i in range(1,games+1):
      user = 1
      bot = 1
      print("Game",i,"of",games)
      while user == bot:
        bot = random.randint(1,3)
        user = input('Enter rock, paper, or scissors\n')
        print()
        if bot == 1 and user == 'paper':
          print('You win!')
        elif bot == 1 and user == 'scissors':
          print('Computer wins!')
        elif bot == 2 and user == 'rock':
          print('Computer wins!')
        elif bot == 2 and user == 'scissors':
          print('You win!')
        elif bot == 3 and user == 'rock':
          print('You win!')
        elif bot == 3 and user == 'paper':
          print('Computer wins!')
        elif bot == 1 and user == 'rock':
          user = 1
          bot = 1
          print('You both chose rock!')
          print()
        elif bot == 2 and user == 'paper':
          user = 1
          bot = 1
          print('You both chose paper!')
          print()
        else:
          user = 1
          bot = 1
          print('You both chose scissors!')
          print()
      if bot == 1:
        print('Computer chose rock.')
      elif bot == 2:
        print('Computer chose paper.')
      else:
        print('Computer chose Scissors.')
      print()
      print('------------------------------------------')
    print('All done.')
main()
