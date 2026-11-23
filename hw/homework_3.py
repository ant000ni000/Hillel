# Запитайте у користувача висоту h та ширину w і виведіть прямокутник із символів * розміром h * w.
#
# Наприклад, для висоти 3 і ширини 5:
#
# Copy code
# *****
# *****
# *****
# (Додаткове завдання) по цим даним виведіть ще 3 фігури:
# 1) Прямокутний трикутник
#
# Copy code
# *
# **
# ***
# ****
# *****
# 2) Перевернутий трикутник
#
# Copy code
# *****
# ****
# ***
# **
# *
# 3) Квадрат із порожниною всередині
#
# Copy code
# *****
# *   *
# *   *
# *   *
# *****


h = int(input("Input high: "))
w = int(input("Input width: "))
def square(h,w):
    for i in range(h):
        print("*"* w)

square(h,w)
def triangle(h,w):
    average = w/h
    for i in range(1,h+1):
        print("*" * (round(average * i)))
triangle(h,w)

def anti_triangle(h,w):
    average = w/h
    for integer in [x for x in range(h,0,-1)]:
        print("*" * (round(average * integer)))
anti_triangle(h,w)

def hollow_square(h,w):
    for i in range(h):
        if i == 0 or i == h-1:
            print("*"* w)
        else:
            print("*"+ " " * (w-2) +"*")
hollow_square(h,w)