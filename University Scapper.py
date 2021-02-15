import html5lib
import pandas
import re
import urllib
from bs4 import BeautifulSoup
from selenium import webdriver



# application link


university = input("Enter University Name: ")
query = urllib.parse.urlencode(
    {"q": "{} international graduate apply".format(university)}
)

driver = webdriver.Chrome(r'C:\Users\Lenovo\PycharmProjects\scraper\chromedriver.exe')


driver.get(r"https://www.google.com/search?{}".format(query))
res = driver.execute_script("return document.documentElement.outerHTML")
soup = BeautifulSoup(res, "html5lib")

apply_l = soup.find(string=re.compile(r"Apply|Admission|Application")).find_parent("a")



apply_link = apply_l["href"]
print("Application Link: ")
print(apply_link)

driver.close()

# university tpe

query_for_type = urllib.parse.urlencode(
    {"search": "{}".format(university)}
)
driver = webdriver.Chrome(
    r"C:\Users\Lenovo\.spyder-py3\chromedriver.exe"
)
driver.get(r"https://en.wikipedia.org/wiki/Special:Search?{}".format(query_for_type))
res = driver.execute_script("return document.documentElement.outerHTML")
soup = BeautifulSoup(res, "html5lib")
univ_type = soup.find(string=re.compile(r"(public|private)", re.IGNORECASE))
print("University type : ")
print(univ_type)
driver.close()


#  funding url


query_for_fund = urllib.parse.urlencode(
    {"q": "{} graduate studies funding".format(university)}
)


driver = webdriver.Chrome(r'C:\Users\Lenovo\PycharmProjects\scraper\chromedriver.exe')


driver.get(r"https://www.google.com/search?{}".format(query_for_fund))
res = driver.execute_script("return document.documentElement.outerHTML")


soup = BeautifulSoup(res, "html5lib")
funding_l = soup.find(
    string=re.compile(r"Funding|Funding Opportunities|Assistanceship]")
).find_parent("a")
funding_link = funding_l["href"]
print("Funding URl:")
print(funding_link)

driver.close()



# setting of university


query = urllib.parse.urlencode({"search":"{}".format(university)})
driver = webdriver.Chrome(r'C:\Users\Lenovo\PycharmProjects\scraper\chromedriver.exe')
driver.get(r"https://en.wikipedia.org/wiki/special:search?{}".format(query))
res = driver.execute_script("return document.documentElement.outerHTML")
soup = BeautifulSoup(res,"html5lib")


uni_setting = soup.find(string=re.compile(r"(urban|rural)", re.IGNORECASE))
print("University Setting : ")
print(uni_setting)
driver.close()

#establishment of university

query_for_date = urllib.parse.urlencode({"search":"{}".format(university)})
driver = webdriver.Chrome(r'C:\Users\Lenovo\PycharmProjects\scraper\chromedriver.exe')
driver.get(r"https://en.wikipedia.org/wiki/special:search?{}".format(query_for_date))
res = driver.execute_script("return document.documentElement.outerHTML")
soup = BeautifulSoup(res,"html5lib")

established = soup.find('th',string='Established').find_next_sibling('td').text
print("University established on : ")
print(established)
driver.close()
