'''
A Node class is provided for you in the editor. A Node object has an integer data field, data, and a Node instance pointer,next , pointing to another node
(i.e.: the next node in the list).
A Node insert function is also declared in your editor. It has two parameters: a pointer, head, pointing to the first node of a linked list, and an integer,data , 
that must be added to the end of the list as a new Node object.

Complete the insert function in your editor so that it creates a new Node (pass data as the Node constructor argument) and inserts it at the tail of the 
linked list referenced by the head parameter. Once the new node is added, return the reference to the head node.

Note: The head argument is null for an empty list.
'''

class Node:
    def __init__(self,data):      
        self.data = data
        self.next = None 
class Solution: 
    def display(self,head):
        current = head
        while current:
            print(current.data,end=' ')
            current = current.next

    def insert(self,head,data):
        if head is None:
            head = Node(data)
            self.tail = head
        else: 
            node = Node(data)
            self.tail.next = node
            self.tail = node
        return head

mylist= Solution()
T=int(input())
head=None
for i in range(T):
    data=int(input())
    head=mylist.insert(head,data)    
mylist.display(head);
