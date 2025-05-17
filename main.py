import os
from cryptography.fernet import Fernet


def write_key(key):
    with open("key.key", "wb") as key_file:
        key_file.write(key)


def load_key():
    with open("key.key", "rb") as key_file:
        my_key = key_file.read()

    return my_key


def add(fernet):
    login = input('Введите логин: ')
    password = input('Введите пароль: ')
    encrypt_password = fernet.encrypt(password.encode())
    with open('password.txt', 'a') as password_file:
        password_file.write(f'{login} | {encrypt_password.decode()}\n')


def view(fernet):
    with open('password.txt', 'r') as password_file:
        for line in password_file.readlines():
            login, password = line.rstrip().split(' | ')
            decrypt_password = fernet.decrypt(password.encode()).decode()
            print(f'Логин: {login} | Пароль: {decrypt_password}')


def main():
    if not os.path.exists("key.key"):
        key = Fernet.generate_key()
        write_key(key)
    else:
        key = load_key()

    fernet = Fernet(key) 

    while True:
        user__response = input("""
            Хотите добавить новый пароль или посмотреть уже существующие?
            1. Посмотреть
            2. Добавить
            3. Выход
        """)
        if user__response == '1':
            view(fernet)
        elif user__response == '2':
            add(fernet)        
        elif user__response == '3':
            break
        else:
            print('Ваш выбор не коректен. Повторите ввод')


if __name__ == "__main__":
    main()
