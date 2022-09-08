x = [2, 5, 13, 17, 3, 89, 3, 5, 2, 90, 5, 65]
y = [25, 8, 7, 11, 1, 5, 7, 6, 8, 4]

number = input('Enter desired number: ')
array = input('Enter desired array (x,y): ')


if array == 'x':
    counter = x.count(int(number))
    print('The amount of times in which', number, 'appears', 'in array', array,'is:', counter)

elif array == 'y':
    counter = y.count(int(number))
    print('The amount of times in which', number, 'appears', 'in array', array,'is:', counter)

else:
    print('INVALID!')


input()