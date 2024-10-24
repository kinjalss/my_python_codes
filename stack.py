#stack functions push ,pop,is_empty,peek and size(stack)
def push(stack,item):
  stack.append(item)
  print("pushed item",item)

def is_empty(stack):
  return len(stack)==0

def pop(stack):
  if(is_empty(stack)):
    return ("stack is empty")
  return stack.pop()

def peek(stack):
  if(is_empty(stack)):
    return ("stack is empty")
  return stack[-1]

def size(stack):
  return len(stack)

stack=[]
push(stack,10)
push(stack,20)
push(stack,30)
print("popped item",pop(stack))
print("peek element",peek(stack))
print("the size of the stack is ",size(stack))
is_empty(stack)