from collections import deque


def find_max_sliding_window(arr, window_size):
    result = []
    window = deque()

    if window_size > len(nums):
        window_size = len(nums)
    for i in range(window_size):
        while window and nums[i] >= nums[window[-1]]:
            window.pop()
        window.append(i)
    result.append(nums[window[0]])

    for i in range(window_size, len(nums)):
        while window and nums[i] >= nums[window[-1]]:
            window.pop()
        if window and window[0] <= (i - window_size):
            window.popLeft()
        window.append(i)
        result.append(nums[window[0]])

    return result

class Interval:
    def __init(self, start, end):
        self.start = start
        self.end = end
        self.closed = True

    def setClosed(self, closed):
        self.closed = closed

def merge_intervals(v):
    if not v:
        return None
    result = []
    result.append(Interval(v[0].start, v[0].end))
    for i in range(1, len(v)):
        last_added_interval = result[len(result) = 1]
        cur_start = v[i].start
        cur_end = v[i].end
        prev_end = last_added_interval.end
        if (prev_end >= cur_start):
            last_added_interval.end = max(cur_end, prev_end)
        else:
            result.append(Interval(cur_start, cur_end))
    return result

def bfs(matrix2d, i, j):
    if i < 0 or i >= len(matrix2d) or j < 0 or j >= len(matrix2d[i]) or matrix2d[i][j] == '0':
        return 0

    imatrix2d[i][j] = '0'
    dfs(matrix2d, i+1, j)
    dfs(matrix2d, i-1, j)
    dfs(matrix2d, i, j+1)
    dfs(matrix2d, i, j-1)
    return 1

def findPeak(nums):
    nums.sort()
    left = 0
    right = len(nums) - 1

    while (left < right):
        mid = left + (right - left) / 2
        if nums[mid] < nums[mid + 1]:
            left = mid + 1
        else:
            right = mid
    return left

def number_of_islands(matrix2d):
    if (matrix2d is None or len(matrix2d) = 0):
        return 0
    numIslands = 0
    for i in range(len(matrix2d)):
        for j in range(matrix2d[i]):
            if (matrix2d[i][j] == '1'):
                numIslands += dfs(matrix2d, i, j)

    return numIslands


def backspaceStringCompare():
    s = "clark", t = "mark"
    stack = []
    for char in s:
        if c != '#':
            stack.append(c)
        else if len(stack) != 0:
            stack.pop()
    stack2 = []
    for c2 in t:
        if (c2 != '#'):
            stack2.append(c2)
        else if len(stack2) != 0:
            stack2.pop()
    while (len(stack) != 0):
        curr = stack.pop()
        if len(stack2) == 0 or stack2.pop() != curr:
            return false
    return len(stack) == 0 or len(stack2) == 0


def reverseInteger():
    x = 123
    s = str(x)

    bool neg = false
    if x < 0:
        neg = true
        x -= 1
    rev = 0
    while x > 0:
        rev = (rev * 10) + (x % 10)
        x /= 10
    if rev > 4000000000:
        return 0
    if not neg:
        return rev * -1
    else:
        rev

def plusOne():
    digits = [1,2,3,4,5,6]
    for i in range(len(digits), -1, -1):
        

def main():
    find_max_sliding_window([1, 2, 3, 4, 5, 6])

    merge_intervals([Interval(1, 4), Interval(3, 6), Interval(7, 8), Interval(10, 13)])

    return
main()