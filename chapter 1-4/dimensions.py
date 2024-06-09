#creatimg immutable lists (cannot be changed along the course of the program) A TUPLE

dimensions = (200,40)
print(dimensions[0])
print(dimensions[1])

#dimensions.append(52)
#error because it cannot be changed

#instead, we can change the value assigned to the variable, making it a new tuple all together
dimensions = (80,5)
print (dimensions[0])
print (dimensions[1])