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
            # Push c onto the stack
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

# Plans for something you might create in memory 
# Can be reused
# represents a state with 2 arrows labelled by label
# use none for a label representing 'e' arrows
class state: 
    # Character 
    label = None
    # In arrow
    edge1 = None
    # Out arrow
    edge2= None

# an nfa
class nfa: 
    initial = None
    accept = None

    # Constructor in python starts and ends in 2 underscores
    # Every function must also has to have self as its first parameter 
    def __init__(self, initial, accept):
        self.initial = initial
        self.accept = accept

def compile(pofix):
    # Stack of NFA's 
    nfastack = []

    for c in pofix: 
        # Catenation
        if c == '.':
            nfa2 =  nfastack.pop()
            nfa1 = nfastack.pop()
            # take 1 of the edges of the accept state and let it 
            # equal to the initial state in the second NFA
            nfa1.accept.edge1 = nfa2.initial
            newnfa = nfa(nfa1.initial, nfa2.accept)
            nfastack.append(newnfa)

        # Alternation
        elif c == '|':
            # pop 2 nfa's off the stack
            nfa2 =  nfastack.pop()
            nfa1 = nfastack.pop()
            # creating an instance of state and connect it to
            # the initial states of the nfa's popped from the stack
            initial = state()
            # creating an instance of state and connect it to
            # the accept states of the nfa's popped from the stack
            accept = state()
            # join initial's in arrow to the inital state of nfa1
            initial.edge1 = nfa1.initial
            # join initial's out arrow to the inital state of nfa2
            initial.edge2 = nfa2.initial
            # nfa1 and nfa2 initial states are no longer
            # initial states because theyre pointing
            # nfa1 accept state to point at the new accept state
            nfa1.accept.edge1 = accept
            # nfa2 accept state to point at the new accept state
            nfa2.accept.edge1 = accept
            # push new nfa to the stack
            newnfa = nfa(initial, accept)
            nfastack.append(newnfa)

        # Zero or more
        elif c == '*':
            # pop single nfa from the stack 
            nfa1 = nfastack.pop()
            # create new initial and accept states
            # creating an instance of state
            accept = state()
            # creating an instance of state
            initial = state()
            # join the new initial state to nfa1's initial state and the
            # new accept state
            initial.edge1 = nfa1.initial
            initial.edge2 = accept
            # join the old accept state to the new accept stare and nfa1's
            # initial state
            nfa1.accept.edge1 = nfa1.initial
            nfa1.accept.edge2 = accept
            # push new nfa to the stack 
            newnfa = nfa(initial, accept)
            nfastack.append(newnfa)

        # Zero or one
        elif c == '?':
             # pop single nfa from the stack 
            nfa1 = nfastack.pop()
            # create new initial and accept states
            # creating an instance of state
            accept = state()
            # creating an instance of state
            initial = state()

            initial.edge1 = nfa1.initial
            initial.edge2 = accept

            # join the old accept state to the new accept stare and nfa1's
            # initial state
            nfa1.accept.edge1 = accept
            # nfa1.accept.edge2 = accept
            # push new nfa to the stack 
            newnfa = nfa(initial, accept)
            nfastack.append(newnfa)

        # One or more
        elif c == '+':
            # pop single nfa from the stack 
            nfa1 = nfastack.pop()
            # create new initial and accept states
            # creating an instance of state
            accept = state()
            # creating an instance of state
            initial = state()
            # join the new initial state to nfa1's initial state and the
            # new accept state
            initial.edge1 = nfa1.initial
            # join the old accept state to the new accept stare and nfa1's
            # initial state
            nfa1.accept.edge1 = nfa1.initial
            nfa1.accept.edge2 = accept
            # push new nfa to the stack 
            newnfa = nfa(initial, accept)
            nfastack.append(newnfa)



        else:
            # creating an instance of state
            accept = state()
            # creating an instance of state
            initial = state()
            # label of arrow coming out of the initial state is going to be c
            initial.label = c
            # edge1 points to the accept state
            initial.edge1 = accept
            # creates a new instance of the NFA class and set the initial state to the initial state just created and the same with accept
            nfastack.append(nfa(initial, accept))
    
    # nfastack should only have a single nfa at the end
    return nfastack.pop()

def followes(state):
    """ Return the set of states that can be reached from states following the e arrows """
    # Create a new set, with state as its only member 
    states = set()
    states.add(state)

    # check id the state that has arrows e from it 
    if state.label is None:
        # check if edge1 is a state
        if state.edge1 is not None:
        # if theres an edge 1, follow it 
            states |= followes(state.edge1)
        # check if edge2 is a state
        if state.edge2 is not None:
        # if theres an edge 2 follow it
            states |= followes(state.edge2)

    # Return the set of states
    return states



def match(infix, string):
    """ Matches the string to the infix regular expression"""

    # shunt and compile the regular epxression 
    # turn infix into postfix
    postfix = shunt(infix)
    # print("postfix: " ,postfix)
    # compile the postfix expression into an nfa
    nfa = compile(postfix)

    #the currrent states and the next states
    current = set()
    next = set()

    # Add the initial state to the current set
    current |= followes(nfa.initial)


    # loop through each character in the string
    for s in string:
        # loop through the current set of states 
        for c in current:
            # check if that state is labelled s 
            if c.label == s: 
                # add the edg1 state to the next set 
                next |= followes(c.edge1)
        #set current to next, and clear out next
        current = next
        next = set()

    #check is the accept state is in the currect states
    return (nfa.accept in current)


#inifixes = ["a.b.c*", "a.(b|d).c*", "(a.(b|d))*", "a.(b.b)*.c"]
#strings = ["", "abc", "abbc", "abcc", "abad", "abbbc"]

inifixes = ["a+"]
strings = ["", "a", "aa"]

for i in inifixes:
    for s in strings:
        print(match(i, s), i, s)

    

