from typing import Any
from array_queue_ext import ArrayQueueExt

class QueueBasedStack(ArrayQueueExt):
    def push(self, elem: Any) -> None:
        self.enqueue(elem)

    def pop(self) -> Any:
        if self.is_empty():
            raise Exception("La pila está vacía")
        return self.dequeue()

    def top(self) -> Any:
        if self.is_empty():
            raise Exception("La pila está vacía")
        return self._data[self._front]