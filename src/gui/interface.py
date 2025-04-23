import tkinter as tk
from tkinter import ttk
from src.tabs.main_tab import create_main_tab
from src.tabs.params_tab import create_params_tab
from src.tabs.plot_tab import create_plot_tab

def run_interface():
    root = tk.Tk()
    root.title("Анализ устойчивости системы")
    root.geometry("1000x600")

    notebook = ttk.Notebook(root)
    notebook.pack(expand=True, fill=tk.BOTH)

    # Создаем вкладки
    frame1 = create_main_tab(notebook)
    frame2 = create_params_tab(notebook)
    frame3 = create_plot_tab(notebook)

    # Добавляем вкладки
    notebook.add(frame1, text="Главное меню")
    notebook.add(frame2, text="Параметры")
    notebook.add(frame3, text="Построение границы D-разбиения")

    root.mainloop()