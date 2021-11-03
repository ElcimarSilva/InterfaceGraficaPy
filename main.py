from tkinter import *


def infos_no_print():
    texto = "Esta é minha mensagem no método"
    texto_do_metodo["text"] = texto


janela = Tk()
janela.title("Minha janela criada em Python")
# janela.geometry("400x400")

texto_orientacao = Label(janela, text="Clique aqui para ver infos do método")
texto_orientacao.grid(column=0, row=0, padx=10, pady=10)

botao = Button(janela, text="Buscar infos que estão no método", command=infos_no_print)
botao = botao.grid(column=0, row=3, padx=10, pady=10)

texto_do_metodo = Label(janela, text="")
texto_do_metodo.grid(column=0, row=5, padx=10, pady=10)

janela.mainloop()
