import pytest
from dequeList import (
    DequeLinkedList,
)  # Replace 'your_module_name' with the actual name of your module


# Test get method
def test_get():
    deque = DequeLinkedList()
    assert deque.get(0) == -1

    deque.insertRear(1)
    deque.insertRear(2)
    deque.insertRear(3)
    assert deque.get(0) == 1
    assert deque.get(1) == 2
    assert deque.get(2) == 3
    assert deque.get(3) == -1


# Test insertFront method
def test_insertFront():
    deque = DequeLinkedList()
    deque.insertFront(1)
    assert deque.getValues() == [1]

    deque.insertFront(0)
    assert deque.getValues() == [0, 1]


# Test insertRear method
def test_insertRear():
    deque = DequeLinkedList()
    deque.insertRear(1)
    assert deque.getValues() == [1]

    deque.insertRear(2)
    assert deque.getValues() == [1, 2]


# Test removeFront method
def test_removeFront():
    deque = DequeLinkedList()
    assert deque.removeFront() is False

    deque.insertRear(1)
    deque.insertRear(2)
    assert deque.removeFront() is True
    assert deque.getValues() == [2]


# Test removeRear method
def test_removeRear():
    deque = DequeLinkedList()
    assert deque.removeRear() is False

    deque.insertRear(1)
    deque.insertRear(2)
    assert deque.removeRear() is True
    assert deque.getValues() == [1]


# Test getValues method
def test_getValues():
    deque = DequeLinkedList()
    assert deque.getValues() == []

    deque.insertRear(1)
    deque.insertRear(2)
    assert deque.getValues() == [1, 2]


# You can add more test cases based on your requirements.
