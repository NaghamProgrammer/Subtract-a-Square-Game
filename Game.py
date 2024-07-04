# File: CS112_A1_T2_3_20231189.py
# Purpose: subtract a square game where two players take turns on subtracting a square number from the total number of coins and the one who reaches zero first wins
# Author: Nagham Wael Mohamed Elsayed
# ID: 20231189


# making sure the number of moves is a square number
import math
def square_check(move) :
    # handle negative input
    if move < 0 :
        return False
    # find the square root of the number
    sqrt_move = math.sqrt(move)
    # if the square root of the number is an integer this means the number is a perfect square
    if sqrt_move.is_integer():
        return True
    else :
        return False


# show a menu to the user to select gameplay style
print("welcome to subtract a square game!")
print('please choose gameplay style by entering 1 or 2 : ')
print('1) auto beginning number')
print('2) choose my own beginning number')
style = int(input("enter your option here: "))


try :
        # option 1 : auto beginning number
        if style == 1 :
            from random import randint
            # generate a random number of coins for the user to begin with
            num_coin = randint(10,1000)
            print("number of coins is: " , num_coin )
            #the game is going on as long as no player has reached zero
            while num_coin > 0 :
                # player 1 turn
                num_move = int(input('player 1: please take a non zero square number of coins: '))
                # if the user entered a number that isn't square or is greater than total number of coins or zero ask them to enter another number
                if square_check(num_move) == False or num_move > num_coin or num_move == 0 :
                    print("player 1: please enter a non zero square number that is less than the total number of coins")
                    continue
                # else the user entered a valid square number from the beginning
                else :
                     num_coin -= num_move
                     # display the new total of coins by subtracting moves from the total of coins
                     print("now we have ", num_coin ," number of coins")
                     # who reaches zero first wins and declare the winner
                     if num_coin <= 0 :
                         print("player 1 won")
                         break
                # player 2 turn
                num_move = int(input('player 2: please take a non zero square number of coins: '))
                # if the user entered a number that isn't square or is greater than total number of coins or zero ask them to enter another number
                if square_check(num_move) == False or num_move > num_coin or num_move == 0 :
                       # loop until the user enters a valid input
                       while square_check(num_move) == False or num_move > num_coin or num_move == 0 :
                           print("player 2: please enter a non zero square number that is less than the total number of coins")
                           num_move = int(input('player 2: please take a square number of coins: '))
                           # after the user enters a valid input display the new total of coins by subtracting moves from the total of coins
                           num_coin -= num_move
                           print("now we have ", num_coin, " number of coins")
                           # who reaches zero first wins and declare the winner
                           if num_coin <= 0:
                               print("player 2 won ")
                               break
                # else the user entered a valid square number from the beginning
                else :
                     num_coin -= num_move
                     print("now we have ", num_coin ," number of coins")
                     if num_coin <= 0 :
                         print("player 2 won")
                         break


       # option 2 : user input beginning number
       # same as in style 1 but replace the random generating of numbers with user input
        elif style == 2 :
            # ask the user to input the number of coins they want to begin with
            num_coin = int(input('please choose number of coins: '))
            print("number of coins is: " , num_coin )
            # the game is going on as long as no player has reached zero
            while num_coin > 0 :
                # player 1 turn
                # same comments and concepts as in style 1
                num_move = int(input('player 1: please take a non zero square number of coins: '))
                if square_check(num_move) == False or num_move > num_coin or num_move == 0 :
                       print("player 1: please enter a non zero square number that is less than the total number of coins")
                       continue
                else :
                     num_coin -= num_move
                     print("now we have ", num_coin ," number of coins")
                     if num_coin <= 0 :
                         print("player 1 won ")
                         break
                # player 2 turn
                # same comments and concepts as in style 1
                num_move = int(input('player 2: please take a non zero square number of coins: '))
                if square_check(num_move) == False or num_move > num_coin or num_move == 0  :
                       while square_check(num_move) == False or num_move > num_coin or num_move == 0 :
                           print("player 2: please enter a non zero square number that is less than the total number of coins")
                           num_move = int(input('player 2: please take a non zero square number of coins: '))
                           num_coin -= num_move
                           print("now we have ", num_coin, " number of coins")
                           if num_coin <= 0:
                               print("player 2 won ")
                               break
                else :
                       num_coin -= num_move
                       print("now we have ", num_coin ," number of coins")
                       if num_coin <= 0 :
                           print("player 2 won ")
                           break


        # in case the user entered an invalid choice for the gameplay style ( any input except for 1 or 2 )
        else :
            print("please enter 1 or 2 only")
# in case the user entered a float or a string
except ValueError :
    print("please enter a valid number")
    while ValueError :
        num_move = int(input('player 1: please take a non zero square number of coins: '))
        if square_check(num_move) == False or num_move > num_coin or num_move == 0:
            print("player 1: please enter a non zero square number that is less than the total number of coins")
            continue
        else:
            num_coin -= num_move
            print("now we have ", num_coin, " number of coins")
            if num_coin <= 0:
                print("player 1 won ")
                break
        num_move = int(input('player 2: please take a non zero square number of coins: '))
        if square_check(num_move) == False or num_move > num_coin or num_move == 0:
            while square_check(num_move) == False or num_move > num_coin or num_move == 0:
                print("player 2: please enter a non zero square number that is less than the total number of coins")
                num_move = int(input('player 2: please take a non zero square number of coins: '))
                num_coin -= num_move
                print("now we have ", num_coin, " number of coins")
                if num_coin <= 0:
                    print("player 2 won ")
                    break
        else:
            num_coin -= num_move
            print("now we have ", num_coin, " number of coins")
            if num_coin <= 0:
                print("player 2 won ")
                break
