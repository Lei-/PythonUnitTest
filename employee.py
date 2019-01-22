import requests


class Employee:
    """ A sample Employee class for unit test """

    def __init__(self, first_name, last_name, pay):
        self.first_name = first_name
        self.last_name = last_name
        self.pay = pay

    @property
    def email(self):
        return '{}.{}@email.com'.format(self.first_name, self.last_name)

    def monthly_schedule(self, month):
        response = requests.get(f'http://company.com/{self.last_name}/{month}')
        if response.ok:
            return response.text
        else:
            return 'Bad Response!'
