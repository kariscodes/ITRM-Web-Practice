# import selenium
from bs4 import BeautifulSoup
import requests

class Search:
    def __init__(self):
        pass
    def search_in_goolenews(self, browser_driver, keyword, days):
        # URL of Search site
        SITE_URL = "https://news.google.com/"
        browser_driver.get(SITE_URL)

        # Search word
        keyword = keyword + 'when:' + str(days) + 'd'
        # Input search word
        xPathCode = '//*[@id="gb"]/div[2]/div[2]/div/form/div[1]/div/div/div/div/div[1]/input[2]'
        browser_driver.find_element_by_xpath(xPathCode).send_keys(keyword)

        # Click search button
        xPathCode = '//*[@id="gb"]/div[2]/div[2]/div/form/button[4]'
        browser_driver.find_element_by_xpath(xPathCode).click()

        # Wait some time...
        browser_driver.implicitly_wait(3)

        # Getting the url of the result page
        url = browser_driver.current_url
        resp = requests.get(url)
        soup = BeautifulSoup(resp.text,'html.parser')

        # Getting titles and links of the result lists.
        titles = []
        links = []
        for link in soup.select('h3 > a'):
            title = link.string
            titles.append(title)
            href = 'https://news.google.com' + link.get('href')[1:]
            links.append(href)

        return titles, links

    def search_in_goolenews_with_contents(self, browser_driver, keyword, days):
        # URL of Search site
        SITE_URL = "https://news.google.com/"
        browser_driver.get(SITE_URL)

        # Search word
        keyword = keyword + 'when:' + str(days) + 'd'
        # Input search word
        xPathCode = '//*[@id="gb"]/div[2]/div[2]/div/form/div[1]/div/div/div/div/div[1]/input[2]'
        browser_driver.find_element_by_xpath(xPathCode).send_keys(keyword)

        # Click search button
        xPathCode = '//*[@id="gb"]/div[2]/div[2]/div/form/button[4]'
        browser_driver.find_element_by_xpath(xPathCode).click()

        # Wait some time...
        browser_driver.implicitly_wait(3)

        # Getting the url of the result page
        url = browser_driver.current_url
        resp = requests.get(url)
        soup = BeautifulSoup(resp.text,'html.parser')

        # Getting titles and links of the result lists.
        titles = []
        links = []
        contents = []

        for link in soup.select('h3 > a'):
            title = link.string
            titles.append(title)
            href = 'https://news.google.com' + link.get('href')[1:]
            links.append(href)
            article = requests.get(href)
            # content = article.text
            content = BeautifulSoup(article.text, 'html.parser')
            # No output from below codes... Try another codes.
            # desc = content.find_all("meta", {"name" : "description"})
            desc = content.find_all("content")
            a = ""
            for c in desc:
                a = a + c.get_text()
            contents.append(a)

        return titles, links, contents