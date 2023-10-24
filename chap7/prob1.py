import random

def display_instruct():
    print("Here are the insturctions to the Tic-Tac_Toe game:\n")
    print("\tWelcome to the greatest intellectual challenge of all time: Tic-Tac_Toe.")
    print("\tThis will be a showdown between your human brain and my silicon processor.\n")
    print("\tYou will make yout move known by entering a number, 0 - 8. The number will be correspond to the board position as illustrated:")
    print("\t\t\t\t\t0 | 1 | 2")
    print("\t\t\t\t\t---------")
    print("\t\t\t\t\t3 | 4 | 5")
    print("\t\t\t\t\t---------")
    print("\t\t\t\t\t6 | 7 | 8")
    print("\tPrepare youself, human, The ultimate battle is about to begin.\n")
    print("Here they are again:")
    print("You probably understand the game by now.")

def print_board(board):
  print(board[0], "|", board[1], "|", board[2])
  print("---------")
  print(board[3], "|", board[4], "|", board[5])
  print("---------")
  print(board[6], "|", board[7], "|", board[8])

def user_input(board):
  n = input("Where will you move? (0 - 8):")

  if (n not in "0 1 2 3 4 5 6 7 8".split()):
      print("Not in range.")
    
      n = user_input(board)

  return int(n)

def board_update(board, index, letter):
  board[index] = letter

def blank(board, index):
  return board[index] == ' '

def board_copy(board):
  list = []
  for i in board:
      list.append(i)
  return list

def computer_choose(board):

  for i in range(0, 8):

      copy = board_copy(board)

      if blank(copy, i):
          board_update(copy, i, 'O')
          if Judgment(copy, 'O'):
              return i

  for i in range(0, 8):

      copy = board_copy(board)

      if blank(copy, i):
          board_update(copy, i, 'X')
          if Judgment(copy, 'X'):
              return i

  point = Computer_Choose_Random(board, [0, 2, 6, 8])

  if point != None:

      return point

  elif board[4] == ' ':

      return 4

  return Computer_Choose_Random(board, [1, 3, 5, 7])

def Computer_Choose_Random(board, info):

  list = []

  for i in info:
      if blank(board, i):
          list.append(i)

  if len(list) > 0:
      return random.choice(list)
  else:
      return None
    
def Judgment(board, letter):

  return ((board[0] == board[1] == board[2] == letter) or
          (board[3] == board[4] == board[5] == letter) or
          (board[6] == board[7] == board[8] == letter) or
          (board[0] == board[3] == board[6] == letter) or
          (board[1] == board[4] == board[7] == letter) or
          (board[2] == board[5] == board[8] == letter) or
          (board[0] == board[4] == board[8] == letter) or
          (board[2] == board[4] == board[6] == letter))


display_instruct()

start = input("Do you require the first move? (y/n):")

# trun = 0 : human first / turn = 1 : computer first
if start == 'y':
  turn = 0
else:
  turn = 1

i = 0
board = [' '] * 10

while i < 10:

    print_board(board)

    board_update(board, user_input(board), 'X')

    if Judgment(board, 'X'):
        print("Player Win")
        break

    i += 1

    if i == 9:
        print_board(board)
        print("Game Tie!")
        break

    board_update(board, computer_choose(board), 'O')

    if Judgment(board, 'O'):
        print_board(board)
        print("Computer Win")
        break

    i += 1