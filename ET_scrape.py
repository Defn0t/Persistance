import datetime
from bs4 import BeautifulSoup
import requests
from requirements import NewsLine, refresh, duplicate_check

url = "https://economictimes.indiatimes.com/news/latest-news"
displayed_feed = []
main_html_text = requests.get(url).text

# Dynamic webpage, each time the server handles the request
# Different responses may be received depending upon the servers response


def extract(html_text):
    temp = []
    soup = BeautifulSoup(html_text, "lxml")
    lists = soup.find("ul", class_="data").findAll("li")
    for item in lists:
        source = "EcoTimes"
        head_line = item.find("a").text
        card_id = head_line
        date = item.find("span", class_="timestamp").attrs["data-time"]
        date = date[:-4]
        date = datetime.datetime.strptime(date, "%d %b, %Y %I:%M %p")
        news = NewsLine(card_id, date, source, head_line)
        temp.append(news)
    temp.sort(key=lambda x: x.time_stamp)
    return temp


def economic_times_feed():

    global main_html_text
    global displayed_feed
    main_html_text = refresh(url, main_html_text)
    live_feed = extract(main_html_text)
    update_feed = duplicate_check(live_feed, displayed_feed)
    displayed_feed += live_feed
    return update_feed









