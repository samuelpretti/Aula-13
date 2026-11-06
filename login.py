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



           
janela.mainloop()


