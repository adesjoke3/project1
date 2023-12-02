# Favorite_Fruit = ["strawberry", "grapes","pineapple", "peach", "banana", "avacando"]
# for fruit in Favorite_Fruit:
#     print("My first favorite fruit is",fruit)

# import random
# random_number = random.randint(1, 20)

# guess = 0
# while guess != random_number:
#     guess = int(input("Guess the number (between 1 and 20): "))
#     if guess < random_number:
#         print("Too low! Try again.")
#     elif guess > random_number:
#         print("Too high! Try again.")
#     else:
#         print("Congratulations! You guessed the correct number.")
#         break

sentence = input("Enter a sentence")


words = sentence.split()
for word in words:
    print(f"{word}: {len(word)}")

numbers = [5,10,15,20]
total = 0


for num in numbers:
    total += num


print("sum of numbers:",total)

password = "adekunlefamily!!"


while True:
    user_input = input("Enter the password")
    if user_input == password:
        print("Password accepted. Access granted!")
        break
    else:
        print("Incorrect password.Try again")

Countdown_number = int("Enter a number to start the count down")
while Countdown_number > 0:
    print(Countdown_number)
    Countdown_number -= 1
print("WAKE UP!!")




