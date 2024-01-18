"""CSC148 Prep 6 Synthesize

=== CSC148 Winter 2023 ===
Department of Computer Science,
University of Toronto

This code is provided solely for the personal and private use of
students taking the CSC148 course at the University of Toronto.
Copying for purposes other than this use is expressly prohibited.
All forms of distribution of this code, whether as given or with
any changes, are expressly prohibited.

Copyright (c) 2021 Diane Horton, Jonathan Calver, Sophia Huynh,
Myriam Majedi, and Jaisie Sin.

=== Module Description ===
This module contains a __main__ block that defines some client code.
Define the three classes so that the example __main__ block will
run with all assertions passing and the output as described.

The provided self-test on MarkUs is the FULL test suite for this week!
This is a more robust set of tests, and there are no hidden test cases.

Your grade will correspond to the number of test cases passed. If you
pass all of them, then you will receive full marks for this prep.
As such, any unspecified behaviour that is not in the self-test is left
as a design decision for you.

Your task for this prep is to complete a program that allows a user to create
checklists with items to be done and record when items are completed:
- A checklist has a name (str) and a list of checklist items.
- A checklist item has a description (str), a deadline (date), and
  the name of the user who completed the item.
- A user has a name (str) and the total number items they have completed (int).

You will need to write one class for each of these entities.
See the __main__ block for an example of how we want to use these classes.

You may choose any reasonable way to store the necessary data. Attributes that
are of type int, str, or bool, and date may be public, but all other attributes
must be private. You may add imports from the typing module, but do NOT add any
other imports.

We will be checking for class docstrings that follow the Class Design Recipe.
You must include attribute type annotations and descriptions for all attributes.
Docstrings for your methods are NOT required.
"""
from __future__ import annotations
from datetime import date

# If you need any imports from the typing module, you may import them above.
# (e.g. from typing import Optional)

#       See the __main__ block below for an example of how the classes will
#       be called and the expected output.
#       Be sure to write class docstrings that describe all attributes that
#       you create, and include type annotations for each attribute.


class User:
    """Stores name of the user and the number of items user has completed.

    === Public Attributes ===
    name: Name of the user
    total_items_checked: Number of completed items
    """
    name: str
    total_items_checked: int

    def __init__(self, name: str) -> None:
        """ Initialize name of the User and the number of items completed.
        >>> Bob = User('Bob')
        >>> Bob.name
        'Bob'
        """
        self.name = name
        self.total_items_checked = 0


class ChecklistItem:
    """An item on the checklist that contains a description, due date and the
    name of the user that completed the item"""

    desc: str
    due: date
    completed_by: str

    def __init__(self, desc: str, due: date) -> None:
        """Initialize attributes in this class"""
        self.desc = desc
        self.due = due
        self.completed_by = ''


class Checklist:
    """A list of checklist items. The name of this list is picked by client
    code and ChecklistItem objects can be added to this list
    === Public Attributes===
    name: Name of the checklist
    Desc: Description of the checklist item
    Due: Due date for the checklist item

    === Private Attributes ===
    _lst_items: list of all checklist items
    """
    name: str
    _lst_items: list[ChecklistItem]
    desc: str
    due: date

    def __init__(self, name: str) -> None:
        """Initialize attributes in this class"""
        self.name = name
        self._lst_items = []

    def create_item(self, desc: str, due: date) -> None:
        """Create Checklist item objects and store them in a list """
        item = ChecklistItem(desc, due)
        self._lst_items.append(item)

    def mark_item_complete(self, description: str, user: User) -> None:
        """Mark the item complete by the user inputted"""
        for item in self._lst_items:
            if item.desc == description:
                item.completed_by = user.name
                user.total_items_checked += 1

    def has_item(self, item_desc: str) -> bool:
        """Return True if the <item_dec> is in the list of items"""
        for item in self._lst_items:
            if item.desc == item_desc:
                return True
        return False

    def __str__(self) -> str:
        """Return the items inside of checklist"""
        item_list = ''
        for item in self._lst_items:
            if item.completed_by == '':
                item_list += '\n[-] ' + item.desc + ' (' + str(item.due) + ')'
            else:
                item_list += '\n[x] ' + item.desc + ' (' + str(item.due) + \
                             '), completed by ' + item.completed_by

        return self.name + item_list


if __name__ == "__main__":
    # Instantiate three users
    manila = User('Manila')
    sofija = User('Sofija')
    felix = User('Felix')

    # Instantiate a checklist
    manilas_checklist = Checklist('Planner for M')

    # Manila adds some items to the checklist, the first one she adds is Math
    # Homework due on March 1st.
    manilas_checklist.create_item('Math Homework', date(2021, 3, 1))
    manilas_checklist.create_item('pick up milk', date(2021, 2, 25))
    manilas_checklist.create_item('CSC148 A1', date(2021, 3, 2))

    # Manila finishes her CSC148 assignment and marks it complete
    manilas_checklist.mark_item_complete('CSC148 A1', manila)

    # Sofija attempts to check off an item as complete that isn't in
    # manilas_checklist.  This does nothing.
    manilas_checklist.mark_item_complete('MAT157 Review', sofija)

    # Sofija picks up milk for Manila.
    manilas_checklist.mark_item_complete('pick up milk', sofija)

    print(manilas_checklist)
    # The output is below. Notice that the order is based on the order they
    # were added to manilas_checklist.  Output:
    # Planner for M
    # [-] Math Homework (2021-03-01)
    # [x] pick up milk (2021-02-25), completed by Sofija
    # [x] CSC148 A1 (2021-03-02), completed by Manila

    # confirm the checklist items are all present in the checklist
    for item_description in ['Math Homework', 'pick up milk', 'CSC148 A1']:
        assert manilas_checklist.has_item(item_description)

    # Felix completed no checklist items
    assert felix.total_items_checked == 0
    # Manila and Sofija each completed one checklist item
    assert manila.total_items_checked == 1
    assert sofija.total_items_checked == 1

    # import python_ta
    #
    # python_ta.check_all(config={
    #     'extra-imports': ['datetime'],
    #     'disable': ['W0212', 'E1136']
    # })
