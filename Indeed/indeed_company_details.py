"""Read indeed company details """

# import packages
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
import pandas as pd


def print_indeed_company_data():
    """ read indeed company details"""

    chrome_driver = Service(r"C:\Users\Hanumant-PC\Downloads\webdriver.exe")
    driver = webdriver.Chrome(service=chrome_driver)
    driver.maximize_window()
    driver.implicitly_wait(10)

    # read urls
    url = "https://www.indeed.com/companies/search?q=product+management"
    driver.get(url)

    # store Data
    job_title = []
    company_name = []
    image_url = []
    description = []
    review = []
    rating = []

    # read job title
    for title in driver.find_elements(By.XPATH, "//div[@class='css-kbqft4 e1wnkr790']"):
        job_title.append(title.text)

    # read company name
    for company_names in driver.find_elements(By.XPATH, "//div[@class='css-7lboi8 e1wnkr790']"):
        company_name.append(company_names.text)

    # read company image url
    for image_urls in driver.find_elements(By.XPATH, "//img[@class='css-1strlbe eu4oa1w0']"):
        image_url.append(image_urls.get_attribute('src'))

    # read review
    for reviews in driver.find_elements(By.XPATH, "//span[@class='css-8yvs57 e1wnkr790']"):
        review.append(reviews.text.strip())

    # read ratings
    for ratings in driver.find_elements(By.XPATH, "//span[@class='css-lws6k3 e1wnkr790']"):
        rating.append(ratings.text)

    # read Description
    for descriptions in driver.find_elements(By.XPATH, "//p[@class='css-h215jb e1wnkr790']"):
        description.append(descriptions.text)

    # create dictionary
    data_dict = {"job_title": job_title, "company_name": company_name, "job_image_urls": image_url,
                 "reviews": review, "ratings": rating,
                 "description": description}

    # create dataframe
    dataframe = pd.DataFrame.from_dict(data_dict, orient='index').fillna(0)
    dataframe = dataframe.transpose()
    print(dataframe)
    driver.implicitly_wait(10)

    dataframe.to_csv('company_indeed_data.csv', index=False, mode='a')

    driver.close()

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_indeed_company_data()
