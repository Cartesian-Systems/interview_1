

easy = """[2023-07-26 12:34:56] [INFO] User logged in successfully.
[2023-07-26 12:35:20] [ERROR] Connection refused by the server.
[2023-07-26 12:36:15] [INFO] User data updated.
[2023-07-26 12:37:05] [INFO] User logged in successfully."""

hard = """[2023-07-26 10:15:23] [INFO] Application started
[2023-07-26 10:15:30] [ERROR] Invalid input received
[2023-07-26 10:15:35] [DEBUG] Processing data
[2023-07-26 10:15:42] [WARNING] Connection timed out
[2023-07-26 10:15:50] [INFO] User logged in
[2023-07-26 10:16:01] [ERROR] Database connection failed
[2023-07-26 10:16:08] [INFO] Request received from 192.168.1.10
[2023-07-26 10:16:15] [DEBUG] Calculating results
[2023-07-26 10:16:22] [ERROR] File not found
[2023-07-26 10:16:30] [INFO] Task completed successfully
[2023-07-26 10:16:38] [DEBUG] Validating user input
[2023-07-26 10:16:45] [ERROR] Out of memory
[2023-07-26 10:16:53] [WARNING] Deprecated function used
[2023-07-26 10:17:01] [INFO] File uploaded
[2023-07-26 10:17:10] [ERROR] Internal server error
[2023-07-26 10:17:17] [DEBUG] Generating report
[2023-07-26 10:17:25] [INFO] Payment received from John Doe
[2023-07-26 10:17:32] [ERROR] Unable to process request
[2023-07-26 10:17:40] [INFO] Configuration saved
[2023-07-26 10:17:48] [DEBUG] Checking permissions"""

fail = """[2023-07-26 12:34:56] [INFO] User logged in successfully.
[2023-07-26 12:35:20]] [ERROR] Connection refused by the server.
[2023-07-26 12:36:15] [INFO] User data updated.
[2023-07-26 12:37:05] [INFO] User logged in successfully."""


def parse_lines(lines: str):
    """Parse lines into a the desired parts"""
    count = 0
    log_level_counts = None
    earliest_timestamp = None
    latest_timestamp = None
    most_frequent_word = None
    unique_words = None

    for line in lines.splitlines():
       pass

    print_results(count, log_level_counts, earliest_timestamp, latest_timestamp, most_frequent_word, unique_words)


def print_results(count: int, log_level_counts: dict, 
                  earliest_timestamp: str, latest_timestamp: str,
                  most_frequent_word: str, unique_words: set):
    """Print the results"""
    print(f"Total log entries: {count}")
    print(f"Log level counts: {log_level_counts}")
    print(f"Earliest timestamp: {earliest_timestamp}")
    print(f"Latest timestamp: {latest_timestamp}")
    print(f"Most frequent word: {most_frequent_word}")
    print(f"Unique words: {unique_words}")

parse_lines(easy)
print("------------------")
parse_lines(hard)
print("------------------")
parse_lines(fail)