import re


class CheckValidation:
    """
    Объект класса CheckValidation обрабатывает запись о научном сотруднике.
    Используется для хранения полей записи и их валидации.
        Attributes
        ----------
            dictionary : dict
                Словарь хранит записи в виде "тип данных о сотруднике": данные о сотруднике.
    """
    dictionary: dict

    def __init__(self, tmp: dict) -> None:
        """
        Инициализирует экземпляр класса записи.
            Parameters
            ----------
                tmp : dict
                    Копия списка с полями записи.
        """
        self.dictionary = tmp.copy()

    def check_email(self) -> bool:
        """
        Проверяет электронную почту на валидность.
            Returns
            -------
                bool:
                    Результат проверки на корректность.
        """
        pattern = r"^[^\s@]+@([^\s@.,]+\.)+[^\s@.,]{2,}$"
        if re.match(pattern, self.dictionary["email"]):
            return True
        return False

    def check_height(self) -> bool:
        """
        Проверяет значение роста на валидность.
            Returns
            -------
                bool:
                    Результат проверки на корректность.
        """
        try:
            height = float(self.dictionary["height"])
        except ValueError:
            return False
        return 1 < height < 2.3

    def check_inn(self) -> bool:
        """
        Проверяет номер ИНН на валидность.
            Returns
            -------
                bool:
                    Результат проверки на корректность.
        """
        pattern = r"^\d{12}$"
        if re.match(pattern, self.dictionary["inn"]):
            return True
        return False

    def check_passport_number(self) -> bool:
        """
        Проверяет номер паспорта на валидность.
            Returns
            -------
                bool:
                    Результат проверки на корректность.
        """
        if isinstance(self.dictionary["passport_number"], int):
            if 100000 <= self.dictionary["passport_number"] < 1000000:
                return True
        return False

    def check_occupation(self) -> bool:
        """
        Проверяет название профессии на валидность.
            Returns
            -------
                bool:
                    Результат проверки на корректность.
        """
        pattern = r"^([а-яА-Я]|[a-zA-Z]|-| ){3,}$"
        if re.match(pattern, self.dictionary["occupation"]):
            return True
        return False

    def check_age(self) -> bool:
        """
        Проверяет значение возраста человека на валидность.
            Returns
            -------
                bool:
                    Результат проверки на корректность.
        """
        if isinstance(self.dictionary["age"], int):
            if 20 <= self.dictionary["age"] < 120:
                return True
        return False

    def check_academic_degree(self) -> bool:
        """
        Проверяет академическую степень на валидность.
            Returns
            -------
                bool:
                    Результат проверки на корректность.
        """
        pattern = r"Бакалавр|Кандидат наук|Специалист|Магистр|Доктор наук"
        if re.match(pattern, self.dictionary["academic_degree"]):
            return True
        return False

    def check_worldview(self) -> bool:
        """
        Проверяет взгляд на мир на валидность.
            Returns
            -------
                bool:
                    Результат проверки на корректность.
        """
        pattern = r"^.+(?:изм|анство)$"
        if re.match(pattern, self.dictionary["worldview"]):
            return True
        return False

    def check_address(self) -> bool:
        """
        Проверяет адрес на валидность.
            Returns
            -------
                bool:
                    Результат проверки на корректность.
        """
        pattern = r"(?:ул\.|Аллея) (?:им[\.\s]|)[^\s]+ [^\s]*(?:\s|)\d+"
        if re.match(pattern, self.dictionary["address"]):
            return True
        return False
