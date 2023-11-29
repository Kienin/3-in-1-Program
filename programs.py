# We'll be creating a module called "programs" that we will be importing in our main program
#
# We have created functions for the three programs so that the user can pick and call them.
# These are the programs that we have coded for class

# Defining the functions:

# Restaurant Menu (Week 4):
def Restaurant():
    # Choices for main dish, side dish, and soda (none options available)
    Main_dish = "[1] Hamburger: $ 7.00\n[2] Pizza slice: $ 6.00\n[3] Hotdog: $ 5.00\n[0] None"
    Side_dish = "[4] Fries: $ 4.00\n[5] Onion rings: $ 3.00\n[0] None"
    Drinks_dish = "[6] Soda: $ 1.00\n[7] Lemonade: $1.00\n[8] Water: $0.00\n[0] None"

    # INPUT - the program will get user's name and choices(main dish, side dish, drinks, and payment method)
    name = input("Welcome the the restaurant! What is your name? ")
    print(f'Hello {name.capitalize()}!\n')

    # Main Dish: put in a while loop for invalid entry-
    print("Main Dishes:\n" + Main_dish)
    while True:
        Main_choice = input("Please select your main dish: (enter number) \n")
        if Main_choice == "1":
            price1 = 7.00
            main1 = "Hamburger"
            break
        elif Main_choice == "2":
            price1 = 6.00
            main1 = "Pizza slice"
            break
        elif Main_choice == "3":
            price1 = 5.00
            main1 = "Hotdog"
            break
        elif Main_choice == "0":
            price1 = 0.00
            main1 = "None"
            break
        else:
            print("Invalid Entry!")
    Main_price = price1

    # Side Dish: put in a while loop for invalid entry-
    print("Side Dishes:\n" + Side_dish)
    while True:
        Side_choice = input("Please select your side dish: (enter number) \n")
        if Side_choice == "4":
            price2 = 4.00
            main2 = "Fries"
            break
        elif Side_choice == "5":
            price2 = 3.00
            main2 = "Onion Rings"
            break
        elif Side_choice == "0":
            price2 = 0.00
            main2 = "None"
            break
        else:
            print("Invalid Entry!")
    Side_price = price2

    # Drinks: put in a while loop for invalid entry-
    print("Drinks options:\n" + Drinks_dish)
    while True:
        Drinks_choice = input("Please select your drink: (enter number) \n")
        if Drinks_choice == "6":
            price3 = 1.00
            main3 = "Soda"
            break
        elif Drinks_choice == "7":
            price3 = 1.00
            main3 = "Lemonade"
            break
        elif Drinks_choice == "8":
            price3 = 0.00
            main3 = "Water"
            break
        elif Drinks_choice == "0":
            price3 = 0.00
            main3 = "None"
            break
        else:
            print("Invalid Entry!")
    Drink_price = price3

    # Payment Method: put in a while loop for invalid entry-
    while True:
        payment = input("Will you be paying with Cash[C] or Card?[R]: ").capitalize()
        if payment == "R":
            print("You are paying with Card.\n")
            break
        elif payment == "C":
            print("You are paying with Cash.\n")
            break
        else:
            print("Invalid Payment Method!")
    Payment = payment

    # PROCESS - calculates subtotal, tax, total
    Subtotal = Main_price + Side_price + Drink_price
    Tax = 0.07
    Total = (Subtotal * Tax) + Subtotal

    # OUTPUT -
    print(f'\n{name.capitalize()}, you have ordered:')
    print(main1 + ": $" + str(round(Main_price, 2)))
    print(main2 + ": $" + str(round(Side_price, 2)))
    print(main3 + ": $" + str(round(Drink_price, 2)))
    print(f'Your Subtotal is: $' + str(round(Subtotal, 2)))
    print("You are taxed: $" + str(round(Subtotal * Tax, 2)))
    print(f"Your Total is: $" + str(round(Total, 2)))

    # Payment method:
    if Payment == "C":
        cash_payment = float(input("\nHow much are you paying with in cash: $ "))
    elif Payment == "R":
        cash_payment = 0
    Cash_payment = cash_payment
    if Cash_payment == 0:
        print("\nYou are charged: $" + str(Total))
    elif Cash_payment >= Total:
        Total_cash_payment = Cash_payment - Total
        print("You gave $" + str(Cash_payment))
        print(f"Your change is: $" + str(round(Total_cash_payment, 2)))
    elif Cash_payment < Total:
        insufficient = float(input("Not enough funds! Please pay Total amount: $ "))
        if insufficient > Total:
            print("You gave $" + str(insufficient))
            print(f"Your change is: $" + str(round(insufficient - Total, 2)))
        elif insufficient == Total:
            print("You are paying with the exact amount due. You have no change.")
        elif insufficient < Total:
            print("Still not enough funds.")
            last_payment = float(input("Please pay the amount due: $ "))
            if last_payment >= Total:
                print("You gave $" + str(last_payment))
                print(f"Your change is: $" + str(round(last_payment - Total, 2)))
            elif last_payment < Total:
                print("Not enough Funds. Order is cancelled")

    print("Thank you for purchasing! Have a good day and please come again!")

# Rock Paper Scissors Revised (Week 8):
def RPS():
    import random

    # INPUT - get name and rounds user wants to play for
    name = str(input("Hi there! What is your name? ")).capitalize()
    print(f"Hello {name}! Let's play Rock, Paper, Scissors!\n")

    # rounds need to be an odd number, so it'll  be best of N rounds
    while True:
        try:
            best_of = int(input("How many rounds do you want to play? (Please enter an odd number): "))
            if best_of % 2 != 0:
                break
            else:
                print("Invalid! Please enter an odd number")
        except ValueError:
            print("Invalid! Please enter an odd number")

    choices = ["r", "p", "s", "rock", "paper", "scissors"]
    player_score = 0
    computer_score = 0

    winning_score = (best_of + 1) // 2

    print(f"\nThis game is best of {best_of}. Good luck {name}!\n")

    '''
    we add 1 to the winning score then dividing it by 2:
    for example: 
        if player wants to play 5 rounds, and they win 3 rounds; they win
        5 + 1 = 6  ->  6 / 2 = 3
        if player wins 3 rounds, they win. They don't have to play till 5 rounds
    '''

    while player_score < winning_score and computer_score < winning_score:
        print('________________________________________')
        print(f"{name} score: {player_score} - Computer score: {computer_score}\n")

        # Get player and computer choice
        player_choice = input("Pick [R]ock, [P]aper, or [S]cissors: ").lower()
        if player_choice not in choices:
            print("Invalid! Please enter [R]ock, [P]aper, or [S]cissors")
            continue
        computer_choice = random.choice(choices)

        # reassign choices into more readable choice:
        if player_choice == "r":
            player_choice = "Rock"
        elif player_choice == "p":
            player_choice = "Paper"
        elif player_choice == "s":
            player_choice = "Scissors"

        if computer_choice == "r":
            computer_choice = "Rock"
        elif computer_choice == "p":
            computer_choice = "Paper"
        elif computer_choice == "s":
            computer_choice = "Scissors"

        if player_choice == "rock":
            player_choice = "Rock"
        elif player_choice == "paper":
            player_choice = "Paper"
        elif player_choice == "scissors":
            player_choice = "Scissors"

        if computer_choice == "rock":
            computer_choice = "Rock"
        elif computer_choice == "paper":
            computer_choice = "Paper"
        elif computer_choice == "scissors":
            computer_choice = "Scissors"
        # PROCESS - determine who wins the round
        print(f"\nYou chose {player_choice} : The Computer chose {computer_choice}")

        if player_choice == computer_choice:
            print("It's a tie!")
        elif (player_choice == "Rock" and computer_choice == "Scissors") or \
                (player_choice == "Paper" and computer_choice == "Rock") or \
                (player_choice == "Scissors" and computer_choice == "Paper"):
            print(f"{name} Wins!")
            player_score += 1
        else:
            computer_score += 1
            print("Computer Wins!")

    print('________________________________________')
    print(f"FINAL SCORE - {name}: {player_score} | Computer: {computer_score}")
    if player_score > computer_score:
        print("Congratulations! You won!!!")
    else:
        print("Better luck next time! Computer Won!!!")

# QR Code Generator (Week 12):
def QR():
    import qrcode
    print("This is a QR Code generator.")
    img = input("Enter a URL: ")
    image = qrcode.make(img)

    name = input("What do you want to name the QR Code: ")
    file_name = (name + ".png")

    image.save(file_name+".png", "PNG")
    print(f"QR Code has been downloaded!\nSearch up '{file_name}' on your file manager.")