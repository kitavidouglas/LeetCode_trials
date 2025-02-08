import heapq

class NumberContainers(object):

    def __init__(self):
        self.index_to_number = {}  # Maps index -> number
        self.number_to_indices = {}  # Maps number -> min-heap of indices

    def change(self, index, number):
        """
        :type index: int
        :type number: int
        :rtype: None
        """
        if index in self.index_to_number:
            old_number = self.index_to_number[index]
            if old_number in self.number_to_indices:
                self.number_to_indices[old_number].discard(index)  # Remove from old number's set

        # Assign the new number to the index
        self.index_to_number[index] = number
        if number not in self.number_to_indices:
            self.number_to_indices[number] = set()
        
        self.number_to_indices[number].add(index)

    def find(self, number):
        """
        :type number: int
        :rtype: int
        """
        if number not in self.number_to_indices or not self.number_to_indices[number]:
            return -1
        return min(self.number_to_indices[number])
