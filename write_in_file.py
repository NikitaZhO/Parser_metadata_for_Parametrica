''' Модуль проверки и записи данных в файл '''


class WriteInFile:
    def __init__(self, write_hint='1', rule_field='1'):
        self.write_hint = write_hint
        self.rule_field = rule_field

    def write_data(self, values, space):
        label = values['label']
        secret = values['secret']
        data_for_file = f'{" " * space}label - {label}\n' \
            f'{" " * space}secret - {secret}\n'

        data_type = values['type']
        if str(type(data_type)) != "<class 'dict'>":
            data_for_file += f'{" " * space}type - {data_type}\n'
        else:
            data_for_file += f'{" " * space}type - Словарь\n'

        try:
            data_for_file += f'{" " * space}default - {values["default"].value}\n'
        except KeyError:
            pass
        except AttributeError:
            pass

        try:
            rule = values['rule']
            if rule is not None:
                if self.rule_field == '1':
                    data_for_file += f'{" " * space}rule - {rule}\n'
        except KeyError:
            pass

        self.write_in_file(data_for_file)

    def write_in_file_field_name(self, space, variable, value):
        if self.write_hint == '1' and value["hint"] != '':
            a = f'{" " * space}=== ПОЛЕ {variable} === \t\t\t\t # {value["hint"]}'
        else:
            a = f'{" " * space}=== ПОЛЕ {variable} ==='
        self.write_in_file(a)

    def write_in_file(self, str_data):
        with open('metadata.txt', 'a') as file:
            file.write(f'{str_data}\n')
