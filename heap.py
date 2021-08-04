# encoding=utf8

def parent(i):
    return (i - 1) // 2


def left(i):
    return 2 * i + 1


def right(i):
    return 2 * i + 2


class MaxHeap:
    def __init__(self):
        self.length = 0
        self.data = []

    def add(self, value):
        self.data.append(value)
        self.length += 1
        self.shift_up(self.length-1)

    def shift_up(self, index):
        if index <= 0:
            return
        parent_index = parent(index)
        if self.data[index] > self.data[parent_index]:
            self.data[index], self.data[parent_index] = self.data[parent_index], self.data[index]
            self.shift_up(parent_index)

    def pop(self):
        if self.length <= 0:
            raise Exception('empty')
        v = self.data[0]
        self.data[0] = self.data[self.length-1]
        self.length -= 1
        self.shift_down(0)
        return v

    def shift_down(self, index):
        if index >= self.length:
            return
        left_child = left(index)
        right_child = right(index)
        max_index = index
        if left_child < self.length and self.data[left_child] > self.data[max_index]:
            max_index = left_child
        if right_child < self.length and self.data[right_child] > self.data[max_index]:
            max_index = right_child
        if max_index == index:
            return
        self.data[index], self.data[max_index] = self.data[max_index], self.data[index]
        self.shift_down(max_index)

    def sort(self, numbers):
        for i in numbers:
            self.add(i)
        values = []
        for i in range(0, self.length-1):
            values.append(self.pop())
        return values

numbers = [2, 2, 2, 2, 133, 12, 2, 3, 4, 5, 2, 2, 9, 223, 4, 5, 1489, 24, 5, 2, 5, 70000, 80000, 10000]
print(numbers)
heap = MaxHeap()
numbers = heap.sort(numbers)
print(numbers)
