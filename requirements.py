import requests


class NewsLine:
    def __init__(self, id, time_stamp, publication, head_line):
        self.id = id
        self.time_stamp = time_stamp
        self.publication = publication
        self.head_line = head_line

    def live(self):
        print(f"[{self.time_stamp.strftime('%H:%M')}] [{self.publication}] {self.head_line}")


def refresh(url, main_html_text):
    try:
        update_html_text = requests.get(url).text

    except requests.exceptions.ConnectionError:
        update_html_text = main_html_text

    return update_html_text


def duplicate_check(live, displayed):
    temp = []
    for object_1 in live:
        flag = 0
        for object_2 in displayed:
            if object_1.id == object_2.id:
                flag = 1
            else:
                pass
        if flag == 0:
            temp.append(object_1)
        else:
            pass
    return temp

