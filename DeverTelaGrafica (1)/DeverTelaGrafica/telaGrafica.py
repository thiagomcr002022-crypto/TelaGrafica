import tkinter as tk  # importa tkinter normal

def validarSenha():
    texUsuario = texNome.get()
    texSenha = texdigiteSenha.get()

    if texUsuario == 't' and texSenha == '2':
        resultadoLogin.config(text = 'login efetuado com suscesso',fg = 'green')
    else:
        resultadoLogin.config(text = 'login falho',fg = 'red')                           



app = tk.Tk()
app.title("Sistema de Login")
app.geometry("300x300")


texUsuario = tk.Label(app,text='usuario')
texUsuario.pack(pady = 10)

texNome = tk.Entry(app)
texNome.pack(pady = 10)

texSenha = tk.Label(app,text='senha')
texSenha.pack(pady = 10)

texdigiteSenha = tk.Entry(app)
texdigiteSenha.pack(pady = 10)

butaoLogin = tk.Button(app,text="login",command=validarSenha)
butaoLogin.pack(pady = 10)

resultadoLogin = tk.Label(app,text='')
resultadoLogin.pack(pady = 10)
app.mainloop()

