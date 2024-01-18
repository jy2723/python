import random

def flip_coin(flips):
    if flips <= 0:
        print("enter a positive integer")
        return

    heads = 0
    tails = 0

    for _ in range(flips):
        result = random.random() 
        if result < 0.5:
            heads += 1
        else:
            tails += 1

    percentage_heads = (heads / flips) * 100
    percentage_tails = (tails / flips) * 100
    print("heads:",percentage_heads)
    print("tails:",percentage_tails)
flips = int(input("enter number:"))
flip_coin(flips)


