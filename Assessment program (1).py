
import random

Die1 = random.randint(1,6)

Die2 = random.randint(1,6)

Score = Die1 + Die2

if Die1 == Die2:
    Score = Score*2

print(Score)

