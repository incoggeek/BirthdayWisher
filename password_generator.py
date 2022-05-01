import random

wordlist = '''abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!
@#$%^&*()+-/1234567890'''

Pass_length = int(input("Enter length of Password :"))
for i in range(Pass_length+1):
    password = ''
    for j in range(i):
        password = password + random.choice(wordlist)
print('Your random generated password,\n', password)

with open("password.txt", "a") as f:
  f.write("\n"+password)