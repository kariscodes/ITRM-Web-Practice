from urllib.request import urlopen
from bs4 import BeautifulSoup

page = urlopen("http://stackoverflow.com/questions/tagged/python")
document = page.read()
page.close()

try:
    # soup = BeautifulSoup(document, 'html5lib')
    soup = BeautifulSoup(document, 'html.parser')
except Exception as e:
    print(e)
except BaseException as be:
    print(e)

questions = soup.find(id="questions")
questions_list = questions.find_all("a", class_="question-hyperlink")

for question in questions_list:
    print(question.get_text())
    print('http://stackoverflow.com' + question.get('href'))