a = {}
scores = 0

l = {'Y': 2, 'X': 1, 'Z': 3}
r = {"A Y": 6, "B Y": 3, "C Y": 0,
     "A X": 3, "B X": 0, "C X": 6,
     "A Z": 0, "B Z": 6, "C Z": 3}
score = 0
for x in open("input.txt"):
    x = x.strip()
    if x in a:
        a[x] += 1
    else:
        a[x] = 0
        
    score += l[x[2]]  
    score += r[x]   
        
print(score)        
