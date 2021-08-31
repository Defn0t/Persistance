from mint_scrape import mint_feed
from ET_scrape import economic_times_feed
from MoneyControl_scrape import money_control_feed
from time import sleep


def print_feed(updates):
    for update in updates:
        update.live()


i = 1
while i > 0:
    update_feed = mint_feed() + economic_times_feed() + money_control_feed()
    update_feed.sort(key=lambda x: x.time_stamp)
    print_feed(update_feed)
    sleep(15)
