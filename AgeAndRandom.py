import random

name = input("What's your name? ")
age = input("How old are you? ")
number = random.randint(1, 10)

print(f"Hello {name}! You're {age} years old!")
if age < str(18):
    print("Sorry but you cannot enter")
    exit()
else:
    print("Welcome to our club!")

input("""I have a game for you. Rules:
1)You need choose a number between 1 and 10
2)You have 1 life so be careful!
So go ahead! Choose the number: """)

if input == number:
    print("Wow! You are very lucky!")
else:
    print("Sorry it's not your day")

#Я зробив аж 3 программи в одній, думаю прикольно вийшло