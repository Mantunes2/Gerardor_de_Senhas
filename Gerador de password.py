import random
import PySimpleGUI as sg
import os


class Gerador_de_password:
    def __init__(self):
        # Layout
        sg.theme('Black')
        layout = [
            [sg.Text('Site/Software',size=(10,1)),
            sg.Input(key='site', size=(10,1))],
            [sg.Text('E-mail/Usuário', size=(10,1)),
            sg.Input(key='usuário', size=(10,1))],
            [sg.Text('Quantidade de caracteres'),sg.Combo(values=list(
                range(30)),key='total_chars', default_value=1, size=(3,1))],
            [sg.Input(size=(32,5))],
            [sg.Button('Gerar senha')]
        ]
        # Declarar janela
        self.janela = sg.Window('Password Generetor', layout)

    def Iniciar(self):
        while True:
            evento, valores = self.janela.read()
            if evento == sg.WINDOW_CLOSED:
                break
            if 'Gerar Senha':
                nova_senha = self.gerar_senha(valores)
                print('nova_senha')
                self.Salvar_senha(nova_senha, valores)
                
    def gerar_senha(self, valores):
        char_list = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz123456789!@#$%¨&*'
        chars = random.choices(char_list, k=int(valores['total_chars']))
        new_pass = ''.join(chars)
        return new_pass

    def Salvar_senha(self, nova_senha, valores):
        with open('senha.txt','a',newline='') as arquivo:
            arquivo.write(
                f"site: {valores[site]}, usuario: {valores[usuario]}, nova senha: {nova_senha}")
        print('Arquivo salvo')

Gen = Gerador_de_password()
Gen.Iniciar()