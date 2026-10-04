import random

attmp = 0
while True:
    print("I'm thinking of a number between 1 and 100.")
    if attmp > 3:
         print("Your attempt is over.")
    user = int(input("Please enter a number to compare with my number: "))
    attmp += 1
    print(f"{3 - attmp} left")

    gues_num = random.randint(1,100)
    # print(gues_num)

    if gues_num == user:

        print(f"Guess {user} \n Correct!")

    elif user - gues_num < 10:
            print(f"Guess {user} Actual {gues_num}  Too High!")

    else:
         print(f"Guess {user} Actual {gues_num} Too low!")

    if attmp == 3:
         cho = input("Play again? y/n: ")
         if cho == "y":
              attmp = 0
         else:
              print("Thanks for choosing us.")
              break
              
              
         
    