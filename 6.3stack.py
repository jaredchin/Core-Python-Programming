stack = []

def pushit():
    stack.append(input(' Enter New string: ').strip())

def popit():
    if len(statck) == 0:
        print('Cannot pop from an empty stack!')
    else:
        print('Removed [', `stack.pop()`, ']')