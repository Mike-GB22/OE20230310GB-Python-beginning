print("mip230310")
print("Задача №6. Домашка\n"
      + "Вы пользуетесь общественным транспортом?\n"
      + "Вероятно, вы расплачивались за проезд и получали билет с номером.\n"
      + "Счастливым билетом называют такой билет с шестизначным номером,\n"
      + "где сумма первых трех цифр равна сумме последних трех.\n"
      + "Т.е. билет с номером 385916 – счастливый, т.к. 3+8+5=9+1+6.\n"
      + "Вам требуется написать программу, которая проверяет счастливость билета.\n"
      + " * Прогармма принимает любое количетсво цифр в номере билета.\n"
      )



number = int(input("Введите номер билета (предполагается 6ти значное): "))
if number<10:
      print("Число должно быть положительынм и больше 9")
      raise SystemExit

numberString = str(number)
length = len(numberString)
separator = " + "
sumIntFirstHalf = 0
sumStrFirstHalf = ""
sumIntOtherHalf = 0
sumStrOtherHalf = ""

for iterator in range (0, length//2):
      digitBegin = numberString[iterator]
      sumIntFirstHalf = sumIntFirstHalf + int(digitBegin)

      digitEnd = numberString[length - 1 - iterator]
      sumIntOtherHalf = sumIntOtherHalf + int(digitEnd)

      if iterator == length//2 - 1 :
            separator = " = "
      sumStrFirstHalf = sumStrFirstHalf + digitBegin + separator
      sumStrOtherHalf = sumStrOtherHalf + digitEnd + separator

print(" * Левая  половина: " + sumStrFirstHalf + str(sumIntFirstHalf))
print(" * Правая половина: " + sumStrOtherHalf + str(sumIntOtherHalf))

if length%2 == 1:
      spigel = numberString[length//2]
      print(f" = Зеркальное число билета: {spigel}\n")
      if (int(spigel) == sumIntFirstHalf) and (sumIntFirstHalf == sumIntOtherHalf):
            print("     !!! Супер счастливый билет !!!")

yesNo = ["нет", "да!"]
print(f"Билет с номером [{numberString}] счастливый: {yesNo[sumIntFirstHalf == sumIntOtherHalf]}\n")






