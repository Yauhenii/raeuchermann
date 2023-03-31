from selenium import webdriver
from selenium.webdriver.common.by import By
from typing import Dict


class PDPParser:
    @staticmethod
    def get_product_info(url: str) -> (str, Dict[str, str]):
        options = webdriver.ChromeOptions()
        options.add_argument("headless")
        driver = webdriver.Chrome('./driver/chromedriver_mac64/chromedriver', chrome_options=options)
        driver.get(url)
        try:
            element = driver.find_element(By.CLASS_NAME, "c24-cookie-consent-functional")
            element.click()
        except:
            print('No cookies to accept')
        # get title
        title_element = driver.find_element(By.CLASS_NAME, "product-info__content").find_element(By.XPATH, 'h1')
        title_text = title_element.text
        # get attributes
        attribute_list = driver.find_element(By.CLASS_NAME, "product-details-short").text.split('\n')[:-1]
        attribute_dict = dict(zip(attribute_list[::2], attribute_list[1::2]))
        return title_text, attribute_dict
