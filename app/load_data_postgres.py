import json
from data import create_table, insert_batch, get_number_of_records, get_last_ten
from validate_data import check_number_of_fields

table_name = "air_quality_system_data"
errors_table_name="invalid_data"

# Returns the list of columns extracted from 'data' attribute of a json variable
def get_columns(meta):
    schema_meta = meta
    schema_view = schema_meta['view']
    schema_columns = schema_view['columns']

    columns = []
    for item in schema_columns:
        columns.append((item["name"], item["dataTypeName"]))

    return columns


if __name__ == '__main__':
    json_file = open('rows.json', "r")
    json_data = json.load(json_file)
    columns_list = get_columns(json_data['meta'])

    create_table(table_name, columns_list)
    create_table(errors_table_name, columns_list)
    result = check_number_of_fields(json_data['data'], len(columns_list))
    insert_batch(table_name, columns_list, result[1])
    insert_batch(errors_table_name, columns_list, result[0])

    print(f"The total number of records is: {get_number_of_records(errors_table_name)}")
    last_ten_rows = get_last_ten(table_name)
    print("The last 10 records inserted are:")
    print("\n".join([str(row) for row in last_ten_rows]))
