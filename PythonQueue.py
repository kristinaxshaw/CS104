names = []
x = 0
while x < 10:
    acceptedName = input('Enter the name of the next person in line: ')
    names.append(acceptedName)
    x = x + 1
print ('\nThis is the line order.')
while len(names):
    print (names.pop(0))
