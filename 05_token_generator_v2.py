import random

# main routine goes here

token = ["unicorn", "horse", "zebra", "donkey"]

# Testing loop to generate 20 tokens
for iteam in range (0,20):
    chosen = random.choice(token)
    print(chosen, end='\t')
   
    