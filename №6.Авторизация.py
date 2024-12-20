import tkinter as tk
from tkinter import messagebox
import sqlite3

# Создание базы данных и таблицы
def init_db():
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT NOT NULL,
            password TEXT NOT NULL
        )
    ''')
    conn.commit()
    conn.close()

# Регистрация пользователя
def register_user(username, password):
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()
    cursor.execute('INSERT INTO users (username, password) VALUES (?, ?)', (username, password))
    conn.commit()
    conn.close()

# Проверка авторизации пользователя
def authenticate_user(username, password):
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM users WHERE username=? AND password=?', (username, password))
    return cursor.fetchone() is not None

# Функция для обработки авторизации
def login():
    username = entry_username.get()
    password = entry_password.get()
    if authenticate_user(username, password):
        messagebox.showinfo("Авторизация", "Успешная авторизация!")
    else:
        messagebox.showerror("Ошибка", "Неверный логин или пароль.")

# Функция для регистрации
def open_registration():
    reg_window = tk.Toplevel(main_window)
    reg_window.title("Регистрация")

    tk.Label(reg_window, text="Логин:").pack()
    entry_reg_username = tk.Entry(reg_window)
    entry_reg_username.pack()

    tk.Label(reg_window, text="Пароль:").pack()
    entry_reg_password = tk.Entry(reg_window, show='*')
    entry_reg_password.pack()

    def register():
        username = entry_reg_username.get()
        password = entry_reg_password.get()
        register_user(username, password)
        messagebox.showinfo("Регистрация", "Вы успешно зарегистрированы!")
        reg_window.destroy()

    tk.Button(reg_window, text="Зарегистрироваться", command=register).pack()

# Инициализация базы данных
init_db()

# Главное окно
main_window = tk.Tk()
main_window.title("Авторизация")

tk.Label(main_window, text="Логин:").pack()
entry_username = tk.Entry(main_window)
entry_username.pack()

tk.Label(main_window, text="Пароль:").pack()
entry_password = tk.Entry(main_window, show='*')
entry_password.pack()

tk.Button(main_window, text="Войти", command=login).pack()
tk.Button(main_window, text="Регистрация", command=open_registration).pack()

main_window.mainloop()
