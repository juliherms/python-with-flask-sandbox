# Esta classe representa um VO de contas
class Account():
    def __init__(self, name, resume, amount):
        self.__name = name
        self.__resume = resume
        self.__amount = amount

    @property
    def name(self):
        self.__name

    @name.setter
    def name(self, name):
        self.__name = name

    @property
    def resume(self):
        self.__resume

    @resume.setter
    def resume(self, resume):
        self.__resume = resume

    @property
    def amount(self):
        self.__amount

    @amount.setter
    def amount(self, amount):
        self.__amount = amount