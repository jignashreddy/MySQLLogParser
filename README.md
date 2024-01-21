# MySQL Log Parser

MySQL Log Parser is a Python script that parses a MySQL log file and extracts information about "update", "insert", and "delete" operations on a specific table.

## Prerequisites

Before you begin, ensure you have met the following requirements:

* You have installed Python 3.6 or later.
* You have a MySQL log file to parse.

To use this script, you need to first enable SQL logging by executing the query `SET global general_log = on;`. Logs can be viewed in table or file. Here we are reading from the file. To set it as file, execute `SET global log_output = 'file';`.

To find the default file path of the log file use the query `SHOW VARIABLES LIKE "%general_log";`. To set a relative path for the log file in desired destination use the query `SET global general_log_file='/tmp/mysql.log';`.

## Using MySQL Log Parser

To use MySQL Log Parser, follow these steps:

1. Update the `LOG_FILE_PATH` and `TABLE_NAME` variables in `log_parser.py` with your log file path and table name, respectively.
2. Run the script with the command: `python log_parser.py`.

## Features

* Extracts and stores timestamps of operations.
* Identifies "update", "insert", and "delete" operations on a specified table.
* For "update" operations, extracts the data being set and the row being updated.
* For "insert" operations, extracts the column names and values.
* For "delete" operations, extracts the row being deleted.

## Contributing to MySQL Log Parser

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.



