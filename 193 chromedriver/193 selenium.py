# type: ignore
# Selenium - Automatizando tarefas no navegador

from pathlib import Path
from time import sleep

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

# Chrome Options
# https://peter.sh/experiments/chromium-command-line-switches/
# Doc Selenium
# https://selenium-python.readthedocs.io/locating-elements.html


def make_chrome_browser(*options: str) -> webdriver.Firefox:
    chrome_options = webdriver.FirefoxOptions()
    # chrome_options.add_argument('--headless') 
    if options is not None:
        for option in options:
            chrome_options.add_argument(option) 

    chrome_service = Service()

    browser = webdriver.Firefox(
        options=chrome_options,
        service=chrome_service,
        )
    return browser



if __name__ == '__main__':
    # TIME_TO_WAIT = 10

    # Example
    # options = '--headless', '--disable-gpu',
    # --headless: Executa o código sem abrir o navegador na tela
    options = ()
    browser = make_chrome_browser(*options)

    # Acessar o navegador neste endereço
    browser.get('https://www.google.com')
    
    # Espere para encontrar o input

    # search_input = WebDriverWait(browser, TIME_TO_WAIT).until(
    #     EC.presence_of_all_elements_located(
    #         (By.NAME, 'q')
    #     )
    # )
    search_input = browser.find_element(By.NAME, 'q') # Encontre a identificação 'q' em NAME no HTML

    # search_input.click
    # search_input2 = ActionChains(search_input)

    search_input.send_keys('Hello World!') # Envie 
    search_input.send_keys(Keys.ENTER) # Entrar
    sleep(2)
    results = browser.find_element(By.ID, 'rso') # Encontrar o elemento ID rso
    sleep(2)
    links = results.find_elements(By.TAG_NAME, 'a') # Encontre a TAG a
    links[0].click() # clique no primeiro link da lista




    # Dorme por 10 segundos
    # sleep(TIME_TO_WAIT)