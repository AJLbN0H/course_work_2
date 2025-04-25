from abc import ABC, abstractmethod
import requests

class API(ABC):

    @abstractmethod
    def _connect_api(self):
        pass

    @abstractmethod
    def get_vacancies(self, keyword):
        pass

class HeadHunterAPI(API):

    def __init__(self):
        self.__url = 'https://api.hh.ru/vacancies'
        self.__headers = {'User-Agent': 'HH-User-Agent'}
        self.__params = {'text': '', 'per_page': 100}

    def _connect_api(self):

        response = requests.get(self.__url, headers=self.__headers, params=self.__params)
        status = response.status_code

        if status == 200:
            return response
        else:
            return 'Возникла ошибка с подключением к API hh.ru'


    def get_vacancies(self, keyword):

        self.__params['text'] = keyword
        vacancies = self._connect_api().json()['items']

        return vacancies

class Vacancy:

    def __init__(self, name, salary, requirement, link_to_vacancy):
        self.name = name
        if salary == 0:
            self.salary = "Зарплата не указана"
        else:
            self.salary = salary
        self. requirement = requirement
        self.link_to_vacancy = link_to_vacancy

    def salary_comparison(self):
        pass



if __name__ == '__main__':
    imp1 = HeadHunterAPI()
    print(imp1.get_vacancies('Водитель'))
