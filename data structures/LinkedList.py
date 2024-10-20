class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def insert_at_beginning(self, data):
            new_node = Node(data)
            new_node.next = self.head
            self.head = new_node

    def insert_at_end(self, data):
        new_node = Node(data)
        new_node.data = data
        new_node.next = None
        if self.head is None:
            self.head = new_node
        else:
            current = self.head
            while current.next is not None:
                current = current.next
            current.next = new_node

    def print_linked_list(self):
        current = self.head
        while current is not None:
            print(current.data, end=" ")
            current = current.next

    def del_element(self, val):
        if self.head is None:
            print("Linked list is empty")
            return
        elif self.head.data == val:
            temp = self.head
            self.head = temp.next
            temp = None
            return
        else:
          current = self.head
          prev = None
          while current is not None and current.data != val:
              prev = current
              current = current.next
          if current is None:
              print("The value is not found in the list")
              return
          else:
              prev.next = current.next
              current = None


list1 = LinkedList()
list1.insert_at_beginning(10)
list1.insert_at_beginning(20)
list1.insert_at_beginning(30)
list1.insert_at_end(40)
list1.insert_at_end(50)
list1.print_linked_list()

list1.del_element(30)
print("\nElements in the list after deleting 30 are: ")
list1.print_linked_list()

list1.del_element(40)
print("\nElements in the list after deleting 50 are: ")
list1.print_linked_list()
