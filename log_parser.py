import re

LOG_FILE_PATH = r'C:\Users\Documents\mysql.log'
TABLE_NAME = "tablename"
TIMESTAMP_REGEX = r"(^[0-9]{6}\s(?:[0-9]{2}\:[0-9]{2}\:[0-9]{2}){1})"
UPDATE_REGEX = r"SET.*WHERE"
ROW_REGEX = r"WHERE\s+\(`(?:(.*?)`\s?=\s?'(.*?)')\)"
INSERT_REGEX = r"\((.*?)\)"
DELETE_REGEX = r"WHERE\s+\(`(?:(.*?)`\s?=\s?'(.*?)')\)"

def extract_data(log_file_path, table_name):
    with open(log_file_path, 'r') as log_file:
        date = []
        queries = []
        tmpdate = []
        for line in log_file:
            tmpdate = re.findall(TIMESTAMP_REGEX, line) if re.findall(TIMESTAMP_REGEX, line) else tmpdate
            if ("update" in line.lower() or "insert" in line.lower() or "delete" in line.lower()) and table_name in line:
                queries.append(line)
                if tmpdate:
                    date.append(tmpdate[0])
        return date, queries

def parse_queries(date, queries):
    update_list = []
    insert_list = []
    delete_list = []
    for i, query in enumerate(queries):
        if "update" in query.lower():
            update = {}
            data1 = re.findall(UPDATE_REGEX, query)
            if data1:
                data2 = re.findall(r"`(.*?)`\s?=\s?'(.*?)'", data1[0])
                update["udata"] = dict(data2)
            tmprow = re.findall(ROW_REGEX, query)
            if tmprow:
                update["row"] = dict(tmprow)
            update_list.append(update)
        elif "insert" in query.lower():
            insert_data = re.findall(INSERT_REGEX, query)
            if insert_data:
                columns = [re.sub(r"\(?`\)?","",col.strip()) for col in insert_data[0].split(",")]
                values = [re.sub(r"\(?'\)?","",val.strip()) for val in insert_data[1].split(",")]
                insert_list.append({"idata": dict(zip(columns, values))})
        elif "delete" in query.lower():
            delete_data = re.findall(DELETE_REGEX, query)
            if delete_data:
                delete_list.append({"drow": dict(delete_data)})
    return update_list, insert_list, delete_list

date, queries = extract_data(LOG_FILE_PATH, TABLE_NAME)
update_list, insert_list, delete_list = parse_queries(date, queries)

print(f"updated rows for table {TABLE_NAME}")
print(update_list)
print("   ")
print(f"inserted rows for table {TABLE_NAME}")
print(insert_list)
print("   ")
print(f"deleted rows for table {TABLE_NAME}")
print(delete_list)