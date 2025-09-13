# Файл interface.py
# Реализация графического интерфейса программы анализа устойчивости

import tkinter as tk
from tkinter import ttk
from src.tabs.login import LoginPage
from src.tabs.params_tab import create_params_tab
from src.tabs.plot_tab import create_plot_tab
from src.tabs.help_tab import create_help_tab


def show_page(pages, page_name):
    """Управляет отображением страниц интерфейса:
    - скрывает текущую страницу
    - отображает запрошенную страницу
    - обновляет ссылку на текущую страницу
    """
    if pages["current"]:
        pages["current"].pack_forget()

    pages["current"] = pages[page_name]
    pages["current"].pack(expand=True, fill=tk.BOTH)

def run_interface():
    """Инициализация и запуск главного окна приложения"""
    # Настройка главного окна
    root = tk.Tk()
    root.title("Анализ устойчивости системы электрододержателей ДСП")
    root.geometry("1200x700")
    root.minsize(1100, 650)

    # Основной контейнер для всех страниц
    container = ttk.Frame(root)
    container.pack(expand=True, fill=tk.BOTH)

    # Словарь для хранения ссылок на страницы
    pages = {"current": None}

    # Инициализация страниц интерфейса
    pages["login"] = LoginPage(container, pages, show_page).main_frame
    pages["tab_container"] = ttk.Frame(container)

    # Конфигурация контейнера с вкладками
    back_btn = ttk.Button(
        pages["tab_container"],
        text="← На главную",
        command=lambda: show_page(pages, "login"),
        style='Back.TButton'
    )
    back_btn.pack(anchor='nw', padx=10, pady=5)

    # Создание и настройка блока вкладок
    notebook = ttk.Notebook(pages["tab_container"])
    notebook.pack(fill='both', expand=True)

    # Добавление функциональных вкладок
    notebook.add(create_params_tab(notebook), text="Параметры системы")
    notebook.add(create_plot_tab(notebook), text="Построение кривой D-разбиения")
    pages["notebook"] = notebook

    # Инициализация страницы справки
    pages["help"] = create_help_tab(container, pages, show_page)

    # Первоначальное отображение стартовой страницы
    show_page(pages, "login")
    root.mainloop()