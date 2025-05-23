# Модуль compute.py
# Реализация математической модели системы

import math
import cmath


def get_param_value(params, key):
    """Вспомогательная функция для получения значения параметра из новой структуры"""
    return params[key]['value']


def calculate_sigma(params):
    """
    Функция для расчета приведенной электродинамической силы sigma.
    """
    mu0 = get_param_value(params, 'mu0')
    I1 = get_param_value(params, 'I')
    alfa3 = get_param_value(params, 'alfa')
    betta3 = get_param_value(params, 'betta')
    lg = get_param_value(params, 'lg')
    R = get_param_value(params, 'R')
    X = get_param_value(params, 'X')
    r13 = get_param_value(params, 'r')
    l = get_param_value(params, 'l')
    l1 = get_param_value(params, 'l1')

    mua = mu0 * 1  # для случая, если относительная магнитная проницаемость равна 1
    pi = math.pi
    sigma = (mua * I1 * ((alfa3 + betta3 * lg) + I1 * R) * betta3 * l * (l * l / 2 + l1 * l)) / \
            (2 * pi * r13 * (I1 * (R ** 2 + X ** 2) + R * (alfa3 + betta3 * lg)))

    return sigma

def calculate_w(omega, params):
    """
    Функция для расчета значения функции комплексной переменной w в зависимости от omega.
    """
    c = get_param_value(params, 'c')
    J = get_param_value(params, 'J')
    b = get_param_value(params, 'b')
    tau = get_param_value(params, 't')  # t в формуле соответствует tau
    sigma = calculate_sigma(params)

    # Создаем комплексное число для расчетов
    p = complex(0, omega)
    P1 = J * p ** 2 + b * p + c
    P2 = J * p ** 2 + b * p + c  # В формуле P1 и P2 одинаковые, так как c1 = c2 = c

    # Расчет комплексной функции w согласно формуле
    term1 = 8 * sigma ** 3 * cmath.exp(-3 * p * tau)
    term2 = (40 * c + 8 * P1 + P2) * sigma ** 2 * cmath.exp(-2 * p * tau)
    term3 = (64 * c ** 2 + 32 * P1 + 2 * P2) * c * sigma * cmath.exp(-p * tau)
    term4 = 32 * c ** 3 + (32 * P1 + P2) * c ** 2

    w = (term1 - term2 + term3 - term4) / (P1 ** 2 * P2)

    return w


def compute_values(params,omega_min, omega_range, step):
    """
    Вычисление значений реальной и мнимой частей функции w для заданного диапазона omega.
    """
    real_values = []
    imag_values = []
    omega_values = []

    omega = omega_min
    while omega <= omega_range:
        w = calculate_w(omega, params)
        real_values.append(w.real)
        imag_values.append(w.imag)
        omega_values.append(omega)
        omega += step

    return omega_values, real_values, imag_values


def compute_stability_boundary(params, omega_min, omega_range, step):
    """
    Вычисление границы устойчивости системы на комплексной плоскости.
    Возвращает значения реальной и мнимой частей функции для заданного диапазона omega.
    """
    real_values = []
    imag_values = []

    omega = omega_min
    while omega <= omega_range:
        w = calculate_w(omega, params)
        real_values.append(w.real)  # Действительная часть
        imag_values.append(w.imag)  # Мнимая часть
        omega += step

    return real_values, imag_values