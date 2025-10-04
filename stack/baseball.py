def calPoints(operations):
    """
    :type operations: List[str]
    :rtype: int
    """
    operation_stack = []

    x = 0
    while x < len(operations):
        curr = operations[x]

        if(curr == '+'):
            el1 = operation_stack[-1]
            el2 = operation_stack[-2]
            acc = el1 + el2
            operation_stack.append(acc)

        elif(curr == 'C'):
            removed_el = operation_stack.pop()

        elif(curr == 'D'):
            el = operation_stack[-1]
            el = el * 2
            operation_stack.append(el)

        else:
            operation_stack.append(int(curr))
        
        x+= 1

    return sum(operation_stack)


arr = ["5", "2", "C", "D", "+"]

print(calPoints(arr))
