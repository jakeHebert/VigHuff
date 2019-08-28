class HuffPQ:
    """
    Huffman Priority Queue implemented by a minimum heap.
    Stores the HuffTrees in a binary tree.
    """
    def __init__(self):
        self._pq = []

    def __len__(self):
        """
        Returns the length of the queue.
        """
        return len(self._pq)

    def heapify(self, index):
        """
        Restore the Min Heap order starting
        with the element at the given index
        """
        left_index = self.get_left_child(index)
        right_index = self.get_right_child(index)
        smallest = index

        if (left_index < len(self)) and self._pq[left_index].compare(self._pq[index]) < 0:
            smallest = left_index

        if (right_index < len(self)) and self._pq[right_index].compare(self._pq[smallest]) < 0:
            smallest = right_index

        if smallest != index:
            temp = self._pq[index]
            self._pq[index] = self._pq[smallest]
            self._pq[smallest] = temp

            self.heapify(smallest)

    def get_parent(self, index):
        """
        Return the parent index of the element at the given index
        """
        return (index-1) // 2

    def get_left_child(self, index):
        """
        Return the left child index of the element at the given index
        """
        return 2*index + 1

    def get_right_child(self, index):
        """
        Return the right child index of the element at the given index
        """
        return 2*index + 2

    def dequeue(self):
        """
        Remove the root element which has the minimum value
        """
        if len(self) == 0:
            return None

        if len(self) == 1:
            root = self._pq[0]
            self._pq = []
            return root

        root = self._pq[0]
        self._pq[0] = self._pq[len(self) - 1]
        del self._pq[len(self) - 1]

        self.heapify(0)
        return root

    def enqueue(self, tree):
        """
        Inserts a new element into the min heap at the bottom
        Then restore the heap order
        """
        self._pq.append(tree)
        index = len(self) - 1

        # Swap the element at the given index with its parent,
        # until the parent is smaller than that element

        while (index != 0) and (self._pq[self.get_parent(index)].compare(self._pq[index]) > 0):

            temp = self._pq[index]
            self._pq[index] = self._pq[self.get_parent(index)]
            self._pq[self.get_parent(index)] = temp

            index = self.get_parent(index)

    def peek(self):
        """
        Returns the node with minimum value.
        :return: the root of the HuffTree.
        """
        return self._pq[0]

    def __str__(self):
        str_heap = ""
        for i in range(len(self)):
            str_heap += " || " + str(self._pq[i])
            if (i+1) % 3 == 0:
                str_heap += "\n"
        return str_heap
