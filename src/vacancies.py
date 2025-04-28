from src.api import HeadHunterAPI

class Vacancy:

    __slots__ = ('name', 'salary', 'requirement', 'link_to_vacancy')

    def __validate_name(self, name):
        if not isinstance(name, str) or not name:
            return 'Вакансия не имеет имени'
        return name

    def __validate_salary(self, salary):
        if not isinstance(salary, int) or salary < 0:
            return 0
        return salary

    def __validate_requirement(self, requirement):
        if not isinstance(requirement, str) or not requirement:
            return 'Описание отсутсвует'
        return requirement

    def __validate_link_to_vacancy(self, link_to_vacancy):
        if not isinstance(link_to_vacancy, str) or not link_to_vacancy:
            return 'Ссылка на вакансию отсутствует'
        return link_to_vacancy


    def __init__(self, name, salary, requirement, link_to_vacancy):
        self.name = self.__validate_name(name)
        self.salary = self.__validate_salary(salary)
        self. requirement = self.__validate_requirement(requirement)
        self.link_to_vacancy = self.__validate_link_to_vacancy(link_to_vacancy)

    def __lt__(self, other):
        return self < other

    def __le__(self, other):
        return self <= other

    def __gt__(self, other):
        return self > other

    def __ge__(self, other):
        return self >= other

    def __repr__(self):
        return f"Vacancy(name='{self.name}', salary='{self.salary}', requirement='{self.requirement}', link_to_vacancy='{self.link_to_vacancy}')"

    def to_dict(self):
        return {
            'name': self.name,
            'salary': self.salary,
            'requirement': self.requirement,
            'link_to_vacancy': self.link_to_vacancy
        }

if __name__ == '__main__':
    imp1 = HeadHunterAPI()
    #print(imp1.get_vacancies('Водитель'))
    imp2 = Vacancy
    str(imp2)