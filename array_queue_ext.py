from data_structures import ArrayQueue

class ArrayQueueExt(ArrayQueue):
    def rotate(self):
        if super().is_empty():
            raise Exception("Estructura vacía. No se puede continuar")
        if super().is_full():
            raise Exception("Estructura llena. No se puede continuar")
        elem = super().dequeue()
        super().enqueue(elem)