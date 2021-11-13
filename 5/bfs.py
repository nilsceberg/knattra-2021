import json
import random

graph = json.load(open("tombstones.json"))

def assign_type(u, types):
    used = [False]*types
    for i in u["neighbours"]:
        v = graph[i-1]
        if "type" in v:
            used[v["type"]] = True

    available_types = list(filter(lambda x: not x[1], enumerate(used)))

    t = 0
    if len(available_types) == 0:
        t = types
        types += 1
    else:
        #t = available_types[0][0]            # deterministic
        t = random.choice(available_types)[0] # fuzzy

    u["type"] = t

    return types

def fuzzy_solution(graph):
    for u in graph:
        if "type" in u:
            del u["type"]

    types = 0

    queue = []
    queue.append(graph[0])

    while len(queue) != 0:
        u = queue.pop()
        types = assign_type(u, types)

        for i in u["neighbours"]:
            v = graph[i-1]
            if "type" not in v:
                queue.append(v)

    return (",".join(map(lambda x: f"({x['id']}:{x['type']})", graph)), types)

best = 100
while True:
    (solution, score) = fuzzy_solution(graph)
    if score < best:
        best = score
        print("----------------------------")
        print(solution)
        print(f"--------- {score} ---------")
