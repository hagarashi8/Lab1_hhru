from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromiumService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.core.utils import ChromeType
import pandas as pd

driver = webdriver.Chrome(service=ChromiumService(ChromeDriverManager(chrome_type=ChromeType.CHROMIUM).install()))

driver.get("https://omsk.hh.ru/search/vacancy?text=Python&area=68")

jobs = driver.find_elements(By.CSS_SELECTOR, "#a11y-main-content > div > div > div.vacancy-serp-item-body > div.vacancy-serp-item-body__main-info")
dataframed = [{"Name": job.find_element(By.CLASS_NAME, "serp-item__title").text, "Company": job.find_element(By.CLASS_NAME, "bloko-text").text} for job in jobs]
df = pd.DataFrame.from_records(dataframed)
df.to_excel("jobs.xlsx")
