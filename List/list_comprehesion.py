
car = ["BMW","Toyata","Aston Martin","Mercedeze","Tata"]
 
new_car = [car for car in car if "M" in car ]


print(new_car)

#copy list

copy_car = car.copy()
print(copy_car)


new_car = car + new_car
print(new_car)