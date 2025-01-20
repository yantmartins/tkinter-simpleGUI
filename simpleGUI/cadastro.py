import PySimpleGUI as sg

event, values = sg.Window("Cadastro", 
                          [
                              [sg.T("Cadastro")],
                              [sg.T("Nome"), sg.In(key='nome')],
                              [sg.T("Senha"), sg.In(key='senha', password_char='*')],
                              [sg.B("Cadastrar"), sg.B("Cancelar")]
                          ]
                          ).read(close=True)

nome = values['nome']
senha = values['senha']

if len(nome) > 1 and len(senha) > 1:
    sg.popup('Cadastrado com sucesso!')
    
    event2, values2 = sg.Window("Login", 
                          [
                              [sg.T("Login")],
                              [sg.T("Nome"), sg.In(key='nome2')],
                              [sg.T("Senha"), sg.In(key='senha2')],
                              [sg.B("Logar"), sg.B("Cancelar")]
                          ]
                          ).read(close=True)
    
    if values2['nome2'] == nome and values2['senha2'] == senha:
        sg.popup("Logado")
    else:
        sg.popup("Login Inválido")
else:
    sg.popup("Cadastro Inválido")
