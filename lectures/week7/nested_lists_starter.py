"""Recursion

=== CSC148 ===
Department of Computer Science,
University of Toronto

=== Module description ===
Starter code for some recursive functions we'll write that operate on
nested lists.

Pattern we can often use:

    if isinstance(obj, int):
        ...
    else:
        for sublist in obj:
            ... f(sublist) ...

"""
from typing import List, Optional, Union


# This function is traced on the first worksheet.
def flatten(obj: Union[int, list]) -> List[int]:
    """Return a (non-nested) list of the integers in <obj>.

    The integers are returned in the left-to-right order they appear
    in <obj>.

    >>> flatten(6)
    [6]
    >>> flatten([1, [-2, 3], -4])
    [1, -2, 3, -4]
    >>> flatten([[0, -1], -2, [[-3, [-5]]]])
    [0, -1, -2, -3, -5]
    """
    if isinstance(obj, int):
        return [obj]
    else:
        s = []
        for sublist in obj:
            s.extend(flatten(sublist))
        return s


def uniques(obj: Union[int, List]) -> List[int]:
    """Return a (non-nested) list of the integers in <obj>, with no duplicates.
    """
    if isinstance(obj, int):
        return [obj]
    else:
        s = []
        for sublist in obj:
            s.extend(uniques(sublist))
        return s


def nested_list_contains(obj: Union[int, List], item: int) -> bool:
    """Return whether the given item appears in <obj>.
    """
    pass


def first_at_depth(obj: Union[int, List], d: int) -> Optional[int]:
    """Return the first (leftmost) number in <obj> at depth <d>.

    Return None if there is no item at depth d.

    Precondition: d >= 0.
    """
    if isinstance(obj, int):
        if d == 0:
            return obj
        return None
    else:
        if d == 0:
            # This is the right answer = we dont need to recurse
            # Also bonus: this prevents us from recursing d = -1
            return None
        else:
            #Know: Object is a list and d is greater than 0
            for sublist in obj:
                s = first_at_depth(sublist, d-1)
                if s is not None:
                    return s
                #Know: there was no item at depth d
                return None


def add_one(obj: Union[list, int]) -> None:
    """Add one to every number stored in <obj>. Do nothing if <obj> is an int.

    If <obj> is a list, *mutate* it to change the numbers stored.
    (Don't return anything in either case.)

    >>> lst0 = 1
    >>> add_one(lst0)
    >>> lst0
    1
    >>> lst1 = []
    >>> add_one(lst1)
    >>> lst1
    []
    >>> lst2 = [1, [2, 3], [[[5]]]]
    >>> add_one(lst2)
    >>> lst2
    [2, [3, 4], [[[6]]]]
    """
    pass


if __name__ == '__main__':
    import python_ta
    python_ta.check_all()

    # import doctest
    # doctest.testmod()
