
# Part 1: Implementing a stack
class Stack:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        else:
            raise IndexError("Stack is empty")

    def peek(self):
        if not self.is_empty():
            return self.items[-1]
        else:
            raise IndexError("Stack is empty")

    def size(self):
        return len(self.items)

# Test the Stack
stack = Stack()
stack.push(1)
stack.push(2)
stack.push(3)
print(stack.pop())  # Should print 3
print(stack.peek())  # Should print 2
print(stack.size())  # Should print 2



# Part 2:Implementing a queue
class Queue:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0

    def enqueue(self, item):
        self.items.append(item)

    def dequeue(self):
        if not self.is_empty():
            return self.items.pop(0)
        else:
            raise IndexError("Queue is empty")

    def front(self):
        if not self.is_empty():
            return self.items[0]
        else:
            raise IndexError("Queue is empty")

    def size(self):
        return len(self.items)

# Test the Queue
queue = Queue()
queue.enqueue(1)
queue.enqueue(2)
queue.enqueue(3)
print(queue.dequeue())  # Should print 1
print(queue.front())  # Should print 2
print(queue.size())  # Should print 2


# Part 3: Solving Practical problems

# Problem 1: Balanced Parenthese
def is_balanced(parentheses):
    stack = Stack()
    for p in parentheses:
        if p == '(':
            stack.push(p)
        elif p == ')':
            if stack.is_empty():
                return False
            stack.pop()
    return stack.is_empty()

# Test the function
print(is_balanced("((()))"))  # Should print True
print(is_balanced("(()"))  # Should print False


# Problem 2: Reverse a string
def reverse_string(s):
    stack = Stack()
    for char in s:
        stack.push(char)
    
    reversed_string = ""
    while not stack.is_empty():
        reversed_string += stack.pop()
    
    return reversed_string

# Test the function
print(reverse_string("Hello, World!"))  # Should print "!dlroW ,olleH"


# Problem 3: Hot Potato Simulation
def hot_potato(names, num):
    queue = Queue()
    for name in names:
        queue.enqueue(name)
    
    while queue.size() > 1:
        for _ in range(num):
            queue.enqueue(queue.dequeue())
        queue.dequeue()
    
    return queue.dequeue()

# Test the function
names = ["Bill", "David", "Susan", "Jane", "Kent", "Brad"]
print(hot_potato(names, 7))  # The winner's name will be printed




# Exercises


# 1.A function that uses a stack to evaluate postfix expressions.
def evaluate_postfix(expression):
    stack = Stack()
    for token in expression:
        if token.isdigit():  # If the token is a number, push to stack
            stack.push(int(token))
        else:
            # Pop two operands for the operator
            right = stack.pop()
            left = stack.pop()
            if token == '+':
                stack.push(left + right)
            elif token == '-':
                stack.push(left - right)
            elif token == '*':
                stack.push(left * right)
            elif token == '/':
                stack.push(left / right)
    return stack.pop()

# Test the function
print(evaluate_postfix("324+37-44*"))  


# 2.Implement Queue Using Two Stacks
class QueueUsingStacks:
    def __init__(self):
        self.stack1 = []  # Stack for enqueue operations
        self.stack2 = []  # Stack for dequeue operations

    def enqueue(self, x):
        """Add an element to the end of the queue."""
        self.stack1.append(x)

    def dequeue(self):
        """Remove the element from the front of the queue."""
        if not self.stack2:  # If stack2 is empty, transfer elements from stack1
            while self.stack1:
                self.stack2.append(self.stack1.pop())
        
        if not self.stack2:  # If stack2 is still empty, the queue is empty
            return -1  # Indicate that the queue is empty
        
        return self.stack2.pop()  # Return the top element from stack2

# Example usage
if __name__ == "__main__":
    queue = QueueUsingStacks()
    queue.enqueue(1)
    queue.enqueue(2)
    queue.enqueue(3)
    
    print(queue.dequeue())  # Output: 1
    print(queue.dequeue())  # Output: 2
    print(queue.dequeue())  # Output: 3
    print(queue.dequeue())  # Output: -1 (queue is empty)



# 3.Task Scheduler Using Queue
def task_scheduler(tasks):
    queue = Queue()
    for task in tasks:
        queue.enqueue(task)

    while not queue.is_empty():
        task = queue.dequeue()
        print(f"Processing task: {task}")

tasks = ["Task 1", "Task 2", "Task 3"]
scheduler = task_scheduler(tasks)


# 4.Convert Infix to Postfix Using Stack

def precedence(op):
    if op in ('+', '-'):
        return 1
    if op in ('*', '/'):
        return 2
    if op == '^':
        return 3
    return 0

def is_right_associative(op):
    return op == '^'

def infix_to_postfix(expression):
    stack = Stack()
    postfix = ""
    for char in expression:
        if char.isalnum():  # If the character is an operand, add it to the result
            postfix += char
        elif char == '(':
            stack.push(char)
        elif char == ')':
            while not stack.is_empty() and stack.peek() != '(':
                postfix += stack.pop()
            stack.pop()  # Remove '('
        else:
            # Pop from stack based on precedence and associativity
            while (not stack.is_empty() and precedence(char) <= precedence(stack.peek()) and
                   (not is_right_associative(char) or precedence(char) < precedence(stack.peek()))):
                postfix += stack.pop()
            stack.push(char)

    # Pop all operators left in the stack
    while not stack.is_empty():
        postfix += stack.pop()

    return postfix

# Test the function
print(infix_to_postfix("a+b*(c^d-e)^(f+g*h)-i"))
