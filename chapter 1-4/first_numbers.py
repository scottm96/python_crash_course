for value in range(1,5):
    print (value)

#list of numbers
numbers = list(range(6))
print (numbers)

#list of numbers with a step size. for example, to count in twos
even_nums =list(range(2,11,2))
print(f'\n{even_nums}')

squares = []
for value in range(1,21):
    squares.append(value**2)
print (squares)

#some simple funtions
print(min(squares))
print(max(squares))
print(sum(squares))

#list comprehensions
squareser = [value**2 for value in range(1,11)]
print(squareser)