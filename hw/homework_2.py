# Створіть програму, яка перевіряє дані реєстрації. Користувач 4-ма окремими функціями input() вводить 4 значення: ім'я користувача, електронна адреса, вік та пароль. Наприклад:
#
# username = "student_01"
#
# email = "student@example.com"
#
# age = 20
#
# password = "Python123"
#
# При перевірці даних треба застосовувати наступні правила:
#
# ім'я користувача містить щонайменше 5 символів, не може починатись з числа і не має пробілів;
# електронна адреса обов'язково містить 1 символ @;
# вік може бути тільки з цифр і не менший за 16;
# пароль має щонайменше 8 символів, не може містити пробіли і не може складатись з одного й того ж символа;
# Програма повинна вивести загальний результат валідації (валідні данні чи ні) та окремо пояснити кожну невдалу перевірку (що саме не так саме у цьому значенні).
#
name = input("Input your name: ")
email = input("Input your email: ")
age = input("Input your age: ")
password = input("Input your passwird: ")

if len(name) >= 5 and not name[0].isdigit() and not " " in name:
    print("Name is correct")
else:
    print("Name Error")
if "@" in email:
    print("Email is correct")
else:
    print("Email Error")
if age.isdigit() and int(age) > 16:
    print("age is correct")
else:
    print("Age error")
if len(password) > 8 and len(set(password.split()))>1 and " " not in password:
    print("Password is correct")
else:
    print("Password error")