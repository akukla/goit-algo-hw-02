from queue import Queue


# Створення черги заявок
queue = Queue()


# Функція для створення нової заявки і додавання її до черги
def generate_request():
    new_request = input("Назва заявки: ")
    queue.put(new_request)
    print(f"\nСтворено нову заявку: {new_request}")


# Функція для обробки заявок з черги
def process_request():
    if not queue.empty():
        request = queue.get()
        print(f"\nОбробка заявки: {request}")
    else:
        print("\nЧерга пуста. Немає заявок для обробки.")


def print_queue():
    print("\nЗаявки в черзі:")
    if not queue.empty():
        for request in queue.queue:
            print(request)
    else:
        print("\nЧерга пуста.")


# Головний цикл програми
while True:
    print("\nОберіть опцію:")
    print("1. Створити нову заявку")
    print("2. Обробити заявку")
    print("3. Список заявок в черзі")
    print("4. Вийти з програми")

    choice = input("Ваш вибір: ")
    if choice == '1':
        generate_request()
    elif choice == '2':
        process_request()
        print_queue()
    elif choice == '3':
        print_queue()
    elif choice == '4':
        print("Вихід з програми.")
        break
    else:
        print("Невірний вибір. Спробуйте ще раз.")
