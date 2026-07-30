#!/usr/bin/python3
"""Reads from standard input and computes metrics.

After every ten lines or upon receiving a keyboard interruption (CTRL + C),
it prints the following statistics:
    - Total file size up to that point.
    - Count of read status codes (200, 301, 400, 401, 403, 404, 405, 500).
"""
import sys


def print_stats(size, status_codes):
    """Print accumulated metrics.

    Args:
        size (int): The accumulated file size.
        status_codes (dict): The accumulated count of status codes.
    """
    print("File size: {}".format(size))
    for key in sorted(status_codes.keys()):
        if status_codes[key] > 0:
            print("{}: {}".format(key, status_codes[key]))


if __name__ == "__main__":
    total_size = 0
    status_codes = {
        "200": 0, "301": 0, "400": 0, "401": 0,
        "403": 0, "404": 0, "405": 0, "500": 0
    }
    line_count = 0

    try:
        for line in sys.stdin:
            line_count += 1
            parts = line.split()

            try:
                # Get the file size (the last element)
                total_size += int(parts[-1])
            except (IndexError, ValueError):
                pass

            try:
                # Get the status code (the second to last element)
                status = parts[-2]
                if status in status_codes:
                    status_codes[status] += 1
            except IndexError:
                pass

            if line_count % 10 == 0:
                print_stats(total_size, status_codes)

        # Print final stats if end of stream is reached normally
        print_stats(total_size, status_codes)

    except KeyboardInterrupt:
        print_stats(total_size, status_codes)
        raise
