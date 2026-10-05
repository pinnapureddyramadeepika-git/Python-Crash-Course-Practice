import random 
lottery_pool = [6,4,2,8,9,6,4,2,3,1,'a','r','d','e','p','g']
my_ticket = [2,4,'a','d']

attempts = 0
winning_ticket = []
while winning_ticket != my_ticket:
    winning_ticket = random.sample(lottery_pool,4)
    attempts += 1
    print(f"My ticket {my_ticket} won after {attempts} attempts!")