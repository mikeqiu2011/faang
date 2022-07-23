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

        node_before_start = self.get_node_before_position(left)
        print(f'node before start: {node_before_start.value}')
        start = node_before_start.next

        temp_list = LinkedList(start.value)
        cur = start.next

        for i in range(right - left):
            temp_list.add_node(cur.value)
            cur = cur.next

        node_after_end = cur
        print(f'node after end: {node_after_end.value}')

        print('temp list is:')
        temp_list.display()

        temp_list = temp_list.reverse()
        print('temp list after reverse')
        temp_list.display()

        node_before_start.next = temp_list.head
        temp_list.tail.next = node_after_end

        return self

    def get_node_before_position(self, n):
        node = self.head
        for i in range(1, n - 1):
            node = node.next

        return node


linkedList = LinkedList(1)
linkedList.add_node(2)
linkedList.add_node(3)
linkedList.add_node(4)
linkedList.add_node(5)
linkedList.display()
# linkedList.reverse().display()

# print(linkedList.get_node_before_position(3).value)

print('postitional reverse')
linkedList.reverseBetween(2,4).display()
