# import packages
import pandas as pd
from bs4 import BeautifulSoup
import requests


class TenderDetails:

    def Tenderscraper(self, url):
        URL = url
        req = requests.get(URL)
        soup = BeautifulSoup(req.content, "html.parser")
        tablehead = []
        tablerow = []
        table = soup.find("table", class_="list_table")
        # print(table)

        # Read table heading

        for TR in table.find_all("tr", class_="list_header")[:1]:
            for th in TR.findAll("td"):
                tablehead.append(th.text)
        # print(tablehead)

        # Read table data

        for TR in table.find_all("tr", class_=["even", "odd"]):
            td = TR.findAll("td")
            tdvalue = [row.text.strip() for row in td]
            tablerow.append(tdvalue)
        # print(tablerow)

        # create dataframe
        df = pd.DataFrame(data=tablerow, columns=tablehead)
        #print(df)

        # convert dataframe to csv file
        #df.to_csv("Tenderdetails.csv", index=False)


# create class object
scraper = TenderDetails()
scraper.Tenderscraper('https://etenders.gov.in/eprocure/app')
