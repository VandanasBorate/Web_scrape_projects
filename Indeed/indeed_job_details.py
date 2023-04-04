"""Read indeed jobs data """

# import packages
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
import pandas as pd


def print_indeed_data():
    """ read indeed jobs details"""

    chrome_driver = Service(r"C:\Users\Hanumant-PC\Downloads\webdriver.exe")
    driver = webdriver.Chrome(service=chrome_driver)
    driver.maximize_window()
    driver.implicitly_wait(10)

    # read indeed urls one by one display data
    dataframe = pd.read_csv(r"C:\Users\Hanumant-PC\PycharmProjects\Indeed\Common\links_names.csv")
    for row in dataframe.itertuples():
        print(row[1])
        driver.get(row[1])

        # store Data
        job_title = []
        company_name = []
        job_location = []
        salary_range = []
        posted = []
        description = []
        ratings = []
        driver.implicitly_wait(10)

       # read job title
        for title in driver.find_elements(By.XPATH, "//a[@class='jcs-JobTitle css-jspxzf eu4oa1w0']"):
            job_title.append(title.text)

        # read company name
        for company_names in driver.find_elements(By.XPATH, "//span[@class='companyName']/a"):
            company_name.append(company_names.text)

        # read location
        for locations in driver.find_elements(By.XPATH, "//div[@class='companyLocation']"):
            job_location.append(locations.text.strip())

        # read salary_range
        for salary_ranges in driver.find_elements(By.XPATH, "//div[@class='metadata salary-snippet-container']/div"):
            salary_range.append(salary_ranges.text.strip().replace('a year', ''))

        # read posted
        for job_posted in driver.find_elements(By.XPATH, "//span[@class='date']"):
            posted.append(job_posted.text.strip().replace('Posted', ''))

        # read Description
        for descriptions in driver.find_elements(By.XPATH, "//div[@class='job-snippet']/ul"):
            description.append(descriptions.text.strip())

        # read Ratings
        for rating in driver.find_elements(By.XPATH, "//span[@class='ratingNumber']/span"):
            ratings.append(rating.text)

        # create dictionary
        data_dict = {"job_title": job_title, "company_name": company_name, "job_location": job_location,
                     "salary_range": salary_range, "job_posted": posted,
                     "description": description, "Ratings": ratings}

        # create dataframe
        dataframe = pd.DataFrame.from_dict(data_dict, orient='index').fillna(0)
        dataframe = dataframe.transpose()
        print(dataframe)
        driver.implicitly_wait(10)

        dataframe.to_csv('indeed_job_data.csv', index=False, mode='a', header=False)


    driver.close()


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_indeed_data()
