# Напишіть програму, яка запитує у користувача суму у євро і потім виводить: мінімальну кількисть купюр та мінімальну кількість монет для того, щоб отримати цю суму у євро. Зверніть увагу на те, що банкноти євро мають номінали: 5, 10, 20, 50, 100, 200 та 500 евро. А монети: 1 та 2 євро, 1, 2, 5, 10, 20 та 50 євроцентів.
#
# Крім того треба надрукувати кількість кожного номіналу котрий використовується для отримання даної суми.
#
# * Бажано, щоб суму можна було вводити як через крапку так і через кому.
#
# Приклад: Введіть суму: 347,78
#
# Кількість банкнот: 5
#
# Кількість монет: 7
#
# Склад суми:
#Q
# 1 x 200
#
# 1 x 100
#
# 2 x 20
#
# 1 x 5
#
# 2 x 1
#
# 1 x 0.5
#
# 1 x 0.2
#
# 1 x 0.05
#
# 1 x 0.02
#
# 1 x 0.01
def hundred_times(list_1):
    return [int(el*100) for el in list_1]
list_of_paper = hundred_times([500,200,100,50,20,10,5])
list_of_coins = hundred_times([2,1,0.5,0.20,0.10,0.05,0.02,0.01])
list_of_money = list_of_paper
dict_of_money = {}
dict_type_of_money = {"paper":0,"coins":0}
type_of_money = "paper"
step = 0

summ=input("Input your digit\n").replace(",",".")
if "." in summ and len(summ[summ.find("."): ])>3: #на випадок якщо число у якому більше анід 2 числа після коми
    summ = summ[:summ.find(".")+3]
summ = round(float(summ) * 100)#я множу число на 100 щоб працбваиим виключно з цілими числами
while summ>0:
    if list_of_money[step]<=summ:
        summ -=list_of_money[step]
        dict_of_money[list_of_money[step]/100] = dict_of_money.get(list_of_money[step]/100, 0) + 1
        dict_type_of_money[type_of_money] +=1
    elif list_of_money[step]>summ:
        step+=1
        # print(len(list_of_money))
        if len(list_of_money)-1<step:
            list_of_money=list_of_coins
            type_of_money = "coins"
            step=0
print("Склад сумми:")
for key, value in dict_of_money.items():
    print(f"{value} x {key}")

print(f"Кількість банкнот:{dict_type_of_money['paper']}")
print(f"Кількість монет:{dict_type_of_money['coins']}")

