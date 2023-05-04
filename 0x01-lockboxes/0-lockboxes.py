#!/usr/bin/python3
"""Contains "canUnlockAll" function"""

def canUnlockAll(boxes):
    """
    Determine if all the boxes can be opened.

    Prototype: def canUnlockAll(boxes)
    boxes is a list of lists
    A key with the same number as a box opens that box
    You can assume all keys will be positive integers
    There can be keys that do not have boxes
    The first box boxes[0] is unlocked
    Return True if all boxes can be opened, else return False
    """
    if type(boxes) is not list: return False
    if len(boxes) == 0: return False

    keysbox = [0]
    for key in keysbox:
        for j in boxes[key]:
            if j not in keysbox and j < len(boxes):
                keysbox.append(j)

    for i in range(len(boxes)):
        if i not in keysbox: return False

    return True
