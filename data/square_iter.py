class SquareIterator:
    def __init__(self, sequence) -> None:
        self._sequence = sequence
        self._index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self._index >= len(self._sequence):
            raise StopIteration
        square = self._sequence[self._index] ** 2
        self._index += 1
        return square


if __name__ == "__main__":
    for x in SquareIterator([1, 2, 3, 4]):
        print(x)
