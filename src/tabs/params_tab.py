from tkinter import ttk
from config import PARAMS


def create_params_tab(parent):
    frame = ttk.Frame(parent)
    params_frame = ttk.LabelFrame(frame, text="Параметры")
    params_frame.pack(fill="both", expand=True, padx=10, pady=10)

    entries = {}
    for param, param_info in PARAMS.items():
        param_row = ttk.Frame(params_frame)
        param_row.pack(fill="x", padx=5, pady=2)

        desc_label = ttk.Label(
            param_row,
            text=f"{param_info['description']} ({param}):",
            width=40,
            anchor="w"
        )
        desc_label.pack(side="left", padx=(0, 5))

        entry = ttk.Entry(param_row, width=12)
        entry.pack(side="left")
        entry.insert(0, str(param_info['value']))
        entries[param] = entry

        if 'unit' in param_info and param_info['unit']:
            unit_label = ttk.Label(param_row, text=param_info['unit'], width=5, anchor="w")
            unit_label.pack(side="left", padx=(5, 0))

    ttk.Label(params_frame, text="").pack()

    # Сохраняем entries для доступа из других модулей
    frame.entries = entries

    return frame