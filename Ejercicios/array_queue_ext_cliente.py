from array_queue_ext import ArrayQueueExt

Cola = ArrayQueueExt()

Cola.enqueue(1)
Cola.enqueue(2)
Cola.enqueue(3)

print("Cola original:\n", Cola,"\n")

Cola.rotate()

print("Cola despues de la rotacion:\n", Cola, "\n")

elem = Cola.dequeue()

print("Elemento removido:", elem, "\n")

print("Cola final:\n", Cola, "\n")
