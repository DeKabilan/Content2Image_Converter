from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time

def content2key(content:str):
    options = Options()
    options.headless = True
    keywords=[]
    driver = webdriver.Chrome(options=options)
    driver.get("https://monkeylearn.com/keyword-extractor-online/")
    search_bar = driver.find_element(By.XPATH, "//textarea")
    search_bar.clear()
    search_bar.send_keys(content)
    submit = driver.find_element(By.XPATH, "//button[contains(@type, 'button')]")
    submit.click()
    time.sleep(3)
    tags = driver.find_elements(By.XPATH, "//span[contains(@class, 'EmbedModel-module--green--aXVCp')]")
    for results in tags:
        keywords.append(results.text)
    driver.close()
    return keywords 
    
print(content2key("Python is the Best Language"))
