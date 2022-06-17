from selenium.webdriver.common.action_chains import ActionChains
from selenium import webdriver
import pyautogui as pa
import pyperclip as pc
import time
from warnings import filterwarnings  # wawningdeprecated


class ConvertToMp3:
    def __init__(self):
        filterwarnings("ignore")
        options = webdriver.ChromeOptions()
        options.add_experimental_option('excludeSwitches', ['enable-logging'])
        # opções para não aparecer as mensagens do driver no prompt
        options.add_argument('--log-level=3')
        self.driver = webdriver.Chrome(chrome_options=options)
        self.driver.implicitly_wait(5)

    def obterLinks(self):
        global listaMusicas
        playlistDesejada = input(
            "Qual a playlist desejada? cole e clique com o botão direito do mouse ")
        self.driver.get(playlistDesejada)
        firstLink = self.driver.current_url
        qtdMsc = input(
            "Qual o numero total de músicas desejadas da playlist? ")
        listaMusicas = [firstLink]

        msc = 1
        while msc < int(qtdMsc):
            skipMsc = self.driver.find_element_by_xpath(
                "//a[@title='Próximo (SHIFT+n)']")
            skipMsc.click()
            link = self.driver.current_url
            pc.copy(link)
            a = pc.paste()
            listaMusicas.append(a)
            msc += 1
            time.sleep(1)

    def downloadSongs(self):
        self.driver.get('https://ytmp3.mobi/pt3/')

        for musica in listaMusicas:
            caixaTexto = self.driver.find_element_by_xpath(
                "//input[@name='video']")
            caixaTexto.click()
            caixaTexto.send_keys(musica)
            time.sleep(1)
            btnConvert = self.driver.find_element_by_xpath(
                "//input[@value='Converter']")
            time.sleep(1)
            btnConvert.click()
            time.sleep(6)
            btnBaixar = self.driver.find_element_by_xpath(
                "//a[@rel='nofollow']")
            time.sleep(1)
            btnBaixar.click()
            time.sleep(3)
            btnRepeat = self.driver.find_element_by_xpath(
                "//a[@href='']")
            btnRepeat.click()


bot = ConvertToMp3()
bot.obterLinks()
bot.downloadSongs()


#bot = ConvertToMp3()
# bot.colarLinks()
# Dados utilizados:
# Youtube Link: https://www.youtube.com/watch?v=xhcSgQXejQY&list=RDxhcSgQXejQY&start_radio=1&rv=xhcSgQXejQY
# conversor: https://video-to-mp3-converter.com/pt
