#2.2. Разработать программу, которая выводит на экран с помощью ASCII-графики таблицу истинности на основе переданных ей на вход аргументов (логическое выражение, аргументы, результат вычисления выражения). Формирование отчета по выполнению задания и размещение его в портфолио, персональном репозитории. 

## Сухачева Валерия, 2 курс 1 подгруппа ИВТ

print('-'*45)
print(chr(124) + "  A  "+chr(124)+"  B"+'  '+ chr(124)+ '  '+'A and B  ' + chr(124)+"  "+ "A or B"+'  '+ chr(124)+ '  '+'A->B  '+chr(124))
print('-'*45)
a = False
b = False
print(chr(124)+ '  ' + str(int(a))+ '  '+chr(124)+'  '+ str(int(b))+'  '+ chr(124)+ '     '+str(int(a and b))+ '     ' + chr(124)+'     '+ str(int(a or b))+'    '+ chr(124)+ '   '+str(int(not a or b))+ '    '+chr(124))
print('-'*45)
a = False
b = True
print(chr(124)+ '  ' + str(int(a))+ '  '+chr(124)+'  '+ str(int(b))+'  '+ chr(124)+ '     '+str(int(a and b))+ '     ' + chr(124)+'     '+ str(int(a or b))+'    '+ chr(124)+ '   '+str(int(not a or b))+ '    '+chr(124))
print('-'*45)
a = True
b = False
print(chr(124)+ '  ' + str(int(a))+ '  '+chr(124)+'  '+ str(int(b))+'  '+ chr(124)+ '     '+str(int(a and b))+ '     ' + chr(124)+'     '+ str(int(a or b))+'    '+ chr(124)+ '   '+str(int(not a or b))+ '    '+chr(124))
print('-'*45)
a = True
b = True
print(chr(124)+ '  ' + str(int(a))+ '  '+chr(124)+'  '+ str(int(b))+'  '+ chr(124)+ '     '+str(int(a and b))+ '     ' + chr(124)+'     '+ str(int(a or b))+'    '+ chr(124)+ '   '+str(int(not a or b))+ '    '+chr(124))
print('-'*45)
