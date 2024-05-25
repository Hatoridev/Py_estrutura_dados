import tkinter as tk
from tkinter import messagebox

def show_series():
    # Criando a série
    series_objeto = [1, 7, 9, 13, 17, 99]
    # Exibindo a série em uma caixa de mensagem
    messagebox.showinfo("Série", series_objeto)

def show_custom_series():
    # Criando a série com índices personalizados
    series_obj2 = {'alfa': 4, 'beta': 7, 'teta': 8, 'gama': -2}
    # Exibindo a série personalizada em uma caixa de mensagem
    messagebox.showinfo("Série Personalizada", series_obj2)

def show_dataframe():
    # Dados para o DataFrame
    disciplinas = {
        'cursos': ['Estatística', 'Economia', 'Calculo', 'Geometria'],
        'créditos': [90, 60, 96, 40],
        'requisito': [True, False, True, False]
    }
    # Exibindo o DataFrame em uma caixa de mensagem
    messagebox.showinfo("DataFrame", disciplinas)

root = tk.Tk()
root.title("Scripts Python com Tkinter")

# Botão para mostrar a série
btn_show_series = tk.Button(root, text="Mostrar Série", command=show_series)
btn_show_series.pack()

# Botão para mostrar a série personalizada
btn_show_custom_series = tk.Button(root, text="Mostrar Série Personalizada", command=show_custom_series)
btn_show_custom_series.pack()

# Botão para mostrar o DataFrame
btn_show_dataframe = tk.Button(root, text="Mostrar DataFrame", command=show_dataframe)
btn_show_dataframe.pack()

root.mainloop()

# Comentários explicativos:

# Este script combina os três scripts anteriores em um único arquivo.

# Cada função definida cria e exibe um componente de dados específico (série ou DataFrame) usando Tkinter.

# Os botões na interface gráfica executam essas funções quando clicados.

# O código Tkinter no final cria os botões e inicia a interface gráfica principal.

