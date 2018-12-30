memory = [None]

def dereference_pointer(pointer):
    return memory[pointer]

class Node(object):
    def __init__(self, npx, element):
        self.npx = npx
        self.element = element
        memory.append(self)
        self.__address = len(memory) - 1

    def get_pointer(self):
        return self.__address

class XORLinkedList(object):
    def __init__(self):
        self.__header = None
        self.__trailer = None
        self.__size = 0

    def add(self, element):
        if self.__trailer:
            npx = self.__trailer ^ 0
            node = Node(npx, element)
            temp_last_trailer = dereference_pointer(self.__trailer)
            temp_last_trailer.npx = temp_last_trailer.npx ^ 0 ^ (node.get_pointer())
        else:
            npx = 0 ^ 0
            node = Node(npx, element)
            self.__header = node.get_pointer()
        self.__trailer = node.get_pointer()
        self.__size += 1

    def get(self, index):
        index += 1
        if index * 2 > self.__size:
            beginner = dereference_pointer(self.__trailer)
            current_prev_pointer = 0
            traverse_l = range(self.__size, index, - 1)
        elif index * 2 <= self.__size:
            beginner = dereference_pointer(self.__header)
            current_prev_pointer = 0
            traverse_l = range(index - 1)
        else:
            return None

        current_node = beginner
        for count in traverse_l:
            temp_prev_pointer = current_prev_pointer
            current_prev_pointer = current_node.get_pointer()
            current_node = dereference_pointer(current_node.npx ^ temp_prev_pointer)
        return current_node