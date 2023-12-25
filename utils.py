
def parse_type(data_dict, space, secret_field, write_in_file):
    for variable, value in data_dict.items():
        if secret_field != '1' and value['secret']:
            continue

        write_in_file.write_in_file_field_name(space, variable, value)

        space += 4

        if value['is_primitive']:
            write_in_file.write_data(value, space)
            space -= 4

        else:
            write_in_file.write_data(value, space)

            parse_type(data_dict[variable]['type'], space, secret_field, write_in_file)


def replace_word(data):
    ignor_data = {
        'bool': 'Логическая',
        'str': 'Строковая',
        'False': '',
        'int': 'Натуральные числа',
        'Max': 'Максимальное',
        'Min': 'Минимальное',
        'InRange': 'Диапазон',
    }

    for key, value in ignor_data.items():
        if key in data:
            data = data.replace(key, value)

    return data