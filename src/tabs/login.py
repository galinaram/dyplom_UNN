# Файл login.py
import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk

import os


class LoginPage:
    def __init__(self, parent, pages, show_page_func):
        self.parent = parent
        self.pages = pages
        self.show_page_func = show_page_func

        # Главный фрейм с вертикальным выравниванием
        self.main_frame = ttk.Frame(parent)
        self.main_frame.pack(expand=True, fill=tk.BOTH, pady=20)  # Добавлены отступы сверху и снизу

        # Стили
        self.style = ttk.Style()
        self.style.configure('Main.TFrame', background='#f5f5f5')
        self.style.configure('Title.TLabel', font=('Arial', 22, 'bold'), background='#f5f5f5')
        self.style.configure('Desc.TLabel', font=('Arial', 13), background='#f5f5f5')
        self.style.configure('Nav.TButton', font=('Arial', 14), padding=12)
        self.style.configure('Back.TButton',
                             font=('Arial', 12),
                             padding=5,
                             foreground='#2c3e50')

        # Контейнер для всего контента (без кнопок)
        self.content_container = ttk.Frame(self.main_frame)
        self.content_container.pack(expand=True, fill=tk.BOTH, pady=(0, 20))  # Отступ снизу для кнопок

        # Заголовок
        self.header_frame = ttk.Frame(self.content_container)
        self.header_frame.pack(fill='x', pady=(0, 30))

        ttk.Label(
            self.header_frame,
            text="Программный комплекс анализа устойчивости\nсистемы электрододержателей ДСП",
            style='Title.TLabel',
            justify='center'
        ).pack(expand=True)

        # Основной контент (изображение + текст)
        self.content_frame = ttk.Frame(self.content_container)
        self.content_frame.pack(expand=True, fill='both')

        # Изображение
        self.image_frame = ttk.Frame(self.content_frame, width=650)
        self.image_frame.pack(side='left', fill='both', padx=(0, 60))

        try:
            img_path = os.path.join("images", "дсп-1.jpg")
            if not os.path.exists(img_path):
                raise FileNotFoundError(f"Изображение не найдено: {os.path.abspath(img_path)}")

            img = Image.open(img_path)
            img = img.resize((600, 450), Image.LANCZOS)
            self.scheme_img = ImageTk.PhotoImage(img)

            ttk.Label(
                self.image_frame,
                image=self.scheme_img,
                background='#f5f5f5'
            ).pack(pady=10, anchor='w')
        except Exception as e:
            print(f"Ошибка загрузки изображения: {e}")
            ttk.Label(
                self.image_frame,
                text="Схема системы электрододержателей",
                style='Desc.TLabel',
                font=('Arial', 14)
            ).pack(expand=True)

        # Текст
        self.desc_frame = ttk.Frame(self.content_frame)
        self.desc_frame.pack(side='left', expand=True, fill='both')

        description_text = """
        Математическая модель системы включает:

        • Крутильные колебания трех электрододержателей
        • Электродинамические силы взаимодействия

        Для анализа устойчивости используется:
        - Метод D-разбиения
        - Критерий Найквиста
        - Построение годографов на комплексной плоскости

        Программа позволяет:
        1. Задавать параметры системы
        2. Строить границы устойчивости
        3. Выявлять и исследовать состояния равновесия
        """

        ttk.Label(
            self.desc_frame,
            text=description_text,
            style='Desc.TLabel',
            justify='left'
        ).pack(anchor='w', padx=20, pady=10)

        # Навигация (кнопки в отдельном контейнере)
        self.nav_frame = ttk.Frame(self.main_frame)
        self.nav_frame.pack(fill='x', pady=(0, 10))  # Отступ только снизу

        buttons = [
            ("Параметры", self.open_parameters),
            ("Устойчивость", self.open_visualization),
            ("Справка", self.open_help)
        ]

        for text, cmd in buttons:
            ttk.Button(
                self.nav_frame,
                text=text,
                command=cmd,
                style='Nav.TButton'
            ).pack(side='left', expand=True, padx=15)

    def show(self):
        self.main_frame.pack(expand=True, fill=tk.BOTH)

    def hide(self):
        self.main_frame.pack_forget()

    def open_parameters(self):
        self.show_page_func(self.pages, "tab_container")
        self.pages["notebook"].select(0)

    def open_visualization(self):
        self.show_page_func(self.pages, "tab_container")
        self.pages["notebook"].select(1)

    def open_help(self):
        self.show_page_func(self.pages, "help")
