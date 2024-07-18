#!/usr/bin/python3
"""
Write a script that reads stdin line by line and computes metrics from a log.
"""

import sys

# Stores all the count of all status codes in a dictionary provided
status_codes_dict = {'200': 0, '301': 0, '400': 0, '401': 0, '403': 0,
                     '404': 0, '405': 0, '500': 0}

total_size = 0
# stores count of the number of lines counted
count = 0

def print_metrics():
    """Print the current metrics"""
    print('File size: {}'.format(total_size))
    for key, value in sorted(status_codes_dict.items()):
        if value != 0:
            print('{}: {}'.format(key, value))

try:
    for line in sys.stdin:
        line_list = line.split()

        if len(line_list) > 4:
            status_code = line_list[-2]
            file_size = int(line_list[-1])

            # Check if the status code received exists in the dictionary and increment its count
            if status_code in status_codes_dict:
                status_codes_dict[status_code] += 1

            # Update total size
            total_size += file_size

            # Update count of lines
            count += 1

        if count == 10:
            print_metrics()
            # Reset count
            count = 0

except KeyboardInterrupt:
    print_metrics()
    raise

finally:
    print_metrics()

