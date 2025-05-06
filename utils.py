
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
