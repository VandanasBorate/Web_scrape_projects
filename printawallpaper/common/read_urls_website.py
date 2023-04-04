""" read printawallpaper urls """

# import libraries
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
import pandas as pd


def links(url):
    """ read urls from using any website name"""
    chrome_driver = Service(r'C:\Users\Hanumant-PC\Downloads\chromedriver.exe')
    driver = webdriver.Chrome(service=chrome_driver)
    driver.maximize_window()
    driver.get(url)
    website_links = []
    # read links
    for link_name in driver.find_elements(By.XPATH, "//a"):
        website_links.append(link_name.get_attribute('href'))

    # create dataframe
    dataframe = pd.DataFrame({"Links": website_links})

    # create csv file
    dataframe.to_csv("links_names.csv",index=False)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    links("https://printawallpaper.com/")
