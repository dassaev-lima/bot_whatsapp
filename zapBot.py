from selenium import webdriver
from time import sleep

class WhatsappBot:

    #definindo construtor da classe
    def __init__(self):
        self.mensagem = ""
        self.grupos = []
        #definindo configurações para usar o webdriver no navegador
        options = webdriver.ChromeOptions()
        options.add_argument("lang=pt-br")
        self.driver = webdriver.Chrome(executable_path=r'.././chromedriver')
    
    def enviar_mensagem(self):
        #Acessando o site
        self.driver.get('https://web.whatsapp.com/')
        sleep(15)

        for cada_grupo in self.grupos:
            #Localizando o grupo dentro da lista
            grupo = self.driver.find_element_by_xpath(f"//span[@title='{cada_grupo}']")
            grupo.click()
            sleep(3)
            #Localizando o campo de envio da mensagem
            chat_box = self.driver.find_element_by_xpath("//div[@class='_3uMse']")
            sleep(2)
            chat_box.click()
            chat_box.send_keys(self.mensagem)
            #Localizando o botao de envio e finalizando o envio
            btn_send = self.driver.find_element_by_xpath("//span[@data-icon='send']")
            sleep(2)
            btn_send.click()
            sleep(5)

            
#Instanciando a classe e invocando o método de enviar a mensagem      
#zap_bot = WhatsappBot()
#zap_bot.enviar_mensagem()