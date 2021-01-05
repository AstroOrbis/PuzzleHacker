
#Imports
import time
import os

#Start of the script
print("PuzzleHacker, a script made by Astro Orbis")
print(" ")
time.sleep (1)

print("Sub to me on YouTube (Astro Orbis)")
print(" ")
time.sleep (1)



#Now to check if they want to Encrypt or Decrypt and send them to the redirection script for the corresponding choice
print("Would you like to encrypt or decrypt? Respond Encrypt' 'Decrypt'. ")
EncryptDecrypt = (input(" "))

if EncryptDecrypt == "Encrypt":
    import Encrypt
else:
    import Decrypt
