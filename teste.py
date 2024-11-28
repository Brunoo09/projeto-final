import tkinter as tk 
import sqlite3
from tkinter import messagebox





def create_db():
    con = sqlite3.connect('meu_db')
    cursor = con.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS pessoas(
                           id INTEGER PRIMARY KEY AUTOINCREMENT,
                           nomes TEXT NOT NULL)''')


    con.commit()
    con.close()




def salvar():
    nome  =  entry_nome.get()
    if nome:
        con = sqlite3.connect('meu_db')
        cursor = con.cursor()
        cursor.execute("INSERT INTO pessoas(nomes)VALUES (?) ", (nome,) )
        con.commit()
        cursor.close()
        messagebox.showinfo('Dado inserido com sucesso', 'inserido com sucesso')
        listar_nomes()
        limpar_dados()


    else:
        messagebox.showerror('Ocorreu um erro', 'erro')        




def listar_nomes():
    con = sqlite3.connect('meu_db')
    cursor = con.cursor()
    cursor.execute('SELECT * FROM   pessoas')
    registros = cursor.fetchall()
    cursor.close()


    listbox.delete(0, tk.END)
    for registro in registros:
        listbox.insert(tk.END,f'ID{registro[0]}, NOME {registro[1]}')



def limpar_dados():
    entry_nome.delete(0,tk.END)


        


root =  tk.Tk()
root.title('CRUD')


entry = tk.Entry(root)
entry.pack()


entry_nome = tk.Entry(root)
entry_nome.pack()



listbox = tk.Listbox(root, width=35, height=25)
listbox.pack()



btn_salvar =  tk.Button(root, text='Salvar', command=salvar)
btn_salvar.pack()


btn_limpar =  tk.Button(root, text='Limpar', command=limpar_dados)
btn_limpar.pack()



create_db()
listar_nomes()


root.mainloop()
