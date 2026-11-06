
import tkinter as tk
from tkinter import messagebox

# Função do botão acessar
def acessar():
    usuario = email.get()
    senha_digitada = senha.get()

    if usuario != "e-mail" and senha_digitada != "senha" and usuario and senha_digitada:
        messagebox.showinfo("Login", "Acesso realizado!")
    else:
        messagebox.showwarning("Atenção", "Preencha todos os campos!")


# Criando a janela
janela = tk.Tk()

janela.title("A+ Login")
janela.geometry("1000x700")
janela.configure(bg="white")


# Área principal
conteudo = tk.Frame(janela, bg="white")
conteudo.pack(expand=True)


# Logo
logo = tk.Label(
    conteudo,
    text="a+ MAIS",
    font=("Arial", 45, "bold"),
    fg="#2996C5",
    bg="white"
)
logo.pack(pady=30)


# Campo de e-mail
email = tk.Entry(
    conteudo,
    font=("Arial", 16),
    bg="#F0EBEB",
    fg="#8D7777",
    relief="flat",
    width=45
)

email.pack(pady=12, ipady=18)
email.insert(0, "e-mail")


# Campo de senha
senha = tk.Entry(
    conteudo,
    font=("Arial", 16),
    bg="#F0EBEB",
    fg="#8D7777",
    relief="flat",
    width=45
)

senha.pack(pady=12, ipady=18)
senha.insert(0, "senha")


# Esconder a senha quando o usuário começar a digitar
def entrar_senha(event):
    if senha.get() == "senha":
        senha.delete(0, tk.END)
        senha.config(show="*")


def sair_senha(event):
    if senha.get() == "":
        senha.config(show="")
        senha.insert(0, "senha")


senha.bind("<FocusIn>", entrar_senha)
senha.bind("<FocusOut>", sair_senha)


# Botão acessar
botao = tk.Button(
    conteudo,
    text="ACESSAR",
    font=("Arial", 14, "bold"),
    bg="#2996C5",
    fg="white",
    width=45,
    height=2,
    relief="flat",
    cursor="hand2",
    command=acessar
)

botao.pack(pady=15)


# Primeiro acesso
primeiro_acesso = tk.Label(
    conteudo,
    text="PRIMEIRO ACESSO",
    font=("Arial", 13, "bold"),
    fg="#2996C5",
    bg="white",
    cursor="hand2"
)

primeiro_acesso.pack(pady=25)


# Mantém a janela aberta
janela.mainloop()
