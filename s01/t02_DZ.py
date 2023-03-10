print("mip230310")
print("Задача №2. Домашка\n"
      + "Найдите сумму цифр трехзначного (или любого) числа.\n"
      + "Input: 123\n"
      + "Output: 6\n"
      )

number = int(input("Введите многозначное число: "))
numberString = str(number)
length = len(numberString)
separator = " + "
sumInt = 0
sumString = ""
for iterator in range (0, length):
      digit = numberString[iterator]
      sumInt = sumInt + int(digit)
      if iterator == length -1 :
            separator = " = "+str(sumInt)
      sumString = sumString + digit + separator

print("\n"+sumString)
print(f"Сумма всех цифер числа [{numberString}]: {sumInt}\n")






