# Michelle Lally
# Shunting Yard Algorithm 

def shunt(infix):
    specials = {'*': 50, '.': 40, '|': 30}
    pofix = ""
    stack = ""

    for c in infix:
        if c == '(':
            stack = stack + c
        elif c == ')':
            # Check the last character in the string
            while stack[-1] != '(':
                # Pushing the operators at the end of the stack to pofix as long as it's not the open bracket
                pofix = pofix + stack[-1]
                # Remove that operator from the stack
                stack = stack[:-1]
            # Remove the ( from the stack 
            stack = stack[:-1]
        elif c in specials: 
            # Check while theres something on the stack, and c's precedence is <= the precedence on the stack
            # specials.get(c , 0) means if c is in specials, get its value from the dictionary otherwise give it the value 0
            # Then check if whats on top of the stack is in specials and get its value from the dictionary otherwise give it 0
            while stack and specials.get(c, 0) <= specials.get(stack[-1], 0):
                # Remove the operator at the top of the stack and put it into pofix 
                pofix, stack = pofix + stack[-1], stack[:-1]
            stack = stack + c
        else:
           pofix = pofix + c 

    while stack:
        # Pushing the operators at the end of the stack to pofix as long as it's not the open bracket
        pofix = pofix + stack[-1]
        # Remove that operator from the stack
        stack = stack[:-1]
        # Remove the ( from the stack 
    return pofix

print(shunt("(a.b)|(c*.d)"))