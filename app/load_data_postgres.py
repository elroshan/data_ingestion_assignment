import json

from dbmanager import create_table, insert_batch, get_number_of_records, get_last_ten
from validate_data import check_number_of_fields

TABLE_NAME = "air_quality_system_data"
ERRORS_TABLE_NAME = "invalid_data"
DATA_FILE = "rows.json"


# Returns a list of columns extracted from 'data' attribute of a json variable
def get_columns(meta):
    schema_meta = meta
    schema_view = schema_meta['view']
    schema_columns = schema_view['columns']

    columns = []
    for item in schema_columns:
        columns.append((item["name"], item["dataTypeName"]))

    return columns


if __name__ == '__main__':
    json_file = open(DATA_FILE, "r")
    json_data = json.load(json_file)
    columns_list = get_columns(json_data['meta'])

    create_table(TABLE_NAME, columns_list)
    create_table(ERRORS_TABLE_NAME, columns_list)
    result = check_number_of_fields(json_data['data'], len(columns_list))
    insert_batch(TABLE_NAME, columns_list, result[1])
    insert_batch(ERRORS_TABLE_NAME, columns_list, result[0])

    print(f"The total number of records is: {get_number_of_records(ERRORS_TABLE_NAME)}")
    last_ten_rows = get_last_ten(TABLE_NAME)
    print("The last 10 records inserted are:")
    print("\n".join([str(row) for row in last_ten_rows]))
