import json
import random

data = json.load(open("candyPiles.json"))

def move(line, n):
    score = sum(line[:n])
    return [score] + line[n:], score

def best_move(line):
    valid_moves = range(2, len(line)+1)
    return random.choice(valid_moves)

def solve(data):
    line = data.copy()

    players = [0, 0]

    turn = 0
    while len(line) > 1:
        line, score = move(line, best_move(line))
        players[turn] += score
        turn = (turn + 1) % 2

    return players, players[0] - players[1]

best = 0
while True:
    players, score = solve(data)
    if score > best:
        best = score
        print(score)
