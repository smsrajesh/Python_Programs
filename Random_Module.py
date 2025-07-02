
"""
import random

random.randint(a,b) -->  a and b values are included
random.randrange(a,b) --> a is inclusive,b is exclusive
random.random() --> Gives a floating point number (0.0 <= n <1.0)
random.uniform(a,b) --> Gives a floating point number b/w the range
random.choice(iterable) --> Gives a value from the mentioned iterable
                            (Iterable - list,tuple,set,dictionary)
random.shuffle(iterable) --> Shuffles the mentioned iterable and prints 
                            a different order

"""

import random

print("Flipping The Coin")

coin_side=random.randint(0,1)
print(coin_side)
if coin_side==0:
    print("Tails")
else:
    print("Heads")

