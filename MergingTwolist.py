# Given two sorted linked lists, merge them so that the resulting list is also sorted.
# Define a Node class for the linked list
class ListNode:
    def __init__(self, value=0, next=None):
        self.value = value
        self.next = next

# Function to merge two sorted lists
def mergeTwoLists(l1, l2):
    dummy = ListNode()  # A dummy node to hold the merged list
    current = dummy  # Pointer to the last node in the merged list
    
    while l1 and l2:
        if l1.value < l2.value:  # Compare the values from both lists
            current.next = l1  # Append the smaller value to the result
            l1 = l1.next  # Move the pointer of l1 forward
        else:
            current.next = l2  # Append the smaller value to the result
            l2 = l2.next  # Move the pointer of l2 forward
        current = current.next  # Move the current pointer forward
    
    current.next = l1 or l2  # Append the remaining elements from the non-empty list
    
    return dummy.next  # Return the merged list, excluding the dummy node

# Example usage:
# Input: 1 -> 2 -> 4, 1 -> 3 -> 4
# Output: 1 -> 1 -> 2 -> 3 -> 4 -> 4

# Creating two linked lists
l1 = ListNode(1, ListNode(2, ListNode(4)))
l2 = ListNode(1, ListNode(3, ListNode(4)))

# Merging two lists
merged_head = mergeTwoLists(l1, l2)
