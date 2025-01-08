from pathlib import Path
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from time import sleep
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

ROOT_FOLDER = Path(__file__).parent
# CHROMEDRIVER_EXEC = ROOT_FOLDER / 'drivers' / 'chrome-win64' / 'setup.exe'

chrome_options = webdriver.ChromeOptions()
# chrome_service = Service(executable_path=CHROMEDRIVER_EXEC)
chrome_browser = webdriver.Chrome(
    # service=chrome_service,
    options=chrome_options,
)
# chrome_options.add_argument('--headless')

chrome_browser.get('https://www.google.com/')
# sleep(10)
TIME_TO_WAIT = 10

search_input = WebDriverWait(chrome_browser, TIME_TO_WAIT).until(
    EC.presence_of_all_elements_located(
        (By.NAME, 'q')
    )
)