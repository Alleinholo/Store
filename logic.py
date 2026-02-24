from data import items, prices


def shop():
    # 2. Ввод данных (Оператор вводит только количество)
    val_phys = int(input(f"Сколько нужно {items[0]}: "))
    val_math = int(input(f"Сколько нужно {items[1]}: "))
    val_term = int(input(f"Сколько нужно {items[2]}: "))

    # 3. Расчет (Используем индексы вместо имен переменных)
    total_cost = (val_phys * prices[0]) + (val_math * prices[1]) + (val_term * prices[2])

    print(f"Общая стоимость: {total_cost}")
    total_cash = int(input("Сколько вы дадите денег? "))
    # Рассчитываем сдачу (может быть отрицательной)
    change = total_cash - total_cost

    if total_cash > total_cost:
        print(f"Ваша сдача: {change}! Спасибо за покупку!")
    elif total_cash == total_cost:
        print(f"У вас без сдачи, спасибо!")  
    else:
        debt = total_cost - total_cash
        print(f"Недостаточно средств. Вы должны: {debt}")

def mod_lists():
    print("\n=== Редактирование товаров ===")
    for item in items: print(item)
    input("Заменить: ")

def mod_prices():
    print("\n=== Редактирование товаров ===")
    for item in items: print(item)
    input("Заменить: ")