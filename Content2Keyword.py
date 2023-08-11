from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

def content2key(content:str):
    keywords=[]
    driver = webdriver.Chrome()
    driver.get("https://www.cortical.io/freetools/extract-keywords")
    search_bar = driver.find_element(By.ID, 'text-input')
    search_bar.clear()
    search_bar.send_keys(content)
    driver.fullscreen_window()
    time.sleep(5)
    submit = driver.find_element(By.XPATH, "//button[contains(@id, 'submit-text')]")
    submit.click()
    time.sleep(5)
    tags = driver.find_elements(By.XPATH, "//span[contains(@class, 'demo-keyword')]")
    for results in tags:
        keywords.append(results.text)
    driver.close()
    return keywords 
    
print(content2key("Python is the Best Language"))