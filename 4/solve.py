import Levenshtein

original = "Implement the solution and write an explanation of the problem."
changed = "Draw a component diagram and create a mockup for a website to represent the solution."


from itertools import product
import itertools
from collections import deque

offset = 0

def do_change(working, change):
    global offset
    (t, s, d) = change
    s += offset

    if t == "insert":
        offset += 1
        return working[:s] + changed[d] + working[s:]
    elif t == "replace":
        return working[:s] + changed[d] + working[s+1:]
    else:
        assert(False) # aaaaah

#alignment = needleman_wunsch(original, changed)
alignment = Levenshtein.editops(original, changed)
print(alignment)

working = original

steps = [original]
for change in alignment:
    print(change)
    working = do_change(working, change)
    print(working)
    steps.append(working)

assert(working == changed)

print(",".join(steps))
