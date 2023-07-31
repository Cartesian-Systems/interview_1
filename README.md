## Interview Question: Log Analysis

### Objective: Write a script that processes a log stream, extracts
useful informationfrom it, and generates a summary report. The log file
contains lines with different log levels, timestamps, and messages. Your
task is to extract specific information and present it in a human-readable
format.

### The function should generate a summary report with the following information:
 - Total number of log entries in the file.
 - Number of log entries for each log level (e.g., INFO, ERROR, WARNING, etc.).
 - The earliest and latest timestamps recorded in the log file.
 - The most frequent word occurring in the log messages.
 - A list of unique words found in the log messages.

### example:
#### input lines
```
[2023-07-26 12:34:56] [INFO] User logged in successfully.
[2023-07-26 12:35:20] [ERROR] Connection refused by the server.
[2023-07-26 12:36:15] [INFO] User data updated.
[2023-07-26 12:37:05] [INFO] User logged in successfully.
```

#### output lines
```
Total log entries: 4
Log level counts: {'INFO': 3, 'ERROR': 1}
Earliest timestamp: 2023-07-26 12:34:56
Latest timestamp: 2023-07-26 12:37:05
Most frequent word: user
Unique words: {'user', 'logged', 'in', 'successfully', 'connection', 'refused', 'by', 'the', 'server', 'data', 'updated'}
```

