
import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk

# ==============================
# CONFIGURAÇÃO DA JANELA
# ==============================

janela = tk.Tk()

janela.title("A+ Login")
janela.geometry("1920x1080")
janela.resizable(False, False)
janela.configure(bg="white")

# Canvas para posicionar os elementos
tela = tk.Canvas(
    janela,
    width=1920,
    height=1080,
    bg="white",
    highlightthickness=0
)

tela.place(x=0, y=0)

# FUNÇÃO PARA BORDAS ARREDONDADAS (usei a IA do vscode para criar essa função, pois não sabia como fazer isso)

def retangulo_arredondado(x1, y1, x2, y2, raio, cor):

    pontos = [
        x1+raio, y1,
        x2-raio, y1,
        x2, y1,
        x2, y1+raio,
        x2, y2-raio,
        x2, y2,
        x2-raio, y2,
        x1+raio, y2,
        x1, y2,
        x1, y2-raio,
        x1, y1+raio,
        x1, y1
    ]

    return tela.create_polygon(
        pontos,
        smooth=True,
        fill=cor,
        outline=cor
    )

# LOGO

imagem = Image.open("image 1.png")

imagem = imagem.resize(
    (290, 170),
    Image.Resampling.LANCZOS
)

logo = ImageTk.PhotoImage(imagem)

tela.create_image(
    960, 285,
    image=logo
)

# CAMPO DE E-MAIL

# Sombra
retangulo_arredondado(
    642, 475, 1279, 568,
    13, "#C9C5C5"
)

# Fundo
retangulo_arredondado(
    640, 471, 1277, 564,
    13, "#EEEAEA"
)

email = tk.Entry(
    janela,
    font=("Arial", 22),
    bg="#EEEAEA",
    fg="#947F7F",
    bd=0,
    highlightthickness=0
)

email.place(
    x=670, y=481,
    width=575, height=73
)

email.insert(0, "e-mail")


def entrar_email(event):
    if email.get() == "e-mail":
        email.delete(0, tk.END)
        email.config(fg="#333333")


def sair_email(event):
    if email.get() == "":
        email.insert(0, "e-mail")
        email.config(fg="#947F7F")


email.bind("<FocusIn>", entrar_email)
email.bind("<FocusOut>", sair_email)



# CAMPO DE SENHA

# Sombra
retangulo_arredondado(
    642, 596, 1279, 689,
    13, "#C9C5C5"
)

# Fundo
retangulo_arredondado(
    640, 592, 1277, 685,
    13, "#EEEAEA"
)

senha = tk.Entry(
    janela,
    font=("Arial", 22),
    bg="#EEEAEA",
    fg="#947F7F",
    bd=0,
    highlightthickness=0
)

senha.place(
    x=670, y=602,
    width=575, height=73
)

senha.insert(0, "senha")


def entrar_senha(event):
    if senha.get() == "senha":
        senha.delete(0, tk.END)
        senha.config(fg="#333333", show="*")


def sair_senha(event):
    if senha.get() == "":
        senha.config(show="", fg="#947F7F")
        senha.insert(0, "senha")


senha.bind("<FocusIn>", entrar_senha)
senha.bind("<FocusOut>", sair_senha)


# FUNÇÃO DO BOTÃO ACESSAR

def acessar():

    usuario = email.get()
    senha_digitada = senha.get()

    if usuario not in ("", "e-mail") and senha_digitada not in ("", "senha"):

        messagebox.showinfo(
            "Login",
            "Dados preenchidos!"
        )

    else:

        messagebox.showwarning(
            "Atenção",
            "Preencha todos os campos!"
        )



# BOTÃO ACESSAR


# Sombra
retangulo_arredondado(
    643, 718, 1278, 802,
    11, "#C9C5C5"
)

# Fundo azul
botao = retangulo_arredondado(
    641, 714, 1276, 798,
    11, "#2996C5"
)

# Texto do botão
texto_botao = tela.create_text(
    958, 756,
    text="ACESSAR",
    fill="white",
    font=("Arial", 18, "bold")
)

# Clique no botão
tela.tag_bind(botao, "<Button-1>", lambda event: acessar())
tela.tag_bind(texto_botao, "<Button-1>", lambda event: acessar())


# PRIMEIRO ACESSO

primeiro_acesso = tela.create_text(
    960, 881,
    text="PRIMEIRO ACESSO",
    fill="#2996C5",
    font=("Arial", 18, "bold"),
    justify="center"
)

tela.tag_bind(
    primeiro_acesso,
    "<Button-1>",
    lambda event: messagebox.showinfo(
        "Primeiro acesso",
        "Área de primeiro acesso"
    )
)




janela.mainloop()
