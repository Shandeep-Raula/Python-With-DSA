# List :- It allows to store multiple items

car = ["BMW","Toyata","Aston Martin","Mercedeze","Tata"]

print(car)

print(type(car))

print(len(car))

if "Tata" in car:
    print("Tata present")

if "Thar" not in car:
    print("Thar is not present")

for i in car:
    print(i)   

print(car[1])

print(car[1:3])

car.append("Lamabergini")
print(car)

car.insert(1,"Range Rover")
print(car)

car2 = ["Porche","Ferrari"]
car.extend(car2)
print(car)

car.pop(1)
print(car)

car.remove("Tata")
print(car)

car[1:3] = ["Pagani"]
print(car) 

car.sort()
print(car)


car.sort(reverse=True)
print(car)