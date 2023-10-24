from PySimpleGUI import PySimpleGUI as sg

#Layout

sg.theme('DarkPurple6')
layout = [
    [sg.Text('Usuario'), sg.Input(key='usuario', size=(20,1))],
    [sg.Text('Senha'), sg.Input(key='senha', password_char='*', size=(21,1))],
    [sg.Checkbox('Salvar o Login?')],
    [sg.Button('Entrar')]
]

#Janela
janela = sg.Window('Login com Python', layout)

#Ler os Eventos
while True:
    eventos, valores = janela.read()
    if eventos == sg.WINDOW_CLOSED:
        break
    if eventos == 'Entrar':
        if valores ['usuario'] == 'maoly' and valores ['senha'] == '123456':
            print('Bem-vindo a Interface Grafica com Python da Maoly!')
