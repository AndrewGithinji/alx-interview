#!/usr/bin/python3
"""
Module that contains the canUnlockAll function
"""


def canUnlockAll(boxes):
    """
    Determines if all the boxes can be opened.
    """
    if type(boxes) is not list:
        return False

    if len(boxes) == 0:
        return False

    keysbox = [0]

    for key in keysbox:
        for j in boxes[key]:
            if j not in keysbox and j < len(boxes):
                keysbox.append(j)

    for i in range(len(boxes)):
        if i not in keysbox:
            return False

    return True
