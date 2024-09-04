n = int(input("Size :"))

list = []

for _ in range(n):
    num = int(input())
    list.append(num)

idx1 = int(input("Enter index1 :"))
idx2 = int(input("Enter index2 :"))
print("Before swapping : ",list)


temp = list[idx1]
list[idx1] = list[idx2]
list[idx2] = temp

print("After swapping : ",list)