# description: https://leetcode.com/problems/implement-stack-using-queues/description/


class MyStack(object):

    def __init__(self):
        self.queue = []
        

    def push(self, x):
        self.queue.append(x)
        

    def pop(self):
        return self.queue.pop()
        

    def top(self):
        return self.queue[-1]
        

    def empty(self):
        return True if not self.queue else False

def main():
    obj = MyStack()

    obj.push(1)
    param_4 = obj.empty()
    param_2 = obj.top()
    param_3 = obj.pop()
    param_4 = obj.empty()

    print(param_2, param_3, param_4)


main()
