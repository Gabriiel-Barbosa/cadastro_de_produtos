#Bibliótecas Importadas 
from cProfile import label
import tkinter as tk
from tkinter import ttk
import datetime as dt
from turtle import color

lista_tipos = ["Arduino Mega", "Arduino Uno", "Proboard Mine", "Jumpers" ]

#código inicial da janela

janela = tk.Tk()

#Lista de códigos para testar o programa 

lista_codigos = []

# Parte Lógica 

def inserir_codigo():
    descricao = entry_descricao.get()
    tipo = combobox_selecionar_tipo.get()
    quantidade = Entry_quantidade.get()
    data_criacao = dt.datetime.now()
    data_criacao = data_criacao.strftime("%d/%m/%Y %H:%M")
    codigo = len(lista_codigos) + 1
    # Essa não é a melhor lógica de tratamento, porém é funcional para o estado atual do código. 
    codigo_str = "COD-{}".format(codigo)
    lista_codigos.append((codigo_str,descricao,tipo,quantidade,data_criacao))

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

Entry_quantidade = tk.Entry()
Entry_quantidade.grid(row=4, column=2, padx=10, pady=10, sticky='nswe',columnspan=2)


botao_criar_codigo =   tk.Button(text="Criar Código", command=inserir_codigo)
botao_criar_codigo.grid(row=5, column=0, padx=10, pady=10, sticky='nswe',columnspan=4)

janela.mainloop()

#Print pra teste da lista. E breve será  trocado para o banco de dados ou um dataframe
print(lista_codigos)