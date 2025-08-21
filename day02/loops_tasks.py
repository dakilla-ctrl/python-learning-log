# Print even numbers from 1 - 20
x = range(1, 21)
for i in x:
    if i % 2 == 0:
        print(i)
    else:
        print('odd')


# Count how many times "a" appears in a string
xx = input('Enter word: ')
c = input('pick a letter: ')
print(c + ' appears ' + str(xx.count(c)) + ' times ')


# FizzBuzz from 1 - 50
for i in range(1, 51):
    if i % 3 == 0 and i % 5 == 0:
        print('FizzBuzz')
    elif i % 3 == 0:
        print('Fizz')
    elif i % 5 == 0:
        print('Buzz')
    else:
        print(i)


# Reverse a string
s = 'testing'
slist = slice(None, None, -1)
print(s[slist])


