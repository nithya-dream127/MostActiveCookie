import argparse
from collections import defaultdict
from datetime import datetime, timezone


def readLogFile(path):
    with open(path, 'r') as file:
        return file.readlines()

def parseArguments():
    parser = argparse.ArgumentParser(
        description='Process a cookie log file and find the most active cookie for a specific day.')
    parser.add_argument('-f', '--file', required=True, help='Path to the cookie log file')
    parser.add_argument('-d', '--date', required=True, help='Date in YYYY-MM-DD format')
    return parser.parse_args()


from collections import defaultdict
from datetime import datetime, timezone

def findMostActiveCookies(log_lines, date):
    cookie_counts = defaultdict(int)
    target_date = datetime.strptime(date, '%Y-%m-%d').date()

    for line in log_lines:
        if line.startswith("cookie,timestamp"):
            continue
        cookie, timestamp = line.strip().split(',')
        log_datetime = datetime.fromisoformat(timestamp).astimezone(timezone.utc)
        log_date = log_datetime.date()
        if log_date == target_date:
            cookie_counts[cookie] += 1

    if not cookie_counts:
        return []

    max_count = max(cookie_counts.values())
    most_active_cookies = [cookie for cookie, count in cookie_counts.items() if count == max_count]

    return most_active_cookies



def main():
    args = parseArguments()
    data = readLogFile(args.file)
    cookies_found = findMostActiveCookies(data, args.date)

    if cookies_found:
        for cookie in cookies_found:
            print(cookie)
    else:
        print("No cookies found for the given date.")


if __name__ == '__main__':
    main()
