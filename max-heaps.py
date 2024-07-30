class MaxHeap:  # Define a new class called MaxHeap
    def __init__(self):  # Initialize the MaxHeap instance
        self.heap = []  # Create an empty list to store heap elements

    def insert(self, key):  # Method to insert a new key into the heap
        self.heap.append(key)  # Add the new key to the end of the heap
        self._bubble_up(len(self.heap) - 1)  # Maintain the max-heap property

    def delete_max(self):  # Method to remove and return the maximum element
        if len(self.heap) == 0:  # Check if the heap is empty
            return None  # Return None if the heap is empty
        if len(self.heap) == 1:  # If there's only one element in the heap
            return self.heap.pop()  # Remove and return that element
        
        max_value = self.heap[0]  # Store the maximum value (root)
        self.heap[0] = self.heap.pop()  # Move the last element to the root
        self._bubble_down(0)  # Restore the max-heap property
        return max_value  # Return the maximum value

    def peek(self):  # Method to return the maximum element without removing it
        return self.heap[0] if self.heap else None  # Return root if heap is not empty

    def _bubble_up(self, index):  # Helper method to maintain max-heap property after insertion
        parent_index = (index - 1) // 2  # Calculate the parent index
        if index > 0 and self.heap[index] > self.heap[parent_index]:  # If the current node is greater than its parent
            self.heap[index], self.heap[parent_index] = self.heap[parent_index], self.heap[index]  # Swap them
            self._bubble_up(parent_index)  # Recursively bubble up the parent

    def _bubble_down(self, index):  # Helper method to maintain max-heap property after deletion
        largest = index  # Start with the current index as the largest
        left_child = 2 * index + 1  # Calculate the left child index
        right_child = 2 * index + 2  # Calculate the right child index

        if left_child < len(self.heap) and self.heap[left_child] > self.heap[largest]:  # If left child is larger
            largest = left_child  # Update largest to left child
        if right_child < len(self.heap) and self.heap[right_child] > self.heap[largest]:  # If right child is larger
            largest = right_child  # Update largest to right child

        if largest != index:  # If the largest is not the current index
            self.heap[index], self.heap[largest] = self.heap[largest], self.heap[index]  # Swap with the largest
            self._bubble_down(largest)  # Recursively bubble down the largest

    def __str__(self):  # Method to return a string representation of the heap
        return str(self.heap)  # Return the string representation of the heap list

max_heap = MaxHeap()  # Create an instance of MaxHeap
max_heap.insert(5)  # Insert the value 5 into the heap
max_heap.insert(3)  # Insert the value 3 into the heap
max_heap.insert(8)  # Insert the value 8 into the heap
max_heap.insert(1)  # Insert the value 1 into the heap

print("Max-Heap:", max_heap)  # Print the current state of the max-heap
print("Maximum:", max_heap.peek())  # Print the maximum value in the heap
print("Deleted Maximum:", max_heap.delete_max())  # Print the deleted maximum value
print("Max-Heap after deletion:", max_heap)  # Print the state of the max-heap after deletion
