"""Exercise 08: Link Lists Utils"""

from __future__ import annotations

__author__: str = "730662974"


class Node:
    """Class node of comp classes"""

    def __init__(self, val: int, next: Node | None):
        """
        Initializes a Node with a value and a pointer to the next node.

        Parameters:
            val (int): The value stored in the node.
            next (Node | None): The next node in the list, or None if this is the last node.
        """
        self.value = val
        self.next = next


def value_at(head: Node | None, index: int) -> int:
    if head is None:  # base case #1: if linked list is empty
        raise IndexError("Index is out of bounds on the list.")

    if index == 0:  # base case #2: if only one head node
        return head.value
    else:
        return value_at(head.next, index - 1)


# if the index is greater than 0 or not empty (none) it will recursively call value_at on the next node
# why index-1?? think of index -1 as incrementing the index briging it closer to 0
# it keeps decreasing eventually when it gets to zero, it will return the value at that head and then it will stop calling value_at again


def max(head: Node | None) -> int:
    """Returns the maximum data value in the linked list."""
    if head is None:  # base case: empty linked lsit
        raise ValueError("Cannot call max with None.")

    if head.next is None:
        # base case: if there is only head node, but nothing else after just return the head node
        return head.value

    max_val: int = max(head.next)
    # initialize a local variable that will keep recursively calling max
    # moves through the linked list to find the max value

    if head.value > max_val:
        # check if the value of the head node is greater than the max value u have found
        return head.value
    else:
        return max_val

    # after the recursive call completes is only when u know the max value
    # if you keep it before, then you would be comparing max_val with an undefined max_value


def linkify(items: list[int]) -> Node | None:
    """Return a linked list of nodes with the same values AKA turn list into LL."""
    # if list is empty return none
    if len(items) == 0:
        return None

    head: Node = Node(items[0], linkify(items[1:]))
    # you want the head node to equal the first element at first,
    # then do recursive step: remember Node has 2 parameters head and next
    # the next value will be the the next one in items use the slice (1: means the second item in the list (index 1) and onwards)

    return head


def scale(head: Node | None, factor: int) -> Node | None:
    """Each value in LL returns the original values multiplied by factor"""
    if head is None:  # base case 1 if there is no head
        return None

    new_node: Node = Node(head.value * factor, scale(head.next, factor))
    # node object takes in two parameters, it's own int value and then next Node
    # create new node, where the head node value is multiplied by the factor that will be an int value
    # then the next parameter is a node, make sure to use the scale in this step;
    # it will call this recursively for each next node

    return new_node
