# div#word-img>
from dotenv import load_dotenv
import os
import time

from selenium import webdriver
from selenium.webdriver.common.by import By

load_dotenv()

driver = webdriver.Chrome()


def typing_test():
    driver.get("https://10fastfingers.com/typing-test/english")
    driver.find_element(By.ID, "inputfield").click()
    words = driver.find_elements(By.CSS_SELECTOR, "#row1 span")
    for word in words:
        word_text = word.text
        driver.find_element(By.ID, "inputfield").send_keys(word_text + " ")
        time.sleep(0.2)


def login():
    driver.get("https://10fastfingers.com/login")
    driver.find_element(By.ID, "UserEmail").send_keys(os.environ["UserEmail"])
    driver.find_element(By.ID, "UserPassword").send_keys(os.environ["UserPassword"])
    driver.find_element(By.ID, "UserPassword").submit()


if __name__ == "__main__":
    login()
    time.sleep(2)
    typing_test()
    time.sleep(5)
    driver.quit()