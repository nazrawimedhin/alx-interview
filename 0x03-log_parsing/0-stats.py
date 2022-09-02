#!/usr/bin/python3
"""reads stdin line by line and computes metrics"""

import sys


def print_stat(tot_file_size, codes):
    """print stat for specified inputs"""
    print("File size: {}".format(tot_file_size))
    codes_sorted = sorted(codes.keys())
    for code in codes_sorted:
        if codes[code] > 0:
            print("{}: {}".format(code, codes[code]))


status_codes = [200, 301, 400, 401, 403, 404, 405, 500]
status_code_counts = {str(status): 0 for status in status_codes}
total_file_size = 0
line_count = 0

if __name__ == "__main__":
    try:
        for line in sys.stdin:
            status_code, file_size = line.split()[-2:]
            if status_code in status_code_counts.keys():
                status_code_counts[status_code] += 1
            file_size = int(file_size)
            total_file_size += file_size
            line_count += 1
            if line_count == 10:
                print_stat(total_file_size, status_code_counts)
                line_count = 0
    except KeyboardInterrupt:
        print_stat(total_file_size, status_code_counts)
        raise
    except Exception:
        pass
    print_stat(total_file_size, status_code_counts)
