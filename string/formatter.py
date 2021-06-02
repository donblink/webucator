import random
import math
def formatter():
    choice = random.choice(["2f", "3f", "4f","5f","6f","7f","8f","9f","10f"])        
    print("format to try : {}".format(choice))
    print("Number to format: math.pi")
    print(" result: {:.3f}".format(math.pi))

formatter()    