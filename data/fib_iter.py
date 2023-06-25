"""
https://realpython.com/python-iterators-iterables/#understanding-iteration-in-python
Instead of yielding items from an existing data stream,
your FibonacciIterator class computes every new value in real time,
yielding values on demand. Note that in this example,
you relied on the default number of Fibonacci numbers, which is 10.
"""


class FibonacciIterator:
    def __init__(self, stop=10) -> None:
        self._stop = stop
        self._index = 0
        self._current = 0
        self._next = 1

    def __iter__(self):
        return self

    def __next__(self):
        if self._index >= self._stop:
            raise StopIteration
        self._index += 1
        fib_number = self._current
        self._current, self._next = (self._next, self._current + self._next)
        return fib_number


if __name__ == "__main__":
    for fib_number in FibonacciIterator():
        print(fib_number)
