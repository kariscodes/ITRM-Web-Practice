# import os
from selenium import webdriver
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# from selenium.webdriver.common.by import By
# from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
import requests
# import pandas as pd

CHROME_PATH = "C:\Program Files (x86)\chromedriver.exe"
try:
    # ff_driver = webdriver.Firefox()
    ff_driver = webdriver.Chrome(CHROME_PATH)
except Exception as e:
    print(e)

SITE_URL = "https://news.google.com/"
ff_driver.get(SITE_URL)
# ff_driver.get("https://www.google.co.kr/")

input_keyword = "대성에너지"
# Input search word
xPathCode = '//*[@id="gb"]/div[2]/div[2]/div/form/div[1]/div/div/div/div/div[1]/input[2]'
ff_driver.find_element_by_xpath(xPathCode).send_keys(input_keyword)
# query = ff_driver.find_element_by_id("lst-ib").send_keys("macbook pro")
# que.send_keys(keyword_str)

# Click search button
# que.send_keys(Keys.RETURN)
xPathCode = '//*[@id="gb"]/div[2]/div[2]/div/form/button[4]'
ff_driver.find_element_by_xpath(xPathCode).click()
# que.send_keys(Keys.ENTER)
# que.send_keys(Keys.RETURN)
# que.submit()
# que.find_element_by_class_name("gb_pf")
# que.click()
# selector = '#gb > div.gb_Pd.gb_8d.gb_Zd > div.gb_Tc.gb_2d.gb_Ke.gb_Ne > div > form > button.gb_pf'
# que.find_element_by_css_selector(selector)
# que.find_element_by_name("button").click()
# ff_driver.find_element_by_name("btnK").click()

# Wait some time...
ff_driver.implicitly_wait(3)
# WebDriverWait(ff_driver, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "h3.r")))
# WebDriverWait(ff_driver, 10)


# print(ff_driver.title)
# print(ff_driver.page_source)
# print(ff_driver.page_source)
# page_results = ff_driver.find_elements(By.CSS_SELECTOR, "h3")
# page_results = ff_driver.find_elements(By.CSS_SELECTOR, "h3")
# page_results = ff_driver.find_elements_by_tag_name("a.href")
# page_results = ff_driver.find_elements_by_tag_name("h3")
# print(page_results)
# page_results = ff_driver.find_elements(By.CSS_SELECTOR, "a.href")
# for item in page_results:
#     print(item.text)
# source = ff_driver.page_source

# Getting the url of the result page
url = ff_driver.current_url
resp = requests.get(url)
soup = BeautifulSoup(resp.text,'html.parser')

# Getting titles and links of the result lists.
titles = []
links = []
for link in soup.select('h3 > a'):
    title = link.string
    href = 'https://news.google.com' + link.get('href')[1:]
    titles.append(title)
    links.append(href)

# Print a series of lists together
for t, l in zip(titles, links):
    print('\n', t, '\n', l)

# Make a file to save the results
# result_data = {'title': titles, 'link': links}
# data_frame = pd.DataFrame(result_data, columns=['title', 'link'])
# data_frame.to_excel('./' + input_keyword + '.xlsx')
# print("Complete!")
# print(soup)
# res_1 = soup.find_all('div', {'class' : 'r'})
# print(res_1)
# res_1 = soup.find_all('h3')
# res_2 = soup.select('span > li > a')
# res_2 = soup.find_all('a', {'class': 'fi'})
# res_2 = soup.find_all('a', {'class':'fl'})
# print(len(res_1), len(res_2))
# for t1 in res_1:
#
#     print(t1.get_text())
# for t2 in res_2:
#     print(t2.get_text())

# entire = bs.find_all('h3')
# print(entire)

# Quit the browser
ff_driver.quit()