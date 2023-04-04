"""Read twitter tweets data """
# import packages
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
import pandas as pd


def print_tweet_data():
    """ read tweets details"""

    chrome_driver = Service(r"C:\Users\Hanumant-PC\Downloads\webdriver.exe")
    driver = webdriver.Chrome(service=chrome_driver)
    driver.maximize_window()
    driver.implicitly_wait(20)

    # read tweets links
    dataframe = pd.read_excel(r"C:\Users\Hanumant-PC\Downloads\twitterTest (Bitgoro).xlsx")

    # store Data
    time_stamp_tweet = []
    influencer = []
    promoter = []
    influencer_tweet = []
    promoter_tweet = []
    influencer_tweet_like = []
    promoter_tweet_like = []
    influencer_tweet_text = []
    promoter_tweet_text = []
    urls = []
    for row in dataframe.itertuples():
        urls.append(row[5])

    # print(urls)
    for link in urls:
        url = link
        driver.get(url)
        print(url)
        driver.implicitly_wait(10)

        # read time_stamp_tweet
        times_stamp = driver.find_element(By.XPATH, "//time").get_attribute('datetime')
        time_stamp_tweet.append(times_stamp)

        # read influencer
        influencers = driver.find_element(By.XPATH, "//div[@data-testid='User-Name']/div/div/a").get_attribute('href')
        influencer.append(influencers)

        # read promoter
        promoters = driver.find_element(By.XPATH,
                                        "//div[@class='css-1dbjc4n r-18u37iz r-1wbh5a2']/div/div/a").get_attribute(
            'href')
        promoter.append(promoters)

        # read influencer_tweet
        influencer_tweets = driver.find_element(By.XPATH,
                                                "//div[@class='css-1dbjc4n r-18u37iz r-1q142lx']/a").get_attribute(
            'href')
        influencer_tweet.append(influencer_tweets)

        # read promoter_tweet
        promoter_tweets = driver.find_element(By.XPATH,
                                              "//div[@class='css-901oao r-14j79pv r-37j5jr r-a023e6 r-16dba41 r-rjixqe r-bcqeeo r-qvutc0']/a").get_attribute(
            'href')
        promoter_tweet.append(promoter_tweets)

        # read influencer_tweet_like
        influencer_tweet_likes = driver.find_element(By.XPATH, "//div[@data-testid='like']/div/div[2]/span/span").text
        influencer_tweet_like.append(influencer_tweet_likes)

        # read promoter_tweet_like
        promoter_tweet_likes = driver.find_element(By.XPATH,
                                                   "//a[@class='css-4rbku5 css-18t94o4 css-901oao r-18jsvk2 r-1loqt21 r-37j5jr r-a023e6 r-16dba41 r-rjixqe r-bcqeeo r-qvutc0']/div/span/span/span").text
        promoter_tweet_like.append(promoter_tweet_likes)

        # read influencer_tweet_text
        influencer_tweet_texts = driver.find_element(By.XPATH, "//div[@data-testid='tweetText']").text.strip()
        influencer_tweet_text.append(influencer_tweet_texts)

        # read promoter_tweet_text
        promoter_tweet_texts = driver.find_element(By.XPATH, "//div[@class='css-1dbjc4n']/div[3]").text.strip()
        promoter_tweet_text.append(promoter_tweet_texts)
        # create dictionary

    data_dict = {"time_stamp_tweet": time_stamp_tweet, "influencer": influencer, "promoter": promoter,
                 "influencer_tweet": influencer_tweet, "promoter_tweet": promoter_tweet,
                 "influencer_tweet_like": influencer_tweet_like, "promoter_tweet_like": promoter_tweet_like,
                 "influencer_tweet_text": influencer_tweet_text, "promoter_tweet_text": promoter_tweet_text}

    # create dataframe
    dataframe = pd.DataFrame.from_dict(data_dict, orient='index')
    dataframe = dataframe.transpose()
    print(dataframe)
    dataframe.to_csv('twitter_data.csv', index=False)

    driver.close()


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_tweet_data()
