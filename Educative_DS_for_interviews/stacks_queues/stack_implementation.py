import numpy as np


class myStack:
    def __init__(self):
        self.stackList = []

    def isEmpty(self):
        return self.size() == 0

    def top(self):
        if self.isEmpty():
            return None
        return self.stackList[-1]

    def size(self):
        return len(self.stackList)

    def push(self, value):
        self.stackList.append(value)

    def pop(self):
        if self.isEmpty():
            return None
        return self.stackList.pop()


# Challenge 2: Implement Two Stacks Using One List


class twoStacks:
    def __init__(self, n):
        self.size = n
        self.arr = np.zeros([n], dtype=int)
        self.top1 = -1
        self.top2 = self.size

    def push1(self, x):
        if self.top1 < self.top2 - 1:
            self.top1 = self.top1 + 1
            self.arr[self.top1] = x
        else:
            print("Stack Overflow")
            exit(1)

    def push2(self, x):
        if self.top1 < self.top2 - 1:
            self.top2 = self.top2 - 1
            self.arr[self.top2] = x
        else:
            print("Stack Overflow")
            exit(1)

    def pop1(self):
        if self.top1 >= 0:
            x = self.arr[self.top1]
            self.top1 = self.top1 - 1
            return x
        else:
            print("Stack Overflow")

    def pop2(self):
        if self.top2 < self.size:
            x = self.arr[self.top2]
            self.top2 = self.top2 + 1
            return x
        else:
            print("Stack Overflow")
            exit(1)

# We can use 2 stacks for this purpose,mainStack to store original values
# and tempStack which will help in enqueue operation.
# Main thing is to put first entered element at the top of mainStack


class newQueue:
    def __init__(self):
        # Can use size from argument to create stack
        self.mainStack = myStack()
        self.tempStack = myStack()
    # Inserts element in the queue

    def enqueue(self, value):
        # Push the value into mainStack in O(1)
        self.mainStack.push(value)
        print(str(value) + " enqueued")
        return True

    # Removes element from queue
    def dequeue(self):
        # If both stacks are empty, end operation
        if self.tempStack.isEmpty():
            if self.mainStack.isEmpty():
                return None
            # Transfer all elements to tempStack
            while self.mainStack.isEmpty() is False:
                value = self.mainStack.pop()
                self.tempStack.push(value)
        # Pop the first value. This is the oldest element in the queue
        temp = self.tempStack.pop()
        print(str(temp) + " dequeued")
        return temp


"""
1. Use a second tempStack.
2. Pop value from mainStack.
3. If the value is greater or equal to the top of tempStack,
  then push the value in tempStack
  else pop all values from tempStack
      and push them in mainStack
      and in the end push value in tempStack
4.repeat from step 2 till mainStack is not empty.
5. When mainStack will be empty,
    tempStack will have sorted values in descending order.
6. Now transfer values from tempStack to mainStack
    to make values sorted in ascending order.
"""


def sortStack(stack):

    tempStack = myStack()

    while stack.isEmpty() is False:

        value = stack.pop()

        if tempStack.top() is not None and value >= int(tempStack.top()):
            # If value is not not none and larger, push it at the top of tempStack
            tempStack.push(value)
        else:
            while tempStack.isEmpty() is False:
                stack.push(tempStack.pop())
            # Place value as the smallest element in tempStack
            tempStack.push(value)
    # Transfer from tempStack to stack
    while tempStack.isEmpty() is False:
        stack.push(tempStack.pop())


def sortStack_sort(stack):
    stack.stackList.sort(reverse=True)
    return stack


def evaluatePostFix(exp):
    stack = myStack()
    for char in exp:
        if char.isdigit():
            # Push numbers in stack
            stack.push(char)
        else:
            # Use top two numbers and evaluate
            left = stack.pop()
            right = stack.pop()
            stack.push(str(eval(right + char + left)))
    # Final answer should be a number
    return int(float(stack.pop()))


def nextGreaterElement(lst):
    s = myStack()
    res = [-1] * len(lst)

    # Reverse iterate list
    for i in range(len(lst) - 1, -1, -1):
        # If stack has elements:
        if not s.isEmpty():
            # While stack has elements
            # and current element is greater than top element
            # pop all elements
            while not s.isEmpty() and s.top() <= lst[i]:
                s.pop()
        # if stack has an element
        # top element will be greater than ith element
        if not s.isEmpty():
            res[i] = s.top()
        # push in the current element in stack
        s.push(lst[i])

    return res


def isBalanced(exp):
    # Iterate through the string exp.
    # For each opening parentheses, push it into stack
    # For every closing parentheses check
    # for its opening parentheses in stack
    # If you can't find the opening parentheses
    # for any closing one then returns false.
    # and after complete traversal of string exp,
    # if there's any opening parentheses left
    # in stack then also return false.
    # At the end return true if you haven't
    # encountered any of the above false conditions.
    closing = ['}', ')', ']']
    stack = myStack()

    for character in exp:
        if character in closing:
            if stack.isEmpty():
                return False
            topElement = stack.pop()
            if character is '}' and topElement is not '{':
                return False
            if character is ')' and topElement is not '(':
                return False
            if character is ']' and topElement is not '[':
                return False
        else:
            stack.push(character)
    if stack.isEmpty() is False:
        return False
    return True


class minStack:
    # Constructor
    def __init__(self):
        self.minStack = myStack()
        self.mainStack = myStack()
        return

        # Removes and returns value from minStack
    def pop(self):
        self.minStack.pop()
        return self.mainStack.pop()

        # Pushes values into minStack
    def push(self, value):
        self.mainStack.push(value)
        if(self.minStack.isEmpty() or self.minStack.top() > value):
            self.minStack.push(value)
        else:
            self.minStack.push(self.minStack.top())

        # Returns minimum value from newStack in O(1) Time

    def min(self):
        if not self.minStack.isEmpty():
            return self.minStack.top()
