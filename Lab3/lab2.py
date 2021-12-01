import argparse
from Validator import Validator
from FileWriter import FileWriter
parser = argparse.ArgumentParser("Парсер для входных и выходных данных")
parser.add_argument("-input", type=str, default="31.txt",
                    help="Входной файл данных")
parser.add_argument("-output", type=str, default="result_31.txt",
                    help="Выходной файл с валидными данными")
pars = parser.parse_args()

data = Validator(pars.input)
valid_data = data.count_valid_data()
invalid_data = data.count_invalid_data()
lst_mistakes = data.count_invalid_arguments()
write_data = FileWriter(pars.output)
write_data.write_to_file(data)
print("Статистика:")
print("Число валидных записей:", valid_data)
print("Общее число невалидных записей:", invalid_data)
print("Число невалидных записей по типу ошибки 'email': ", lst_mistakes[0])
print("Число невалидных записей по типу ошибки 'height': ", lst_mistakes[1])
print("Число невалидных записей по типу ошибки 'inn': ", lst_mistakes[2])
print("Число невалидных записей по типу ошибки 'passport_number': ", lst_mistakes[3])
print("Число невалидных записей по типу ошибки 'occupation': ", lst_mistakes[4])
print("Число невалидных записей по типу ошибки 'age': ", lst_mistakes[5])
print("Число невалидных записей по типу ошибки 'academic_degree': ", lst_mistakes[6])
print("Число невалидных записей по типу ошибки 'worldview': ", lst_mistakes[7])
print("Число невалидных записей по типу ошибки 'address': ", lst_mistakes[8])
