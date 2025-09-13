# Файл help_tab.py
# Реализация вкладки справки для программы анализа устойчивости

import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk


def create_help_tab(parent, pages, show_page):
    """Создает и возвращает фрейм справки с навигацией и вкладками

    Параметры:
        parent: Родительский виджет
        pages: Словарь страниц приложения
        show_page: Функция переключения страниц

    Возвращает:
        ttk.Frame: Сконфигурированный фрейм справки
    """
    main_frame = ttk.Frame(parent)

    # Навигационная панель с кнопкой возврата
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
    _add_help_tabs(notebook)

    return main_frame


def _add_help_tabs(notebook):
    """Добавляет вкладки с теоретической информацией и руководством

    Параметры:
        notebook: Виджет ttk.Notebook для размещения вкладок
    """
    # Вкладка с теоретическими основами
    tab1 = ttk.Frame(notebook)
    _create_theory_tab(tab1)
    notebook.add(tab1, text="Теоретические основы")

    # Вкладка с руководством пользователя
    tab2 = ttk.Frame(notebook)
    _add_scrolled_text(tab2, """1. Вкладка 'Параметры системы':
       - Задайте параметры электрододержателей и электрической цепи
       - Используйте значения по умолчанию для начального анализа

2. Вкладка 'Построение кривой D-разбиения':
       - Настройте диапазон частот (omega) и шаг вычислений
       - Нажмите 'Построить' для получения кривой D-разбиения
       - Результат устойчивости отобразится в текстовом поле""")
    notebook.add(tab2, text="Руководство пользователя")


def _create_theory_tab(parent):
    """Создает вкладку с теоретическими основами и схемами"""
    paned = ttk.PanedWindow(parent, orient=tk.HORIZONTAL)
    paned.pack(fill=tk.BOTH, expand=True)

    # Текстовый блок с формулами
    text_frame = ttk.Frame(paned)
    _add_scrolled_text(text_frame,
"""1. Устройство дуговой сталеплавильной печи (ДСП)
  - Основная нагрузка на свод печи
  - Три электрода с током до сотен тысяч ампер

2. Ключевые формулы модели:

   Электродинамические силы:
ΔFⱼ,imp = ΔIₖ(μₐIⱼ⁰l)/(2πrⱼₖ⁰)  
ΔFⱼ,kp = ΔIₖ(μₐIⱼ⁰l₁)/(2πrⱼₖ⁰)

   Система дифференциальных уравнений:
J₁Θ̈₁ + b₁Θ̇₁ + c₁Θ₁ + l²(l/2 + l₁)μₐ(I₁⁰I₂⁰)/(2πr₁₂⁰)(Θ₁-Θ₂) + l²(l/2 + l₁)μₐ(I₁⁰I₃⁰)/(2πr₁₃⁰)(Θ₁-Θ₃) = ΔM₁  
J₂Θ̈₂ + b₂Θ̇₂ + c₂Θ₂ + l²(l/2 + l₁)μₐ(I₂⁰I₁⁰)/(2πr₁₂⁰)(Θ₂-Θ₁) + l²(l/2 + l₁)μₐ(I₂⁰I₃⁰)/(2πr₂₃⁰)(Θ₂-Θ₃) = ΔM₂  
J₃Θ̈₃ + b₃Θ̇₃ + c₃Θ₃ + l²(l/2 + l₁)μₐ(I₃⁰I₁⁰)/(2πr₃₁⁰)(Θ₃-Θ₁) + l²(l/2 + l₁)μₐ(I₃⁰I₂⁰)/(2πr₃₂⁰)(Θ₃-Θ₂) = ΔM₃

   Моменты сил:
ΔMᵢₘₚ = -(μₐIᵢ⁰)/(2πrᵢⱼ)·(l²/2)·((αⱼ+βⱼl₉⁰)+I⁰R)/(Iᵢ⁰(R²+χ²)+R(αⱼ+βⱼl₉⁰))·βⱼΘⱼ(t-τ)  
ΔMᵢₚ = -(μₐIᵢ⁰)/(2πrᵢⱼ)·lᵢl·((αⱼ+βⱼl₉⁰)+I⁰R)/(Iᵢ⁰(R²+χ²)+R(αⱼ+βⱼl₉⁰))·βⱼlΘⱼ(t-τ)

   Характеристическое уравнение:
8σ³e⁻³ᵖᵗ - (40c + 8P₁ + P₂)σ²e⁻²ᵖᵗ + (64c² + 32P₁ + 2P₂)cσe⁻ᵖᵗ - 32c³ - (32P₁ + P₂)c² + P₁²P₂ = 0  
где P₁ = Jp² + bp + c₁, P₂ = Jp² + bp + c₂

   Критерий устойчивости:
w(p) = [8σ³e⁻³ᵖᵗ - (40c+8P₁+P₂)σ²e⁻²ᵖᵗ + (64c²+32P₁+2P₂)cσe⁻ᵖᵗ - 32c³ - (32P₁+P₂)c²]/(P₁²P₂)  
Система устойчива при w = -1

3. Параметры модели:
- μₐ = μ₀μᵣ (μ₀=1.257·10⁻⁶ Гн/м)
- Jᵢ - момент инерции
- bᵢ - коэффициент рассеивания
- cᵢ - приведенная жесткость
- τ = χ/(2πfR) - запаздывание
- l - длина проводника
- l₁ - длина электрода
- Iᵢ⁰ - стационарный ток
- α - анодно-катодное напряжение
- β - градиент столба дуги
- R - активное сопротивление
- χ - реактивное сопротивление"""
                       )

    # Блок с изображениями
    img_paned = ttk.PanedWindow(paned, orient=tk.VERTICAL)
    _load_image(img_paned, "images/рисунок-1.png", "Рис 1. Схема комплекса ДСП", 500, 350)
    _load_image(img_paned, "images/рисунок-2.png", "Рис 2. Упрощенная эквивалентная механическая модель", 500, 300)

    paned.add(text_frame, weight=2)
    paned.add(img_paned, weight=1)


def _load_image(parent, path, caption, width, height):
    """Загружает и отображает изображение с подписью

    Параметры:
        parent: Родительский виджет
        path: Путь к файлу изображения
        caption: Текст подписи
        width: Ширина изображения
        height: Высота изображения
    """
    try:
        frame = ttk.Frame(parent)
        img = Image.open(path).resize((width, height), Image.LANCZOS)
        photo = ImageTk.PhotoImage(img)

        label = ttk.Label(frame, image=photo)
        label.image = photo
        label.pack(pady=5)

        ttk.Label(frame, text=caption, justify=tk.CENTER).pack()
        parent.add(frame, weight=1)
    except Exception as e:
        print(f"Ошибка загрузки изображения {path}: {e}")


def _add_scrolled_text(parent, text):
    """Добавляет текстовое поле с прокруткой

    Параметры:
        parent: Родительский виджет
        text: Текст для отображения
    """
    frame = ttk.Frame(parent)
    text_widget = tk.Text(frame, wrap='word', padx=10, pady=10)
    scrollbar = ttk.Scrollbar(frame, command=text_widget.yview)

    text_widget.configure(yscrollcommand=scrollbar.set)
    text_widget.insert('1.0', text)
    text_widget.config(state='disabled')

    scrollbar.pack(side='right', fill='y')
    text_widget.pack(side='left', fill='both', expand=True)
    frame.pack(fill='both', expand=True)