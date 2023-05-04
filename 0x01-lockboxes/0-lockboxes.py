#!/usr/bin/python3
"""
Module that contains the canUnlockAll function.

The canUnlockAll function checks if all the boxes in a list of boxes can be
opened using the keys contained in other boxes. A box can be opened if it has a
key that has the same number as another box.
"""

from typing import List


def canUnlockAll(boxes: List[List[int]]) -> bool:
    """
    Checks if all the boxes in a list of boxes can be opened using the keys
    contained in other boxes.

    Args:
        boxes: A list of lists. Each list represents a box and contains the
            numbers of the boxes that can be opened with the keys inside the
            box.

    Returns:
        True if all boxes can be opened, else False.
    """
    if not isinstance(boxes, list):
        return False

    if not boxes:
        return False

    visited_boxes = [False] * len(boxes)
    visited_boxes[0] = True
    stack = [0]

    while stack:
        box = stack.pop()

        for key in boxes[box]:
            if key < len(boxes) and not visited_boxes[key]:
                visited_boxes[key] = True
                stack.append(key)

    return all(visited_boxes)
