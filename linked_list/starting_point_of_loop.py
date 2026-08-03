class Node:
    def __init__(self, data):
        self.data = data
        self.reference = None
def create_single_ll_from_array(arr):
    head = Node(arr[0])
    a = head
    for i in range(1, len(arr)):
        new_node = Node(arr[i])
        a.reference = new_node
        a = a.reference
    return head
def print_single_ll(head):
    a = head
    print(a.data, end=" ")
    while a.reference is not None:
        a = a.reference
        print(a.data, end=" ")
    print()
def starting_point_of_loop_brute_force(head):
    visited = set()
    a=head
    while a.next is not None:
        a=a.next
        if a in visited:
            return a.data
        visited.add(a)
    return None

def starting_point_of_loop_opt(head):
    slow = head
    fast = head

    # Detect loop using Floyd's Cycle-Finding Algorithm
    while fast and fast.next is not None:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            slow=head
            while slow != fast:
                slow = slow.next
                fast = fast.next
            return slow.data
    return None

    # If no loop is found
    if not fast or not fast.next:
        return None

    # Find the starting point of the loop
    slow = head
    while slow != fast:
        slow = slow.next
        fast = fast.next

    return slow.data

node1 = Node(1)
node2 = Node(2)
node1.next = node2
node3 = Node(3)
node2.next = node3
node4 = Node(4)
node3.next = node4
node5 = Node(5)
node4.next = node5

# Make a loop from node5 to node2
node5.next = node2

# Set the head of the linked list
head = node1

print(starting_point_of_loop_brute_force(head))  # Output: 2
print(starting_point_of_loop_opt(head))  # Output: 2