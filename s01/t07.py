print("mip230310")
print("Задача №7."
      + "Дано натуральное число. Требуется определить, является ли год с данным номером високосным.\n"
      + "Если год является високосным, то выведите YES, иначе выведите NO.\n"
      + "Напомним, что в соответствии с григорианским календарем, год является високосным,\n"
      + "если его номер кратен 4, но не кратен 100, а также если он кратен 400.\n"
      + "Input: 2016\n"
      + "Output: YES\n"
      )

year = int(input("Какой год: "))
flag = year%400 == 0 or (year%4 == 0 and year%100!=0)
yesNo = ["нет", "да"]


print(f"\nГод [{year}] является высокосным: ", yesNo[flag])








