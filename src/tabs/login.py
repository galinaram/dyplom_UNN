# Файл login.py
import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
import os


class LoginPage:
    def __init__(self, parent, pages):
        self.parent = parent
        self.pages = pages

        # Главный фрейм страницы
        self.main_frame = ttk.Frame(parent)

        # Настройка стилей
        self.style = ttk.Style()
        self.style.configure('Main.TFrame', background='#f5f5f5')
        self.style.configure('Title.TLabel', font=('Arial', 18, 'bold'), background='#f5f5f5')
        self.style.configure('Desc.TLabel', font=('Arial', 11), background='#f5f5f5')
        self.style.configure('Nav.TButton', font=('Arial', 12), padding=10)

        # 1. Верхняя часть - Название проекта
        self.header_frame = ttk.Frame(self.main_frame)
        self.header_frame.pack(fill='x', pady=(0, 20))

        ttk.Label(
            self.header_frame,
            text="Программный комплекс анализа устойчивости\nсистемы электрододержателей ДСП",
            style='Title.TLabel',
            justify='center'
        ).pack(expand=True)

        # 2. Центральная часть (изображение + описание)
        self.content_frame = ttk.Frame(self.main_frame)
        self.content_frame.pack(expand=True, fill='both')

        # 2.1 Левая часть - Изображение
        self.image_frame = ttk.Frame(self.content_frame, width=300)
        self.image_frame.pack(side='left', fill='y', padx=(0, 20))

        try:
            path = r"images/дсп-1.jpg"
            img = Image.open(path)
            img = img.resize((300, 300), Image.LANCZOS)
            self.scheme_img = ImageTk.PhotoImage(img)
            ttk.Label(
                self.image_frame,
                image=self.scheme_img,
                background='#f5f5f5'
            ).pack(pady=20)
        except:
            ttk.Label(
                self.image_frame,
                text="Схема системы электрододержателей",
                style='Desc.TLabel'
            ).pack(expand=True)

        # 2.2 Правая часть - Описание модели
        self.desc_frame = ttk.Frame(self.content_frame)
        self.desc_frame.pack(side='left', expand=True, fill='both')

        description_text = """
        Математическая модель системы включает:

        • Крутильные колебания трех электрододержателей
        • Электродинамические силы взаимодействия
        • Упругие и демпфирующие характеристики

        Для анализа устойчивости используется:
        - Метод D-разбиения
        - Критерий Найквиста
        - Построение годографов на комплексной плоскости

        Программа позволяет:
        1. Задавать параметры системы
        2. Строить границы устойчивости
        3. Анализировать критические режимы
        """

        ttk.Label(
            self.desc_frame,
            text=description_text,
            style='Desc.TLabel',
            justify='left'
        ).pack(anchor='w', padx=20)

        # 3. Нижняя часть - Кнопки навигации
        self.nav_frame = ttk.Frame(self.main_frame)
        self.nav_frame.pack(fill='x', pady=(20, 0))

        buttons = [
            ("Параметры", self.open_parameters),
            ("Расчет", self.open_calculations),
            ("Графики", self.open_visualization),
            ("Справка", self.open_help)
        ]

        for text, cmd in buttons:
            ttk.Button(
                self.nav_frame,
                text=text,
                command=cmd,
                style='Nav.TButton'
            ).pack(side='left', expand=True, padx=10)

    def show(self):
        """Показать эту страницу"""
        self.main_frame.pack(expand=True, fill=tk.BOTH)

    def hide(self):
        """Скрыть эту страницу"""
        self.main_frame.pack_forget()

    def open_parameters(self):
        self.hide()
        self.pages["notebook"].pack(expand=True, fill=tk.BOTH)
        self.pages["notebook"].select(0)  # Выбираем вкладку параметров

    def open_calculations(self):
        self.hide()
        self.pages["notebook"].pack(expand=True, fill=tk.BOTH)
        # Здесь можно добавить выбор соответствующей вкладки

    def open_visualization(self):
        self.hide()
        self.pages["notebook"].pack(expand=True, fill=tk.BOTH)
        self.pages["notebook"].select(1)  # Выбираем вкладку графиков

    def open_help(self):
        print("Открытие справки")
        # Здесь можно реализовать открытие справки