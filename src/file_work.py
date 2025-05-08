from abc import ABC, abstractmethod
import json
from fileinput import filename
from json import JSONDecodeError


class FileWork(ABC):

    def __init__(self, filename):
        self._filename = filename

    @abstractmethod
    def add_vacancy(self, vacancy):
        pass

    @abstractmethod
    def get_data_from_file(self):
        pass

    @abstractmethod
    def file_cleaning(self):
        pass

    @abstractmethod
    def delete_vacancy(self, vacancies_list):
        pass


class WorkingWithJSON(FileWork):

    data = list

    def __init__(self, filename="vacancies.json"):
        super().__init__(filename)
        self.data = []

    def add_vacancy(self, vacancy):

        self.get_data_from_file()

        self.data.append(vacancy)

        with open(self._filename, 'w', encoding='utf-8') as f:
            json.dump(self.data, f, ensure_ascii=False)

    def get_data_from_file(self):

        try:
            with open(self._filename, 'r', encoding='utf-8') as f:
                self.data = json.load(f)
                return self.data

        except JSONDecodeError:
            self.data = []

        except FileNotFoundError:
            with open(self._filename, 'w', encoding='utf-8'):
                status = 'Файл создан'

    def file_cleaning(self):

        with open(self._filename, 'w', encoding='utf-8') as f:
            del f

    def delete_vacancy(self, vacancies_list):

        data = self.get_data_from_file()

        clean_data = []

        with open(self._filename, 'w', encoding='utf-8') as f:

            self.file_cleaning()

            for vacancy in data:
                if vacancy == vacancies_list:
                    clean_data.append(vacancy)

            if clean_data:
                self.add_vacancy(clean_data)
