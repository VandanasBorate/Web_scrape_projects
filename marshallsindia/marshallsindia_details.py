""" Read marshallsindia website product details"""

# import libraries
import requests
from bs4 import BeautifulSoup
import pandas as pd


def data_marshallsindia():
    """ Return marshallsindia website product details """

    urls = "https://www.marshallsindia.com/main/product-page-new.php"
    req = requests.get(urls)
    soup = BeautifulSoup(req.content, 'html.parser')
    design_code = []
    product_urls = []
    prices = []
    sizes = []
    colours = []
    catalogue_names = []
    design_descriptions = []
    country_of_origins = []
    pastings = []
    product_images = []
    product_details = []

    # read product_design_code
    design_codes = soup.findAll("div", class_='prod_code')

    # read product_urls
    products_url = soup.select('div.prod_img > a')
    for product_url in products_url:
        product_urls.append(product_url['href'])

        # read product_images
    products_image = soup.select('.prod_img img')
    for product_img in products_image:
        product_images.append(product_img['src'])

    # read product_details multiple pages using design code
    for i in design_codes:
        url = "https://www.marshallsindia.com/main/product-details-page.php?pid={}".format(i.text)
        # read product design code
        design_code.append(i.text)

        req = requests.get(url)
        soup = BeautifulSoup(req.content, 'html.parser')

        # read product_prices
        for price in soup.findAll("span", class_="money"):
            prices.append(price.text)

        table = soup.find("div", class_="right_table")

        # read product catalogue_name
        for catalogue_name in table.findAll('tr')[1:2]:
            for p_catalogue_name in catalogue_name.findAll('td')[1:2]:
                catalogue_names.append(p_catalogue_name.text)

            # read product catalogue_name
        for size in table.findAll('tr')[2:3]:
            for p_size in size.findAll('td')[1:2]:
                sizes.append(p_size.text)

        # read product design_description
        for design_description in table.findAll('tr')[3:4]:
            for p_design_description in design_description.findAll('td')[1:2]:
                design_descriptions.append(p_design_description.text)

        # read product colour
        for colour in table.findAll('tr')[4:5]:
            for p_colour in colour.findAll('td')[1:2]:
                colours.append(p_colour.text)

        # read product country_of_origin
        for country_of_origin in table.findAll('tr')[5:6]:
            for p_country_of_origin in country_of_origin.findAll('td')[1:2]:
                country_of_origins.append(p_country_of_origin.text)

        # read product pasting
        for pasting in table.findAll('tr')[6:7]:
            for p_pasting in pasting.findAll('td')[1:2]:
                pastings.append(p_pasting.text)

        # read product_detail
        for product_detail in soup.findAll('div', "left_info"):
            product_details.append(product_detail.text.strip().replace('\n', '').replace('        ', ' '))

    # create dataframe
    dataframe = pd.DataFrame(
        {"Design_Codes": design_code, "Product_urls": product_urls, "Price": prices, "Size": sizes, "Colour": colours,
         "Pasting": pastings, "Catalogue_name": catalogue_names, "Design_description": design_descriptions,
         "Product_image": product_images, "Product_detail": product_details})

    # create csv file
    dataframe.to_csv('marshallsindia_details.csv', index=False)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    data_marshallsindia()
