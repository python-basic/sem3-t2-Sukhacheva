#2.3. Разработать скрипт с функцией, которая для ряда Фибоначчи, где количество элементов, n = 22, возвращает подмножество значений или единственное значение (по вариантам). Для нахождения элемента требуется использовать слайсы. Формирование отчета по выполнению задания и размещение его в портфолио, персональном репозитории. 

lst = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987, 1597, 2584, 4181, 6765, 10946]
print(lst)
print('\n')
print('Задание 2.1')
print(lst[12::-2])
print('\n')
print('Задание 2.22')
car = ("name", " DeLorean DMC-12", "motor_pos", "rear", "n_of_wheels", 4, "n_of_passengers", 2, "weight", 1.230, "height", 1.140, "length", 4.216, "width", 1.857, "max_speed", 177)

for i in car[::2]:
  if type(i) == str:
    print(i)
   
