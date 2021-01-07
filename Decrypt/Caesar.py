#imports
import time
import os

#the original alphabet
alphabet = "abcdefghijklmnopqrstuvwxyz"
#num of shifts
key = 0

newMessage = ""
message = input("Enter encrypted message: ")
key = int(input("Enter the number of shifts: "))

for character in message:
    if character in alphabet:
        #find location and returns number index/position
        location = alphabet.find(character)
        #new location for encrypted letter
        newLocation = (location - key) % 26
        #gets the encyrpted letter
        newCharacter = alphabet[newLocation]
        #add the new character to newMessage
        newMessage += newCharacter
    else:
        #adds the character as is, example ! space ? #
        newMessage += character

print("Your decrypted message is: " + newMessage)
print("Your output will also be available in the 'Output' folder in the root of this project.")
os.system('cd . && cd Output && echo' + newMessage + '> Caesar_Decryption_Output.txt')