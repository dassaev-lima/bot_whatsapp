import PySimpleGUI as sg
from zapBot import WhatsappBot

class TelaZapBot:

    sg.theme('Green')
    def __init__(self):
    #layout
        layout = [
            [sg.Text('''Envie mensagem para varios contatos de uma só vez Sem trabalho ou dificuldade,
lembre de escrever o nome dos grupos exatamente como está no aplicativo separando-os por vírgula''',text_color='white')],
            [sg.Text('Grupos ou Contatos:',size=(10,0),text_color='white'),sg.Input(key=('grupos'))],
            [sg.Text('Mensagem:',size=(10,0),text_color='white'),sg.Input(key=('msg'))],
            [sg.Button('Enviar Mensagem')],
            [sg.Output(size=(60,5))]
        ]
    #janela
        self.janela = sg.Window('Bem-vindo à Interface Whatsapp Bot',layout)
    #extraindo dados da tela
    def iniciar(self):
        while True:
            self.button,self.values = self.janela.Read()
            grupos = self.values['grupos']
            msg = self.values['msg']
            
            try:
                zap_bot = WhatsappBot()
                for elem in grupos.split(','):
                    zap_bot.grupos.append(elem)
                print(zap_bot.grupos)
                zap_bot.mensagem = msg
                zap_bot.enviar_mensagem()
                print('Mensagem enviada com Sucesso')
            except BaseException as ex:
                print('falha ao enviar mensagem')

tela_zap_bot = TelaZapBot()
tela_zap_bot.iniciar()