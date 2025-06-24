import sqlite3
import hashlib
import getpass
import os
# функция для хэширования пароля
def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()
# функция для расхэширования пароля (т.к. sha256 не обратим, нам нужно хранить соль и исходный пароль для проверки)
def check_password(hashed_password, user_input):
    return hashed_password == hash_password(user_input)
# создаем соединение с базой данных
conn = sqlite3.connect('passwords.db')
c = conn.cursor()
# создаем таблицу для хранения паролей
c.execute('''CREATE TABLE IF NOT EXISTS passwords
             (username text, password text)''')
# функция для генерации и хранения пароля
def generate_password(username):
    password = getpass.getpass("Введите пароль: ")
    hashed_password = hash_password(password)
    c.execute("INSERT INTO passwords VALUES (?, ?)", (username, hashed_password))
    conn.commit()
    print("Пароль успешно сгенерирован и сохранен!")
# функция для получения пароля из базы данных
def get_password(username):
    c.execute("SELECT password FROM passwords WHERE username=?", (username,))
    hashed_password = c.fetchone()
    if hashed_password:
        user_input = getpass.getpass("Введите пароль для подтверждения: ")
        if check_password(hashed_password[0], user_input):
            print("Пароль подтвержден!")
        else:
            print("Неправильный пароль!")
    else:
        print("Пользователь не найден!")
# главная функция
def main():
    while True:
        print("1. Сгенерировать и сохранить пароль")
        print("2. Получить пароль из базы данных")
        print("3. Выход")
        choice = input("Выберите действие: ")
        if choice == "1":
            username = input("Введите имя пользователя: ")
            generate_password(username)
        elif choice == "2":
            username = input("Введите имя пользователя: ")
            get_password(username)
        elif choice == "3":
            break
        else:
            print("Неправильный выбор!")
if _name_ == "_main_":
    main()
