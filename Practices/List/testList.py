import pytest
from listSingle import (
    LinkedList,
)  # Replace 'your_module_name' with the actual name of your module


# Test get method
def test_get():
    linked_list = LinkedList()
    assert linked_list.get(0) == -1

    linked_list.insertTail(1)
    linked_list.insertTail(2)
    linked_list.insertTail(3)
    assert linked_list.get(0) == 1
    assert linked_list.get(1) == 2
    assert linked_list.get(2) == 3
    assert linked_list.get(3) == -1


# Test insertHead method
def test_insertHead():
    linked_list = LinkedList()
    linked_list.insertHead(1)
    assert linked_list.getValues() == [1]

    linked_list.insertHead(0)
    assert linked_list.getValues() == [0, 1]


# Test insertTail method
def test_insertTail():
    linked_list = LinkedList()
    linked_list.insertTail(1)
    assert linked_list.getValues() == [1]

    linked_list.insertTail(2)
    assert linked_list.getValues() == [1, 2]


# Test remove method
def test_remove():
    linked_list = LinkedList()
    assert linked_list.remove(0) is False

    linked_list.insertTail(1)
    linked_list.insertTail(2)
    assert linked_list.remove(1) is True
    assert linked_list.getValues() == [1]


# Test getValues method
def test_getValues():
    linked_list = LinkedList()
    assert linked_list.getValues() == []

    linked_list.insertTail(1)
    linked_list.insertTail(2)
    assert linked_list.getValues() == [1, 2]


# You can add more test cases based on your requirements.
