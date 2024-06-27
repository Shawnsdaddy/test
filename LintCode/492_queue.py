class MyQueue:
    head = None
    tail = None
    def enqueue(self,item):
        if not self.head:
            self.head = ListNode(item)
        else:
            if not self.tail:
                self.tail = ListNode(item)
                self.head.next = self.tail
            else:
                self.tail.next = ListNode(item)
                self.tail = self.tail.next

    def dequeue(self):
        if not self.head:
            return -1
        else:
            val = self.head.val
            self.head = self.head.next
            return val

class ListNode(object):
    def __init__(self, val, next=None):
        self.val = val
        self.next = next