# Файл plotter.py
# Реализация визуализации границы устойчивости системы

import matplotlib.pyplot as plt


def plot_stability_boundary(real_values, imag_values):
    """Строит график границы устойчивости на комплексной плоскости

    Параметры:
        real_values (list): Список значений действительной части
        imag_values (list): Список значений мнимой части

    Возвращает:
        None: Отображает интерактивное окно с графиком
    """
    # Инициализация фигуры с квадратным соотношением сторон
    plt.figure(figsize=(8, 8))

    # Основной график границы устойчивости
    plt.plot(real_values, imag_values, color="red", label="Граница устойчивости")

    # Оси координат
    plt.axhline(0, color="black", linewidth=0.5, linestyle="--")
    plt.axvline(0, color="black", linewidth=0.5, linestyle="--")

    # Настройка оформления
    plt.title("Граница устойчивости системы электрододержателей")
    plt.xlabel("Действительная часть")
    plt.ylabel("Мнимая часть")
    plt.legend()
    plt.grid(True)

    # Отображение графика
    plt.show()