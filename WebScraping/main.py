import k_msword
import k_console
from selenium import webdriver

CHROME_PATH = "C:\Program Files (x86)\chromedriver.exe"
try:
    web_driver = webdriver.Chrome(CHROME_PATH)
except Exception as e:
    print(e)

keywords = ['대성에너지', '대성그룹', '대성홀딩스']   # Test
# RETURN_TYPE = '__CONSOLE__'
# RETURN_TYPE = '__MSWORD_EACH__'
RETURN_TYPE = '__MSWORD_ALL__'
# RETURN_TYPE = '__WEBPAGE__'

if RETURN_TYPE == '__CONSOLE__':
    k_console.do_write(web_driver, keywords)

if RETURN_TYPE == '__MSWORD_EACH__':
    k_msword.do_write_each(web_driver, keywords)

if RETURN_TYPE == '__MSWORD_ALL__':
    k_msword.do_write_all(web_driver, keywords)

# Quit the browser
web_driver.quit()