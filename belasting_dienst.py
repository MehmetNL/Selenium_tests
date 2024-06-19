import select
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.chrome.options import Options

#### Variabels
url = "https://www.belastingdienst.nl/wps/wcm/connect/nl/toeslagen/content/hulpmiddel-proefberekening-toeslagen"
geboorte_dag = "18"
geboorte_maand = "05"
geboorte_jaar = "1987"
woonplaats ="Nederland"
inkomen = 10000
####### Configuratie

options = Options()
options.add_argument('--headless')
options.add_argument('--no-sandbox')
options.add_argument('--disable-dev-shm-usage')


driver = webdriver.Chrome(options=options)
driver.get(url)
driver.maximize_window()
titel = driver.title
print("Controlle juiste pagina")
assert titel == "Proefberekening toeslagen", f"Test bevindt zich niet op de juiste pagina of titel is gewijzigd. Huidige titel: {titel}"


print("Jaartal 2024 is gekozen")
Select(driver.find_element(By.ID, "V1-1_pbt")).select_by_visible_text("2024")

print("Huurtoeslag is gekozen")
driver.find_element(By.ID, "V1-3_pbt_1").click()

driver.find_element(By.XPATH,"//*[@id='divV2-1_pbt']/div[2]/div[2]/label").click()

print("Geboorte Datum ingevuld")
driver.find_element(By.ID,"V2-3_pbt-1").send_keys(geboorte_dag)
driver.find_element(By.ID,"V2-3_pbt-2").send_keys(geboorte_maand)
driver.find_element(By.ID,"V2-3_pbt-3").send_keys(geboorte_jaar)

print("Woonplaats wordt gekozen")

Select(driver.find_element(By.ID,"V2-11_pbt")).select_by_visible_text(woonplaats)

print("Inkomen wordt ingevuld")

driver.find_element(By.ID,"V3-10_pbt").send_keys(inkomen)

print("Hebt u 1 of meer thuiswonende kinderen? NEE")
driver.find_element(By.XPATH,"//*[@id='divV6-1_pbt']/div/div[2]/label").click()

print("Wonen er nog andere mensen in uw huis?NEE")
driver.find_element(By.XPATH,"//*[@id='divV9-1_pbt']/div/div[2]/label").click()

print("Woont u op kamers?NEE")
driver.find_element(By.XPATH,"//*[@id='divV10-1_pbt']/div[2]/div[2]").click()

print("Woont u in groepswoning voor ouderen of begeleid wonen?NEE")
driver.find_element(By.XPATH,"//*[@id='divV10-2_pbt']/div/div[2]").click()

print("Is uw huurhuis aangepast omdat iemand in huis een handicap heeft?NEE")
driver.find_element(By.XPATH,"//*[@id='divV10-5_pbt']/div[2]/div[2]").click()

print("ingevulde huur is 1000,00 euro")
driver.find_element(By.ID,"V10-10_pbt").send_keys("1000,00")
print("Servicekosten? NEE")
driver.find_element(By.XPATH,"//*[@id='divV10-11_pbt']/div/div[2]/label/span").click()
driver.find_element(By.ID,"butResults_pbt").click()
resultaat = driver.find_element(By.ID,"divE2_pbt").text
assert resultaat == "U kunt geen huurtoeslag krijgen omdat uw kale huur en servicekosten samen hoger zijn dan de huurgrens van € 879,66.",f"Test is niet geslaagd!"
print("Test is succesvol...")

time.sleep(3)
