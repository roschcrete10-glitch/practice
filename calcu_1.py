# Addition
# Subtraction
# Multiplication
# Division
# Modulus
# Power

def add(a,b):
    print(f"{a} + {b} Total {a+b}")

def subs(a,b):
    print(f"{a} - {b} Total {a-b}") 

def mult(a,b):
    print(f"{a} * {b} Total {a*b}")

def devi(a,b):
    print(f"{a} / {b} Total {a/b}")

def modu(a,b):
    print(f"{a} % {b} Total {a%b}")

def powe(a,b):
    print(f"{a} ** {b} Total {a**b}")


while True:
    
    print("#####################################################")
    choice = input("Choose an option: \n 1. Add two numbers: \n 2. Substract two numbers: \n 3. Multiply two numbers: \n 4. Devide two numbers: \n 5. Modulus check two numbers: \n 6. Power of two numbers: \n 7. Exit: ")
    if choice == "1":
        try:
            ask1 = int(input("Please Enter your first number: "))
            ask2 = int(input("Please Enter your second number: "))
            add(ask1, ask2)
        except ValueError:
            print("Please enter valid number.")

    elif choice == "2":
        try:
            ask1 = int(input("Please Enter your first number: "))
            ask2 = int(input("Please Enter your second number: "))
            subs(ask1, ask2)
        except ValueError:
            print("Please enter valid number.")
    elif choice == "3":
            try:
                ask1 = int(input("Please Enter your first number: "))
                ask2 = int(input("Please Enter your second number: "))
                mult(ask1, ask2)
            except ValueError:
                print("Please enter valid number.")
    elif choice == "4":
            try:
                ask1 = int(input("Please Enter your first number: "))
                ask2 = int(input("Please Enter your second number: "))
                if ask2 == 0:
                    print("Enter valid second number.")
                    break
                devi(ask1, ask2)
            except ValueError:
                print("Please enter valid number.")
    elif choice == "5":
            try:
                ask1 = int(input("Please Enter your first number: "))
                ask2 = int(input("Please Enter your second number: "))
                modu(ask1, ask2)
            except ValueError:
                print("Please enter valid number.")

    elif choice == "6":
            try:
                ask1 = int(input("Please Enter your first number: "))
                ask2 = int(input("Please Enter your second number: "))
                powe(ask1, ask2)
            except ValueError:
                print("Please enter valid number.")
    elif choice == "7":
         print("Thanks for choosing us.")
         break
    else:
         print("Choose an option which are available.")

    