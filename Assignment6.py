def file_operations(filename: str) -> None:
  with open(filename, "w", encoding="utf-8") as f:
    f.write("Line 1: Welcome to Advanced Python Programming.\n")
    f.write("Line 2: File handling with context managers.\n")

  with open(filename, "a", encoding="utf-8") as f:
    f.write("Line 3: Appended line.\n")

  with open(filename, "r", encoding="utf-8") as f:
    content = f.read()

  print("--- File Contents ---")
  print(content)


if __name__ == "__main__":
  file_operations("sample_a6.txt")