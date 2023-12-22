from collections import deque


# Функція перевірки рядка на паліндром
def is_palindrome(input_string):
    # Перетворення рядка в чергу
    deq = deque(input_string.lower().replace(' ', ''))
    # Перевірка на паліндром, підхід з циклом допомагає не перевіряти на парність довжини рядка
    while len(deq) > 1:
        if deq.popleft() != deq.pop():
            return False
    return True

if __name__ == '__main__':
    # Головний цикл програми
    while True:
        user_input = input("Введіть рядок для тестування (або 'q' для виходу): ")
        if user_input == 'q':
            break
        print('Рядок є паліндромом' if is_palindrome(user_input) else 'Рядок не є паліндромом')
