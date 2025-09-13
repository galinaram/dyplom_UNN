# Модуль compute.py
# Реализация математической модели системы электрододержателей ДСП

import math
import cmath


def get_param_value(params, key):
    """Получает значение параметра из словаря параметров"""
    return params[key]['value']


def calculate_sigma(params):
    """
    Вычисляет приведенную электродинамическую силу sigma по формуле:
    sigma = (μa * I1 * ((α3 + β3*lg) + I1*R) * β3 * l * (l²/2 + l1*l)) /
            (2π * r13 * (I1*(R² + X²) + R*(α3 + β3*lg)))
    где:
    μa - магнитная проницаемость
    I1 - ток
    α3, β3 - коэффициенты
    lg, R, X, r13, l, l1 - геометрические параметры системы
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

    mua = mu0 * 1  # относительная магнитная проницаемость
    pi = math.pi

    numerator = mua * I1 * ((alfa3 + betta3 * lg) + I1 * R) * betta3 * l * (l * l / 2 + l1 * l)
    denominator = 2 * pi * r13 * (I1 * (R ** 2 + X ** 2) + R * (alfa3 + betta3 * lg))

    return numerator / denominator


def calculate_w(omega, params):
    """
    Вычисляет значение комплексной функции w(ω) по формуле:
    w(ω) = [8σ³e^(-3pτ) - (40c + 8P1 + P2)σ²e^(-2pτ) +
            (64c² + 32P1 + 2P2)cσe^(-pτ) - (32c³ + (32P1 + P2)c²)] / (P1² * P2)
    где:
    p = iω (комплексная переменная)
    P1 = P2 = Jp² + bp + c
    σ - приведенная электродинамическая сила
    τ - временная задержка
    """
    c = get_param_value(params, 'c')
    J = get_param_value(params, 'J')
    b = get_param_value(params, 'b')
    tau = get_param_value(params, 't')  # временная задержка
    sigma = calculate_sigma(params)

    p = complex(0, omega)  # комплексная переменная
    P = J * p ** 2 + b * p + c  # характеристический полином

    # Расчет слагаемых функции w
    term1 = 8 * sigma ** 3 * cmath.exp(-3 * p * tau)
    term2 = (40 * c + 8 * P + P) * sigma ** 2 * cmath.exp(-2 * p * tau)
    term3 = (64 * c ** 2 + 32 * P + 2 * P) * c * sigma * cmath.exp(-p * tau)
    term4 = 32 * c ** 3 + (32 * P + P) * c ** 2

    return (term1 - term2 + term3 - term4) / (P ** 2 * P)


def compute_values(params, omega_min, omega_max, step):
    """
    Вычисляет значения функции w(ω) в диапазоне частот [omega_min, omega_max] с шагом step
    Возвращает:
    - список частот omega
    - список действительных частей w(ω)
    - список мнимых частей w(ω)
    """
    real_values = []
    imag_values = []
    omega_values = []

    omega = omega_min
    while omega <= omega_max:
        w = calculate_w(omega, params)
        real_values.append(w.real)
        imag_values.append(w.imag)
        omega_values.append(omega)
        omega += step

    return omega_values, real_values, imag_values


def compute_stability_boundary(params, omega_min, omega_max, step):
    """
    Вычисляет границу устойчивости (действительную и мнимую части w(ω))
    для анализа устойчивости методом D-разбиения
    """
    return compute_values(params, omega_min, omega_max, step)[1:]