class MinHeap:  # Define a new class called MinHeap
    def __init__(self):  # Initialize the MinHeap instance
        self.heap = []  # Create an empty list to store heap elements

    def insert(self, key):  # Method to insert a new key into the heap
        self.heap.append(key)  # Add the new key to the end of the heap
        self._bubble_up(len(self.heap) - 1)  # Maintain the min-heap property

    def delete_min(self):  # Method to remove and return the minimum element
        if len(self.heap) == 0:  # Check if the heap is empty
            return None  # Return None if the heap is empty
        if len(self.heap) == 1:  # If there's only one element in the heap
            return self.heap.pop()  # Remove and return that element
        
        min_value = self.heap[0]  # Store the minimum value (root)
        self.heap[0] = self.heap.pop()  # Move the last element to the root
        self._bubble_down(0)  # Restore the min-heap property
        return min_value  # Return the minimum value

    def peek(self):  # Method to return the minimum element without removing it
        return self.heap[0] if self.heap else None  # Return root if heap is not empty

    def _bubble_up(self, index):  # Helper method to maintain min-heap property after insertion
        parent_index = (index - 1) // 2  # Calculate the parent index
        if index > 0 and self.heap[index] < self.heap[parent_index]:  # If the current node is smaller than its parent
            self.heap[index], self.heap[parent_index] = self.heap[parent_index], self.heap[index]  # Swap them
            self._bubble_up(parent_index)  # Recursively bubble up the parent

    def _bubble_down(self, index):  # Helper method to maintain min-heap property after deletion
        smallest = index  # Start with the current index as the smallest
        left_child = 2 * index + 1  # Calculate the left child index
        right_child = 2 * index + 2  # Calculate the right child index

        if left_child < len(self.heap) and self.heap[left_child] < self.heap[smallest]:  # If left child is smaller
            smallest = left_child  # Update smallest to left child
        if right_child < len(self.heap) and self.heap[right_child] < self.heap[smallest]:  # If right child is smaller
            smallest = right_child  # Update smallest to right child

        if smallest != index:  # If the smallest is not the current index
            self.heap[index], self.heap[smallest] = self.heap[smallest], self.heap[index]  # Swap with the smallest
            self._bubble_down(smallest)  # Recursively bubble down the smallest

    def __str__(self):  # Method to return a string representation of the heap
        return str(self.heap)  # Return the string representation of the heap list

min_heap = MinHeap()  # Create an instance of MinHeap
min_heap.insert(5)  # Insert the value 5 into the heap
min_heap.insert(3)  # Insert the value 3 into the heap
min_heap.insert(8)  # Insert the value 8 into the heap
min_heap.insert(1)  # Insert the value 1 into the heap

print("Min-Heap:", min_heap)  # Print the current state of the min-heap
print("Minimum:", min_heap.peek())  # Print the minimum value in the heap
print("Deleted Minimum:", min_heap.delete_min())  # Print the deleted minimum value
print("Min-Heap after deletion:", min_heap)  # Print the state of the min-heap after deletion