import time
n = int(input("Please enter how many times you want the cypher to be shifted: "))
s = list(input("\nPlease enter your cypher text: "))
for i in range(len(s)):
    if s[i] == " ":
        new = 32
    else:
        if s[i].isupper():
            new = ord(s[i]) + n
            while new > 90:
                new -= 26
        else:
            new = ord(s[i]) + n
            while new > 122:
                new -= 26
    s[i] = chr(new)
print("Below is your cypher text!\n")
time.sleep (.5)
print("".join(s))
print("\n")