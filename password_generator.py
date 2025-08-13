import random
import string
from colorama import Fore, Style, init

# инициализация colorama (нужно для Windows)
init()

def generate_password(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

while True:
    try:
        user_length = int(input(Fore.CYAN + "Введите длину пароля: " + Style.RESET_ALL))
        if user_length <= 0:
            print(Fore.RED + "Длина должна быть положительным числом!" + Style.RESET_ALL)
            continue
        break
    except ValueError:
        print(Fore.RED + "Пожалуйста, введите число!" + Style.RESET_ALL)

print(Fore.GREEN + "Ваш пароль: " + Fore.YELLOW + generate_password(user_length) + Style.RESET_ALL)
