from logic import shop, mod_lists, mod_prices
from data import items, prices, main_menu, mod_shop_menu

def mod_shop():
    while True:
        print("\n=== МЕНЮ РЕДАКТИРОВАНИЯ ===")
        for i, item in enumerate(mod_shop_menu, 1):
            print(f"{i}. {item}")
        choice = input("Выберите пункт меню: ").strip()
        if choice == "1":
            print("\n=== Списки ===")
            for item, price in zip(items, prices):
                print(f"{item:<10} — {price} руб.")
            input("\nНажмите Enter для продолжения...")
        elif choice == "2":
            mod_lists()
        elif choice == "3":
            mod_prices()
        elif choice == "4":
            return
        else:
            print("Неверный выбор. Попробуйте снова.\n")


def menu():
    while True:
        print("\n=== МЕНЮ МАГАЗИНА ===")
        for i, item in enumerate(main_menu, 1):
            print(f"{i}. {item}")
        choice = input("Выберите пункт меню: ").strip()
        if choice == "1":
            shop()
            print("\nВозврат в меню...\n")
        elif choice == "2":
            mod_shop()
        elif choice == "3":  # "Выход"
            print("До свидания!")
            break
        else:
            print("Неверный выбор. Попробуйте снова.\n")


if __name__ == "__main__":
    menu()
