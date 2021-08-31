import datetime
from bs4 import BeautifulSoup
import requests
from requirements import NewsLine, refresh, duplicate_check

url = "https://www.moneycontrol.com/news/news-all/"
displayed_feed = []
main_html_text = requests.get(url).text


def extract(html_text):
    temp = []
    soup = BeautifulSoup(html_text, "lxml")
    lists = soup.find("ul", {"id":"cagetory"}).findAll("li", class_="clearfix")
    for item in lists:
        source = 'MoneyCon'
        head_line = item.find("h2").find("a").text
        card_id = item.attrs["id"]
        date = item.find("span").text
        date = date[:-4]
        date = datetime.datetime.strptime(date, "%B %d, %Y %I:%M %p")
        news = NewsLine(card_id, date, source, head_line)
        temp.append(news)
    temp.sort(key=lambda x: x.time_stamp)
    return temp


def money_control_feed():

    global main_html_text
    global displayed_feed
    main_html_text = refresh(url, main_html_text)
    live_feed = extract(main_html_text)
    update_feed = duplicate_check(live_feed, displayed_feed)
    displayed_feed += live_feed
    return update_feed











