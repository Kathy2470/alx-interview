def canUnlockAll(boxes):
    # Start with the first box (box 0)
    visited = set()
    stack = [0]

    while stack:
        box_index = stack.pop()
        if box_index not in visited:
            visited.add(box_index)
            # Add all keys from the current box to the stack
            for key in boxes[box_index]:
                if key not in visited:
                    stack.append(key)

    # Check if all boxes have been visited
    return len(visited) == len(boxes)
