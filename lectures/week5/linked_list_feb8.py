"""Linked List

=== CSC148 ===
Department of Computer Science,
University of Toronto

=== Module Description ===
This module contains the code for a linked list implementation with two classes,
LinkedList and _Node.

Code template we can use:

    curr = self._first
    while curr is not None:
        # ... curr.item ...
        curr = curr.next

But don't try to shoe-horn every single thing into this template!  It's not
always suited to the task.

Today we implemented 3 linked list methods.  The first two only traversed the
linked list: __eq__ and __getitem__.  The third one mutated a linked list:
insert.  We finished insert in the last moments of class, so make sure the code
makes sense to you.

There are several very important take-away lessons from this rather successful
coding experience today:
- While loops are easy to mess up. It really helps to first write down the
  condition under which the loop must stop, and then flip that around to get
  your while condition (the condition under which the loop must NOT stop).
- It really helps to write down what you know at key points, including after a
  while loop. There is often subtle logic implicit in the code. It's better to
  write it down explicitly. You can even use asserts to check your logic. This
  can save you from some subtle bugs.

I'll add one more important thing I didn't get a chance to say:
- Whenever you saw apple.banana, you'd better be sure that apple is not None!
  Reasoning through that can not only avoid bugs, but we saw that it can
  help you with the logic of your program.

Short version: Think before you code. It will save you time.
"""
from __future__ import annotations

from typing import Any, Callable, Optional, Union


class _Node:
    """A node in a linked list.

    Note that this is considered a "private class", one which is only meant
    to be used in this module by the LinkedList class, but not by client code.

    === Attributes ===
    item:
        The data stored in this node.
    next:
        The next node in the list, or None if there are no more nodes.
    """
    item: Any
    next: Optional[_Node]

    def __init__(self, item: Any) -> None:
        """Initialize a new node storing <item>, with no next node.
        """
        self.item = item
        self.next = None  # Initially pointing to nothing


class LinkedList:
    """A linked list implementation of the List ADT.
    """
    # === Private Attributes ===
    # _first:
    #     The first node in the linked list, or None if the list is empty.
    _first: Optional[_Node]

    # This implementation of LinkedList has a fancier initializer
    # and a __str__ method that permit things like:
    #     >>> linky = LinkedList([1, 223, 30, 16])
    #     >>> print(linky)
    #     '[1 -> 223 -> 30 -> 16]'
    # You'll write these methods later.

    # You did this in Prep 5:
    def append(self, item: Any) -> None:
        """Append <item> to the end of this list.
        """
        if self._first is None:
            self._first = _Node(item)
        else:
            curr = self._first
            while curr.next is not None:
                curr = curr.next
            curr.next = _Node(item)

    def print_items(self) -> None:
        """Print the items in this linked list.
        """
        curr = self._first
        while curr is not None:
            print(curr.item)
            curr = curr.next

    def __eq__(self, other: LinkedList) -> bool:
        """Return whether this list and the other list are equal.

        >>> lst1 = LinkedList([1, 2, 3])
        >>> lst2 = LinkedList([])
        >>> lst1.__eq__(lst2)
        False
        >>> lst2.append(1)
        >>> lst2.append(2)
        >>> lst2.append(3)
        >>> lst1.__eq__(lst2)
        True
        """
        curr1 = self._first
        curr2 = other._first
        # Note:
        # "blah is None" does the same thing as "blah == None" and is considered
        # better Python style.
        # "blah is not None" does the same thing as "blah != None" and is
        # also considered better Python style.
        while (curr1 is not None) and (curr2 is not None):
            # If they're NOT equal then return False.
            # otherwise: advance ahead and keep looping.
            if curr1.item != curr2.item:
                return False
            else:
                # Know: curr1.item == curr2.item
                curr1 = curr1.next
                curr2 = curr2.next
        # Know: All the nodes we examined were ==.
        # Know: (curr1 is None) or (curr2 is None) or both
        # i.e., we've reached the end of one linked list or both.
        # If BOTH are at end the end, return True; otherwise return False
        if (curr1 is None) and (curr2 is None):
            return True
        else:
            return False
        # Could we have said curr1 == curr2? I think these are equivalent,
        # but this alternative version requires more thinking.

    def __getitem__(self, index: int) -> Any:
        """Return the item at position <index> in this list.

        Raise IndexError if <index> is >= the length of this list.

        Precondition: index >= 0

        >>> linky = LinkedList([100, 4, -50, 13])
        >>> linky[0]          # Equivalent to linky.__getitem__(0)
        100
        >>> linky[2]
        -50
        >>> linky[100]
        Traceback (most recent call last):
        IndexError
        >>> linky = LinkedList([])
        >>> linky.__getitem__(0)
        Traceback (most recent call last):
        IndexError
        """
        # (a) initialize curr and i
        curr = self._first
        i = 0
        # (b) stop iterating when: (curr is None) or (i == index)
        # Continue if: not[ (curr is None) or (i == index) ]
        # QU: could index be 0?  Yes!
        while (curr is not None) and (i < index):
            curr = curr.next
            i = i + 1
        # Know: (curr is None) or (i == index) or both!
        assert (curr is None) or (i == index)  # or both!
        if curr is None:
            # We did not find the item at the desired index: the list was too
            # short
            raise IndexError
        else:
            # Know: curr is not None.
            # Know: (curr is None) or (i == index)
            # Therefore: i == index!!  We found it and didn't fall off the list.
            return curr.item

    def insert(self, index: int, item: Any) -> None:
        """Insert the given item at the given index in this list.

        Raise IndexError if index > len(self) or index < 0.
        Note that adding to the end of the list is okay.
        >>> linky = LinkedList([0, 1, 2, 3, 4])
        >>> linky.insert(3, 99)
        >>> print(linky)
        [0 -> 1 -> 2 -> 99 -> 3 -> 4]
        >>> linky = LinkedList([])
        >>> linky.insert(0, 99)
        >>> print(linky)
        [99]
        """
        new_node = _Node(item)
        if index == 0:
            new_node.next = self._first
            self._first = new_node
        else:
            curr = self._first
            i = 0
            # Stop if (i == index - 1) or (curr is None)
            # We flipped that to get the while loop condition.
            # We didn't have time, but try to simplify this by applying
            # one of De Morgan's laws:
            #     not (A or B) = (not A) and (not B)
            #     not (A and B) = (not A) or (not B)
            while not ((i == index - 1) or (curr is None)):
                curr = curr.next
                i = i + 1
            # Know: (i == index - 1) or (curr is None) or both
            if curr is None:
                # We could not find a node at index; the list is too short!
                raise IndexError
            else:
                # Know: (i == index - 1) or (curr is None)
                # curr is not None
                # therefore: (i == index - 1). We found ths spot!
                rest_of_list = curr.next
                curr.next = new_node
                new_node.next = rest_of_list

    # def pop(self, index: int) -> Any:
    #     """Remove and return the item at position <index>.
    #
    #     Raise IndexError if index >= len(self) or index < 0.
    #
    #     >>> lst = LinkedList([1, 2, 10, 200])
    #     >>> lst.pop(1)
    #     2
    #     >>> lst.pop(2)
    #     200
    #     >>> lst.pop(148)
    #     Traceback (most recent call last):
    #     IndexError
    #     >>> lst.pop(0)
    #     1
    #     """
    #     pass

    # def remove(self, item: Any) -> None:
    #     """Remove the FIRST occurrence of <item> in this list.
    #
    #     Do nothing if this list does not contain <item>.
    #     (Note: Python lists actually raise a ValueError.)
    #
    #     >>> lst = LinkedList([1, 2, 3])
    #     >>> lst.remove(2)
    #     >>> str(lst)
    #     '[1 -> 3]'
    #     >>> lst.remove(2)
    #     >>> str(lst)
    #     '[1 -> 3]'
    #     >>> lst.remove(3)
    #     >>> str(lst)
    #     '[1]'
    #     >>> lst.remove(1)
    #     >>> str(lst)
    #     '[]'
    #     >>> lst.remove(1)
    #     >>> str(lst)
    #     '[]'
    #     """
    #     pass

    # (Blank lines inserted just to keep this code off the screen.)

    def __init__(self, items: list) -> None:
        """Initialize a new linked list containing the given items.

        The first node in the linked list contains the first item
        in <items>.
        """
        if items == []:  # No items, and an empty list!
            self._first = None
        else:
            self._first = _Node(items[0])
            curr = self._first
            for item in items[1:]:
                curr.next = _Node(item)
                curr = curr.next

    def __str__(self) -> str:
        """Return a string representation of this list in the form
        '[item1 -> item2 -> ... -> item-n]'.

        >>> str(LinkedList([1, 2, 3]))
        '[1 -> 2 -> 3]'
        >>> str(LinkedList([]))
        '[]'
        """
        items = []
        curr = self._first
        while curr is not None:
            items.append(str(curr.item))
            curr = curr.next
        return '[' + ' -> '.join(items) + ']'


if __name__ == '__main__':
    # import python_ta
    # python_ta.check_all()

    import doctest

    doctest.testmod()
