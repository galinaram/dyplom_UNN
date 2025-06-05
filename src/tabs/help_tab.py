import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk


def create_help_tab(parent, pages, show_page):
    """Создает фрейм справки с кнопкой возврата и вкладками"""
    main_frame = ttk.Frame(parent)

    # Создаем панель с кнопкой назад
    nav_frame = ttk.Frame(main_frame)
    nav_frame.pack(fill='x', pady=5)

    # Кнопка "Назад"
    back_btn = ttk.Button(
        main_frame,
        text="← На главную",
        command=lambda: show_page(pages, "login"),
        style='Back.TButton'
    )
    back_btn.pack(anchor='nw', padx=10, pady=10)

    # Блокнот с вкладками справки
    notebook = ttk.Notebook(main_frame)
    notebook.pack(fill='both', expand=True, padx=10, pady=5)

    # Добавляем вкладки справки
    _add_help_tabs(notebook)

    return main_frame

def _add_help_tabs(notebook):
    """Добавляет вкладки в блокнот справки с разделённым окном"""
    # Вкладка 1: Теоретические основы
    tab1 = ttk.Frame(notebook)

    # Создаем основной контейнер с разделением
    main_paned = ttk.PanedWindow(tab1, orient=tk.HORIZONTAL)
    main_paned.pack(fill=tk.BOTH, expand=True)

    # Левая панель - текст
    text_frame = ttk.Frame(main_paned)
    text_canvas = tk.Canvas(text_frame)
    text_scrollbar = ttk.Scrollbar(text_frame, orient="vertical", command=text_canvas.yview)
    scrollable_text = ttk.Frame(text_canvas)

    scrollable_text.bind(
        "<Configure>",
        lambda e: text_canvas.configure(
            scrollregion=text_canvas.bbox("all")
        )
    )
    text_canvas.create_window((0, 0), window=scrollable_text, anchor="nw")
    text_canvas.configure(yscrollcommand=text_scrollbar.set)

    # Правая панель - изображения (вертикальное разделение)
    img_paned = ttk.PanedWindow(main_paned, orient=tk.VERTICAL)


    help_text = """1. Устройство дуговой сталеплавильной печи (ДСП)
   - Основная нагрузка на свод печи
   - Три электрода с током до сотен тысяч ампер

2. Ключевые формулы модели:

       Электродинамические силы:
       ΔFⱼ,imp = ΔIₖ(μₐIⱼ⁰l)/(2πrⱼₖ⁰)
       ΔFⱼ,kp = ΔIₖ(μₐIⱼ⁰l₁)/(2πrⱼₖ⁰)

       Система уравнений движения:
       J₁Θ̈₁ + b₁Θ̇₁ + c₁Θ₁ + l²(l/2 + l₁)μₐ(I₁⁰I₂⁰)/(2πr₁₂⁰)(Θ₁-Θ₂) + ... = ΔM₁

       Характеристическое уравнение:
       8σ³e⁻³ᵖᵗ - (40c + 8P₁ + P₂)σ²e⁻²ᵖᵗ + ... = 0

       Критерий устойчивости:
       w(p) = [8σ³e⁻³ᵖᵗ - ... - 32c³] / (P₁²P₂)
       Система устойчива при w = -1

3. Параметры модели:
       - μₐ = μ₀μᵣ - магнитная проницаемость
       - Jᵢ - момент инерции
       - cᵢ - приведенная жесткость
       - τ = χ/(2πfR) - запаздывание"""

    ttk.Label(scrollable_text, text=help_text, justify=tk.LEFT, padding=10).pack()

    # Добавляем изображение 1 (верхнее)
    try:
        img1_frame = ttk.Frame(img_paned)
        dsp_img = Image.open("images/рисунок-1.png")
        dsp_img = dsp_img.resize((500, 350), Image.LANCZOS)
        dsp_photo = ImageTk.PhotoImage(dsp_img)
        img_label = ttk.Label(img1_frame, image=dsp_photo)
        img_label.image = dsp_photo
        img_label.pack(pady=5)
        ttk.Label(img1_frame, text="Рис 1. Схема комплекса ДСП", justify=tk.CENTER).pack()
        img_paned.add(img1_frame, weight=1)
    except Exception as e:
        print(f"Ошибка загрузки изображения ДСП: {e}")

    # Добавляем изображение 2 (нижнее)
    try:
        img2_frame = ttk.Frame(img_paned)
        mech_img = Image.open("images/рисунок-2.png")
        mech_img = mech_img.resize((500, 300), Image.LANCZOS)
        mech_photo = ImageTk.PhotoImage(mech_img)
        img_label = ttk.Label(img2_frame, image=mech_photo)
        img_label.image = mech_photo
        img_label.pack(pady=5)
        ttk.Label(img2_frame,
                  text="Рис 2. Упрощенная эквивалентная механическая модель",
                  justify=tk.CENTER).pack()
        img_paned.add(img2_frame, weight=1)
    except Exception as e:
        print(f"Ошибка загрузки изображения модели: {e}")

    # Упаковываем элементы
    text_canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
    text_scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
    text_frame.pack(fill=tk.BOTH, expand=True)

    main_paned.add(text_frame, weight=2)
    main_paned.add(img_paned, weight=1)

    # Остальные вкладки без изменений...
    notebook.add(tab1, text="Теоретические основы")

    # Вкладка 2: Руководство пользователя
    tab2 = ttk.Frame(notebook)
    _add_scrolled_text(tab2, """1. Вкладка 'Параметры системы':
       - Задайте параметры электрододержателей и электрической цепи
       - Используйте значения по умолчанию для начального анализа

2. Вкладка 'Построение кривой D-разбиения':
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