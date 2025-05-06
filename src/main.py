
from src.api import HeadHunterAPI
from src.file_work import WorkingWithJSON
from src.vacancies import Vacancy
from utils import display_of_vacancies

api_vacancies = HeadHunterAPI()
file_work = WorkingWithJSON()

def user_interaction():
    global top_vacancies
    while True:
        action_number = input("\nВыберите номер действия:\n"
                              "1. Поиск вакансий по ключевому слову\n"
                              "2. Поиск вакансий в файле по ID или по ключевому слову\n"
                              "3. Получить топ N вакансий по зарплате\n"
                              "4. Записать вакансию в файл\n"
                              "5. Очистить файл с вакансиями\n"
                              "6. Выход\n"
                              "Выбран вариант: ")

        if action_number == '1':

            status = 0

            search_query = input('\nВведите поисковой запрос: ')

            while True:
                if status != 1:
                    try:
                        top_vacancies = int(input('\nВведите количество вакансий, которое вы хотите получить: '))
                    except ValueError:
                        print('\nВы неверно ввели количество вакансий')

                    else:

                        vacancies = api_vacancies.get_vacancies(search_query, top_vacancies)

                        print(f'\nНайдено {len(vacancies)} вакансий, соответствующих вашему запросу')

                        if vacancies:

                            display_of_vacancies(vacancies)

                        else:
                            print('\nВакансии не найдены')

                        save_option = input('\nСохранить вакансии в файл? Да/Нет\n'
                                'Вы ввели: ')

                        while True:
                            if save_option.lower() == 'да':
                                for vacancy in vacancies:
                                    file_work.add_vacancy(vacancy)

                                print("\nВакансии сохранены в файл 'vacancies.json'")
                                status = 1
                                break

                            elif save_option.lower() == 'нет':
                                status = 1
                                break

                            else:
                                print('\nВы ввели неверный вариант ответа')
                                save_option = input('\nСохранить вакансии в файл? Да/Нет\n'
                                                'Вы ввели: ')
                else:
                    break

        elif action_number == '2':

            status = 0

            search_query = input('\nВыберите вариант поиска:'
                                 '\n1. По ID'
                                 '\n2. По ключевому слову ')

            while True:

                if status != 1:

                    if len(search_query) == 9:

                        try:
                            int_search_query = int(search_query)
                        except ValueError:
                            print('\nВы неверно ввели ID\n'
                          'ID состоит из 9 цифр')

                        else:
                            data_vacancies = file_work.get_data_from_file()

                            if data_vacancies:

                                id_vacancies = []

                                for vacancy in data_vacancies:

                                    status = 1

                                    if vacancy['id'] == int_search_query:
                                        id_vacancies.append(vacancy)

                                if id_vacancies:
                                    display_of_vacancies(id_vacancies)

                                else:
                                    print('\nВакансии с данным ID не найдены')
                                    break

                            else:
                                print('\nФайл с вакансиями пуст')
                                break

                    else:
                        print('\nВы неверно ввели ID\n'
                          'ID состоит из 9 цифр')
                        search_query = input('\nВведите ID вакансии: ')

                else:
                    break

        elif action_number == '4':

            status = 0

            print('\nВведите данные вакансии:')

            while True:
                if status != 1:
                    id = input('ID: ')

                    if len(id) == 9:
                        try:
                            int_id = int(id)
                        except ValueError:
                            print('\nВы неверно ввели ID\n'
                          'ID состоит из 9 цифр')

                        else:
                            name = input('Название: ')

                            while True:
                                if status != 1:
                                    try:
                                        salary = int(input('Зарплату: '))
                                    except ValueError:
                                        print('Неверно введена зарплата')
                                    else:
                                        requirement = input('Требования: ')
                                        url = input('Ссылка на вакансию: ')

                                        while True:
                                            if 'https://hh.ru/vacancy/' not in url:
                                                print('Неверно введена ссылка на вакансию')
                                                url = input('Ссылка на вакансию: ')

                                            else:
                                                vacancy = Vacancy(id=int_id, name=name, salary=salary, requirement=requirement, url=url)
                                                file_work.add_vacancy(vacancy.to_dict())

                                                print(f"\nВакансия записана в файл 'vacancies.json'")
                                                status = 1
                                                break
                                else:
                                    break

                    else:
                        print('\nВы неверно ввели ID\n'
                              'ID состоит из 9 цифр')

                else:
                    break

        elif action_number == '5':

            file_work.delete_vacancy()
            print('\nФайл очищен')

        elif action_number == '6':
            break

        else:
            print('Вы неверно ввели номер действия')

if __name__ == '__main__':
    user_interaction()
