""" read printawallpaper  product details using Common-> Links_name.csv files"""
import csv

# import libraries
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
import pandas as pd


def printawallpaper_detail():
    """ read urls from using any website name"""

    chrome_driver = Service(r'C:\Users\Hanumant-PC\Downloads\chromedriver.exe')
    driver = webdriver.Chrome(service=chrome_driver)
    driver.maximize_window()

    # read csv files urls
    data = pd.read_csv(r"C:\Users\Hanumant-PC\PycharmProjects\printawallpaper\common\links_names.csv")
    for url in data.itertuples():

        product_names = []
        product_urls = []
        prices = []
        tags = []
        category = []
        product_images = []
        product_description = []
        product_sku = []
        print(url[1])
        driver.get(url[1])
        # read product name
        for product_name in driver.find_elements(By.XPATH,
                                                 "//p[@class='name product-title woocommerce-loop-product__title']/a"):
            product_names.append(product_name.text)

        while '' in product_names:
            product_names.remove('')

            # read product urls
        for product_url in driver.find_elements(By.XPATH, "//div[@class='image-none']/a"):
            product_urls.append(product_url.get_attribute('href'))
        while '' in product_urls:
            product_urls.remove('')

        # read product price
        for product_price in driver.find_elements(By.XPATH, "//span[@class='woocommerce-Price-amount amount']/bdi"):
            prices.append(product_price.text.replace("' '", '').replace('₹', ''))
        while '' in prices:
            prices.remove('')

        # read product tags
        for product_tag in driver.find_elements(By.XPATH, "//span[@class='tagged_as']/a"):
            tags.append(product_tag.text.strip())
        while '' in tags:
            tags.remove('')

        # read product category
        for product_category in driver.find_elements(By.XPATH,
                                                     "//p[@class='category uppercase is-smaller no-text-overflow product-cat op-7']"):
            category.append(product_category.text.strip())
        while '' in category:
            category.remove('')

        # read product images
        for product_image in driver.find_elements(By.XPATH,
                                                  "//img[@class='attachment-woocommerce_thumbnail size-woocommerce_thumbnail lazyloaded']"):
            product_images.append(product_image.text.strip())
        while '' in product_images:
            product_images.remove('')

        # read product descriptions
        for product_descriptions in driver.find_elements(By.XPATH,
                                                         "//div[@class='product-short-description']/p"):
            product_description.append(product_descriptions.text.strip())
        while '' in product_description:
            product_description.remove('')
        # read product sku
        for products_sku in driver.find_elements(By.XPATH, "//span[@class='sku']/a"):
            product_sku.append(products_sku.text.strip())
        while '' in product_sku:
            product_sku.remove('')

        # create dataframe
        data_dict = {"Product_name": product_names, "Product_url": product_urls, "Price": prices, "Category": category,
                     "Product_image": product_images, "Product_description": product_description,
                     "Products_sku": product_sku, "Tags": tags}
        dataframe = pd.DataFrame.from_dict(data_dict, orient='index')
        dataframe = dataframe.transpose()

        # create csv file
        dataframe.to_csv("printawallpaper_details.csv", index=False, mode='a',header=False)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    printawallpaper_detail()
