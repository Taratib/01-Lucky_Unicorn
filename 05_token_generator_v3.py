import random

# main routine goes here
token = ["unicorn", "horse", "zebra", "donkey"]
balance = 100

# Testing loop to generate 20 tokens
for iteam in range (0,20):
    chosen = random.choice(token)
    
    # Adjust balance
    if chosen == "unicorn":
        balance += 4
    elif chosen == "donkey":
        balance -= 1
    else:
        balance -= 0.5

    # output
    print("Token: {} , Blance: ${}".format(chosen, balance))
