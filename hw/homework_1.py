# Напишіть програму, яка отримує від користувач колір світлофора. І в залежності від кольора видає одне із повідомлень:
#
# red — зупинитися;
# yellow — очікувати або підготуватися відповідно до навчальної моделі;
# green — рух дозволено за умови безпеки;
# будь-яке інше значення — невідомий сигнал.
# Реалізуйте два варіанти:
#
# Через if/elif/else.
# Через match/case.
#
color = input("Enter your color").lower().strip()

if color == "red":
    print("STOP")
elif color == "yellow":
    print("Attention")
elif color == "green":
    print("RUN!")
else:
    print("Error")

match color:
    case "red":
        print("STOP")
    case "yellow":
        print("Attention")
    case "green":
        print("RUN")
    case _:
        print("Error")