#2.1. Разработать скрипт с функцией, которая строит таблицу истинности для логического выражения (по вариантам) для двух и трех аргументов (используются различные наборы значений аргументов). Вариант 8
print('Задание № 1 (3,5,15)')


def function(a,b,c):
  return int(a and (b or (not b) and (not c)))

def func():
  print('_'*31)
  print(chr(124)+'  A'+'  '+chr(124)+' '+' B  '+chr(124)+' '+' C  '+chr(124)+'A∧(B∨¬B∧¬C)'+''+chr(124))
  print('-'*31)
  for a1 in range(0,2):
    for b1 in range(0,2):
      for c1 in range(0,2):
        print('| ', a1,' | ', b1 , ' | ', c1, ' |    ' ,function(a1,b1,c1), '    |');
        print('-'*31) 

func()
def test_function():
  assert function(0,0,0) == 0
  assert function(0,0,1) == 0
  assert function(0,1,0) == 0
  assert function(0,1,1) == 0
  assert function(1,0,0) == 1
  assert function(1,0,1) == 0
  assert function(1,1,0) == 1
  assert function(1,1,1) == 1

test_function()


print('\n')

def function1(x,y,z):
  return int((x or y) and (not z))

def func1():
  print('_'*31)
  print(chr(124)+'  A'+'  '+chr(124)+' '+' B  '+chr(124)+' '+' C  '+chr(124)+' (A∨B)∧¬C'+'  '+chr(124))
  print('-'*31)
  for a2 in range(0,2):
    for b2 in range(0,2):
      for c2 in range(0,2):
        print('| ', a2,' | ', b2 , ' | ', c2, ' |    ' ,function1(a2,b2,c2), '    |');
        print('-'*31) 

func1()

def test_function1():
  assert function1(0,0,0) == 0
  assert function1(0,0,1) == 0
  assert function1(0,1,0) == 1
  assert function1(0,1,1) == 0
  assert function1(1,0,0) == 1
  assert function1(1,0,1) == 0
  assert function1(1,1,0) == 1
  assert function1(1,1,1) == 0

test_function1()

print('\n')


def function2(w,e):
  return int(not (not w) or e and w or (not (not e) or w))

def func2():
  print('_'*27)
  print(chr(124)+'  B'+'  '+chr(124)+' '+' C  '+chr(124)+'¬B→C∧B∨(¬C→B)'+chr(124))
  print('-'*27)
  for b3 in range(0,2):
    for c3 in range(0,2):
      print('| ', b3 , ' | ', c3, ' |     ' ,function2(b3,c3), '     |');
      print('-'*27) 

func2()

def test_function3():
  assert function2(0,0) == 0
  assert function2(0,1) == 1
  assert function2(1,0) == 1
  assert function2(1,1) == 1

test_function3()

print('\n')
