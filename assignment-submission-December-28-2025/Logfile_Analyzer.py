import re
from collections import Counter
from datetime import datetime

LOG_TIMESTAMP_PATTERN = r"\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}"

def load_logs(file_path):
    with open(file_path, "r", encoding="utf-8") as f:
        return f.readlines()

def count_log_levels(lines):
    levels = Counter()
    for line in lines:
        if "ERROR" in line:
            levels["ERROR"] += 1
        elif "WARNING" in line:
            levels["WARNING"] += 1
        elif "INFO" in line:
            levels["INFO"] += 1
        elif "DEBUG" in line:
            levels["DEBUG"] += 1
    return levels

def search_keyword(lines, keyword):
    return [line for line in lines if keyword.lower() in line.lower()]

def parse_timestamp(line):
    match = re.search(LOG_TIMESTAMP_PATTERN, line)
    if match:
        return datetime.strptime(match.group(), "%Y-%m-%d %H:%M:%S")
    return None

def filter_by_date_range(lines, start, end):
    results = []
    for line in lines:
        ts = parse_timestamp(line)
        if ts and start <= ts <= end:
            results.append(line)
    return results

def most_common_messages(lines, top_n=5):
    messages = Counter(lines)
    return messages.most_common(top_n)

def main():
    file_path = input("Enter log file path: ")
    try:
        lines = load_logs(file_path)
    except FileNotFoundError:
        print("File not found. Please check the path.")
        return

    while True:
        print("\nLog Analyzer Menu")
        print("1. Count log levels")
        print("2. Search by keyword")
        print("3. Filter by date range (YYYY-MM-DD HH:MM:SS)")
        print("4. Show most frequent messages")
        print("5. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            levels = count_log_levels(lines)
            print("\nLog Level Counts:")
            for level, count in levels.items():
                print(f"{level}: {count}")

        elif choice == "2":
            keyword = input("Enter keyword to search: ")
            results = search_keyword(lines, keyword)
            print(f"\nFound {len(results)} matching lines:\n")
            for line in results:
                print(line.strip())

        elif choice == "3":
            start_str = input("Start datetime: ")
            end_str = input("End datetime: ")
            try:
                start = datetime.strptime(start_str, "%Y-%m-%d %H:%M:%S")
                end = datetime.strptime(end_str, "%Y-%m-%d %H:%M:%S")
                results = filter_by_date_range(lines, start, end)
                print(f"\nFound {len(results)} lines in range:\n")
                for line in results:
                    print(line.strip())
            except ValueError:
                print("Invalid datetime format.")

        elif choice == "4":
            top = most_common_messages(lines)
            print("\nMost Frequent Messages:\n")
            for msg, count in top:
                print(f"{count}x -> {msg.strip()}")

        elif choice == "5":
            print("Exiting analyzer.")
            break

        else:
            print("Invalid option. Try again.")

if __name__ == "__main__":
    main()
