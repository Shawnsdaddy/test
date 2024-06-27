import collections


class ZigzagIterator2:
    def __init__(self, vecs):
        self.queue = []
        for vec in vecs:
            if vec:
                self.queue.insert(0,vec[::-1])

    def next(self):
        vec = self.queue.pop()
        value = vec.pop()
        if vec:
            self.queue.insert(0,vec)
        return value

    def hasNext(self):
        # Check if there is any vector that still has elements to iterate
        return len(self.queue)>0

# Example usage

vecs = [[1, 2, 3], [4, 5, 6, 7], [8, 9]]
zigzag_iterator = ZigzagIterator2(vecs)

zigzag_order = []
while zigzag_iterator.hasNext():
    zigzag_order.append(zigzag_iterator.next())

print(zigzag_order)