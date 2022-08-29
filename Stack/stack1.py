# Best example is browser history undo any last taskor 
#!LIFO: Last In First Out
#TODO: Push/Pop : 0(1), Search element by value: 0(N)

#! Stacks using List

stack =[]
stack.append(10)
stack.append(20)
stack.append(30)
stack.append(40)
stack.append(50)

stack.pop()
print(stack)

#? checks the stack empty or not
print(len(stack) == 0)
print(not stack)

# ? Accessing the last element
print(stack[-1])


#! Stacks using Modules