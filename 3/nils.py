import json

line = json.load(open("waitingSpirits.json"))

def can_see(line, i, j):
    for x in range(i+1, j):
        if line[x] >= line[i] or line[x] >= line[j]:
            return False
    return True

distances = [0]*len(line)
for i in range(len(distances)):
    n = 0
    for j in range(i+1, len(line)):
        if can_see(line, i, j):
            n += 1
    distances[i] = n

print(",".join(map(str, distances)))
