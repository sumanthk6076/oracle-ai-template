import sys


def count_lines(file_path):
    with open(file_path, "r", encoding="utf-8") as f:
        return sum(1 for _ in f)


def main():
    if len(sys.argv) != 2:
        print("Usage: python count_lines.py <file_path>")
        sys.exit(1)

    file_path = sys.argv[1]

    try:
        count = count_lines(file_path)
        print(f"{file_path}: {count} line(s)")
    except FileNotFoundError:
        print(f"Error: file not found — {file_path}")
        sys.exit(1)


if __name__ == "__main__":
    main()
