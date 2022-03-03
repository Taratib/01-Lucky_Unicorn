import random

# Functions go here
def yes_no (question):
    valid = False
    while not valid:
        response = input(question).lower()

        if response  == "yes" or response == "y":
            response = "yes"
            return response
        
        elif response == "no" or response  == "n":
            respons = "no"
            return response

        else:
            print ("please answer yes / no")
  
def instructions():
    print("**** How to play ****")
    print()
    print("The rules of the game go here")
    print()
    return ""

def num_check(question, low, high):

    error= "Please enter an whole number between 1 and 10\n"

    valid = False 
    while not valid:
        try:
            # ask the question
            response = int(input(question))

            # if the amount is too low / too high give
            if low < response <= high:
               return response

            # output an error
            else:
                print(error)

        except ValueError:
            print(error)

def statement_generator(statement, decoration):

    sides = decoration * 3

    statement = "{} {} {}".format(sides, statement, sides)
    top_bottom = decoration * len(statement)

    print(top_bottom)
    print(statement)
    print(top_bottom)

    return ""

# Main Routine goes here

statement_generator("Welcome to the Luky Unicorn Game", "*")
print()
played_before = yes_no("Have you played the game before? ")
print()

if played_before == "no":
    statement_generator("How to play", ".")
    instructions()

print()
played_before = yes_no("Let's get Started...")

# Ask user how much they want to play with
how_much = num_check("How much would you like to play with? ", 0, 10)

balance = how_much

rounds_played = 0

play_again = input("Press <Enter> to play...").lower()
while play_again == "":

    # increase # of rounds played
    rounds_played += 1

    # Print round number
    print()
    print("*** Round #{} ***".format(rounds_played))
  
    chosen_num = random.randint(1, 100)
    
    # Adjust balance
    # if the random # is between 1 and 5,
    # user gets a unicorn (add $4 to balance)
    if 1 <= chosen_num <= 5:
        chosen = "unicorn"
        balance += 4
    
    # if random # is between 6 and 36 
    # user gets a donkey (subtract $1 from balance)
    elif 6 <= chosen_num <= 36:
            chosen = "donkey"
            balance -= 1
    
    # The token is either a hoarse or zebra... 
    # in both cases, subtract $0.50 from the balance 
    else:
        # if the number is even, set the chosen 
        # item to a horse
        if chosen_num % 2 == 0:
            chosen = "horse"

        # otherwise set it to a zebra
        else:
            chosen = "zebra"
            balance -= 0.5


    print("You got a {}. Your balance is ${:.2f}".format(chosen, balance))

    if balance < 1:
        # If balance is to low, exit the game and 
        # output a suitable message
        play_again = "xxx"
        print("Sorry you have to run out of money")
    else:
        play_again = input("Press Enter to play again or 'xxx' to quit")

print()
print("Final balance", balance)
print() 