from functools import reduce

r = {"A Y": 4, "B Y": 5, "C Y": 6,
     "A X": 3, "B X": 1, "C X": 2,
     "A Z": 8, "B Z": 9, "C Z": 7}

with open("input.txt") as file:
    lines = file.readlines()
           
print(sum(r[x.strip()] for x in lines))