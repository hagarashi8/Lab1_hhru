import time
from typing import List
from styleframe import StyleFrame
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromiumService
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.core.utils import ChromeType, log
import pandas as pd

def log_decorator(msg:str = "Doing stuff"):
    def resulting_decorator(func):
        def resulting_function(*args, **kwargs):
            start = time.time()
            print(msg)
            res = func(*args, **kwargs)
            print(f"Done in {time.time()-start}s")
            return res
        return resulting_function
    return resulting_decorator

@log_decorator("Getting driver...")
def get_driver() -> WebDriver:
    return webdriver.Chrome(service=ChromiumService(ChromeDriverManager(chrome_type=ChromeType.CHROMIUM).install()))

@log_decorator("Loading page...")
def get_page(driver: WebDriver, url: str) -> None:
    driver.get(url)

@log_decorator("Getting job list...")
def get_job_list(driver:WebDriver) -> List[WebElement]:
    return driver.find_elements(By.CSS_SELECTOR, "#a11y-main-content > div > div > div.vacancy-serp-item-body > div.vacancy-serp-item-body__main-info")

@log_decorator("Saving...")
def df_and_save(jobs: List[WebElement], filename:str)-> None:
    dataframed = [{"Name": job.find_element(By.CLASS_NAME, "serp-item__title").text, "Company": job.find_element(By.CLASS_NAME, "bloko-text").text} for job in jobs]
    df = pd.DataFrame.from_records(dataframed)
    sf = StyleFrame(df)
    writer = StyleFrame.ExcelWriter(filename)
    sf.to_excel(excel_writer=writer, sheet_name="Jobs", best_fit=("Name", "Company"))
    writer.close()


