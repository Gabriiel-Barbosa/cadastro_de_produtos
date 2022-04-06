#Bibliótecas Importadas 
from cProfile import label
import tkinter as tk
from tkinter import ttk
import datetime as dt
from turtle import color

lista_tipos = ["Arduino Mega", "Arduino Uno", "Proboard Mine", "Jumpers" ]

#código inicial da janela

janela = tk.Tk()

#título da janela

janela.title("Ferramenta de Cadastro de Produtos")

label_descricao = tk.Label(text="Descrição do Material")
label_descricao.grid(row=1, column=0, padx=10, pady=10, sticky='nswe',columnspan=4)

entry_descricao = tk.Entry()
entry_descricao.grid(row=2, column=0, padx=10, pady=10, sticky='nswe',columnspan=4)

label_tipo_unidade = tk.Label(text="Tipo da Unidade do Material    ")
label_tipo_unidade.grid(row=3, column=0, padx=10, pady=10, sticky='nswe',columnspan=2)


combobox_selecionar_tipo= ttk.Combobox(values=lista_tipos)
combobox_selecionar_tipo.grid(row=3, column=2, padx=10, pady=10, sticky='nswe', columnspan=2 )

label_quantidade = tk.Label(text="Quantidade na unidade de material")
label_quantidade.grid(row=4, column=0, padx=10, pady=10, sticky='nswe',columnspan=2)

label_quantidade = tk.Entry()
label_quantidade.grid(row=4, column=2, padx=10, pady=10, sticky='nswe',columnspan=2)


botao_criar_codigo =   tk.Button(text="Criar Código")
botao_criar_codigo.grid(row=5, column=0, padx=10, pady=10, sticky='nswe',columnspan=4)

janela.mainloop()
