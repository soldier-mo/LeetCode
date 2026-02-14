# description: https://leetcode.com/problems/implement-queue-using-stacks/description/


class MyQueue(object):

    def __init__(self):
        self.stack1 = []
        self.stack2 = []

    def push(self, x):
        self.stack1.append(x)

    def pop(self):
        if (not self.stack2):
            while self.stack1:
                self.stack2.append(self.stack1.pop())

        return self.stack2.pop()

    def peek(self):
        if (not self.stack2):
            while self.stack1:
                self.stack2.append(self.stack1.pop())

        return self.stack2[-1]

    def empty(self):
        return not self.stack1 and not self.stack2


def main():
    obj = MyQueue()



    obj.push(1)
    obj.push(2)
    print(obj.peek())
    print(obj.pop())
    print(obj.empty())

main()
