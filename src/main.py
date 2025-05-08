
from src.api import HeadHunterAPI
from src.file_work import WorkingWithJSON
from src.vacancies import Vacancy
from utils import display_of_vacancies, display_of_number_vacancies

api_vacancies = HeadHunterAPI()
file_work = WorkingWithJSON()
vacant = Vacancy

def user_interaction():

    while True:
        action_number = input("\nВыберите номер действия:\n"
                              "1. Поиск вакансий по ключевому слову\n"
                              "2. Поиск вакансий в файле по ключевому слову или по ID\n"
                              "3. Получить топ N вакансий по зарплате из файла или сайта\n"
                              "4. Записать вакансию в файл\n"
                              "5. Очистить файл с вакансиями\n"
                              "6. Выход\n"
                              "Выбран номер: ")

        if action_number == '1':

            status = 0

            while True:

                if status != 1:

                    user_selection = input('\nВыберете номер действия:'
                                       '\n1. Начать поиск вакансий по ключевому слову'
                                       '\nЕсли вы хотите выйти из этого меню:'
                                       '\n2. Выход'
                                       '\nВыбран номер: ')

                    if user_selection == '1':

                        while True:

                            if status != 1:

                                search_query = input("\nВведите поисковой запрос: ")

                                if search_query.split() == []:
                                    print("\nВы не ввели поисковой запрос!")

                                else:
                                    print(search_query.split())
                                    while True:

                                        if status != 1:

                                            try:
                                                top_vacancies = int(
                                                    input('\nВведите какое количество вакансий вы хотите получить: '))
                                            except ValueError:
                                                print('\nВы неверно ввели количество вакансий!')

                                            else:
                                                vacancies = api_vacancies.get_vacancies(search_query, top_vacancies)

                                                if vacancies:

                                                    display_of_number_vacancies(len(vacancies), vacancies)

                                                    display_of_vacancies(vacancies)

                                                    save_option = input('\nСохранить вакансии в файл? Да/Нет\n'
                                                                        'Ввод: ')

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
                                                            save_option = input('\nВы ввели неверный вариант ответа!'
                                                                                '\nСохранить вакансии в файл? Да/Нет'
                                                                                '\nВы ввели: ')

                                                else:
                                                    print(f"\nВакансии по запросу '{search_query}' не найдены")

                                        else:
                                            break
                            else:
                                break

                    elif user_selection == '2':
                        break

                    else:
                        print('\nВы ввели неверный номер действия!')
                else:
                    break

        elif action_number == '2':

            status = 0

            while True:

                if status != 1:

                    search_query = input('\nВыберите номер действия:'
                                 '\n1. Поиск по ID'
                                 '\n2. Поиск по ключевому слову'
                                 '\nЕсли вы хотите выйти из этого меню:'
                                 '\n3. Выход'
                                 '\nВыбран номер: ')

                    if search_query == '1':

                        user_id = input('\nВведите ID вакансии: ')

                        while True:

                            if status != 1:

                                if len(user_id) == 9:

                                    try:
                                        int_user_id = int(user_id)
                                    except ValueError:
                                        user_id = input('\nВы неверно ввели ID!'
                                            '\nID состоит из 9 цифр'
                                            '\nВведите ID вакансии: ')

                                    else:
                                        data_vacancies = file_work.get_data_from_file()

                                        if data_vacancies:

                                            id_vacancies = []

                                            for vacancy in data_vacancies:

                                                status = 1

                                                if vacancy['id'] == int_user_id:
                                                    id_vacancies.append(vacancy)

                                            if id_vacancies:

                                                display_of_number_vacancies(len(id_vacancies), id_vacancies)

                                                display_of_vacancies(id_vacancies)

                                                if len(id_vacancies) == 1:

                                                    deleted_option = input('\nХотите ли удалить эту вакансию? Да/Нет'
                                                                       '\nВвод: ')
                                                    while True:
                                                        if deleted_option.lower() == 'да':

                                                            file_work.delete_vacancy(id_vacancies)
                                                            print('\nВакансия удалена')
                                                            break

                                                        elif deleted_option.lower() == 'нет':
                                                            status = 1
                                                            break

                                                        else:
                                                            deleted_option = input('\nВы ввели неверный вариант ответа!'
                                                                               '\nХотите ли удалить эту вакансию? Да/Нет'
                                                                               '\nВвод: ')

                                                else:
                                                    deleted_option = input('\nХотите ли удалить эти вакансии? Да/Нет'
                                                                       '\nВвод: ')

                                                    while True:
                                                        if deleted_option.lower() == 'да':

                                                            file_work.delete_vacancy(id_vacancies)
                                                            print('\nВакансии удалены')
                                                            break

                                                        elif deleted_option.lower() == 'нет':
                                                            break

                                                        else:
                                                            deleted_option = input('\nВы ввели неверный вариант ответа!'
                                                                               '\nХотите ли удалить эти вакансии? Да/Нет'
                                                                               '\nВвод: ')

                                            else:
                                                print(f"\nВакансии с ID: '{user_id}' не найдены")
                                                status = 1
                                                break

                                        else:
                                            print(f"\nВакансии с ID: '{user_id}' не найдены так как файл 'vacancies.json' пуст")
                                            status = 1
                                            break

                                else:
                                    user_id = input('\nВы неверно ввели ID!'
                                                '\nID состоит из 9 цифр'
                                                '\nВведите ID вакансии: ')
                            else:
                                break

                    elif search_query == '2':

                        user_search = input('\nВведите поисковой запрос: ')

                        data_vacancies = file_work.get_data_from_file()

                        if data_vacancies:

                            id_vacancies = []

                            for vacancy in data_vacancies:

                                status = 1

                                if user_search in vacancy['name'] or vacancy['name'] == user_search:
                                    id_vacancies.append(vacancy)

                            if id_vacancies:

                                display_of_number_vacancies(len(id_vacancies), id_vacancies)

                                display_of_vacancies(id_vacancies)

                                if len(id_vacancies) == 1:

                                    deleted_option = input('\nХотите ли удалить эту вакансию? Да/Нет'
                                                           '\nВвод: ')
                                    while True:
                                        if deleted_option.lower() == 'да':

                                            file_work.delete_vacancy(id_vacancies)
                                            print('\nВакансия удалена')
                                            break

                                        elif deleted_option.lower() == 'нет':
                                            status = 1
                                            break

                                        else:
                                            deleted_option = input('\nВы ввели неверный вариант ответа!'
                                                                   '\nХотите ли удалить эту вакансию? Да/Нет'
                                                                   '\nВвод: ')

                                else:
                                    deleted_option = input('\nХотите ли удалить эти вакансии? Да/Нет'
                                                           '\nВвод: ')

                                    while True:
                                        if deleted_option.lower() == 'да':

                                            file_work.delete_vacancy(id_vacancies)
                                            print('\nВакансии удалены')
                                            break

                                        elif deleted_option.lower() == 'нет':
                                            break

                                        else:
                                            deleted_option = input('\nВы ввели неверный вариант ответа!'
                                                                   '\nХотите ли удалить эти вакансии? Да/Нет'
                                                                   '\nВвод: ')

                            else:
                                print(f"\nВакансии с названием: '{user_search}' не найдены")
                                break

                        else:
                            print(f"\nВакансии с названием: '{user_search}' не найдены так как файл 'vacancies.json' пуст")
                            break

                    elif search_query == '3':
                        break

                    else:
                        print('\nВы ввели неверный номер действия!')


                else:
                    break

        elif action_number == '3':

            status = 0

            while True:

                if status != 1:

                    search_query = input('\nВыберете номер действия:'
                                         '\n1. В файле'
                                         '\n2. На сайте'
                                         '\nЕсли вы хотите выйти из этого меню:'
                                         '\n3. Выход'
                                         '\nВыбран вариант: ')

                    if search_query == '1':

                        top_n = input('\nВведите топ N (топ сколько вакансий вы хотите получить): ')

                        while True:
                            if top_n:

                                data_vacancies = file_work.get_data_from_file()

                                top_vacancies = []

                                top_vacancies_salary = 0

                                if data_vacancies:
                                    for vacancy in data_vacancies:
                                        if vacant.__ge__(vacancy['salary'], top_vacancies_salary):
                                            top_vacancies.append(vacancy)
                                            top_vacancies_salary = vacancy['salary']

                                    display_of_vacancies(top_vacancies)

                                else:
                                    print("Файл 'vacancies.json' пуст")

                            else:
                                print('\nВы не ввели поисковой запрос!')

                    elif search_query == '2':
                        pass

                    elif search_query == '3':
                        break

                    else:
                        print('\nВы ввели неверный номер действия!')

        elif action_number == '4':

            status = 0

            while True:

                if status != 1:

                    user_selection = input('\nВыберете номер действия:'
                                       '\n1. Начать запись вакансии в файл'
                                       '\nЕсли вы хотите выйти из этого меню:'
                                       '\n2. Выход'
                                       '\nВыбран вариант: ')

                    if user_selection == '1':

                        while True:
                            if status != 1:
                                id = input('\nID: ')

                                if len(id) == 9:
                                    try:
                                        int_id = int(id)
                                    except ValueError:
                                        print('\nВы неверно ввели ID!'
                          '\nID состоит из 9 цифр')

                                    else:
                                        name = input('Название: ')

                                        while True:
                                            if status != 1:
                                                try:
                                                    salary = int(input('Зарплата: '))
                                                except ValueError:
                                                    print('Неверно введена зарплата!')
                                                else:
                                                    requirement = input('Требования: ')
                                                    url = input('Ссылка на вакансию: ')

                                                    while True:
                                                        if 'https://hh.ru/vacancy/' not in url:
                                                            url = input('\nНеверно введена ссылка на вакансию!'
                                                            '\nПример: https://hh.ru/vacancy/'
                                                            '\nСсылка на вакансию: ')

                                                        else:
                                                            vacancy = Vacancy(id=int_id, name=name, salary=salary, requirement=requirement, url=url)
                                                            file_work.add_vacancy(vacancy.to_dict())

                                                            print(f"\nВакансия записана в файл 'vacancies.json'")
                                                            status = 1
                                                            break
                                            else:
                                                break

                                else:
                                    print('\nВы неверно ввели ID!'
                              '\nID состоит из 9 цифр')

                            else:
                                break

                    elif user_selection == '2':
                        break

                    else:
                        print('\nВы ввели неверный номер действия!')

                else:
                    break

        elif action_number == '5':
            file_work.file_cleaning()
            print("\nФайл 'vacancies.json' очищен")

        elif action_number == '6':
            break

        else:
            print('\nВы ввели неверный номер действия!')

if __name__ == '__main__':
    user_interaction()
