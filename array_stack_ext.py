from data_structures import ArrayStack

class ArrayStackExt(ArrayStack):
    def __init__(self, maxlen=None) -> None:
        super().__init__()
        self.maxlen = maxlen

    def push(self, elem):
        if self.maxlen is not None and len(self._data) >= self.maxlen:
            raise Exception()
        super().push(elem)



