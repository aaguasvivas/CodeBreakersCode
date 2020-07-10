from stack_implementation import myStack


class myQueue:
    def __init__(self):
        self.queueList = []

    def isEmpty(self):
        return len(self.queueList) == 0

    def front(self):
        if self.isEmpty():
            return None
        return self.queueList[0]

    def back(self):
        if self.isEmpty():
            return None
        return self.queueList[-1]

    def size(self):
        return len(self.queueList)

    def enqueue(self, value):
        self.queueList.append(value)

    def dequeue(self):
        if self.isEmpty():
            return None
        front = self.front()
        self.queueList.remove(self.front())
        return front


'''
1.Start with Enqueuing 1
2.Dequeue a number from queue
3.append 0 to it and enqueue it back to queue.
4.Perform step 2 but with appending 1 to the
  origional number and enqueue back to queue.

Queue takes integer values so before enqueueing it make
sure to convert String to integer. Size of Queue should
be 1 more than number because for a single number we're
enqueing two variations of it , one with appended 0
while other with 1 being appended.
'''


def findBin(number):
    result = []
    queue = myQueue()
    queue.enqueue(1)

    for i in range(number):
        result.append(str(queue.dequeue()))
        s1 = result[i] + "0"
        s2 = result[i] + "1"
        queue.enqueue(s1)
        queue.enqueue(s2)
    return result  # For number = 3, result = {"1","10","11"}

# 1.Push first k elements in queue in a stack.
# 2.Pop Stack elements and enqueue them at the end of queue
# 3.Dequeue queue elements till "k" and append them at the end of queue


def reverse(queue, k):
    if queue.isEmpty() is True or k > queue.size() or k < 0:
        # Handling invalid input
        return None

    stack = myStack()
    for i in range(k):
        stack.push(queue.dequeue())

    while stack.isEmpty() is False:
        queue.dequeue(stack.pop())

    size = queue.size()

    for i in range(size - k):
        queue.enqueue(queue.dequeue())

    return queue
