class Node:
    def __init__(self,data,next=None):
        self.data=data
        self.next=next

# utility function to insert node at the end of the linked list
# for generating nodes, this lite
def insertNode(head, val):
    newNode = Node(val)
    if head == None:
        head = newNode
        return head
    temp = head
    while temp.next != None:
        temp = temp.next
    temp.next = newNode
    return head

def printList(head):
    while head.next != None:
        print(head.data, end='->')
        head = head.next
    print(head.data)


def intersection_brute(head1,head2):
        a=head1
        b=head2.next
        while a is not None: #is already been iterated
            while b is not None:
                if a==b:
                    return a.data
                else:
                    b=b.next
            b=head2.next
            a=a.next
        return None

def intersection_opt_diff(head1,head2):

    def diff(head1,head2):
        a=head1
        b=head2
        a_count=0
        b_count=0
        while a is not None or b is not None:
            if a is not None:
                a_count+=1
                a=a.next
            if b is not None:
                b_count+=1
                b=b.next
        return a_count-b_count
    
    difference=diff(head1,head2)
    a=head1
    b=head2
    if difference>=0:
        while difference!=0:
            a=a.next
            difference-=1
    else:
        while difference!=0:
            b=b.next
            difference+=1
    
    while a is not None:
        if a==b:
            return a.data
        else:
            a=a.next
            b=b.next
    return None

def intersection_opt_same(head1,head2):
    a=head1
    b=head2
    while a!=b:
        if a is None:
            a=head2
        else:
            a=a.next
        if b is None:
            b=head1
        else:
            b=b.next
    return a.data

#intersection_opt does not run on infinite loops because there is a case where both the a and b will be None, there is no condition like that in the question
            
if __name__ == '__main__':
    head = None
    head = insertNode(head, 1)
    head = insertNode(head, 3)
    head = insertNode(head, 1)
    head = insertNode(head, 2)
    head = insertNode(head, 4)
    head1 = head
    head = head.next.next.next
    headSec = None
    headSec = insertNode(headSec, 3)
    head2 = headSec
    headSec.next = head
    print('List1: ', end='')
    printList(head1)
    print('List2: ', end='')
    printList(head2)
    print('Intersection_brute: ', end='')
    print(intersection_brute(head1, head2))
    print('Intersection_opt_diff: ', end='')
    print(intersection_opt_diff(head1, head2))
    print('Intersection_opt_same: ', end='')
    print(intersection_opt_same(head1, head2))



                    
                
                  
