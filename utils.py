
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

def display_of_number_vacancies(number: int, list_vacancies: list) -> print:

    str_number = str(number)

    if len(str_number) == 1:

        if number == 1:
            print(f'\nНайдена {len(list_vacancies)} вакансия, соответствующая вашему запросу')

        elif number == 2 or number == 3 or number == 4:
            print(f'\nНайдено {len(list_vacancies)} вакансии, соответствующие вашему запросу')

        else:
            print(f'\nНайдено {len(list_vacancies)} вакансий, соответствующие вашему запросу')

    elif len(str_number) == 2:

        if number == 11 or number == 12 or number == 13 or number == 14 or number == 15 or number == 16 or number == 17 or number == 18 or number == 19:
            print(f'\nНайдено {len(list_vacancies)} вакансий, соответствующие вашему запросу')

        else:
            if str_number[1] == 1:
                print(f'\nНайдена {len(list_vacancies)} вакансия, соответствующая вашему запросу')

            elif int(str_number[1]) == 2 or int(str_number[1]) == 3 or int(str_number[1]) == 4:
                print(f'\nНайдено {len(list_vacancies)} вакансии, соответствующие вашему запросу')

            else:
                print(f'\nНайдено {len(list_vacancies)} вакансий, соответствующие вашему запросу')

    else:
        print(f'\nНайдено {len(list_vacancies)} вакансий, соответствующие вашему запросу')
