class node:
    def __init__(self, data):
        self.data = data
        self.next = None

#optimal force approach will be using the floyf theorum(fast,slow), enter the loop, then run either fast
# or slow pointer to count the number of nodes in the loop 

#brute_force is hashing, we can use a set to store the nodes we have seen
def len_of_loop(head):
    a=head
    count={}
    i=1
    while a.next is not None:
        if a in count:
            return i-count[a]
        count[a]=i
        a=a.next
        i=i+1
    return 0
def len_of_loop_floyd(head):
    slow = head
    fast = head
    while fast.next is not None and fast.next.next is not None:
        slow = slow.next
        fast = fast.next.next
        if slow ==fast: #now we are in the loop
            count =1
            fast = fast.next
            while fast!= slow:
                count += 1
                fast = fast.next
            return count
node1 = node(1)
node2 = node(2)
node3 = node(3)
node4 = node(4)
node5 = node(5)

node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node5
node5.next = node2  # Creating a loop for testing

head = node1
print(len_of_loop(head))  # Output should be the length of the loop, which is
print(len_of_loop_floyd(head))  # Output should be the length of the loop, which is 3