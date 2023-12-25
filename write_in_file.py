''' Модуль проверки и записи данных в файл '''
import utils

class WriteInFile:
    def __init__(self, write_hint='1', rule_field='1', secret_field='1'):
        self.write_hint = write_hint
        self.rule_field = rule_field
        self.secret_field = secret_field

    def write_data(self, values, space):
        label = values['label']
        data_for_file = f'{" " * space}label - {label}\n'

        if self.secret_field != 1:
            if values['secret'] is False:
                data_for_file = f'{" " * space}secret - Не секретное поле\n'
            else:
                data_for_file = f'{" " * space}secret - Секретное поле\n'

        if values['is_iterable'] is True:
            data_for_file += f'{" " * space}type - Список\n'
        else:
            data_type = values['type']
            if not isinstance(data_type, dict):

                data_type = utils.replace_word(data_type)

                data_for_file += f'{" " * space}type - {data_type}\n'
            else:
                data_for_file += f'{" " * space}type - Словарь\n'

        try:
            data_for_file += f'{" " * space}default - {values["default"].value}\n'
        except KeyError:
            pass
        except AttributeError:
            data_for_file += f'{" " * space}default - {values["default"]}\n'

        try:
            rule = values['rule']

            # rule = utils.replace_word(rule)
            if 'Match' in str(rule):
                rule = 'регулярное выражение - ' + rule
            if rule is not None:
                if self.rule_field == '1':
                    rule = utils.replace_word(rule)
                    data_for_file += f'{" " * space}rule - {rule}\n'
        except KeyError:
            pass

        self.write_in_file(data_for_file)

    def write_in_file_field_name(self, space, variable, value):
        if self.write_hint == '1' and value["hint"] != '':
            a = f'{" " * space}=== ПОЛЕ {variable} === \t\t Пояснение к полю: {value["hint"]}'
        else:
            a = f'{" " * space}=== ПОЛЕ {variable} ==='
        self.write_in_file(a)

    def write_in_file(self, str_data):
        with open('metadata.txt', 'a', encoding='utf-8') as file:
            file.write(f'{str_data}\n')
