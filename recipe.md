# {{PROBLEM}} Function Design Recipe

Copy this into a `recipe.md` in your project and fill it out.

## 1. Describe the Problem

As a user
So that I can find my tasks among all my notes
I want to check if a line from my notes includes the string `#TODO`.


## 2. Design the Function Signature

_Include the name of the function, its parameters, return value, and side effects._

```python
# EXAMPLE

def includes_todo(note_line):
    """Checking if a line from notes includes #TODO

    Parameters: (list all parameters and their types)
        a string as a line from a note

    Returns: (state the return value and its type)
        True if it contains #TODO, False if not

    Side effects: (state any side effects)
        This function doesn't print anything or have any other side-effects
    """
    pass # Test-driving means _not_ writing any code here yet.
```

## 3. Create Examples as Tests

_Make a list of examples of what the function will take and return._

```python
# EXAMPLE

"""
>>> includes_todo("#TODO buy milk")
True
>>> includes_todo("drink tea")
False
>>> includes_todo("learn to test-drive my code #TODO")
True
>>> includes_todo("TODO buy milk")
False
>>> includes_todo("#todo walk dog")
False
```

_Encode each example as a test. You can add to the above list as you go._

## 4. Implement the Behaviour

_After each test you write, follow the test-driving process of red, green, refactor to implement the behaviour._

Here's an example for you to start with:

```python
# EXAMPLE

from lib.includes_todo import *

"""
Given a string which includes "#TODO"
Function returns True
"""
def test_for_correct_string():
    result = includes_todo("#TODO buy milk")
    assert result == True
```

Ensure all test function names are unique, otherwise pytest will ignore them!
