import json
from tqdm import tqdm
from CheckValidation import CheckValidation


class Validator:
    """
    Объект класса Validator проверяет записи файла на валидность.
    Он нужен для валидации записей исходного файла, подсчета
    валидных/невалидных записей и записей по типам ошибок
        Attributes
        ----------
            data : list
                 Список записей.
    """
    data: list

    def __init__(self, path: str) -> None:
        """
        Инициализирует экземпляр класса валидатор.
            Parameters
            ----------
                path : str
                    Путь к входному файлу с данными.
        """
        self.data = []
        tmp = json.load(open(path, encoding='windows-1251'))
        for elem in tmp:
            self.data.append(CheckValidation(elem.copy()))

    def validation(self, index: int) -> dict:
        """
        Выполняет валидацию записи.
            Attributes
            ----------
                index : index
                    Индекс записи в списке записей
            Returns
            -------
                dict:
                    Словарь вида: "тип данных о сотруднике": флаг валидности.
        """
        result = {"email": self.data[index].check_email(),
                  "height": self.data[index].check_height(),
                  "inn": self.data[index].check_inn(),
                  "passport_number": self.data[index].check_passport_number(),
                  "occupation": self.data[index].check_occupation(),
                  "age": self.data[index].check_age(),
                  "academic_degree": self.data[index].check_academic_degree(),
                  "worldview": self.data[index].check_worldview(),
                  "address": self.data[index].check_address()}
        return result.copy()

    def count_valid_data(self) -> int:
        """
        Производит подсчет валидных записей.
            Returns
            -------
                int:
                    Число валидных записей.
        """
        valid_counter = 0
        for elem in tqdm(range(len(self.data)), desc="Подсчёт валидных записей", ncols=100):
            if not (False in self.validation(elem).values()):
                valid_counter += 1
        return valid_counter

    def count_invalid_data(self) -> int:
        """
        Производит подсчет невалидных записей.
            Returns
            -------
                int:
                    Число невалидных записей.
        """
        invalid_counter = 0
        for elem in tqdm(range(len(self.data)), desc="Подсчёт невалидных записей", ncols=100):
            if False in self.validation(elem).values():
                invalid_counter += 1
        return invalid_counter

    def count_invalid_arguments(self):
        """
        Производит подсчет невалидных записей по типам ошибок.
            Returns
            -------
                list:
                    Список невалидных записей по типам ошибок.
        """
        result = []
        c_email = 0
        c_height = 0
        c_inn = 0
        c_passport_number = 0
        c_occupation = 0
        c_age = 0
        c_academic_degree = 0
        c_worldview = 0
        c_address = 0

        for elem in tqdm(range(len(self.data)), desc="Подсчёт невалидных записей по типам ошибок", ncols=100):
            if not self.data[elem].check_email():
                c_email += 1
            if not self.data[elem].check_height():
                c_height += 1
            if not self.data[elem].check_inn():
                c_inn += 1
            if not self.data[elem].check_passport_number():
                c_passport_number += 1
            if not self.data[elem].check_occupation():
                c_occupation += 1
            if not self.data[elem].check_age():
                c_age += 1
            if not self.data[elem].check_academic_degree():
                c_academic_degree += 1
            if not self.data[elem].check_worldview():
                c_worldview += 1
            if not self.data[elem].check_address():
                c_address += 1
        result.append(c_email)
        result.append(c_height)
        result.append(c_inn)
        result.append(c_passport_number)
        result.append(c_occupation)
        result.append(c_age)
        result.append(c_academic_degree)
        result.append(c_worldview)
        result.append(c_address)
        return result
