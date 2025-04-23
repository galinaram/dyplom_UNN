import matplotlib.pyplot as plt

def plot_stability_boundary(real_values, imag_values):
    """
    Функция для построения границы устойчивости на комплексной плоскости.
    Ось X — действительная часть, ось Y — мнимая часть.
    """
    plt.figure(figsize=(8, 8))

    # Построение графика на комплексной плоскости
    plt.plot(real_values, imag_values, label="Граница устойчивости", color="red")

    # Настройки графика
    plt.axhline(0, color="black", linewidth=0.5, linestyle="--")  # Ось X
    plt.axvline(0, color="black", linewidth=0.5, linestyle="--")  # Ось Y
    plt.xlabel("Действительная часть")
    plt.ylabel("Мнимая часть")
    plt.title("Граница устойчивости системы")
    plt.legend()
    plt.grid(True)

    # Отображение графика
    plt.show()
