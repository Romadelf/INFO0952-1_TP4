class Queue:
    def __init__(self):
        self.items = []

    def enqueue(self, val):
        self.items.insert(0, val)

    def dequeue(self):
        return self.items.pop()

    def isempty(self):
        return self.items == []


if __name__ == "__main__":
    q = Queue()
    q.enqueue(1)
    q.enqueue(2)
    print(q.dequeue())  # 1
    print(q.isempty())  # False
    print(q.dequeue())  # 2
    print(q.isempty())  # True
