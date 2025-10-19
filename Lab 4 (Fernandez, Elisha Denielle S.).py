class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def insert_at_end(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        last = self.head
        while last.next:
            last = last.next
        last.next = new_node

    def display(self):
        current = self.head
        count = 1
        if not current:
            print("Empty list.")
            return
        while current:
            print(f"{count}. {current.data}")
            current = current.next
            count += 1

    def remove_beginning(self):
        if self.head:
            removed = self.head.data
            self.head = self.head.next
            return removed
        else:
            print("Cannot remove from an empty list.")
            return None

    def remove_end(self):
        if not self.head:
            print("Cannot remove from an empty list.")
            return None
        if not self.head.next:
            removed = self.head.data
            self.head = None
            return removed
        second_last = self.head
        while second_last.next and second_last.next.next:
            second_last = second_last.next
        removed = second_last.next.data
        second_last.next = None
        return removed

    def remove_at(self, position):
        if position < 0:
            print("Invalid position. Cannot remove.")
            return None
        if not self.head:
            print("Cannot remove from an empty list.")
            return None
        if position == 0:
            removed = self.head.data
            self.head = self.head.next
            return removed
        current = self.head
        prev = None
        count = 0
        while current and count < position:
            prev = current
            current = current.next
            count += 1
        if not current:
            print("Position out of bounds. Cannot remove.")
            return None
        removed = current.data
        prev.next = current.next
        return removed


# Example usage
burger = LinkedList()
burger.insert_at_end("Bottom Bun")
burger.insert_at_end("Meat and Vegetables")
burger.insert_at_end("Top Bun")

print("Original Burger Layers:")
burger.display()
print()

removed_beginning = burger.remove_beginning()
print("Removed from beginning:")
if removed_beginning:
    print(f"1. {removed_beginning}")
print()

removed_end = burger.remove_end()
print("Removed from end:")
if removed_end:
    print(f"3. {removed_end}")
print()

removed_specific = burger.remove_at(20)
print("Removed specific layer (position 20):")
if removed_specific:
    print(f"- {removed_specific}")
else:
    print("Position out of bounds. Cannot remove.")
print()

print("Updated Burger Layers:")
burger.display()
