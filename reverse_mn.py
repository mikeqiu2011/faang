# Definition for singly-linked list.
class Node:
    def __init__(self, value=0, next=None):
        self.value = value
        self.next = next



class LinkedList:
    def __init__(self, value):
        node = Node(value)
        self.head = node
        self.tail = node
        self.length = 0

    def add_node(self, value):
        node = Node(value)
        self.tail.next = node
        self.tail = node
        self.length += 1

    def display(self):
        cur = self.head
        while cur:
            print(cur.value)
            cur = cur.next

    def reverse(self):
        if self.length <= 1:
            return self

        first = self.head
        second = first.next
        first.next = None
        self.tail = first

        while second:
            temp = second.next
            second.next = first
            first = second
            second = temp

        self.head = first
        return self

    def reverseBetween(self, left: int, right: int):
        if left < 1 or right > self.length or left > right:
            return False




linkedList = LinkedList(1)
linkedList.add_node(2)
linkedList.add_node(3)
linkedList.add_node(4)
linkedList.add_node(5)
linkedList.display()
linkedList.reverse().display()