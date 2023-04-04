""" read builtinnyc urls """

# import libraries
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
import pandas as pd
from time import sleep


def links(url):
    """ read urls from using any website name"""

    # options = webdriver.ChromeOptions()
    # options.add_argument('--headless')
    # options.add_argument("start-maximized")
    # options.add_argument(
    #     '--user-agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36"')

    chrome_driver = Service(r'C:\Users\Hanumant-PC\Downloads\chromedriver.exe')
    driver = webdriver.Chrome(service=chrome_driver)
    driver.maximize_window()
    driver.implicitly_wait(10)
    driver.get(url)
    website_links = []
    # read links
    for link_name in driver.find_elements(By.XPATH, "//a"):
        website_links.append(link_name.get_attribute('href'))

    # create dataframe
    dataframe = pd.DataFrame({"Links": website_links})
    print(dataframe)

    # create csv file
    dataframe.to_csv("comany_links_names.csv", index=False)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    links("https://www.indeed.com/q-Product-Management-l-New-York,-NY-jobs.html?vjk=25325a8060331f5c")
