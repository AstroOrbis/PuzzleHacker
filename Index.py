
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
EncryptDecrypt = (input("\n"))

if EncryptDecrypt == "Encrypt":
    import Encrypt
elif EncryptDecrypt == "Decrypt":
    import Decrypt
else:
    print("Invalid awnser - restarting the script.")
    os.system('python3 Index.py')
