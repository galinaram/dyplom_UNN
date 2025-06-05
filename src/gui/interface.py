# Файл interface.py
import tkinter as tk
from tkinter import ttk
from src.tabs.login import LoginPage
from src.tabs.params_tab import create_params_tab
from src.tabs.plot_tab import create_plot_tab
from src.tabs.help_tab import create_help_tab

def return_to_main(pages):
    """Возвращает на главную страницу из любых вкладок"""
    pages["tab_container"].pack_forget()
    pages["help"].pack_forget()
    pages["login"].pack(expand=True, fill=tk.BOTH)

def run_interface():
    root = tk.Tk()
    root.title("Анализ устойчивости системы электрододержателей ДСП")
    root.geometry("1200x700")  # Увеличенный размер окна
    root.minsize(1100, 650)

    container = ttk.Frame(root)
    container.pack(expand=True, fill=tk.BOTH)

    pages = {}

    login_page = LoginPage(container, pages)
    pages["login"] = login_page.main_frame

    notebook = ttk.Notebook(container)
    frame2 = create_params_tab(notebook)
    frame3 = create_plot_tab(notebook)
    notebook.add(frame2, text="Параметры системы")
    notebook.add(frame3, text="Построение кривой D-разбиения")
    pages["notebook"] = notebook

    help_frame = create_help_tab(container, pages)
    pages["help"] = help_frame

    # Создаем общий фрейм для кнопки и вкладок
    tab_container = ttk.Frame(container)
    pages["tab_container"] = tab_container

    # Добавляем кнопку "На главную" в отдельный фрейм
    nav_frame = ttk.Frame(tab_container)
    back_btn = ttk.Button(
        nav_frame,
        text="← На главную",
        command=lambda: return_to_main(pages),
        style='Back.TButton'
    )
    back_btn.pack(side='left', padx=10, pady=5)
    nav_frame.pack(fill='x')

    # Помещаем notebook в тот же контейнер
    notebook.pack(fill='both', expand=True)
    tab_container.pack(fill='both', expand=True)

    login_page.show()
    root.mainloop()