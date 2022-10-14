class MyCircularQueue:
    def __init__(self, size: int):
        self.cir_queue = [0] * size
        self.rear = -1
        self.front = 0
        self.size = 0

    def enqueue(self, value: int) -> bool:
        if self.is_full():
            return False
        self.rear = (self.rear + 1) % len(self.cir_queue)
        self.cir_queue[self.rear] = value
        self.size += 1
        return True

    def dequeue(self) -> bool:
        if self.is_empty():
            return False
        self.front = (self.front + 1) % len(self.cir_queue)
        self.size -= 1
        return True

    def get_front(self) -> int:
        return -1 if self.is_empty() else self.cir_queue[self.front]

    def get_rear(self):
        return -1 if self.is_empty() else self.cir_queue[self.rear]


    def is_empty(self):
        return self.size == 0

    def is_full(self):
        return self.size == len(self.cir_queue)


# Do not change the following code
operations = []
for specific_operation in input().split(','):
    operations.append(specific_operation.strip())
data = []
for item in input().split(','):
    item = item.strip()
    if item == '-':
        data.append([])
    else:
        data.append([int(item)])
obj = MyCircularQueue(data[0][0])
result = []
for i in range(len(operations)):
    if i == 0:
        result.append(None)
    elif operations[i] == "enqueue":
        result.append(obj.enqueue(data[i][0]))
    elif operations[i] == "get_rear":
        result.append(obj.get_rear())
    elif operations[i] == "get_front":
        result.append(obj.get_front())
    elif operations[i] == "dequeue":
        result.append(obj.dequeue())
    elif operations[i] == "is_full":
        result.append(obj.is_full())
    elif operations[i] == "is_empty":
        result.append(obj.is_empty())

print(result)
