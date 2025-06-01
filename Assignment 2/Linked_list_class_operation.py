class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def add_node(self, data):
        
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return

        current = self.head
        while current.next:
            current = current.next
        current.next = new_node

    def print_list(self):
        
        current = self.head
        if not current:
            print("List is empty.")
            return

        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")

    def delete_nth_node(self, n):
        
        try:
            if not self.head:
                raise IndexError("Cannot delete from an empty list.")

            if n <= 0:
                raise IndexError("Index must be a positive integer.")

           
            if n == 1:
                print(f"Deleting node {n} with value {self.head.data}")
                self.head = self.head.next
                return

            current = self.head
            count = 1
            while current and count < n - 1:
                current = current.next
                count += 1

            if not current or not current.next:
                raise IndexError("Index out of range.")

            print(f"Deleting node {n} with value {current.next.data}")
            current.next = current.next.next

        except IndexError as e:
            print("Error:", e)



if __name__ == "__main__":
    Test_link = LinkedList()
    print("Initial list:")
    Test_link.print_list()

    print("\nAdding nodes:")
    for value in [10, 20, 30, 40, 50]:
        Test_link.add_node(value)
    Test_link.print_list()

    print("\nDeleting 3rd node:")
    Test_link.delete_nth_node(3)
    Test_link.print_list()

    print("\nDeleting 1st node:")
    Test_link.delete_nth_node(1)
    Test_link.print_list()

    print("\nDeleting node at index 10 (should raise error):")
    Test_link.delete_nth_node(10)
    Test_link.print_list()

    print("\nDeleting from an empty list:")
    empty_list = LinkedList()
    empty_list.delete_nth_node(1)



""" Output:
   
Initial list:
List is empty.

Adding nodes:
10 -> 20 -> 30 -> 40 -> 50 -> None

Deleting 3rd node:
Deleting node 3 with value 30
10 -> 20 -> 40 -> 50 -> None

Deleting 1st node:
Deleting node 1 with value 10
20 -> 40 -> 50 -> None

Deleting node at index 10 (should raise error):
Error: Index out of range.
20 -> 40 -> 50 -> None

Deleting from an empty list:
Error: Cannot delete from an empty list. """