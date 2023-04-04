import random
from time import sleep
from art import *
import os

score = 0


def error(error):
  os.system("clear")
  print(error, "Restarting")
  sleep(2)
  os.system("python main.py")


def ded(board1, board2, board3, board4, board5):
  os.system("clear")
  print_board(board1, board2, board3, board4, board5)
  sleep(2)
  os.system("clear")
  os.system("python main.py")


def tutorial():
  tutext = "1. Type in a letter and a number to choose where your player will be placed. Zero is an empty space. After you choose your coordinates bombs will be dropped at random coordinates and you have to hope you dont get hit. Try to get as many points as possible. The player is the number one and the bombs is two."

  index = 0

  for x in range(0, len(tutext)):
    index += 1
    os.system("clear")
    print(tutext[:index])
    sleep(0.05)


def main():
  os.system("clear")
  tprint("bomb game", font="small")
  print("1:   START")
  print("2: How to play")
  print("\n")

  i = input()

  os.system("clear")
  if i == "1":
    start_game()
  elif i == "2":
    tutorial()


def print_board(board1, board2, board3, board4, board5):
  print("    1  2  3  4  5")
  print("a ", board1)
  print("b ", board2)
  print("c ", board3)
  print("d ", board4)
  print("e ", board5)


def start_game():
  score = 0
  os.system("clear")

  letters = ["a", "b", "c", "d", "e"]

  died = False

  while died == False:
    os.system("clear")

    board1 = [0, 0, 0, 0, 0]
    board2 = [0, 0, 0, 0, 0]
    board3 = [0, 0, 0, 0, 0]
    board4 = [0, 0, 0, 0, 0]
    board5 = [0, 0, 0, 0, 0]

    print_board(board1, board2, board3, board4, board5)

    print("\n")
    print("Pick a letter and a number")
    print("\n")

    i = input()

    os.system("clear")
    if int(i[-1]) > 5:
      error("Invalid coordinate")
    if i[0] == "a":
      board1[int(i[-1]) - 1] = 1
      print_board(board1, board2, board3, board4, board5)
    elif i[0] == "b":
      board2[int(i[-1]) - 1] = 1
      print_board(board1, board2, board3, board4, board5)
    elif i[0] == "c":
      board3[int(i[-1]) - 1] = 1
      print_board(board1, board2, board3, board4, board5)
    elif i[0] == "d":
      board4[int(i[-1]) - 1] = 1
      print_board(board1, board2, board3, board4, board5)
    elif i[0] == "e":
      board5[int(i[-1]) - 1] = 1
      print_board(board1, board2, board3, board4, board5)
    else:
      error("Invalid coordinate")

    print("\n")
    print("Bombs incoming")
    print("\n")

    sleep(2)

    os.system("clear")

    for x in range(0, 2):
      randlet = random.choice(letters)
      randnum = random.randint(1, 5)

      if randlet == "a":
        if board1[randnum - 1] == 1:
          died = True
          board1[randnum - 1] = 2
        else:
          board1[randnum - 1] = 2
      elif randlet == "b":
        if board2[randnum - 1] == 1:
          died = True
          board2[randnum - 1] = 2
        else:
          board2[randnum - 1] = 2
      elif randlet == "c":
        if board3[randnum - 1] == 1:
          died = True
          board3[randnum - 1] = 2
        else:
          board3[randnum - 1] = 2
      elif randlet == "d":
        if board4[randnum - 1] == 1:
          died = True
          board4[randnum - 1] = 2
        else:
          board4[randnum - 1] = 2
      elif randlet == "e":
        if board5[randnum - 1] == 1:
          died = True
          board5[randnum - 1] = 2
        else:
          board5[randnum - 1] = 2
      if died == True:
        ded(board1, board2, board3, board4, board5)
        break

    score += 1

    os.system("clear")

    print_board(board1, board2, board3, board4, board5)
    print("\n")
    print("You Survived!")
    print("+1 Score")
    print("Total: ", score)
    print("\n")

    sleep(5)


main()