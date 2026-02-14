# description: https://leetcode.com/problems/implement-stack-using-queues/description/


class MyStack(object):

    def __init__(self):
        self.queue1 = []
        self.queue2 = []

    def push(self, x):
        self.queue2.append(x)

        while self.queue1:
            self.queue2.append(self.queue1.pop(0))

        self.queue1, self.queue2 = self.queue2, self.queue1

    def pop(self):
        return self.queue1.pop(0)

    def top(self):
        return self.queue1[0]

    def empty(self):
        return len(self.queue1) == 0


def main():
    obj = MyStack()

    obj.push(1)
    print(obj.top())
    obj.push(2)
    print(obj.top())

    obj.push(3)
    print(obj.pop())
    print(obj.empty())


main()
