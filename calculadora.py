import tkinter as tk


def make_root() -> tk.Tk:
    root = tk.Tk()
    root.title('Calculadora')
    root.config(padx=10, pady=10, background= '#fff')
    root.resizable(False, False)
    return root

def make_label(root) -> tk.Label:
    label = tk.Label(
        root, text = 'Sem Conta Ainda',
        anchar='e', justify='right', background='#fff'
    )
    label.grid(row=0, column=0, columnspan=5)
    return label
# so pra testar