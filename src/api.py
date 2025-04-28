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
        self.__params = {'text': '', 'per_page': 100}

    def _connect_api(self):

        response = requests.get(self.__url, params=self.__params)
        status = response.status_code

        if status == 200:
            return response
        else:
            return 'Возникла ошибка с подключением к API hh.ru'


    def get_vacancies(self, keyword):

        self.__params['text'] = keyword
        response = self._connect_api()
        vacancies = response.json()['items']
        return vacancies

if __name__ == '__main__':
    imp1 = HeadHunterAPI()
    print(imp1.get_vacancies('Водитель'))
