# Hello! This is Kevin Dacanay
# and the purpose of this assignment is to put together the programs we created
# during the semester into one large program

# The programs that are included are:
# - Restaurant Menu (Week 4)
# - Rock Paper Scissors Revised (Week 8)
# - QR Code Generator (Week 12)

# -------------------------------------------------
# Import "programs" module that contains our three programs
from programs import *


# Option for user to choose from:
print(f"\nHello! This is a three-in-one program.\n\n You have three options to choose from:"
      f"\n Option [1]: Restaurant Menu"
      f"\n Option [2]: Rock Paper Scissors Revised"
      f"\n Option [3]: QR Code Generator"
      f"\n Option [0]: Quit")

options = "1", "2", "3", "0", "x", "X"
while True:
    choice = input("\nEnter the number of your choice: ")
    while choice not in options:
        choice = input("Invalid option! Please select [1] [2] or [3] ")

    print(f"You have chosen Option {choice}:\n")

    if choice == "1":
        Restaurant()
    elif choice == "2":
        RPS()
    elif choice == "3":
        QR()
    else:
        print("Goodbye. Have a good day!")
        break

    again = input("\nDo you want to choose again? y/n: ")
    if again != "y":
        print("Goodbye. Have a good day!")
        break