from tkinter import *

janela = Tk()
janela.title("Fábrica de Software 33")
janela.geometry("700x900")
texto1 = Label(janela,text="Feira Bosque da Paz", font=("Arial",22))
texto1.pack(pady=20,padx=30)

def mudarNome():
    texto1.config(text="Olá, Mundo da Fábrica")

salvar = Button(janela,text="Salvar", command=mudarNome)
salvar.pack(pady=20)

janela.mainloop()