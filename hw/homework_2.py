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

general_errors = []

if len(name)<5:
    general_errors.append("Error in name: Name has to be longer than 5 symbols")
if name and name[0].isdigit():
    general_errors.append("Error in name: Name must not start with digit")
if " " in name:
    general_errors.append("Error in name: Name must not include space in it")

if email.count("@") != 1:
    general_errors.append("Error in email: You must have only(or at least) 1 '@' symbol")

if not age.isdigit():
    general_errors.append("Error in age: Age has to be a digit")
elif int(age) <16: #тут elif тому що якщо користувач передав число то я перестрибую у цій еліф і перевіряю вік на 16+,
    # якщо користувач передав наприклад строку, то вік в elif не буде перевірятись і код не крашнится
    general_errors.append("Error in age: You have to be at least 16")



if len(password)<8:
    general_errors.append("Your password must contains at least 8 symbols")
if len(set(password)) ==1 :
    general_errors.append("Your password cannot include the only 1 same symbol")
if " " in password:
    general_errors.append("Your password has to not include spaces")

print("You are registered successfully!" if not general_errors else f"You are not registered because of\n: {"\n".join(general_errors)}")