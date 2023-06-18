class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

head = Node(1, Node(22, Node(333, Node(4444, Node(55555)))))

def print_list(head, end='\n'):
    while head:
        print(head.value, end=', ' if head.next else '')
        head = head.next
    print(end=end)

print_list(head)

def reverse_list(head, tail=None):
    while head:
        head.next, tail, head = tail, head, head.next
    return tail

print_list(reverse_list(head))
