PATH = "input.txt"

L = []
R = []
with open(PATH, "r") as file:
    for line in file:
        line = line.split()
        left_pair, right_pair = int(line[0]), int(line[1])
        L.append(left_pair)
        R.append(right_pair)
L.sort()
R.sort()
total_distance = 0
for a,b in zip(L, R):
    total_distance += abs(a-b)
print(total_distance)