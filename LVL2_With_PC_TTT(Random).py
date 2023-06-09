# <---------------Includes--------------->
# P: PC vs PC
# Y: PC vs Human
# N: Human vs Human
# Q: Quit
# Uses Randomisation ---> __PC is BRAINLESS__

import os
import random
import time
xo = ['-', '-', '-', '-', '-', '-', '-', '-', '-']

def board():
    print(xo[0], '|', xo[1], '|', xo[2])
    print(xo[3], '|', xo[4], '|', xo[5])
    print(xo[6], '|', xo[7], '|', xo[8])


def CheckWin(checkChar):
    # rows
    if xo[0] == checkChar and xo[1] == checkChar and xo[2] == checkChar:
        return True
    if xo[3] == checkChar and xo[4] == checkChar and xo[5] == checkChar:
        return True
    if xo[6] == checkChar and xo[7] == checkChar and xo[8] == checkChar:
        return True
    # columns
    if xo[0] == checkChar and xo[3] == checkChar and xo[6] == checkChar:
        return True
    if xo[1] == checkChar and xo[4] == checkChar and xo[7] == checkChar:
        return True
    if xo[2] == checkChar and xo[5] == checkChar and xo[8] == checkChar:
        return True
    # diagonals
    if xo[0] == checkChar and xo[4] == checkChar and xo[8] == checkChar:
        return True
    if xo[2] == checkChar and xo[4] == checkChar and xo[6] == checkChar:
        return True
    return False

print("The Co-ordinate format is:")
print("0 | 1 | 2")
print("3 | 4 | 5")
print("6 | 7 | 8")

PCvsHMN = input("Q: Quit\nP: PC vs PC\nY: PC vs Human\nN: Human vs Human\n")

if(PCvsHMN == 'n' or PCvsHMN == 'N'):
    run = 'x'
    while (True):
        if run == 'x':
            player1 = int(input("Enter PlayerX Number:"))
            if player1<0 or player1>8:
                print("Invalid Position")
            elif xo[player1] == '-':
                xo[player1] = 'x'
                run = 'o'
                os.system("cls")
                if CheckWin('x'):
                    board()
                    print("Player1 wins!")
                    break
                elif '-' not in xo:
                    board()
                    print("Game Over!")
                    break
                else:
                    # sys.system("cls")
                    board()
        else:
            os.system("cls")
            board()
            print("Occupied position!")
           
        if run == 'o':
            player2 = int(input("Enter PlayerO Number:"))
            if player2>8 and player2<0:
                print("Invalid Position")
            elif xo[player2] == '-':
                xo[player2] = 'o'
                run = 'x'
                os.system("cls")
                if CheckWin('o'):
                    board()
                    print("Player2 wins!")
                    break
                elif '-' not in xo:
                    board()
                    print("Game Over!")
                    break
                else:
                    # sys.system("cls")
                    board()
        else:
            os.system("cls")
            board()
            print("Occupied position!")

elif(PCvsHMN == 'y' or PCvsHMN == 'Y'):
    PCturns = [0,1,2,3,4,5,6,7,8]
    run = 'x'
    while (True):
        if run == 'x':
            player1 = int(input("Enter PlayerX Number:"))
            if player1<0 or player1>8:
                    print("Invalid Position")
            elif xo[player1] == '-':
                PCturns.remove(player1)
                xo[player1] = 'x'
                run = 'o'
                os.system("cls")
                if CheckWin('x'):
                    board()
                    print("Player1 wins!")
                    break
                elif '-' not in xo:
                    board()
                    print("Game Over!")
                    break
                else:
                    # sys.system("cls")
                    board()
        else:
            os.system("cls")
            board()
            print("Occupied position!") 

        if run == 'o':
            player2 = random.choice(PCturns)
            PCturns.remove(player2)
            if xo[player2] == '-':
                xo[player2] = 'o'
                run = 'x'
                os.system("cls")
                if CheckWin('o'):
                    board()
                    print("Player2 wins!")
                    break
                elif '-' not in xo:
                    board()
                    print("Game Over!")
                    break
                else:
                    # sys.system("cls")
                    board()
        else:
            os.system("cls")
            board()
            print("Occupied position!")

elif(PCvsHMN == 'q' or PCvsHMN == 'Q'):
    exit(0)

elif(PCvsHMN == 'p' or PCvsHMN == 'p'):
    PCturns = [0,1,2,3,4,5,6,7,8]
    while (True):
        player1 = random.choice(PCturns)
        if xo[player1] == '-':
            PCturns.remove(player1)
            xo[player1] = 'x'
            os.system("cls")
            if CheckWin('x'):
                board()
                print("Player1 wins!")
                break
            elif '-' not in xo:
                board()
                print("Game Over!")
                break
            else:
                # sys.system("cls")
                board()
        time.sleep(0.8)
        player2 = random.choice(PCturns)
        PCturns.remove(player2)
        if xo[player2] == '-':
            xo[player2] = 'o'
            os.system("cls")
            if CheckWin('o'):
                board()
                print("Player2 wins!")
                break
            elif '-' not in xo:
                board()
                print("Game Over!")
                break
            else:
                # sys.system("cls")
                board()
        time.sleep(0.8)
    


#0 1 2 4 7 5 3 6 8 -Game Over Condition
