from Node import Node

class ListaSE:
    def __init__(self):
        self.head = None  # Cabeça da lista

    def insert(self, id, name):
        # Insere um nó no início da lista.
        new_node = Node(id, name)
        new_node.next = self.head
        self.head = new_node

    def remove(self, id):
        # Remove um nó da lista pelo ID
        current = self.head
        prev = None
        while current is not None:
            if current.id == id:
                if prev:
                    prev.next = current.next
                else:
                    self.head = current.next
                return True  # ID encontrado e removido
            prev = current
            current = current.next
        return False  # ID não encontrado

    def display(self):
        # Exibe os elementos da lista.
        current = self.head
        print(f"{'ID':<5} {'Nome'}")
        print('-' * 20)
        while current:
            print(f"{current.id:<5} {current.name}")
            current = current.next

    def reverse(self):
        # Inverte a lista
        prev = None
        current = self.head
        while current is not None:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
        self.head = prev

    def bubble_sort(self, by='id'):
        # Ordena a lista pelo ID ou pelo nome usando Bubble Sort
        if self.head is None or self.head.next is None:
            return

        end = None
        while end != self.head:
            current = self.head
            while current.next != end:
                next_node = current.next
                if by == 'id':
                    if current.id > next_node.id:
                        # Troca os dados dos nós
                        current.id, next_node.id = next_node.id, current.id
                        current.name, next_node.name = next_node.name, current.name
                elif by == 'name':
                    if current.name > next_node.name:
                        # Troca os dados dos nós
                        current.id, next_node.id = next_node.id, current.id
                        current.name, next_node.name = next_node.name, current.name
                current = current.next
            end = current

    def search(self, id):
        current = self.head
        steps = 0
        while current:
            steps += 1
            if current.id == id:
                return current, steps
            current = current.next
        return None, steps
