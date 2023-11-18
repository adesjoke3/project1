print("your in a maigcal land with three doors!")
door = input ("witch door will you chose(1,2,3)?")
if door == "1":
    print("you found hidden treasure congratulations!")
elif door == "2":
    print("a friendly dragon appears and offers you a wish. what do you wish for?")
    wish = input ("i wish for:")
    print(f"you wished for {wish}. the dragon grants your wish!")
elif door == "3":
    print("oops! you fell into a pit, but a helpful squirrel rescues you.")
else:
    print("invalid choice. please choose a door (1,2 or 3).")

