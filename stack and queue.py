
class Stack:
    '''
        A stack uses a LIFO policy , the last element to be inserted is the one removed first i.e a stack of plates
    '''
    def __init__(self, args = []):
        self.args = args
    def push(self,x):
        self.args.append(x)
    def pop(self):
        if self.args != []:
            self.args.pop()

stack = Stack([1,3,5,7])
stack.pop()
stack.push(11)
#prints 1 3 5 11
print(stack.args)


class Queue:
    '''
        A queue follows a FIFO policy, the first element inserted is usually the first to be ejected i.e a bank queue
    '''
    def __init__(self, args = []):
        self.args = args
    def enqueue(self,x):
        self.args.append(x)
    def dequeue(self):
        if self.args != []:
            self.args.pop(0)
            
            
queue = Queue([1,2,3,4])
queue.enqueue(5)
queue.dequeue()
# returns 2 3 4 5
print(queue.args)


