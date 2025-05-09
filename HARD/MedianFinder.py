'''
The median is the middle value in an ordered integer list. If the size of the list is even, there is no middle value, and the median is the mean of the two middle values.

For example, for arr = [2,3,4], the median is 3.
For example, for arr = [2,3], the median is (2 + 3) / 2 = 2.5.
Implement the MedianFinder class:

MedianFinder() initializes the MedianFinder object.
void addNum(int num) adds the integer num from the data stream to the data structure.
double findMedian() returns the median of all elements so far. Answers within 10-5 of the actual answer will be accepted.
 

Example 1:

Input
["MedianFinder", "addNum", "addNum", "findMedian", "addNum", "findMedian"]
[[], [1], [2], [], [3], []]
Output
[null, null, null, 1.5, null, 2.0]

Explanation
MedianFinder medianFinder = new MedianFinder();
medianFinder.addNum(1);    // arr = [1]
medianFinder.addNum(2);    // arr = [1, 2]
medianFinder.findMedian(); // return 1.5 (i.e., (1 + 2) / 2)
medianFinder.addNum(3);    // arr[1, 2, 3]
medianFinder.findMedian(); // return 2.0
 

Constraints:

-105 <= num <= 105
There will be at least one element in the data structure before calling findMedian.
At most 5 * 104 calls will be made to addNum and findMedian.
 

Follow up:

If all integer numbers from the stream are in the range [0, 100], how would you optimize your solution?
If 99% of all integer numbers from the stream are in the range [0, 100], how would you optimize your solution?

'''

import heapq

class MedianFinder(object):
    def __init__(self):
        """
        Initialize two heaps:
        - self.small is a max-heap (we store negatives) for the lower half of numbers.
        - self.large is a min-heap for the upper half.
        Invariant:
        len(self.small) == len(self.large)  or  len(self.small) == len(self.large) + 1
        """
        self.small = []  # max-heap via negatives
        self.large = []  # min-heap

    def addNum(self, num):
        """
        :type num: int
        :rtype: None
        """
        # 1) Push onto max-heap (small)
        heapq.heappush(self.small, -num)
        # 2) Balance: move the largest from small → large
        heapq.heappush(self.large, -heapq.heappop(self.small))

        # 3) Maintain size invariant: small can have at most one more
        if len(self.large) > len(self.small):
            heapq.heappush(self.small, -heapq.heappop(self.large))

    def findMedian(self):
        """
        :rtype: float
        """
        # If odd total, small has one extra
        if len(self.small) > len(self.large):
            return float(-self.small[0])
        # If even, average the two heaps' tops
        return (-self.small[0] + self.large[0]) / 2.0
