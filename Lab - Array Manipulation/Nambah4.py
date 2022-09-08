x = [2, 5, 13, 17, 3, 89, 3, 5, 2, 90, 5, 65]

x.remove(89), x.remove(90), x.remove(65), x.append(42)

result = 0
for n in x:
    result = result + n

print('The sum of all the elements is equal to ',result)