from abc import ABC, abstractmethod


class VacanciesAPI(ABC):
    @abstractmethod
    def get_vacancies(self):
        pass
