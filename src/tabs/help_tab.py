import tkinter as tk
from tkinter import ttk


def create_help_tab(parent, pages):
    """Создает фрейм справки с кнопкой возврата и вкладками"""
    main_frame = ttk.Frame(parent)

    def return_to_main():
        """Возвращает к основным вкладкам"""
        main_frame.pack_forget()
        pages["notebook"].pack_forget()
        pages["login"].pack(expand=True, fill=tk.BOTH)

    # Создаем панель с кнопкой назад
    nav_frame = ttk.Frame(main_frame)
    nav_frame.pack(fill='x', pady=5)

    # Кнопка "Назад"
    back_btn = ttk.Button(
        nav_frame,
        text="← Назад",
        command=return_to_main,
        style='Back.TButton'
    )
    back_btn.pack(side='left', padx=10, pady=5)

    # Блокнот с вкладками справки
    notebook = ttk.Notebook(main_frame)
    notebook.pack(fill='both', expand=True, padx=10, pady=5)

    # Добавляем вкладки справки
    _add_help_tabs(notebook)

    return main_frame


def _add_help_tabs(notebook):
    """Добавляет вкладки в блокнот справки"""
    # Вкладка 1: Теоретические основы
    tab1 = ttk.Frame(notebook)
    _add_scrolled_text(tab1, """11. Метод D-разбиения:
   - Основан на построении границы устойчивости в комплексной плоскости
   - Критерий Найквиста: система устойчива, если годограф не охватывает точку (-1, 0j)

    2. Математическая модель электрододержателей:
   - Уравнения крутильных колебаний с учетом электромагнитных сил
   - Учет запаздывания в системе
   - Симметрия параметров для трехфазной системы""")
    notebook.add(tab1, text="Теоретические основы")

    # Вкладка 2: Руководство пользователя
    tab2 = ttk.Frame(notebook)
    _add_scrolled_text(tab2, """1. Вкладка 'Параметры системы':
   - Задайте параметры электрододержателей и электрической цепи
   - Используйте значения по умолчанию для начального анализа

    2. Вкладка 'График':
   - Настройте диапазон частот (omega) и шаг вычислений
   - Нажмите 'Построить' для получения кривой D-разбиения
   - Результат устойчивости отобразится в текстовом поле""")
    notebook.add(tab2, text="Руководство пользователя")

    # Вкладка 3: Примеры расчетов
    tab3 = ttk.Frame(notebook)
    _add_scrolled_text(tab3, """Пример 1: Базовая конфигурация
   - Параметры по умолчанию
   - Результат: система устойчива

    Пример 2: Увеличенное запаздывание
   - Установите τ = 0.5
   - Результат: система становится неустойчивой

    Пример 3: Уменьшенная жесткость
   - Установите c = 5000
   - Результат: появление автоколебаний""")
    notebook.add(tab3, text="Примеры расчетов")


def _add_scrolled_text(parent, text):
    """Добавляет текстовое поле с прокруткой"""
    text_frame = ttk.Frame(parent)
    text_widget = tk.Text(text_frame, wrap='word', padx=10, pady=10)
    scrollbar = ttk.Scrollbar(text_frame, command=text_widget.yview)

    text_widget.configure(yscrollcommand=scrollbar.set)
    text_widget.insert('1.0', text)
    text_widget.config(state='disabled')

    scrollbar.pack(side='right', fill='y')
    text_widget.pack(side='left', fill='both', expand=True)
    text_frame.pack(fill='both', expand=True)