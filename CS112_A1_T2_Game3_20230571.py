# File: CS112_A1_T2_3_20230571
# Purpose: Subtract a square game
# Author: Menna Allah Mohy ELDin Abdelsamia Mahmoud
# ID: 20230571
import math  # library that has a function calculates square root of a number and checks if it is integer
import random  # library that has a function that choose a random number of coins


def square_number(num):
    square_root = math.sqrt(num)  # calculating the square root of the number
    return square_root.is_integer()  # if the number is integer then it is square number


def random_coin(num):
    num = random.randint(100, 500)
    while square_number(num):
        num = random.randint(100, 500)
    return num


#function to produce an error message if the user enters string
def no_string(num):
    while True:
        try:
            num = int(num)
            return num
        except ValueError:
            num = input("Please enter a valid number: ")
            continue


def main():  # welcome message and display status
    print("Welcome to Subtract a square game!")
    # aking user how he wants to play
    menu = no_string(input("Choose\n1) to play with a random number of coins \n2) to enter a number\n"))
    while menu not in [1, 2]:  # making sure user enters a valid option
        menu = no_string(input("please choose a valid option (1/2)"))
    if menu == 1:  # wants a random number
        CoinNum = random_coin(menu)
    else:
        CoinNum = no_string(input("Please enter a starting number: "))
    # making sure the starting number is not square number to start the game
    while square_number(CoinNum):
        CoinNum=no_string(input("Please select a non square number: "))
    # making sure the starting number>0 to start the game
    while CoinNum <= 0:
        CoinNum = no_string(input("Please enter a positive number: "))
    print("number of coins is: ", CoinNum)
    while CoinNum > 0:  # game starting
     move = no_string(input("Player 1: Please select a positive square number of coins: "))
     while True:
        if move <= 0:
            move = no_string(input("Please select a positive square number of coins: "))
            continue
        elif move > CoinNum:
            move = no_string(input("please select an equal or smaller number: "))
            continue
        # verification that the number is square number "recalling the function"
        elif not square_number(move):
            move = no_string(input("This is not a square number, please enter a square number: "))
            continue
        else:
            break
     CoinNum = CoinNum - move
     print ("Now we have", CoinNum, "coins")
     if CoinNum == 0:  # who reach 0 first wins
        print("Player 1 is WINNER!")
        break
     #player 2 turn
     move = no_string(input("Player 2: Please select a positive square number of coins:  "))
     while True:
        if move <= 0:
            move = no_string(input("Please select a positive square number of coins: "))
            continue
        elif move > CoinNum:
            move = no_string(input("please select an equal or smaller number: "))
            continue
            # verification that the number is square number "recalling the function"
        elif not square_number(move):
            move = no_string(input("This is not a square number, please enter a square number: "))
            continue
        else:
            break

     CoinNum = CoinNum - move
     print("Now we have", CoinNum, "coins")
     if CoinNum == 0:
        print("Player 2 is WINNER!")
        break


main()