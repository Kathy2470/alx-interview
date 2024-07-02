#!/usr/bin/python3

def canUnlockAll(boxes):
    n = len(boxes)
    unlocked = set([0])
    queue = [0]

    while queue:
        box = queue.pop(0)
        for key in boxes[box]:
            if key not in unlocked and 0 <= key < n:
                unlocked.add(key)
                queue.append(key)

    return len(unlocked) == n
