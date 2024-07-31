# Question 1
# Given an array of integers, find the Kth largest element.
import heapq
def find_kth_largest(nums, k):
    return heapq.nlargest(k, nums)[-1]

nums = [3, 2, 1, 5, 6, 4]
k = 2
print(find_kth_largest(nums, k)) 


# Question 2
# Merge K sorted linked lists and return it as one sorted list.
import heapq
def merge_k_lists(lists):
    min_heap = []
    for i, lst in enumerate(lists):
        if lst:
            heapq.heappush(min_heap, (lst[0], i, 0))  

    result = []
    while min_heap:
        val, list_idx, elem_idx = heapq.heappop(min_heap)
        result.append(val)
        if elem_idx + 1 < len(lists[list_idx]):
            next_tuple = (lists[list_idx][elem_idx + 1], list_idx, elem_idx + 1)
            heapq.heappush(min_heap, next_tuple)

    return result
lists = [[1, 4, 5], [1, 3, 4], [2, 6]]
print(merge_k_lists(lists)) 


# QUestion 3
#  Design a data structure that supports adding numbers and finding the median.
import heapq

class MedianFinder:
    def __init__(self):
        self.max_heap = []  
        self.min_heap = [] 

    def add_num(self, num):
        heapq.heappush(self.max_heap, -num)  
        if self.max_heap and self.min_heap and (-self.max_heap[0] > self.min_heap[0]):
            val = -heapq.heappop(self.max_heap)
            heapq.heappush(self.min_heap, val)

        if len(self.max_heap) > len(self.min_heap) + 1:
            val = -heapq.heappop(self.max_heap)
            heapq.heappush(self.min_heap, val)
        elif len(self.min_heap) > len(self.max_heap):
            val = heapq.heappop(self.min_heap)
            heapq.heappush(self.max_heap, -val)

    def find_median(self):
        if len(self.max_heap) > len(self.min_heap):
            return -self.max_heap[0]
        return (-self.max_heap[0] + self.min_heap[0]) / 2
mf = MedianFinder()
mf.add_num(1)
mf.add_num(2)
print(mf.find_median())  
mf.add_num(3)
print(mf.find_median())  


# Question 4
# Given a non-empty array of integers, return the K most frequent elements.
from collections import Counter
import heapq

def top_k_frequent(nums, k):
    count = Counter(nums)
    return heapq.nlargest(k, count.keys(), key=count.get)
nums = [1, 1, 1, 2, 2, 3]
k = 2
print(top_k_frequent(nums, k)) 


# Question 5
# Given an array and a sliding window size, return the maximum value in each sliding window.
from collections import deque

def max_sliding_window(nums, k):
    if not nums:
        return []
    
    deq = deque()
    max_nums = []
    
    for i in range(len(nums)):
        if deq and deq[0] < i - k + 1:
            deq.popleft()
        
        while deq and nums[deq[-1]] < nums[i]:
            deq.pop()
        
        deq.append(i)
        
        if i >= k - 1:
            max_nums.append(nums[deq[0]])
    
    return max_nums
nums = [1, 3, -1, -3, 5, 3, 6, 7]
k = 3
print(max_sliding_window(nums, k))  # Output: [3, 3, 5, 5, 6, 7]