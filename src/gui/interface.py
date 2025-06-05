# Файл interface.py
import tkinter as tk
from tkinter import ttk
from src.tabs.login import LoginPage
from src.tabs.params_tab import create_params_tab
from src.tabs.plot_tab import create_plot_tab
from src.tabs.help_tab import create_help_tab

def show_page(pages, page_name):
    """Показывает указанную страницу и скрывает все остальные"""
    if pages["current"]:
        pages["current"].pack_forget()

    pages["current"] = pages[page_name]
    pages["current"].pack(expand=True, fill=tk.BOTH)

def run_interface():
    root = tk.Tk()
    root.title("Анализ устойчивости системы электрододержателей ДСП")
    root.geometry("1200x700")
    root.minsize(1100, 650)

    container = ttk.Frame(root)
    container.pack(expand=True, fill=tk.BOTH)

    pages = {
        "current": None
    }

    # Создаем все фреймы
    login_page = LoginPage(container, pages, show_page)
    pages["login"] = login_page.main_frame

    # Контейнер для вкладок с кнопкой назад
    tab_container = ttk.Frame(container)
    pages["tab_container"] = tab_container

    # Кнопка "На главную" для вкладок
    back_btn = ttk.Button(
        tab_container,
        text="← На главную",
        command=lambda: show_page(pages, "login"),
        style='Back.TButton'
    )
    back_btn.pack(anchor='nw', padx=10, pady=5)

    # Блокнот с вкладками
    notebook = ttk.Notebook(tab_container)
    notebook.pack(fill='both', expand=True)

    # Добавляем вкладки
    frame2 = create_params_tab(notebook)
    frame3 = create_plot_tab(notebook)
    notebook.add(frame2, text="Параметры системы")
    notebook.add(frame3, text="Построение кривой D-разбиения")
    pages["notebook"] = notebook

    # Фрейм справки
    help_frame = create_help_tab(container, pages, show_page)
    pages["help"] = help_frame

    # Показываем главную страницу при запуске
    show_page(pages, "login")
    root.mainloop()