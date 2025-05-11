from abc import ABC, abstractmethod
import requests

class API(ABC):

    @abstractmethod
    def _connect_api(self):
        pass

    @abstractmethod
    def get_vacancies(self, keyword, page):
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


    def get_vacancies(self, keyword, page):

        self.__params['text'] = keyword
        self.__params['per_page'] = page
        response = self._connect_api()
        vacancies = response.json()['items']

        dict_vacancy = []

        for vacancy in vacancies:

            if vacancy['id'] not in dict_vacancy:

                if vacancy['salary'] and vacancy['salary']['from'] is not None and vacancy['salary']['to'] is not None:

                    average_salary = round((vacancy['salary']['from'] + vacancy['salary']['to']) / 2)

                    dict_vacancy.append(
                    {
                        'id': int(vacancy['id']),
                        'name': vacancy['name'],
                        'salary': average_salary,
                        'requirement': vacancy['snippet']['requirement'],
                        'url': vacancy['alternate_url']
                    }
                )

                elif vacancy['salary'] and vacancy['salary']['from'] is None:
                    dict_vacancy.append(
                    {
                        'id': int(vacancy['id']),
                        'name': vacancy['name'],
                        'salary': vacancy['salary']['to'],
                        'requirement': vacancy['snippet']['requirement'],
                        'url': vacancy['alternate_url']
                    }
                )

                elif vacancy['salary'] and vacancy['salary']['to'] is None:
                    dict_vacancy.append(
                    {
                        'id': int(vacancy['id']),
                        'name': vacancy['name'],
                        'salary': vacancy['salary']['from'],
                        'requirement': vacancy['snippet']['requirement'],
                        'url': vacancy['alternate_url']
                    }
                )

        return dict_vacancy

if __name__ == '__main__':
    imp1 = HeadHunterAPI()
    print(imp1.get_vacancies('Водитель', 1))