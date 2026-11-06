import tkinter as tk

janela = tk.Tk()

janela.title("A+ Login")
janela.geometry ("1920x1080")
janela.configure(bg="white")

conteudo = tk.Frame (janela, bg="white")
conteudo.pack(expand=True)

imagem_logo = tk.PhotoImage(file="image 1.png")

logo = tk.Label(
    conteudo,
    image=imagem_logo,
    bg="white"
    )

logo.pack(pady=30)

email = tk.Entry(
    conteudo,
    text="Email",
    font= ("Arial", 16),
    bg="#F0EBEB",
    fg="#8D7777",
    width=35,
    relief="flat"
)

email.pack (pady=12, ipady=18)

senha = tk.Entry(
    conteudo,
    font= ("Arial", 16),
    bg="#F0EBEB",
    fg="#8D7777",
    width=35,
    relief="flat",
    show="*"
)

senha.pack (pady=12, ipady=18)

botao = tk.Button(
    conteudo,
    text="acessar",
    font= ("Arial", 14, "bold"),
    bg="#2996C5",
    fg="white",
    width=35,
    height=2,
    relief="flat",
    cursor="hand2"
)

botao.pack(pady=15)

primeiro_acesso = tk.Label(
    conteudo,
    text="PRIMEIRO ACESSO",
    font=("Arial", 13, "bold"),
    fg="#2996C5",
    bg="white",
    cursor="hand2"
)

primeiro_acesso.pack(pady=25)




           
janela.mainloop()


