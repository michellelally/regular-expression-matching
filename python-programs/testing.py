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