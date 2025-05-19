# Файл interface.py
import tkinter as tk
from tkinter import ttk
from src.tabs.login import LoginPage
from src.tabs.params_tab import create_params_tab
from src.tabs.plot_tab import create_plot_tab

def run_interface():
    root = tk.Tk()
    root.title("Анализ устойчивости системы")
    root.geometry("1000x600")

    # Создаем контейнер для всех страниц
    container = ttk.Frame(root)
    container.pack(expand=True, fill=tk.BOTH)

    # Словарь для хранения всех фреймов (страниц)
    pages = {}

    # Создаем страницы и добавляем их в словарь
    login_page = LoginPage(container, pages)
    pages["login"] = login_page.main_frame

    # Создаем вкладки параметров и графиков
    notebook = ttk.Notebook(container)
    frame2 = create_params_tab(notebook)
    frame3 = create_plot_tab(notebook)
    notebook.add(frame2, text="Параметры")
    notebook.add(frame3, text="Построение границы D-разбиения")
    pages["notebook"] = notebook

    # Показываем главную страницу
    login_page.show()

    root.mainloop()