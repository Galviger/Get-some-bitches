import random
import time
from tqdm import tqdm

currentBitches = int(input('How many bitches you got?\n'))
myBitches = None
def getBitches():
    randnum = random.randrange(0, 4)
    myBitches = currentBitches + randnum
    print('Searching for bitches...')
    for i in tqdm(range(1, 101)):
        time.sleep(0.1)
    if myBitches == 0:
        print("Rip bozo, can't get any bitches")
    elif myBitches == 1:
        print("Congrats! Now you got 1 bitch.")
    elif myBitches == 2 or myBitches == 3:
        print(f"Congrats! Now you got {myBitches} bitches.")

if currentBitches == 0:
    getBitches()