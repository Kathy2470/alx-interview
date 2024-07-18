#!/usr/bin/python3
import sys
import signal

total_size = 0
status_codes = {200: 0, 301: 0, 400: 0, 401: 0, 403: 0, 404: 0, 405: 0, 500: 0}

def print_stats():
    print(f"Total file size: {total_size}")
    for code in sorted(status_codes.keys()):
        if status_codes[code] > 0:
            print(f"{code}: {status_codes[code]}")

def signal_handler(sig, frame):
    print_stats()
    sys.exit(0)

signal.signal(signal.SIGINT, signal_handler)

line_count = 0
for line in sys.stdin:
    line_count += 1
    parts = line.split()
    if len(parts) < 9:
        continue

    ip, _, _, date, request, _, status_code, file_size = parts[0], parts[1], parts[2], parts[3], parts[4], parts[5], parts[6], parts[8]

    if request != '"GET /projects/260 HTTP/1.1"' or not file_size.isdigit():
        continue

    total_size += int(file_size)
    if status_code.isdigit():
        status_code = int(status_code)
        if status_code in status_codes:
            status_codes[status_code] += 1

    if line_count % 10 == 0:
        print_stats()

print_stats()
