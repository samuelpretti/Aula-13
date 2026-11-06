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



           
janela.mainloop()


