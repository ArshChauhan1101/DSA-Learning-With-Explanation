# Write a function to reverse a singly linked list.
# Define a Node class for the linked list
class ListNode:
    def __init__(self, value=0, next=None):
        self.value = value
        self.next = next

# Function to reverse the linked list
def reverseLinkedList(head):
    prev = None  # This will hold the previous node
    curr = head  # Start with the head of the list

    while curr:
        next_node = curr.next  # Store the next node
        curr.next = prev  # Reverse the link
        prev = curr  # Move the previous pointer to current node
        curr = next_node  # Move to the next node in the original list

    return prev  # Prev will be the new head of the reversed list

# Example usage:
# Input: 1 -> 2 -> 3 -> None
# Output: 3 -> 2 -> 1 -> None

# Creating a linked list 1 -> 2 -> 3 -> None
head = ListNode(1, ListNode(2, ListNode(3)))

# Reversing the linked list
new_head = reverseLinkedList(head)
