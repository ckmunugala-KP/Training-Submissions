import datetime
import os

DIARY_FILE = "diary.txt"


def write_entry():
    """Write a new diary entry"""
    entry = input("\nWrite your diary entry:\n")
    date_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    with open(DIARY_FILE, mode="a", encoding="utf-8") as file:
        file.write(f"\n[{date_time}]\n")
        file.write(entry + "\n")

    print("\n✅ Diary entry saved successfully.")


def read_entries():
    """Read all diary entries"""
    if not os.path.exists(DIARY_FILE):
        print("\n📭 No diary entries found.")
        return

    with open(DIARY_FILE, mode="r", encoding="utf-8") as file:
        content = file.read()

        if content.strip() == "":
            print("\n📭 Diary is empty.")
        else:
            print("\n📖 Your Diary Entries:")
            print("-" * 40)
            print(content)
            print("-" * 40)


def clear_diary():
    """Clear all diary entries"""
    confirm = input("\nAre you sure you want to clear the diary? (yes/no): ").lower()
    if confirm == "yes":
        with open(DIARY_FILE, mode="w", encoding="utf-8") as file:
            file.write("")
        print("\n🗑️ Diary cleared successfully.")
    else:
        print("\n❌ Operation cancelled.")


def menu():
    """Display menu"""
    print("\n--- Personal Diary Application ---")
    print("1. Write a new diary entry")
    print("2. Read diary entries")
    print("3. Clear diary")
    print("4. Exit")


def main():
    while True:
        menu()
        choice = input("\nEnter your choice (1-4): ")

        if choice == "1":
            write_entry()
        elif choice == "2":
            read_entries()
        elif choice == "3":
            clear_diary()
        elif choice == "4":
            print("\n👋 Exiting Diary Application. Goodbye!")
            break
        else:
            print("\n⚠️ Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
