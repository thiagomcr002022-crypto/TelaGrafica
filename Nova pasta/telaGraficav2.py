def login():
    usuario = entrada_usuario.get()
    senha = entrada_senha.get()
    if usuario == 'admin' and senha == '123':
        resultado['text'] = 'login efetuado com suscesso'
        resultado['fg'] = 'green'
    else:
        resultado['text'] = 'login falho'
        resultado['fg'] = 'red'
janela = tk.Tk()
janela.title('tela de login')
janela.geometry('300x200')
janela.configure(bg ='#34495E')

tk.Label(janela,text="usuario",fg='white',bg='#34495E').grid(row=0,column=0,padx=10)

entrada_usuario = tk.Entry(janela)
entrada_usuario.grid(row=0,column=1,padx=10,pady=10)

tk.Label(janela,text="senha",fg='white',bg='#34495E').grid(row=1,column=0,padx=10)

entrada_senha = tk.Entry(janela,show='*')
entrada_senha.grid(row=1,column=1,padx=10,pady=10)

tk.Button(janela, text='entrar', command=login ,bg = '#27Ae60',fg='white' ).grid(row=2,column=1,columnspan=10,pady=10)


resultado = tk.Label(janela,text='',bg='#34495E')
resultado.grid(row=3,column=0,columnspan=2)

janela.mainloop()