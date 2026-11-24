def process_text_file(input_file: str, output_file: str) -> None:
  with open(input_file, "r", encoding="utf-8") as infile:
    lines = infile.readlines()

  total_lines = len(lines)
  first_two_lines = lines[:2]

  with open(output_file, "w", encoding="utf-8") as outfile:
    outfile.writelines(first_two_lines)

  print(f"Total number of lines in '{input_file}': {total_lines}")
  print(f"First {len(first_two_lines)} line(s) written to '{output_file}'.")


if __name__ == "__main__":
  source_path = "input.txt"
  dest_path = "first_two_lines.txt"

  with open(source_path, "w", encoding="utf-8") as f:
    f.write("First line of the file.\n")
    f.write("Second line of the file.\n")
    f.write("Third line of the file.\n")
    f.write("Fourth line of the file.\n")

  process_text_file(source_path, dest_path)