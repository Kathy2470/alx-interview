#!/usr/bin/python3
import sys
import signal

total_size = 0
status_codes = {200: 0, 301: 0, 400: 0, 401: 0, 403: 0, 404: 0, 405: 0, 500: 0}


def print_stats():
    """Prints the accumulated statistics."""
    print(f"Total file size: {total_size}")
    for code in sorted(status_codes.keys()):
        if status_codes[code] > 0:
            print(f"{code}: {status_codes[code]}")


def signal_handler(sig, frame):
    """Handles the interrupt signal to print stats and exit."""
    print_stats()
    sys.exit(0)


signal.signal(signal.SIGINT, signal_handler)

line_count = 0
for line in sys.stdin:
    try:
        parts = line.split()
        if len(parts) < 9:
            continue

        file_size = parts[-1]
        status_code = parts[-2]
        request = parts[5] + ' ' + parts[6] + ' ' + parts[7]

        if request != '"GET /projects/260 HTTP/1.1"':
            continue

        if file_size.isdigit():
            total_size += int(file_size)

        if status_code.isdigit():
            status_code = int(status_code)
            if status_code in status_codes:
                status_codes[status_code] += 1

        line_count += 1
        if line_count % 10 == 0:
            print_stats()
    except Exception:
        continue

print_stats()
