#setting or creating an empty list
motorcycles = []

#adding elements to list [.append() can also be used to add to the end of the list] 
motorcycles.insert(0, "quadbike")
motorcycles.insert(1, "suzuki")
motorcycles.insert(0 , "yokohama")
motorcycles.append("yamaha")
motorcycles.append("boxer")
motorcycles.append("royal")
print(motorcycles)

#removing element from list
del motorcycles[0]
print(motorcycles)

#removing element from a list using value
motorcycles.remove('royal')
print(motorcycles)

#removing an element from the list and utilizing it
motor1 = motorcycles.pop(0)
print(motorcycles)
print(motor1)

too_expensive = "suzuki"
motorcycles.remove(too_expensive)
print(motorcycles)
print(f"\t A {too_expensive.title()} is too expensive for me you know")