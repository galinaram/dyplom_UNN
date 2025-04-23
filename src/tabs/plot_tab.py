from tkinter import ttk
from matplotlib.figure import Figure
from src.calculations.compute import compute_stability_boundary
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

    entries = {}
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

def create_plot_tab(parent):
    frame = ttk.Frame(parent)
    frame.grid_columnconfigure(0, weight=3)
    frame.grid_columnconfigure(1, weight=1)
    frame.grid_rowconfigure(0, weight=1)

    # Фрейм для графика (слева)
    plot_frame = ttk.Frame(frame)
    plot_frame.grid(row=0, column=0, sticky="nsew", padx=5, pady=5)

    # Фрейм для полей ввода (справа)
    input_frame = ttk.Frame(frame)
    input_frame.grid(row=0, column=1, sticky="nsew", padx=5, pady=5)

    entries = {}
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

    # Сохраняем элементы для доступа из других модулей
    frame.fig = fig
    frame.canvas = canvas
    frame.omega_entry = omega_range_entry
    frame.step_entry = step_entry
    frame.result_label = result_label
    frame.plot_button = plot_button

    return frame