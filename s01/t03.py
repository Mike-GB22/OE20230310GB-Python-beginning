print("mip230310")
print("Задача №3.")
print("В некоторой школе решили набрать три новых математических класса и оборудовать кабинеты для них новыми партами.\n"
      + "За каждой партой может сидеть два учащихся.\n"
      + "Известно количество учащихся в каждом из трех классов.\n"
      + "Выведите наименьшее число парт, которое нужно приобрести для них.\n"
      + "Пример: Input: 20 21 22(ввод чисел НЕ в одну строку); \nOutput: 32")

classes = int(input("\nКоличество классов: "))
iterator = 0
desks = 0
studentsAll = 0
while iterator < classes:
      iterator = iterator + 1
      students = int(input("\nКоличество учащихся в классе №"+str(iterator)+": "))
      studentsAll = studentsAll + students
      tempDesks = int((students+1) / 2)
      desks = desks + tempDesks
     
      print(f"Для класса [{iterator}], где [{students}] учиников, нужно парт: ", tempDesks)

print(f"\nВсего для [{classes}] классов, где в сумме [{studentsAll}] учащихся, нужно парт: ", desks)









