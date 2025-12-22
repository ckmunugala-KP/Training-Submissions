import csv
import json
import os

def csv_to_json(csv_file_path, json_file_path):
    try:
        data = []

        # Read CSV file
        with open(csv_file_path, mode='r', newline='', encoding='utf-8') as csv_file:
            csv_reader = csv.DictReader(csv_file)

            for row in csv_reader:
                data.append(row)

        # Write JSON file
        with open(json_file_path, mode='w', encoding='utf-8') as json_file:
            json.dump(data, json_file, indent=4)

        print("\n✅ Conversion successful!")
        print(f"📄 JSON file created: {json_file_path}")

    except FileNotFoundError:
        print("\n❌ Error: CSV file not found.")
    except Exception as e:
        print(f"\n❌ Unexpected error: {e}")


def main():
    print("📂 CSV to JSON Converter")

    csv_path = input("Enter CSV file path: ").strip()
    json_path = input("Enter output JSON file name (e.g., output.json): ").strip()

    if not csv_path.endswith(".csv"):
        print("\n❌ Please provide a valid CSV file.")
        return

    if not json_path.endswith(".json"):
        print("\n❌ Output file must be a .json file.")
        return

    csv_to_json(csv_path, json_path)


if __name__ == "__main__":
    main()
