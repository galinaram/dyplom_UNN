import tkinter as tk
from tkinter import ttk


def create_main_tab(parent):
    frame = ttk.Frame(parent)

    label = tk.Label(
        frame,
        text="Исследование устойчивости состояния равновесия системы, описывающей колебания электрододержателей дуговой сталеплавильной печи",
        font=("Arial", 24),
        wraplength=800
    )
    label.place(relx=0.5, rely=0.5, anchor="center")

    return frame