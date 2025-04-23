import tkinter as tk
from tkinter import ttk, BOTH
from src.calculations.compute import compute_stability_boundary
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from config import PARAMS


def get_params_from_entries(entries):
    """
    Получает параметры из полей ввода и возвращает их в виде словаря.
    Теперь учитывает новую структуру PARAMS с 'value' и 'description'
    """
    params = PARAMS.copy()  # Используем исходные параметры
    for key, entry in entries.items():
        try:
            # Обновляем только значение параметра, сохраняя описание
            params[key]['value'] = float(entry.get())
        except ValueError:
            # Если значение неверное, используем значение по умолчанию
            params[key]['value'] = PARAMS[key]['value']
    return params


def check_stability(real_values, imag_values):
    """
    Проверяет, находится ли точка w = -1 внутри замкнутой кривой.
    """
    from matplotlib.path import Path
    points = list(zip(real_values, imag_values))
    path = Path(points)
    return path.contains_point((-1, 0))


def on_plot_button_click(entries, omega_range_entry, step_entry, canvas, fig, result_label):
    """
    Обработчик события для кнопки "Построить график".
    Строит график устойчивости на встроенном виджете и проверяет устойчивость.
    """
    params = get_params_from_entries(entries)
    try:
        omega_range = float(omega_range_entry.get())
        step = float(step_entry.get())
    except ValueError:
        omega_range = 100  # Значение по умолчанию
        step = 0.01  # Значение по умолчанию

    # Вычисление значений для границы устойчивости
    real_values, imag_values = compute_stability_boundary(params, omega_range, step)

    # Проверка устойчивости
    unstable = check_stability(real_values, imag_values)

    # Очистка текущего графика
    fig.clear()
    ax = fig.add_subplot(111)

    # Построение графика
    ax.plot(real_values, imag_values, color="red", label="Граница устойчивости")

    # Настройки графика
    ax.axhline(0, color="black", linewidth=0.5, linestyle="--")
    ax.axvline(0, color="black", linewidth=0.5, linestyle="--")
    ax.set_xlabel("Действительная часть")
    ax.set_ylabel("Мнимая часть")
    ax.set_title("Кривая D-разбиения")

    # Настройка легенды (правый верхний угол, меньший размер)
    ax.legend(loc='upper right', prop={'size': 9})

    ax.grid(True)

    # Обновляем текст результата
    stability_text = "Состояние равновесия неустойчиво" if unstable else "Состояние равновесия устойчиво"
    result_label.config(
        text=f"Вывод:\n{stability_text}",
        foreground="red" if unstable else "green",
        background="white",
        font=("Arial", 12),
        relief="solid",
        padding=(10, 10),
        anchor="center",
        justify="center"
    )

    # Отображение обновленного графика
    canvas.draw()

    return unstable, ax


def run_interface():
    """
    Запускает графический интерфейс приложения.
    """
    root = tk.Tk()
    root.title("Анализ устойчивости системы")
    root.geometry("1000x600")

    # Создаем набор вкладок
    notebook = ttk.Notebook()
    notebook.pack(expand=True, fill=BOTH)

    # Создаем фреймы
    frame1 = ttk.Frame(notebook)
    frame2 = ttk.Frame(notebook)
    frame3 = ttk.Frame(notebook)

    frame1.pack(fill=BOTH, expand=True)
    frame2.pack(fill=BOTH, expand=True)
    frame3.pack(fill=BOTH, expand=True)

    # Добавляем фреймы в качестве вкладок
    notebook.add(frame1, text="Главное меню")
    notebook.add(frame2, text="Параметры")
    notebook.add(frame3, text="Построение границы D-разбиения")

    # Добавляем Label с текстом в главное меню
    label_dsp = tk.Label(frame1,
                         text="Исследование устойчивости состояния равновесия системы, описывающей колебания электрододержателей дуговой сталеплавильной печи",
                         font=("Arial", 24),
                         wraplength=800)
    label_dsp.place(relx=0.5, rely=0.5, anchor="center")


    # Создание фрейма для ввода параметров
    params_frame = ttk.LabelFrame(frame2, text="Параметры")
    params_frame.pack(fill="both", expand=True, padx=10, pady=10)

    entries = {}
    for idx, param in enumerate(PARAMS.keys()):
        param_info = PARAMS[param]

        # Создаем строку параметра
        param_row = ttk.Frame(params_frame)
        param_row.pack(fill="x", padx=5, pady=2)

        # Описание и имя параметра (фиксированная ширина для выравнивания)
        desc_label = ttk.Label(param_row, text=f"{param_info['description']} ({param}):", width=40, anchor="w")
        desc_label.pack(side="left", padx=(0, 5))

        # Поле ввода значения
        entry = ttk.Entry(param_row, width=12)
        entry.pack(side="left")
        entry.insert(0, str(param_info['value']))
        entries[param] = entry

        # Единица измерения (если есть)
        if 'unit' in param_info and param_info['unit']:
            unit_label = ttk.Label(param_row, text=param_info['unit'], width=5, anchor="w")
            unit_label.pack(side="left", padx=(5, 0))

    # Добавляем отступ снизу
    ttk.Label(params_frame, text="").pack()

    # for idx, param in enumerate(PARAMS.keys()):
    #     # Используем описание параметра в качестве подписи
    #     label_text = f"{PARAMS[param]['description']} ({param}):"
    #     label = ttk.Label(params_frame, text=label_text)
    #     label.grid(row=idx, column=0, padx=5, pady=5, sticky="w")
    #
    #     entry = ttk.Entry(params_frame)
    #     entry.grid(row=idx, column=1, padx=5, pady=5)
    #     entry.insert(0, str(PARAMS[param]['value']))
    #     entries[param] = entry

    # Разделение frame3 на две колонки
    frame3.grid_columnconfigure(0, weight=3)
    frame3.grid_columnconfigure(1, weight=1)
    frame3.grid_rowconfigure(0, weight=1)

    # Фрейм для графика (слева)
    plot_frame = ttk.Frame(frame3)
    plot_frame.grid(row=0, column=0, sticky="nsew", padx=5, pady=5)

    # Фрейм для полей ввода (справа)
    input_frame = ttk.Frame(frame3)
    input_frame.grid(row=0, column=1, sticky="nsew", padx=5, pady=5)

    # Создание графика
    fig = Figure(figsize=(6, 4), dpi=100)
    canvas = FigureCanvasTkAgg(fig, master=plot_frame)
    canvas_widget = canvas.get_tk_widget()
    canvas_widget.pack(fill="both", expand=True)

    # Поля ввода omega и шага
    omega_label = ttk.Label(input_frame, text="Максимальное значение omega:")
    omega_label.pack(padx=5, pady=5)
    omega_range_entry = ttk.Entry(input_frame)
    omega_range_entry.pack(padx=5, pady=5)
    omega_range_entry.insert(0, "100")

    step_label = ttk.Label(input_frame, text="Шаг вычислений:")
    step_label.pack(padx=5, pady=5)
    step_entry = ttk.Entry(input_frame)
    step_entry.pack(padx=5, pady=5)
    step_entry.insert(0, "0.01")

    # Label для вывода результата
    result_label = ttk.Label(
        input_frame,
        text="Вывод:\nЗдесь будет результат",
        background="white",
        font=("Arial", 12),
        relief="solid",
        padding=(10, 10),
        anchor="center",
        justify="center"
    )
    result_label.pack(pady=20, fill="x")

    # Кнопка построения графика
    plot_button = ttk.Button(
        input_frame,
        text="Построить график",
        command=lambda: on_plot_button_click(
            entries, omega_range_entry, step_entry, canvas, fig, result_label
        )
    )
    plot_button.pack(pady=10)

    root.mainloop()