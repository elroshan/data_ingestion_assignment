def check_number_of_fields(data_list, n):
    errors = []
    for item in data_list:
        if len(item) != n:
            errors.append(item)
            data_list.remove(item)
    return errors, data_list



