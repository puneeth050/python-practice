import math
import numpy as np
def g(t):
    if t>0:
        noOfItems = 20
        remValue = np.mod(t,noOfItems)
        loops = math.ceil(t/noOfItems)
        for i in range(loops):
            if i == loops - 1:
                if remValue > 0:
                    #range = 0 - remValue - 1
                    print(remValue)
                else:
                    print(noOfItems)   
            else:
                print(noOfItems)

g(40)