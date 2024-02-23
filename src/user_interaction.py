from src.debug_user_json import DebugUserJson
from src.hh_debug import HH_debug
from src.sort_vacancies import SortVacancies
from src.connect_HH import connect_HH


class UserInteractionHH(HH_debug):
    def hh_user_search(self):
        search_query = self.user_input_str()
        top_n = self.user_input_int()
        result_search = connect_HH(search_query, top_n)
        result_search.get_json()


class UserInteractionJson(DebugUserJson):
    def json_user_search(self):
        vacancies_list = []
        json_file = SortVacancies()
        json_vacancies = json_file.sort_vacancies_hh
        payment = self.payment = self.user_input_int()
        city = self.user_input_str()
        for vacancies in json_vacancies:
            if payment > vacancies["payment_from"]:
                continue
            if city == vacancies["city"]:
                vacancies_list.append(vacancies)
            if city == "":
                vacancies_list.append(vacancies)
        for result in vacancies_list:
            print(f"Город: {result['city']}\nДата публикации: {result['data']}\n"
                  f"Должность: {result['name']}\nРаботодатель: {result['employer']}\n"
                  f"Занятость: {result['schedule']}\nЗарплата от {result['payment_from']}\n"
                  f"Зарплата до: {result['payment_to']}\n")
        if len(vacancies_list) == 0:
            print(f'Результатов 0')


if __name__ == '__main__':
    r = UserInteractionJson()
    r.json_user_search()
