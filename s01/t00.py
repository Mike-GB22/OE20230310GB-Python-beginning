print("mip230310")
print("Задача 0.")
print("Найти наибольшее число из 2х\n")

a = int(input("Input A: "))
b = int(input("Input B: "))

print("")

if a == b:
    print ("A and B is equal")
elif a > b:
    print (f"A [{a}] is more then B [{b}]")
else:
    print (f"B [{b}] is more then A [{a}]")

print("")