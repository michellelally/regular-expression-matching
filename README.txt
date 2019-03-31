Regular Expression Matching with Python

This project is used to match strings of text to a regular expression by building a non-deterministic finite automata for the expression. 
It is done by using a combination of algorithms that can;
Understand both infix and postfix notation expressions and be capable of translating one to the other, 
Read in regular expressions and identify the special characters with each of their meanings
Build a non-deterministic finite automata from a postfix notation expression
Match a string to the regular expression to the equivalent NFA built

Steps:
1. The user should enter either a singular or list of expressions in infix notation that they want to check if it matches a string of text. The expression should include any of the following characters: 
	.		Concatenation of characters, the 2 characters together. 
	|		Alternation of characters, one character or the other 
	*		Any amount, including zero of the character
	?		Only zero or one of the character
	+		Only one or more of the character
	a-z, A-z, 0-9 	Literal charaters, the char in the strings 
	
	Note:	Concatenation character does not have to be included in expression, the program should know its use 		is being implied. The charatercan still be used though if the user would prefer.
		It would be appreciated to try keep the expressions at a limited length for the moment, as described 		in the Issues section, the program may run into a bug with recursion and cause an infinite loop. 		Should this occur, Ctrl+C should stop execution and the expression that caused the bug should be 		altered/removed 

2. The user then can enter the string or a list of strings they want to check the expression against. These strings can be numbers or letters. The user should refrain from using characters as it may cause issues with the special characters. 

3. Once these have been entered, running the program is the next step which will output a True or False as to whether the string was matched against the expression and a list of all expression and strings. 


How it's done

1. Infix to Postfix Conversion Algorithm
The expression is read in infix notation which needs to be converted to postfix. This has to maintaine the order of precedence as it effects the outcome of the matching process.
The function that will deal with the translation, will first check the expression that the concatentation operator has been appeneded where needed. 
It simply will check if the character is one of the special characters. If it is, then there is no need for concatenation and the character will become part of the infix expression
If it is not a special character, it then checks if the character to the right of it is a special character as it will not require concatenation.
Otherwise, the dot will be added just after that character and then to the infix expression. 

Once this has all been done, the expression must be converted to postfix notation. This is accomplished by using an algorithm known as The Shunting Yard Algorithm.

The procedure used is as follows:

    	Expressions are parsed left to right.
    	Each time a number or operand is read, we push it to the stack.
    	Each time an operator comes up, we pop the required operands from the stack, perform the operations, and 	push the result back to the stack.
    	We are finished when there are no tokens (numbers, operators, or any other mathematical symbol) to read. The 	final number on the stack is the result.

A more psuedocode kind of algorithm for the Shunting Yard...

Read in 1 character at a time, we'll call it 'c'
Check if c = '('
	If c is a '(', add/push c to a stack
Check if c = ')'
	If c is a ')'
		Check if the last character added to the stack is a '('
		While the last character added is not a '('
			Take the character at the top of the stack and append it to the postfix expression
			Remove the character from the stack 
If c is a special character, ., |, *, ?, +
	Check the character at the top of the stack and compare the precedence values
	If c's precedence > the character on the stack, 
		Pop the character off the stack and and append it to the postfix expression 
		Remove the character from the stack
	Else if c's precedence < the character on the stack,
		Put c onto the stack
Else
	Put c on the stack 
While the stack is not empty
	Pop the characters from the stack into the postfix expression



2. Postfix to NFA Conversion Algorithm 
The postfix expression is passed into a function which will process it and hopefully build a non-deterministic finite automata from it, as long as it doesn't run into any bugs!!
The algorithm that makes this possible, is known as Thompsons Construction. 
It gives the idea of breaking an expression into a collection of small NFA's, one for each character in the expression, which will be combined to provide a diagram of one large NFA which will then be used to check if a string matches the expression. 

The procedure used is as follows:

    	Expressions are parsed left to right.
	Each character that is read in, has an NFA built for it. 
	The NFA will require an initial state and an accept state.
	Each NFA is added to a stack where all the letters' NFA's will exist
	When a special character is read, the NFA's on the stack will then be removed. It can be 1 or 2, dependent 	on the type of special character
	The NFA's will then be joined to create a bigger NFA which is then added to the stack
	Adding each individual NFA to the stack everytime 

Thompsons Construction Psuedocode...

An NFA class will contain an inital and an accept state which will both have a label for the character and at least one arrow and at most 2 arrows
Read in 1 character at a time, we'll call it 'c'
If c = '.'
	Pop 2 NFA's off the stack
	Take an arrow from the accept state of the first NFA 
	Set it to equal to the initial state of the second NFA
	This creates a new NFA 
	Append the new NFA to the stack

If c = '|'
	Pop 2 NFA's off the stack
	A new initial and accept state needs to be created
	Take the arrows of the new initial state and join it to the inital state of the first and second NFA 
	Take the arrows of the new accept state and join accept states of the first and second NFA to the new accept state

If c = '*'
	Pop single nfa from the stack 
	Create new initial and accept states
	Take an arrow from the new initial state and join it to the NFA's initial state
        Take an arow from the initial state and let it equal an accept state
	Join the old accept state to the new accept state
	This creates a new NFA 
	Append it to the stack
	
if c = '+'
	Pop single nfa from the stack 
	Create new initial and accept states
	Take an arrow from the new initial state and join it to the NFA's initial state
	Join the old accept state to the NFA's initial state
	Take an edge from the NFA's initial state and join it to the new accept state
	This creates a new NFA 
	Append it to the stack



Not sure about this test data, didn't really spend too much time on making proper data that really tests the internals of the program 

Test Data: 
inifixes = ["abc*", "a?(b|d)c*", "(a(b|d))*", "d(bb)c?", "b+aa?", "d+(ba)*", "b*(b?d?)c"]
strings = ["", "abc", "abccc", "abbc", "bbcc", "abad", "daab", "abbbc", "dbdbc", "abbabcc"]

