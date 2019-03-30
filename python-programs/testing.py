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


#

word = "a(bb)*c"
infix = iter(word)


temp = ""

for c in infix:
    try:
        if c in ('+', '|', '?', '*', '.', '('):
            temp += c
        else:
            if next(infix) not in ('+', '|', '?', '*', '.', ')'):
                temp += c + "."
                print("2")
            else: 
                temp += c
                print("3")
    except StopIteration:
        temp += c
        break

print("temp : ", temp)
