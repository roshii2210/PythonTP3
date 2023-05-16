from queue_base_stack import QueueBasedStack

Pila = QueueBasedStack()

Pila.push(1)
Pila.push(2)
Pila.push(3)

print("Pila original: \n", Pila, "\n")

top_elem = Pila.top()
print("Ultimo elemento de la pila :", top_elem, "\n")

popped_elem = Pila.pop()
print("Elemento removido de la pila :", popped_elem, "\n")

print("Pila despues de las operaciones: \n", Pila, "\n")

while not Pila.is_empty():
    elem = Pila.pop()
    print("Elemento removido:", elem, "\n")

print("Pila final: \n", Pila, "\n")
