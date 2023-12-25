import default_varieble
from config import config
import utils
from write_in_file import WriteInFile


def main():
    metadata_config = config.__metadata__()

    write_hint = str(default_varieble.write_hint)
    secret_field = str(default_varieble.secret_field)
    rule_field = str(default_varieble.rule_field)

    write_in_file = WriteInFile(write_hint, rule_field)

    with open('metadata.txt', 'w', encoding='utf-8') as file:
        file.write('')

    # Проверяем верхний уровень dict, если есть вложенности запускаем цикл
    for variable, value in metadata_config.items():
        space = 0

        if secret_field != '1' and value['secret']:
            continue

        write_in_file.write_in_file_field_name(space, variable, value)

        if value['is_primitive']:
            space += 4
            write_in_file.write_data(value, space)
        else:
            space += 4
            write_in_file.write_data(value, space)

            utils.parse_type(metadata_config[variable]['type'], space, secret_field, write_in_file)


if __name__ == '__main__':
    main()
