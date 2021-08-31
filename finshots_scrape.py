from selenium import webdriver
from bs4 import BeautifulSoup
import textwrap
import lxml
import requests
archive_daily = "https://finshots.in/archive/"

titles = []
links = []


def num_of_pages(url):
    html_text = requests.get(url).text
    soup = BeautifulSoup(html_text, 'lxml')
    element = soup.find("span", class_="page-number")
    number = element.text[-2:]
    return int(number)


def make_database(titles , links , base_url):
    for number in range(1, num_of_pages(base_url)):
        url = base_url + "page/" + str(number)
        html_text = requests.get(url).text
        soup = BeautifulSoup(html_text, "lxml")

        divs = soup.findAll("div", class_="post-card-content")
        for div in divs:
            element = div.find('a')
            links.append('https://finshots.in' + element["href"])
            titles.append(element.find('h2').text)


def article_print(url):
    html_text = requests.get(url).text
    soup = BeautifulSoup(html_text, "lxml")
    content = soup.findAll('p')
    title = soup.find('h1')
    title = title.text
    print("")
    print(title)
    print("")
    line =''
    for para in content[:len(content)-4]:
        line += para.text + " "
    print(textwrap.fill(line))


article_print("https://finshots.in/archive/explainer-on-ransomwares/")




