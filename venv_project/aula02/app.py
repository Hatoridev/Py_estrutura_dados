from gui import Gui
import backend as core

app = None

def view_command():
    rows = core.view()
    app.listClientes.delete(0, END)
    for row in rows:
        app.listClientes.insert(END, row)

def search_command():
    app.listClientes.delete(0, END)
    rows = core.search(app.txtNome.get(), app.txtSobrenome.get(), app.txtEmail.get(), app.txtCPF.get())
    for row in rows:
        app.listClientes.insert(END, row)

def insert_command():
    core.insert(app.txtNome.get(), app.txtSobrenome.get(), app.txtEmail.get(), app.txtCPF.get())
    view_command()

def update_command():
    core.update(selected[0], app.txtNome.get(), app.txtSobrenome.get(), app.txtEmail.get(), app.txtCPF.get())
    view_command()

def del_command():
    id = selected[0]
    core.delete(id)
    view_command()

def get_selected_row(event):
    global selected
    index = app.listClientes.curselection()[0]
    selected = app.listClientes.get(index)

    app.entNome.delete(0, END)
    app.entNome.insert(END, selected[1])
    app.entSobrenome.delete(0, END)
    app.entSobrenome.insert(END, selected[2])
    app.entEmail.delete(0, END)
    app.entEmail.insert(END, selected[3])
    app.entCPF.delete(0, END)
    app.entCPF.insert(END, selected[4])

    return selected

if __name__ == "__main__":
    app = Gui()
    app.listClientes.bind('<<ListboxSelect>>', get_selected_row)
    app.btnViewAll.configure(command=view_command)
    app.btnBuscar.configure(command=search_command)
    app.btnInserir.configure(command=insert_command)
    app.btnUpdate.configure(command=update_command)
    app.btnDel.configure(command=del_command)
    app.btnClose.configure(command=app.window.destroy)
    app.run()

# Este arquivo conecta o frontend (GUI) com o backend (operações do banco de dados).

# Define funções de comando que interagem com os métodos do backend e atualizam a interface gráfica.

# get_selected_row captura a linha selecionada na lista e preenche os campos de entrada.

# Configura os botões na GUI para chamar as funções de comando apropriadas.

# Executa a aplicação chamando app.run().

