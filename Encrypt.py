#Imports
import os
import time

#Introduction
time.sleep (.7)
print(" ")
print("Encryption select")
print(" ")

#Selection screen
print("Choose the string that corresponds to the puzzle you want to solve!")
time.sleep(.5)
print("Caesarean Cypher (Caesar)")
time.sleep(4)

#Set var PuzzleType

puzzleType = (input("Type the string corresponding to your puzzle, then press enter!"))
time.sleep(1.5)

if puzzleType == "Caesar":
    os.system('cd Encrypt && python3 Caesar.py')
