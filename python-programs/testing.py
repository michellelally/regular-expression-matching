s = "|f+o*o?"
d = '101'

for c in s:
    if c not in ('+', '|', '?', '*', '.'):
        print(c)

print('+'.isalnum())
print('*'.isalnum())
print('?'.isalnum())
print('|'.isalnum())
print('.'.isalnum())

infix = "a(bb)*c"

new = ""

temp = ""

for i, c in enumerate(infix):
    if c in ('+', '|', '?', '*', '.', '('):
        temp += c
    else:
        try:
            if infix[i+1] not in ('+', '|', '?', '*', '.', ')'):
                temp += c + "."
                print("2")
            else: 
                temp += c
                print("3")
        except IndexError:
            temp += c
            break

print("temp : ", temp)
