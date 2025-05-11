from src.file_work import WorkingWithJSON

def display_of_vacancies(list_vacancies: list) -> print:

    for vacancy in list_vacancies:

        if vacancy['requirement'] is None:
            print(f'\nID: {vacancy['id']}\n'
                  f'Название: {vacancy['name']}\n'
                  f'Зарплата: {vacancy['salary']}\n'
                  f'Требования: Не указаны\n'
                  f'Ссылка на вакансию: {vacancy['url']}')


        else:
            print(f'\nID: {vacancy['id']}\n'
                  f'Название: {vacancy['name']}\n'
                  f'Зарплата: {vacancy['salary']}\n'
                  f'Требования: {vacancy['requirement']}\n'
                  f'Ссылка на вакансию: {vacancy['url']}')

def display_of_number_vacancies(len_list_vacancies: int, list_vacancies: list) -> print:

    str_number = str(len_list_vacancies)

    if len(str_number) == 1:

        if len_list_vacancies == 1:
            print(f'\nНайдена {len(list_vacancies)} вакансия, соответствующая вашему запросу')

        elif len_list_vacancies == 2 or len_list_vacancies == 3 or len_list_vacancies == 4:
            print(f'\nНайдено {len(list_vacancies)} вакансии, соответствующие вашему запросу')

        else:
            print(f'\nНайдено {len(list_vacancies)} вакансий, соответствующих вашему запросу')

    elif len(str_number) == 2:

        if len_list_vacancies == 11 or len_list_vacancies == 12 or len_list_vacancies == 13 or len_list_vacancies == 14 or len_list_vacancies == 15 or len_list_vacancies == 16 or len_list_vacancies == 17 or len_list_vacancies == 18 or len_list_vacancies == 19:
            print(f'\nНайдено {len(list_vacancies)} вакансий, соответствующие вашему запросу')

        else:
            if str_number[1] == 1:
                print(f'\nНайдена {len(list_vacancies)} вакансия, соответствующая вашему запросу')

            elif int(str_number[1]) == 2 or int(str_number[1]) == 3 or int(str_number[1]) == 4:
                print(f'\nНайдено {len(list_vacancies)} вакансии, соответствующие вашему запросу')

            else:
                print(f'\nНайдено {len(list_vacancies)} вакансий, соответствующих вашему запросу')

    else:
        print(f'\nНайдено {len(list_vacancies)} вакансий, соответствующие вашему запросу')

def display_range_vacancies(top_n: int, list_vacancies: list) -> print:

    status = 0

    for vacancy in list_vacancies:
        if vacancy['requirement'] is None:
            print(f'\nID: {vacancy['id']}\n'
                      f'Название: {vacancy['name']}\n'
                      f'Зарплата: {vacancy['salary']}\n'
                      f'Требования: Не указаны\n'
                      f'Ссылка на вакансию: {vacancy['url']}')

            status += 1

            if status == top_n:
                break

        else:
            print(f'\nID: {vacancy['id']}\n'
                      f'Название: {vacancy['name']}\n'
                      f'Зарплата: {vacancy['salary']}\n'
                      f'Требования: {vacancy['requirement']}\n'
                      f'Ссылка на вакансию: {vacancy['url']}')

            status += 1

            if status == top_n:
                break

def deleted_option(list_vacancies: list) -> print:

    status = 0

    if len(list_vacancies) == 1:

        while True:

            if status != 1:

                deleted_option = input('\nВыберете номер действия:'
                                       '\n1. Удалить эту вакансию'
                                       '\n2. Не удалять'
                                       '\nВыбран номер: ')

                if deleted_option == '1':

                    WorkingWithJSON().delete_vacancy(list_vacancies)
                    print('\nВакансия удалена')
                    status = 1
                    break

                elif deleted_option == '2':
                    status = 1
                    break

                else:
                    print('\nВы ввели неверный номер действия!')

            else:
                break

    else:
        while True:

            if status != 1:

                deleted_option = input('\nВыберете номер действия:'
                                       '\n1. Удалить эти вакансии'
                                       '\n2. Не удалять'
                                       '\nВыбран номер: ')

                if deleted_option == '1':

                    WorkingWithJSON().delete_vacancy(list_vacancies)
                    print('\nВакансии удалены')
                    status = 1
                    break

                elif deleted_option == '2':
                    status = 1
                    break

                else:
                    print('\nВы ввели неверный номер действия!')

            else:
                break

def display_top_vacancies(list_vacancies: list) -> print:

    status = 0

    while True:

        if status != 1:

            try:
                top_n = int(input(
                    '\nВведите топ N (топ сколько вакансий вы хотите получить): '))
            except ValueError:
                print('\nВы неверно ввели топ N!')
            else:
                if top_n == 1:

                    sorted_range_vacancies = sorted(
                        list_vacancies,
                        key=lambda x: x[
                            'salary'],
                        reverse=True)

                    display_range_vacancies(top_n,
                                            sorted_range_vacancies)

                    status = 1
                    break

                elif top_n > 1:
                    user_selection_3 = input(
                        '\nВыберете номер действия:'
                        '\n1. Отсортировать по возрастанию'
                        '\n2. Отсортировать по убыванию'
                        '\nВыбрано действие: ')

                    if user_selection_3 == '1':

                        sorted_range_vacancies = sorted(
                            list_vacancies,
                            key=lambda x: x[
                                'salary'],
                            reverse=False)

                        display_range_vacancies(top_n,
                                                sorted_range_vacancies)

                        status = 1
                        break

                    elif user_selection_3 == '2':

                        sorted_range_vacancies = sorted(
                            list_vacancies,
                            key=lambda x: x[
                                'salary'],
                            reverse=True)

                        display_range_vacancies(top_n,
                                                sorted_range_vacancies)

                        status = 1
                        break

                    else:
                        print('\nВы ввели неверный номер действия!')

                else:
                    print('\nНельзя вывести топ 0')

        else:
            break
