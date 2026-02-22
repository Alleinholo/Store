from logic import shop, mod_shop
import time

def menu():
    while True:
        print("\n=== МЕНЮ МАГАЗИНА ===")
        print("1. Начать покупки")
        print("2. Следующая секция (в разработке)")
        print("0. Выход")

        choice = input("Выберите пункт меню: ").strip()  # Внутри цикла!

        if choice == "1":
             shop()  # Выполнится и вернётся сюда
             print("\nВозврат в меню...\n")
        elif choice == "2":
             print("Эта секция еще не написана. Возврат в Нексус...\n")
        elif choice == "0":
             print("До свидания!")
             break
        else:
             print("Неверный выбор. Попробуйте снова.\n")

if __name__ == "__main__":
    menu()