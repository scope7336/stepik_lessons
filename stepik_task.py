"""num = int(input())
num_1 = num + 1
num_2 = num - 1
print(num, num_1, num_2 )
n = int(input())
print('The next number for the number ' + str(n) + ' is ' + str(n + 1) + '.')
print('The previous number for the number ' + str(n) + ' is ' + str(n - 1) + '.')"""

"""cost_1 = int(input(" Введите стоимость монитора: "))
cost_2 = int(input("Введите стоимость системного блока: "))
cost_3 = int(input("Введите стоимость клавиатуры: "))
cost_4 = int(input("Введите стоимость мыши: "))
multip_1 = (cost_1 * 3)
multip_2 = (cost_2 * 3)
multip_3 = (cost_3 * 3)
multip_4 = (cost_4 * 3)
print(multip_1 + multip_2 + multip_3 + multip_4)"""

"""num_1 = int(input())
num_2 = int(input())
print(f"{num_1} + {num_2} = {num_1 + num_2}")
print(f"{num_1} - {num_2} = {num_1 - num_2}")
print(f"{num_1} * {num_2} = {num_1 * num_2}")"""

"""a1 = int(input())
d = int(input())
n = int(input())
an = (a1 + d * (n - 1))
print(an)"""

"""x = int(input())
y = x + x
z = x + y
v = z + x
n = v + x
print(x, y, z, v, n, sep = "---")"""

# geometric progression
"""b1 = int(input())
q = int(input())
n = int(input())
print(b1 * q ** (n-1))"""

# distance in meter
"""meter = int(input())
cent = (meter // 100)
print(cent)"""

# tangerines
"""n = int(input())
k = int(input())
tan = (k // n)
nut = (k % n)
print(tan, nut, sep="\n")"""

# The very inevitability
"""n = int(input())
print(n//2  + n%2)"""

# compartment number
"""n = int(input())
print((n - 1)//4+1)"""

# Time interval recalculation
"""min = int(input())
print(min, f'мин - это {min // 60} час {min % 60} минут.')"""

# three-digit number
"""num = int(input())
last_num = (num % 10)
second_num = (num // 10) % 10
first_num = (num // 100)
print("Сумма цифр =", last_num + second_num + first_num)
print("Произведение цифр =", last_num * second_num * first_num)"""

# permutation of numbers
"""abc = int(input())
c = (abc % 10)
b = (abc // 10) % 10
a = (abc // 100)
print(a, b, c, sep= "")
print(a, c, b, sep = "")
print(b, a, c, sep='')
print(b, c, a, sep='')
print(c, a, b, sep='')
print(c, b, a, sep='')"""

# four_digit number
"""abcde= int(input())
d = abcde % 10
c = abcde % 100 // 10
b = abcde % 10000 //1000
a =  abcde // 10000
e = abcde % 1000 // 10
print(a)
print(b)
print(c)
print(d)
print(e)"""

# password
"""passw_1 = input()
passw_2 = input()
if passw_1 != passw_2:
    print("Пароль не принят")
if passw_1 == passw_2:
    print("Пароль принят")"""

# Even, Odd
"""num = int(input())
if num  % 2 == 0:
    print("четное ")
else:
    print("нечетное")"""

# ratio
"""num = int(input())
num_1 = num // 1000 # first digit
num_2 = num // 100 % 10 # second digit
num_3 = num % 100 // 10 # third digit
num_4 = num % 10 # fourth digit
if num_1 +num_4 == num_2 - num_3:
    print("ДА")
else:
    print("НЕТ")"""

# Roskomnadzor
"""age = int(input())
if age >= 18:
    print("Доступ разрешен ")
else:
    print("Доступ запрещен")"""

# Arithmetic progression
"""a1 = int(input())
a2 = int(input())
a3 = int(input())
if a2 - a1 == a3 -a2:
    print("YES")
else:
    print("NO")"""

# the smallest of two numbers
"""num_1 = int(input())
num_2 = int(input())
if num_1 > num_2:
    print(num_2)
else:
    print(num_1)"""

# the smallest of four numbers
"""a, b, c, d = int(input()), int(input()), int(input()), int(input())
if a > b:
    a = b
if c > d:
    c = d
if a > c:
    a = c
print(a)"""

# growing group
"""age = int(input())
if age <= 13:
    print("детство")
if age >= 14 and age <= 24:
    print("молодость")
if age >= 25 and age <= 59:
    print("зрелость")
if age >= 60:
    print("старость")"""

# only plus
"""num_1 = int(input())
num_2 = int(input())
num_3 = int(input())
sum = 0
if num_1 > 0 :
    sum += num_1

if num_2 > 0:
    sum += num_2

if num_3 > 0:
    sum += num_3
print(sum)"""

# affoliation one
"""x = int(input())
if -1 < x < 17:
    print("Принадлежит")
else:
    print("Не принадлежит")"""

# affoliation two
"""x = int(input())
if x <= -3 or x >= 7:
    print("Принадлежит")
else:
    print("Не принадлежит")"""

# affoliantion three
"""x = int(input())
if -30 < x <= -2 or 7 < x <= 25:
    print("Принадлежит")
else:
    print("Не принадлежит")"""

# beautiful number
"""num = int(input())
if 1000 <= num <= 9999 and (num % 7 == 0  or num % 17 == 0):
    print("YES")
else:
    print("NO")"""

# inequality of a triangle
"""a = int(input())
b = int(input())
c = int(input())
if a < b + c and b < c + a and c < b + a:
    print("YES")
else:
    print("NO")"""

# Leap year
"""year = int(input())
if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
    print("YES")
else:
    print("NO")"""

# Rook move
"""x_1 = int(input())
y_1 = int(input())
x_2 = int(input())
y_2 = int(input())
if x_1 == x_2 or y_1 == y_2:
    print("YES")
else:
    print("NO")"""

# king's move
"""x_1 = int(input())
y_1 = int(input())
x_2 = int(input())
y_2 = int(input())
if (x_1 - 1 <= x_2 <= x_1 + 1) and (y_1 <= y_2 <= y_1 + 1):
    print("YES")
else:
    print("NO")"""


# Speedster race
"""zoom_n = int(input())
flash_k = int(input())
if zoom_n > flash_k :
    print("NO")
elif flash_k > zoom_n:
    print("YES")
elif zoom_n == flash_k:
    print("Don't know")"""


# triangle view
"""a = int(input())
b = int(input())
c = int(input())
if a == b and b == c and c == a:
    print("Равносторонний")
elif a == b or b == c or c == a:
    print("Равнобдеренный")
else:
    print("Разносторонний")"""


# Average number
"""num_1 = int(input())
num_2 = int(input())
num_3 = int(input())
if num_2 < num_1 < num_3 or num_3 < num_1 < num_2:
    print(num_1)
elif num_1 < num_2 < num_3 or num_3 < num_2 < num_1:
    print(num_2)
else:
    print(num_3)"""


# amount of days
"""month = int(input())
if month == 4 or month == 6 or month == 11 or month == 9:
    print("30")
elif month == 2:
    print("28")
else :
    print("31")"""


# weighing ceremony
"""weight = int(input())
if weight <= 59:
    print("Легкий вес")
elif 60 <= weight < 64:
    print("Первый полусредний вес")
elif 64 <= weight <= 69:
    print("Полусредний вес")"""


# handwritten calculatorelif
"""num = int(input())
num_1 = int(input())
math_op = input()
if math_op == "+":
    print(num + num_1)
elif math_op == "-":
    print(num - num_1)
elif math_op == "*":
     print(num * num_1)
elif math_op == "/":
    if num_1 == 0:
        print("На ноль делить нельзя!")
    else:
        print(num / num_1)
else:
    print("Неверная операция")"""

# color mixer
"""main_color = input()
main_color1 = input()
if main_color == ("красный, желтый, синий"):
    main_color = True
if main_color1 == ("красный, желтый, синий"):
    main_color1 = True
elif main_color == ("красный") and main_color1 == ("синий") or main_color == ("синий") and main_color1 == ("красный"):
    print("фиолетовый")
elif main_color == ("красный") and main_color1 == ("желтый") or main_color == ("желтый") and main_color1 == ("красный"):
    print("оранжевый")
elif main_color == ("синий") and main_color1 == ("желтый") or main_color == ("желтый") and main_color1 == ("синий"):
    print("зеленый")
elif main_color == ("красный") and main_color1 == ("красный"):
    print("красный")
elif main_color == ("синий") and main_color1 == ("синий"):
    print("синий")
elif main_color == ("желтый") and main_color1 == ("желтый"):
    print("желтый")
else:
    print("ошибка цвета")"""


# roulette wheel color
"""number = int(input())
if number == 0:
    print("зеленый")
elif number <= -1:
    print("ошибка ввода")
elif number <= 10 and number % 2 == 0:
    print("черный")
elif number <= 10 and number % 2 != 0:
    print("красный")
elif 11 <= number <= 18 and number % 2 == 0:
    print("красный")
elif 11 <= number <= 18 and number % 2 != 0:
    print("черный")
elif 19 <= number <= 28 and number % 2 == 0:
    print("черный")
elif 19 <= number <= 28 and number % 2 != 0:
    print("красный")
elif 29 <= number <= 36 and number % 2 == 0:
    print("красный")
elif 29 <= number <= 36 and number % 2 != 0:
    print("черный")
else:
    print("ошибка ввода")"""


# area of triangle
"""a = float(input())
b = float(input())
c = (a * b) / 2
print(c)"""


# two old ladies
"""speed = float(input())
lad_1 = float(input())
lad_2 = float(input())
time = speed / (lad_1 + lad_2)
print(time)"""


# reverse number
"""a = float(input())
if a == 0:
    print("Обратного числа не существует")
else:
    print(1 / a)"""


# 451 degrees Fahrenheit
"""degress_fahr = float(input())
degrees_cel = 5 / 9 * (degress_fahr - 32)
print(degrees_cel)"""


# dog age
"""age = int(input())
if age <= 2:
    print(age * 10.5)
elif age > 2:
    print((age - 2) * 4 + 21)"""


# first digit after dot
"""a = float(input())
b = (a * 10)
c = int(b % 100)
m = int(c % 10)
print(m)"""


# fractional part
"""numb = float(input())
frac = (numb % 1)
print(frac)"""


# the largest and the smallest
"""a = int(input())
b = int(input())
c = int(input())
d = int(input())
e = int(input())
num_min = (min(a, b, c, d, e))
num_max = (max(a, b, c, d, e))
print("Наименьшее число =", num_min)
print("Наибольшее число =", num_max)"""


# sorting three
"""first_num = int(input())
second_num = int(input())
third_num = int(input())
print(max(first_num, second_num, third_num))
print(first_num + second_num + third_num - (min(first_num, second_num, third_num) + max(first_num, second_num, third_num)))
print(min(first_num, second_num, third_num))"""


# interesting number
"""a,b,c = input()
a = int(a)
b = int(b)
c = int(c)
if a + b + c - max(a,b,c) - min(a,b,c) == max(a,b,c) - min(a,b,c):
    print("Число интересное")
else:
    print("Число неинтересное")"""


# absolute amount
"""a_1, a_2, a_3, a_4, a_5 = float(input()), float(input()), float(input()), float(input()), float(input())
print(abs(a_1) + abs(a_2) + abs(a_3) + abs(a_4) + abs(a_5))"""


# Manhattan distance
"""p_1 = int(input())
p_2 = int(input())
q_1 = int(input())
q_2 = int(input())
distance_m = abs(p_1 - q_1) + abs(p_2 - q_2)
print(distance_m)"""