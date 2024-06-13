#succesvol inlog check.
from selenium import webdriver
from selenium import *
from selenium.common import *
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

### Github actiom

from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

options = webdriver.ChromeOptions()
options.add_argument('--headless')
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

##### Variabelen####
base_url = "https://demo.playground-crm.com"
username = "admin"
password = "admin"

#### Begin test ####
driver = webdriver.Chrome()
driver.get(base_url)
titel_base = driver.title
assert titel_base == "Playground CRM"
print(titel_base)
driver.find_element(By.ID,"user").send_keys(username)
driver.find_element(By.ID,"password").send_keys(password)
driver.find_element(By.XPATH,"//*[@id='js-main']/div/div/form/center/div[1]/button").click()
#### Controlle na succesvol login ####
controlleer_login = driver.find_element(By.XPATH,"//*[@id='header']/nav/div/ul/li[6]/a").text
print(controlleer_login)
assert controlleer_login == "Ger personal account for free", f"Controlle tekst {controlleer_login} komt NIET overeen met Get personal account for free"


time.sleep(2)

