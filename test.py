

easy = """
[2023-07-26 12:34:56] [INFO] User logged in successfully.
[2023-07-26 12:35:20] [ERROR] Connection refused by the server.
[2023-07-26 12:36:15] [INFO] User data updated.
[2023-07-26 12:37:05] [INFO] User logged in successfully.
"""

hard = """
[2023-07-26 10:15:23] [INFO] Application started
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
[2023-07-26 10:17:48] [DEBUG] Checking permissions
"""

fail = """
[2023-07-26 12:34:56] [INFO] User logged in successfully.
[2023-07-26 12:35:20]] [ERROR] Connection refused by the server.
[2023-07-26 12:36:15] [INFO] User data updated.
[2023-07-26 12:37:05] [INFO] User logged in successfully.
"""


def parse_lines(lines: str):
    """Parse lines into a the desired parts"""
    pass


parse_lines(easy)
print("------------------")
parse_lines(hard)
print("------------------")
parse_lines(fail)