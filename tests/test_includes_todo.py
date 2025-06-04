from lib.includes_todo import *

def test_for_correct_string():
    result = includes_todo("#TODO buy milk")
    assert result == True

def test_simple_string():
    result = includes_todo("drink tea")
    assert result == False

def test_for_todo_at_end():
    result = includes_todo("learn to test-drive my code #TODO")
    assert result == True

def test_for_no_hash_tag():
    result = includes_todo("TODO buy milk")
    assert result == False

def test_for_lower_case():
    result = includes_todo("#todo walk dog")
    assert result == False