class Stack:
    def __init__(self):
        self.list = []
        self.cnt = 0
        self.stacks = [[] for _ in range(3)]


    def push(self, item, stack_number):
        # choose from 1, 2, 3
        stack_index = stack_number - 1
        self.stacks[stack_index].append(self.cnt)
        self.list.append(item)
        self.cnt += 1


    def pop(self, stack_number):
        # choose from 1, 2, 3
        stack_index = stack_number - 1
        if len(self.stacks[stack_index]) <= 0:
            return None
        result = self.list[self.stacks[stack_index].pop()]
        self.cnt -= 1
        return result


if __name__ == '__main__':
    stack = Stack()
    stack.push(1, 1)
    stack.push(2, 1)
    stack.push(3, 1)
    stack.push(5, 2)
    stack.push(6, 3)
    print(stack.pop(1))
    print(stack.pop(2))
    print(stack.pop(3))
    print(stack.pop(1))
