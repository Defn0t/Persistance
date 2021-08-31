import datetime
from bs4 import BeautifulSoup
import requests
from requirements import NewsLine, refresh, duplicate_check


url = "https://www.livemint.com/latest-news"
displayed_feed = []
main_html_text = requests.get(url).text

# Server refresh bug
# Headlines/ articles are likely to be updated one they are posted
# Possible modification of headlines


def extract(html_text):
    temp = []
    soup = BeautifulSoup(html_text, "lxml")
    cards = soup.findAll("div", class_="listingNew clearfix impression-candidate")
    for card in cards:
        source = "LiveMint"
        card_id = card.attrs["id"]
        head_line = card.find("h2").find("a").text
        head_line = head_line[11: len(head_line) - 9]
        date = card.find("span", {"data-updatedtime": True}).attrs["data-updatedtime"]
        date = datetime.datetime.strptime(date, "%Y-%m-%dT%H:%M:%S")
        news = NewsLine(card_id, date, source, head_line)
        temp.append(news)
    temp.sort(key=lambda x: x.time_stamp)
    return temp


def mint_feed():

    global main_html_text
    global displayed_feed
    main_html_text = refresh(url, main_html_text)
    live_feed = extract(main_html_text)
    update_feed = duplicate_check(live_feed, displayed_feed)
    displayed_feed += live_feed
    return update_feed





