# Thompsons construction 
# Michelle Lally

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
        if c == '.':
            nfa2 =  nfastack.pop()
            nfa1 = nfastack.pop()
            # take 1 of the edges of the accept state and let it 
            # equal to the initial state in the second NFA
            nfa1.accept.edge1 = nfa2.initial
            newnfa = nfa(nfa1.initial, nfa2.accept)
            nfastack.append(newnfa)

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
            # join its arrow to the inital state of nfa1
            initial.edge1 = nfa1.initial
            # join its arrow to the inital state of nfa1
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

        elif c == '.':
            # pop single nfa from the stack 
            nfa1 = nfastack.pop()
            # create new initial and accept states
            # creating an instance of state
            accept = state()
            # creating an instance of state
            initial = state()
            # join the new initla state to nfa1's initial state and the
            # new accept state
            initial.edge1 = nfa1.initial
            initial.edge2 = accept
            # join the old accept state to the new accept srare and nfa1's
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

print(compile("ab.cd.|"))
print(compile("aa.*"))

    

