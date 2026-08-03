class Node:
    def __init__(self, data, next_node=None):
        self.data = data
        self.next = next_node

#actually as easy meathod is there

#now the is _small_palindrom with same time complexity of the bigger one works, if we use a copy of the linked list and reverse it, then compare the two linked lists, if they are same then it is a palindrome
def copy_linked_list(head):
    if head is None:
        return None
    new_head = Node(head.data)
    current_old = head.next
    current_new = new_head
    while current_old is not None:
        current_new.next = Node(current_old.data)
        current_new = current_new.next
        current_old = current_old.next
    return new_head #same as using the a and b, i did 

def is_small_palinfrome(head):
    copy_head = copy_linked_list(head)
    rev_head = reverse_linked_list(copy_head)
    while head is not None and rev_head is not None:
        if head.data != rev_head.data:
            return False
        head = head.next
        rev_head = rev_head.next
    return True


# Function to reverse linked list
# using recursion approach
def reverse_linked_list(head): #here we are using recursion to reverse the linked list, reverse the head as well as the whole linked list
    # Check if the list is empty
    # or has only one node
    if head is None or head.next is None:
        
        # No change is needed;
        # return the current head
        return head

    # Recursive step: Reverse the remaining part
    # of the list and obtain the new head
    new_head = reverse_linked_list(head.next)

    # Store the next node in 'front' to reverse the link
    front = head.next

    # Update the 'next' pointer of 'front' to 
    # point to the current head, effectively
    # reversing the link direction
    front.next = head

    # Set the 'next' pointer of the current
    # head to 'None' to break the original link
    head.next = None

    # Return the new head obtained
    # from the recursion
    return new_head
    
def is_palindrome(head):
    # Check if the linked list is empty
    # or has only one node
    if head is None or head.next is None:
        # It's a palindrome by definition
        return True

    # Initialize two pointers, slow and fast,
    # to find the middle of the linked list
    slow = head
    fast = head

    # Traverse the linked list to find the
    # middle using slow and fast pointers
    while fast.next is not None and fast.next.next is not None:
        # Move slow pointer one step at a time
        slow = slow.next

        # Move fast pointer two steps at a time
        fast = fast.next.next

    # Reverse the second half of the
    # linked list starting from the middle
    new_head = reverse_linked_list(slow.next)

    # Pointer to the first half
    first = head

    # Pointer to the reversed second half
    second = new_head
    while second is not None:
        # Compare data values of
        # nodes from both halves

        # If values do not match,
        # the list is not a palindrome
        if first.data != second.data:
            # Reverse the second half
            # back to its original state
            reverse_linked_list(new_head)
            # Not a palindrome
            return False

        # Move the first pointer
        first = first.next

        # Move the second pointer
        second = second.next

    # Reverse the second half
    # back to its original state
    reverse_linked_list(new_head)

    # The linked list is a palindrome
    return True
    
# Function to print the linked list
def print_linked_list(head):
    temp = head
    while temp is not None:
        print(temp.data, end=" ")
        temp = temp.next
    print()

def main():
    # Create a linked list with
    # values 1, 5, 2, 5, and 1 (15251, a palindrome)
    head = Node(1)
    head.next = Node(5)
    head.next.next = Node(2)
    head.next.next.next = Node(3)
    head.next.next.next.next = Node(1)

    # Print the original linked list
    print("Original Linked List: ", end="")
    print_linked_list(head)

    # Check if the linked list is a palindrome
    if is_palindrome(head):
        print("The linked list is a palindrome.")
    else:
        print("The linked list is not a palindrome.")

    if is_small_palinfrome(head):
        print("The linked list is a palindrome (small method).")

if __name__ == "__main__":
    main()

