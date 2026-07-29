#!/usr/bin/python3
"""Defines a singly linked list"""


class Node:
    """Represent a node of a singly linked list"""

    def __init__(self, data, next_node=None):
        """Initialize a new Node

        Args:
            data (int): data of the new Node
            next_node (Node): next Node of the new Node
        """
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """Retrieve the data of the Node"""
        return self.__data

    @data.setter
    def data(self, value):
        """Set the data of the Node

        Args:
            value (int): The new data
        """
        if type(value) is not int:
            raise TypeError("data must be an integer")
        self.__data = value

    @property
    def next_node(self):
        """Retrieve the next Node"""
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        """Set the next Node

        Args:
            value (Node): The new next Node
        """
        if value is not None and type(value) is not Node:
            raise TypeError("next_node must be a Node object")
        self.__next_node = value


class SinglyLinkedList:
    """Represent a singly linked list"""

    def __init__(self):
        """Initialize a new SinglyLinkedList"""
        self.__head = None

    def sorted_insert(self, value):
        """Insert a new Node into the correct sorted position

        Args:
            value (int): The value to insert
        """
        new = Node(value)
        if self.__head is None or self.__head.data > value:
            new.next_node = self.__head
            self.__head = new
            return
        temp = self.__head
        while temp.next_node is not None and temp.next_node.data <= value:
            temp = temp.next_node
        new.next_node = temp.next_node
        temp.next_node = new

    def __str__(self):
        """Print the entire list, one node number per line"""
        nodes = []
        temp = self.__head
        while temp is not None:
            nodes.append(str(temp.data))
            temp = temp.next_node
        return "\n".join(nodes)
