from setuptools import setup, find_packages
import os
"""Установка объекта sympy функции из строки.
    Количество переменных проверяется. Отображение функции настраивается.

    Parameters
    ===========

    input_investigated_function: str
        Входная строка с функцией
    functions_symbols: tuple, optional
        Переменные функции
    functions_title: str
        Заголовок для отображения
    functions_designation: str
        Обозначение для отображения
    is_display_input: bool
        Отображать входную функцию или нет
    _is_system: bool
        Вызов функции программой или нет

    Returns
    ===========

    input_investigated_function: str
        Входная строка с функцией
    investigated_function: sympy
        Исследуемая функция
    functions_symbols: tuple
        Переменные функции
    """



setup(
    url = 'https://gitlab.com/optimization-tasks-in-machine-learning/tz9_merging_library',
    version = '0.1.0',
    name = 'tz9_merging_library',
    description = 'ТЗ9 Объединенная библиотека',
    author = 'Быханов Никита, Алексеев Леонид, Семёнова Полина, Янина Марина, Буркина Елизавета, Егорин Никита',
    author_email = 'leonidalekseevv@mail.ru',
    license = 'MIT',
    python_requires = '>=3.7',
    package_data = {
        '': ['*.pyc'],
    },
    package_dir = {
        '': os.path.dirname(os.path.realpath(__file__)),
    },
    packages = [
        'tz8_stochastic_optimization',
        'tz7_cutting_optimisation',
        'tz6_classification',
        'tz5_constrained_optimization',
        'tz4_regression',
        'tz3_multidimensional_optimization',
        'tz2_numerical_optimization',
        'tz1_find_extremums',
    ],
)
