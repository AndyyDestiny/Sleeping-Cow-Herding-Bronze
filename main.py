b = [eval(i) for i in input().split(" ")]

minimum = b[1] - b[0]
maximum = b[1] - b[0]

if b[2] - b[1] > b[1] - b[0]:
    maximum = b[2] - b[1]
else:
    minimum = b[2] - b[1]

if minimum <= 2: 
    print("Least moves: 1")
else:
    print("Least moves: 2")
print("Max moves: " + str(maximum - 1))
