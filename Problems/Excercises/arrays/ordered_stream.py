'''
There is a stream of n (idKey, value) pairs arriving in an arbitrary order,
where idKey is an integer between 1 and n and value is a string. No two pairs have the same id.

Design a stream that returns the values in increasing order of their IDs by
returning a chunk (list) of values after each insertion. The concatenation of all the
chunks should result in a list of the sorted values.

Implement the OrderedStream class:

OrderedStream(int n) Constructs the stream to take n values.
String[] insert(int idKey, String value) Inserts the pair (idKey, value) into the stream,
then returns the largest possible chunk of currently inserted values that appear next in the order.
'''

class OrderedStream(object):

    def __init__(self, n: int):
        """
        :type n: int
        """
        self.n = n
        self.stream = [None] * self.n
        self.pointer = 0

    def insert(self, idKey, value):
        """
        :type idKey: int
        :type value: str
        :rtype: List[str]
        """
        self.stream[idKey - 1] = value
        res = []
        if idKey - 1 == self.pointer and self.stream[self.pointer]:
            while self.pointer < self.n and self.stream[self.pointer]:
                res.append(self.stream[self.pointer])
                self.pointer += 1
            return res