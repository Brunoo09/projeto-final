import tkinter as tk
import sqlite3
from tkinter import messagebox

root = tk.Tk()
root.title('IMC')
root.geometry('500x500')

def calculo():
    peso = float(input_peso.get())
    altura = float(input_altura.get())
    calculo = peso / (altura**2)
    print(f'{calculo:.2f}')
    Calculo.config(text=f'SEU IMC {calculo:.2f}')
    
    if calculo < 18.5:
        abaixo = tk.Label(root, text='ABAIXO DO PESO')
        abaixo.pack()
    elif calculo > 18.5:
        adequado = tk.Label(root, text='PESO ADEQUADO')
        adequado.pack()
    elif calculo > 25:
        pre_obeso = tk.Label(root, text='PRÉ-OBESO') 
        pre_obeso.pack()
    elif calculo > 30:
        obesidade = tk.Label(root, text='OBESIDADE') 

def create_db():
    con = sqlite3.connect('meu_db')
    cursor = con.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS pessoas(
                           id INTEGER PRIMARY KEY AUTOINCREMENT,
                           nomes TEXT NOT NULL)''')


    con.commit()
    con.close()

def salvar():
    nome  =  entry_Calculo.get()
    if nome:
        con = sqlite3.connect('meu_db')
        cursor = con.cursor()
        cursor.execute("INSERT INTO pessoas(nomes)VALUES (?) ", (nome,) )
        con.commit()
        cursor.close()
        messagebox.showinfo('Dado inserido com sucesso', 'inserido com sucesso')
    else:
        messagebox.showerror('Ocorreu um erro', 'erro')



input_peso = tk.Entry(root)
input_peso.pack()

input_altura = tk.Entry(root)
input_altura.pack()

bnt_calcular = tk.Button(root, text='cadastrar', command=calculo)
bnt_calcular.pack()

btn_salvar = tk.Button(root, text="salvar", command=salvar)
btn_salvar.pack()

Calculo = tk.Label(root, text='=')
Calculo.pack()

create_db()
root.mainloop()
