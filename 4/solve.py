original = "Implement the solution and write an explanation of the problem."
changed = "Draw a component diagram and create a mockup for a website to represent the solution."


from itertools import product
import itertools
from collections import deque

# Borrowed from https://johnlekberg.com/blog/2020-10-25-seq-align.html
def needleman_wunsch(x, y):
    """Run the Needleman-Wunsch algorithm on two sequences.

    x, y -- sequences.

    Code based on pseudocode in Section 3 of:

    Naveed, Tahir; Siddiqui, Imitaz Saeed; Ahmed, Shaftab.
    "Parallel Needleman-Wunsch Algorithm for Grid." n.d.
    https://upload.wikimedia.org/wikipedia/en/c/c4/ParallelNeedlemanAlgorithm.pdf
    """
    N, M = len(x), len(y)
    s = lambda a, b: int(a == b)

    DIAG = -1, -1
    LEFT = -1, 0
    UP = 0, -1

    # Create tables F and Ptr
    F = {}
    Ptr = {}

    F[-1, -1] = 0
    for i in range(N):
        F[i, -1] = -i
    for j in range(M):
        F[-1, j] = -j

    option_Ptr = DIAG, LEFT, UP
    for i, j in product(range(N), range(M)):
        option_F = (
            F[i - 1, j - 1] + s(x[i], y[j]),
            F[i - 1, j] - 1,
            F[i, j - 1] - 1,
        )
        F[i, j], Ptr[i, j] = max(zip(option_F, option_Ptr))

    # Work backwards from (N - 1, M - 1) to (0, 0)
    # to find the best alignment.
    alignment = deque()
    i, j = N - 1, M - 1
    while i >= 0 and j >= 0:
        direction = Ptr[i, j]
        if direction == DIAG:
            element = i, j
        elif direction == LEFT:
            element = i, None
        elif direction == UP:
            element = None, j
        alignment.appendleft(element)
        di, dj = direction
        i, j = i + di, j + dj
    while i >= 0:
        alignment.appendleft((i, None))
        i -= 1
    while j >= 0:
        alignment.appendleft((None, j))
        j -= 1

    return list(alignment)

def print_alignment(x, y, alignment):
    print("".join(
        "-" if i is None else x[i] for i, _ in alignment
    ))
    print("".join(
        "-" if j is None else y[j] for _, j in alignment
    ))

def changes(x, y, alignment):
    return list(zip(
        "".join(
            "-" if i is None else x[i] for i, _ in alignment
        ),
        "".join(
            "-" if j is None else y[j] for _, j in alignment
        )
    ))

def do_change(working, change, index):
    (a, b) = change
    if a == b:
        return working

    if a == "-":
        return working[:index] + b + working[index:]
    else:
        return working[:index] + b + working[index+1:]

alignment = needleman_wunsch(original, changed)
print(alignment)
print_alignment(original, changed, alignment)

working = original

steps = [original]
for i, change in enumerate(changes(original, changed, alignment)):
    print(change, i)
    working = do_change(working, change, i)
    print(working)
    steps.append(working)

assert(working == changed)

print(",".join(steps))
