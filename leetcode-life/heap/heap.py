'''
堆是特殊空间的有顺序的完全二叉树，root是最大值的是大顶堆，否者小顶堆
堆：数据流中的第K大（小）问题
heapq 默认是小顶堆
'''

import heapq

# 默认小顶堆
heap = []
heapq.heappush(heap, 19)
heapq.heappush(heap, 4)
heapq.heappush(heap, 9)
heapq.heappush(heap, 10)
heapq.heappush(heap, 10)
heapq.heappush(heap, 11)
heap.remove(10)
print(heap)
print(heapq.nlargest(2, heap))
print(heapq.heappop(heap))  # 返回最小值

# 大顶堆 使用负数
heapmax = [19, 4, 9, 10, 11]
heapm = [-num for num in heapmax]
heapq.heapify(heapm)
print(heapm)
print(-heapq.heappop(heapm))  # 返回最大值

test = []
heapq.heappush(test, -1)
heapq.heappush(test, -2)
heapq.heappush(test, -0)
print(test)
