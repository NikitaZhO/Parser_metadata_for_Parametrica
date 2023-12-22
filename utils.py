
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
