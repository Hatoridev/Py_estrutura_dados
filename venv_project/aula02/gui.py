from tkinter import *

class Gui:
    """Classe da Interface Gráfica"""

    x_pad = 5
    y_pad = 3
    width_entry = 30

    def __init__(self):
        self.window = Tk()
        self.window.wm_title("PYSQL versão 1.0")

        self.lblnome = Label(self.window, text="Nome")
        self.lblsobrenome = Label(self.window, text="Sobrenome")
        self.lblemail = Label(self.window, text="Email")
        self.lblcpf = Label(self.window, text="CPF")

        self.txtNome = StringVar()
        self.txtSobrenome = StringVar()
        self.txtEmail = StringVar()
        self.txtCPF = StringVar()

        self.entNome = Entry(self.window, textvariable=self.txtNome, width=self.width_entry)
        self.entSobrenome = Entry(self.window, textvariable=self.txtSobrenome, width=self.width_entry)
        self.entEmail = Entry(self.window, textvariable=self.txtEmail, width=self.width_entry)
        self.entCPF = Entry(self.window, textvariable=self.txtCPF, width=self.width_entry)

        self.listClientes = Listbox(self.window, width=100)
        self.scrollClientes = Scrollbar(self.window)

        self.btnViewAll = Button(self.window, text="Ver todos")
        self.btnBuscar = Button(self.window, text="Buscar")
        self.btnInserir = Button(self.window, text="Inserir")
        self.btnUpdate = Button(self.window, text="Atualizar Selecionados")
        self.btnDel = Button(self.window, text="Deletar Selecionados")
        self.btnClose = Button(self.window, text="Fechar")

        self._grid_widgets()
        self._style_widgets()

    def _grid_widgets(self):
        self.lblnome.grid(row=0, column=0)
        self.lblsobrenome.grid(row=1, column=0)
        self.lblemail.grid(row=2, column=0)
        self.lblcpf.grid(row=3, column=0)

        self.entNome.grid(row=0, column=1, padx=50, pady=5)
        self.entSobrenome.grid(row=1, column=1, padx=50, pady=5)
        self.entEmail.grid(row=2, column=1, padx=50, pady=5)
        self.entCPF.grid(row=3, column=1, padx=50, pady=5)

        self.listClientes.grid(row=0, column=2, rowspan=10, padx=10, pady=10)
        self.scrollClientes.grid(row=0, column=3, rowspan=10, padx=10, pady=10, sticky='NS')

        self.btnViewAll.grid(row=4, column=0, columnspan=2, pady=5)
        self.btnBuscar.grid(row=5, column=0, columnspan=2, pady=5)
        self.btnInserir.grid(row=6, column=0, columnspan=2, pady=5)
        self.btnUpdate.grid(row=7, column=0, columnspan=2, pady=5)
        self.btnDel.grid(row=8, column=0, columnspan=2, pady=5)
        self.btnClose.grid(row=9, column=0, columnspan=2, pady=5)

    def _style_widgets(self):
        self.listClientes.configure(yscrollcommand=self.scrollClientes.set)
        self.scrollClientes.configure(command=self.listClientes.yview)

        for child in self.window.winfo_children():
            widget_class = child.__class__.__name__
            if widget_class == "Button":
                child.grid_configure(sticky='WE', padx=self.x_pad, pady=self.y_pad)
            elif widget_class == "Listbox":
                child.grid_configure(padx=0, pady=0, sticky='NS')
            elif widget_class == "Scrollbar":
                child.grid_configure(padx=0, pady=0, sticky='NS')
            else:
                child.grid_configure(padx=self.x_pad, pady=self.y_pad, sticky='N')

    def run(self):
        self.window.mainloop()

# A classe Gui cria a interface gráfica usando tkinter.

# No método __init__, os widgets são instanciados e configurados.

# Os métodos _grid_widgets e _style_widgets organizam e estilizam os widgets.

# O método run inicia o loop principal da interface gráfica.

