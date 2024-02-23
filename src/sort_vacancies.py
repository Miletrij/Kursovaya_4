import json
from datetime import datetime
from config import FILE
from pprint import pprint


class SortVacancies:
    def __init__(self):
        self.hh_sort = []
        self.date_format = None

    @property
    def sort_vacancies_hh(self):
        with open(FILE, encoding="utf-8") as file:
            content = json.load(file)
        for i in content["items"]:
            if i["salary"]["from"] is None:
                i["salary"]["from"] = 0
            if i["salary"]["to"] is None:
                i["salary"]["to"] = 0
            if i["published_at"]:
                date = datetime.strptime(i["published_at"], "%Y-%m-%dT%H:%M:%S+%f")
                self.date_format = f"{date:%d.%m.%Y}"
            self.hh_sort.append({
                "name": i["name"],
                "city": i["area"]["name"],
                "payment_from": i["salary"]["from"],
                "payment_to": i["salary"]["to"],
                "employer": i["employer"]["name"],
                "schedule": i["schedule"]["name"],
                "data": self.date_format
            })
        return self.hh_sort


if __name__ == '__main__':
    r = SortVacancies()
    pprint(r.sort_vacancies_hh)

