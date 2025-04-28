from cryptography.fernet import Fernet
from main import load_key


def authorization(login_input, password_input, fernet):
    with open('password.txt', 'r') as password_file:
        for line in password_file.readlines():
            login, encrypted_password = line.strip().split(' | ')
            decrypted_password = fernet.decrypt(encrypted_password.encode()).decode()
            if login == login_input and decrypted_password == password_input:
                return True 

    return False


def main():
    key = load_key()
    fernet = Fernet(key)

    while True:
        login = input('Введите логин: ')
        password = input('Введите пароль: ')
        if authorization(login, password, fernet):
            print('Вы авторизованы')
            break  
        else:
            print('Неверный логин или пароль. Попробуйте еще раз.')


if __name__ == "__main__":
    main()