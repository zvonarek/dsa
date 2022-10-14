#FIFO
#enqueue: pushing to end of queue, O(1)
#dequeue: remove from the start, O(1)
#contrary to having O(n) with arrays

#225 Implement Stack using Queues
class MyStack:
    def __init__(self):
        self.q = deque()
    def push(self, x:int) -> None:
        self.q.append(x)
    def pop(self) -> int:
        for i in range(len(self.q) - 1):
            self.push(self.q.popleft())
        return self.q.popleft()
    def top(self) -> int:
        return self.q[-1]
    def empty(self) -> bool:
        return len(self.q) == 0