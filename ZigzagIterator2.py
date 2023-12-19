class ZigzagIterator2:
    def __init__(self, vecs):
        self.vecs = [v for v in vecs if v]  # Remove empty vectors
        self.indexes = [0] * len(self.vecs)  # Current index in each vector
        self.current = 0  # Current vector to pull from

    def next(self):
        if not self.hasNext():
            raise StopIteration("No more elements to iterate.")

        # Get the next element from the current vector
        current_vec = self.vecs[self.current]
        value = current_vec[self.indexes[self.current]]
        self.indexes[self.current] += 1

        # Move to the next vector that has remaining elements
        self.current = (self.current + 1) % len(self.vecs)
        while self.indexes[self.current] == len(self.vecs[self.current]):
            self.current = (self.current + 1) % len(self.vecs)

        return value

    def hasNext(self):
        # Check if there is any vector that still has elements to iterate
        return any(self.indexes[i] < len(vec) for i, vec in enumerate(self.vecs))

# Example usage
vecs = [[1, 2, 3], [4, 5, 6, 7], [8, 9]]
zigzag_iterator = ZigzagIterator2(vecs)

zigzag_order = []
while zigzag_iterator.hasNext():
    zigzag_order.append(zigzag_iterator.next())

zigzag_order
