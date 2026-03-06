import random

random_num = random.randint(1,100)
print(random_num)



guess  = int(input("guess the random number: "))

while guess != random_num:
    print("guess is wrong")

    if guess < random_num:
        print("High")
    elif guess > random_num:
        print("Low")

    guess = int(input("Try again: "))
print("guess is correct")